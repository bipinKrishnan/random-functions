import pytest

import torch
from torch.utils.data import Dataset, DataLoader

from random_functions.pytorch import check_dataloaders
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
