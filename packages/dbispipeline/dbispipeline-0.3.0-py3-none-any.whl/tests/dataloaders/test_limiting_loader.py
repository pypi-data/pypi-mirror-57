import unittest
from collections import defaultdict

from .dummy_loader import VeryDumbLoader
from dbispipeline.dataloaders.wrappers import LimitingLoader



class TestLimitingLoader(unittest.TestCase):

    def test_max_both(self):
        loader = LimitingLoader(
                max_targets=7,
                max_documents_per_target=8,
                loader=VeryDumbLoader(
                    n_samples=500,
                    n_classes=20))
        xtrain, ytrain = loader.load()

        self.assertLessEqual(len(set(ytrain)), 7)
        self.assertLessEqual(len(xtrain), 7 * 8)
        d = defaultdict(list)
        for x, y in zip(xtrain, ytrain):
            d[y].append(x)
        for key, value in d.items():
            self.assertLessEqual(len(value), 8)

    def test_max_targets(self):
        loader = LimitingLoader(
                max_targets=7,
                max_documents_per_target=None,
                loader=VeryDumbLoader(
                    n_samples=500,
                    n_classes=20))
        xtrain, ytrain = loader.load()

        self.assertLessEqual(len(set(ytrain)), 7)

    def test_max_documents(self):
        loader = LimitingLoader(
                max_targets=None,
                max_documents_per_target=8,
                loader=VeryDumbLoader(
                    n_samples=500,
                    n_classes=20))
        xtrain, ytrain = loader.load()

        print(sorted(list(set(ytrain))))
        self.assertLessEqual(len(set(ytrain)), 20)
        self.assertLessEqual(len(xtrain), 20 * 8)
        d = defaultdict(list)
        for x, y in zip(xtrain, ytrain):
            d[y].append(x)
        for key, value in d.items():
            self.assertLessEqual(len(value), 8)

