import torch
from torch.utils.data import Dataset, DataLoader
import random
import numpy as np

from random_functions.pytorch.utils import check_dataloaders, seed_everything
from random_functions.utils import Capturing


class LoadDummyData(Dataset):
    def __init__(self, rows):
        super().__init__()
        self.data = torch.randn(rows, 2)

    def __getitem__(self, idx):
        return self.data[idx, 0], self.data[idx, 1]

    def __len__(self):
        return len(self.data)


def test_check_dataloaders():
    rows = 100
    bs1 = 4
    bs2 = bs1 + 1
    bs3 = bs1 + 2

    dl1 = DataLoader(LoadDummyData(rows=rows), batch_size=bs1)
    dl2 = DataLoader(LoadDummyData(rows=rows), batch_size=bs2)
    dl3 = DataLoader(LoadDummyData(rows=rows), batch_size=bs3)

    with Capturing() as outputs:
        check_dataloaders(dl1, dl2, dl3)
    outputs = [eval(i)[0] for i in outputs if "torch.Size" in i]

    assert outputs == [bs1, bs2, bs3]

def test_seed_everything():
    seed = 3

    def get_states(seed):
        seed_everything(seed)
        states = [random.getstate(), np.random.get_state()[1], torch.get_rng_state()]
        if torch.cuda.is_available():
            states.append(torch.cuda.get_rng_state())
        return states

    new_states = get_states(seed)
    new_sec_states = get_states(seed)
    new_diff_states = get_states(seed+1)

    for new, new_sec, new_diff in zip(*(new_states, new_sec_states, new_diff_states)):
        if type(new)==torch.Tensor or type(new)==np.ndarray:
            assert (new == new_sec).all()
            assert (new != new_diff).any()
        elif type(new)==tuple:
            assert new == new_sec
            assert new != new_diff
        else:
            raise ValueError("Unknown datatype found!")

