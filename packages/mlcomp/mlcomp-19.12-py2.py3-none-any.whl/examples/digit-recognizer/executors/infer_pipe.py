import numpy as np

from mlcomp.utils.config import Config
from mlcomp.worker.executors import Executor
from mlcomp.worker.interfaces import Interface

from dataset import MnistDataset


@Executor.register
class InferPipe(Executor):
    def __init__(self,
                 model: Interface,
                 suffix: str):
        self.model = model
        self.suffix = suffix

    @property
    def dataset(self):
        if self.suffix == 'test':
            return MnistDataset(file='data/test.csv')

        return MnistDataset(file='data/train.csv',
                            fold_csv='data/fold.csv',
                            is_test=True
                            )

    def work(self):
        input = {
            'dataset': self.dataset
        }
        res = self.model(input)
        np.save(f'data/{self.model.name}_{self.suffix}', res['prob'])

    @classmethod
    def _from_config(cls,
                     executor: dict,
                     config: Config,
                     additional_info: dict):
        args = Executor.kwargs_for_interface(executor, config)
        model = Interface.from_config(args)
        return cls(model, executor['suffix'])
