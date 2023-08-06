import os

import numpy as np
import pandas as pd

from mlcomp.db.providers import ModelProvider
from mlcomp.utils.config import Config
from mlcomp.worker.executors import Executor
from mlcomp.worker.executors.kaggle import Submit


@Executor.register
class SubmitMnist(Submit):
    def __init__(self, prob_file: str, out_file: str, model_id: int = None):
        super().__init__(
            competition='digit-recognizer',
            file=out_file
        )

        self.prob_file = prob_file
        self.out_file = out_file
        self.model_id = model_id

    def work(self):
        self.message = f'Task id = {self.task.id}'

        prob = np.load(self.prob_file)
        argmax = prob.argmax(axis=1)
        pd.DataFrame({
            'ImageId': np.arange(1, len(argmax) + 1),
            'Label': argmax
        }).to_csv(self.out_file, index=False)

        score = super().work()

        if self.model_id:
            provider = ModelProvider(self.session)
            model = provider.by_id(self.model_id)
            model.score_public = score
            provider.commit()

    @classmethod
    def _from_config(cls,
                     executor: dict,
                     config: Config,
                     additional_info: dict):
        slot = executor['slot']
        model_name = slot['name']
        prob_file = os.path.join(config.data_folder, model_name + '_test.npy')
        out_file = os.path.join(config.data_folder, model_name + '.csv')
        return cls(
            model_id=slot.get('id'),
            prob_file=prob_file,
            out_file=out_file
        )
