#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for pagerank.py"""

import unittest

import numpy as np

from sknetwork.ranking.pagerank import PageRank, BiPageRank
from sknetwork.data import rock_paper_scissors, movie_actor


# noinspection PyMissingOrEmptyDocstring
class TestPageRank(unittest.TestCase):

    def setUp(self):
        self.bipagerank = BiPageRank()

    def test_pagerank(self):
        ground_truth = np.ones(3) / 3
        self.adjacency = rock_paper_scissors()

        self.pagerank_sps = PageRank(solver='spsolve')
        self.pagerank_sps.fit(self.adjacency)
        scores = self.pagerank_sps.scores_
        self.assertAlmostEqual(np.linalg.norm(scores - ground_truth), 0.)

        self.pagerank_sps.fit(self.adjacency, personalization=np.array([0, 1, 0]))
        self.pagerank_sps.fit(self.adjacency, personalization={1: 1})

        self.pagerank_high_damping = PageRank(damping_factor=0.99)
        self.pagerank_high_damping.fit(self.adjacency)
        scores = self.pagerank_high_damping.scores_
        self.assertAlmostEqual(np.linalg.norm(scores - ground_truth), 0., places=1)

        self.pagerank_lcz = PageRank(solver='lanczos')
        self.pagerank_lcz.fit(self.adjacency)
        scores = self.pagerank_lcz.scores_
        self.assertAlmostEqual(np.linalg.norm(scores - ground_truth), 0.)

        self.pagerank_lsq = PageRank(solver='lsqr')
        self.pagerank_lsq.fit(self.adjacency)
        scores = self.pagerank_lsq.scores_
        self.assertAlmostEqual(np.linalg.norm(scores - ground_truth), 0.)

    def test_bipartite(self):
        biadjacency = movie_actor()
        n1, n2 = biadjacency.shape
        self.bipagerank.fit(biadjacency, {0: 1})
        row_scores = self.bipagerank.row_scores_
        self.assertEqual(len(row_scores), n1)
        col_scores = self.bipagerank.col_scores_
        self.assertEqual(len(col_scores), n2)
        scores = self.bipagerank.scores_
        self.assertEqual(len(scores), n1 + n2)
