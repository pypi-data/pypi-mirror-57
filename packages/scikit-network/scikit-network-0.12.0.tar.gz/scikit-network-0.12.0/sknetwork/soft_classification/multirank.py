#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov, 2019
@author: Nathan de Lara <ndelara@enst.fr>
"""

from functools import partial
from multiprocessing import Pool
from typing import Union, Optional

import numpy as np
from scipy import sparse

from sknetwork.ranking import PageRank, BiPageRank
from sknetwork.soft_classification.base import BaseSoftClassifier


class MultiRank(BaseSoftClassifier):
    """Semi-Supervised clustering based on personalized PageRank.

    Parameters
    ----------
    damping_factor:
        Damping factor for personalized PageRank.
    solver:
        Which solver to use for PageRank.
    rel_tol:
        Relative tolerance parameter.
        Values lower than rel_tol / n_nodes in each personalized PageRank are set to 0.
    sparse_output:
        If ``True``, returns the membership as a sparse CSR matrix.
        Otherwise, returns a dense ndarray.
    n_jobs:
        If an integer value is given, denotes the number of workers to use (-1 means the maximum number will be used).
        If ``None``, no parallel computations are made.

    Attributes
    ----------
    membership_: CSR matrix or ndarray
        Component (i, k) indicates the level of membership of node i in the k-th cluster.
        If the provided labels are not consecutive integers starting from 0,
        the k-th column of the membership corresponds to the k-th label in ascending order.
        The rows are normalized to sum to 1.

    Example
    -------
    >>> from sknetwork.data import karate_club
    >>> multirank = MultiRank()
    >>> adjacency, labels_true = karate_club(return_labels=True)
    >>> seeds = {0: labels_true[0], 33: labels_true[33]}
    >>> membership_ = multirank.fit_transform(adjacency, seeds)
    >>> membership_.shape
    (34, 2)

    References
    ----------
    Lin, F., & Cohen, W. W. (2010, August). `Semi-supervised classification of network data using very few labels.
    <https://lti.cs.cmu.edu/sites/default/files/research/reports/2009/cmulti09017.pdf>`_
    In 2010 International Conference on Advances in Social Networks Analysis and Mining (pp. 192-199). IEEE.

    """

    def __init__(self, damping_factor: float = 0.85, solver: str = 'lanczos', rel_tol: float = 1e-4,
                 sparse_output: bool = True, n_jobs: Optional[int] = None):
        super(MultiRank, self).__init__()

        self.damping_factor = damping_factor
        self.solver = solver
        self.rel_tol = rel_tol
        self.sparse_output = sparse_output
        if n_jobs == -1:
            self.n_jobs = None
        elif n_jobs is None:
            self.n_jobs = 1
        else:
            self.n_jobs = n_jobs

    def fit(self, adjacency: Union[sparse.csr_matrix, np.ndarray], seeds: Union[np.ndarray, dict]) -> 'MultiRank':
        """Compute personalized PageRank using each given labels as seed set.

        Parameters
        ----------
        adjacency:
            Adjacency matrix of the graph.
        seeds: Dict or ndarray,
            If dict, ``(key, val)`` indicates that node ``key`` has label ``val``.
            If ndarray, ``seeds[i] = val`` indicates that node ``i`` has label ``val``.
            Negative values are treated has no label.

        Returns
        -------
        self: :class:`MultiRank`

        """
        if isinstance(self, BiMultiRank):
            pr = BiPageRank(self.damping_factor, self.solver)
        else:
            pr = PageRank(self.damping_factor, self.solver)

        n: int = adjacency.shape[0]
        if isinstance(seeds, np.ndarray):
            if seeds.shape[0] != n:
                raise ValueError('Dimensions mismatch between adjacency and seeds vector.')
        elif isinstance(seeds, dict):
            tmp = -np.ones(n)
            for key, val in seeds.items():
                tmp[key] = val
            seeds = tmp
        else:
            raise TypeError('"seeds" must be a dictionary or a one-dimensional array.')

        unique_labels: np.ndarray = np.unique(seeds[seeds >= 0])
        n_labels: int = len(unique_labels)
        if n_labels < 2:
            raise ValueError('There must be at least two distinct labels.')

        if self.n_jobs != 1:
            local_function = partial(pr.fit_transform, adjacency)
            personalizations = []
            for i, label in enumerate(unique_labels):
                personalization = np.zeros(n)
                personalization[seeds == label] = 1.
                personalizations.append(personalization)
            with Pool(self.n_jobs) as pool:
                membership = np.array(pool.map(local_function, personalizations))
            membership = membership.T
        else:
            membership = np.zeros((n, n_labels))
            for i, label in enumerate(unique_labels):
                personalization = np.zeros(n)
                personalization[seeds == label] = 1.
                membership[:, i] = pr.fit_transform(adjacency, personalization=personalization)[:n]

        membership[membership <= self.rel_tol / n] = 0

        norm = np.sum(membership, axis=1)
        membership[norm > 0] /= norm[norm > 0, np.newaxis]

        if self.sparse_output:
            self.membership_ = sparse.csr_matrix(membership)
        else:
            self.membership_ = membership

        return self


class BiMultiRank(MultiRank):
    """Semi-Supervised clustering based on personalized PageRank for bipartite graphs.
    See :class:`sknetwork.ranking.BiPageRank`
    """

    def __init__(self, damping_factor: float = 0.85, solver: str = 'lanczos', rel_tol: float = 1e-4,
                 sparse_output: bool = True, n_jobs: Optional[int] = None):
        MultiRank.__init__(self, damping_factor, solver, rel_tol, sparse_output, n_jobs)
