from collections import defaultdict
import warnings
import random

from dbispipeline.base import Loader


class LimitingLoader(Loader):

    def __init__(
            self,
            max_targets,
            max_documents_per_target,
            loader,
            strategy='first',
            random_seed=None):

        valid_strategies = ['first', 'random']
        if strategy not in valid_strategies:
            raise ValueError(f'the strategy {strategy} is not valid. Please '
                             f'choose from {valid_strategies}')

        self.max_targets = max_targets
        self.max_documents_per_target = max_documents_per_target
        self.loader = loader
        self.strategy = strategy
        self.random_seed = random_seed

        if self.random_seed is not None:
            random.seed(self.random_seed)

    @property
    def run_count(self):
        return self.loader.run_count

    def load(self):
        pairs = []
        if hasattr(self.loader, 'load_validate'):
            pairs.append(self.loader.load_validate())
        if hasattr(self.loader, 'load_test'):
            pairs.append(self.loader.load_test())
            pairs.append(self.loader.load_train())
        else:
            pairs.append(self.loader.load())

        dicts = []
        for pair in pairs:
            entry = defaultdict(list)
            for data, label in zip(*pair):
                entry[str(label)].append(data)
            dicts.append(entry)

        result = ()
        for bunch in dicts:
            bunch_result = [], []
            for key in self._sample(list(bunch.keys()), self.max_targets):
                values = self._sample(bunch[key], self.max_documents_per_target)
                for value in values:
                    bunch_result[0].append(value)
                    bunch_result[1].append(key)
            result += bunch_result
        return result

    def _sample(self, values, sample_limit):
        if sample_limit is None:
            return values

        if sample_limit >= len(values):
            warnings.warn(
                f'sample_limit ({sample_limit}) >= targets '
                f'({len(values)})')
            return values

        if self.strategy == 'first':
            return values[:sample_limit]

        if self.strategy == 'random':
            return random.sample(values, sample_limit)

    @property
    def configuration(self):
        wrapped_configuration = self.loader.configuration
        wrapped_configuration.update({
            'max_targets': self.max_targets,
            'max_documents_per_target': self.max_documents_per_target,
            'strategy': self.strategy,
            'random_seed': self.random_seed,
        })
        return wrapped_configuration
