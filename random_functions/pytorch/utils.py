import torch 
import numpy as np
import os
import random


def check_dataloaders(*args) -> None:
    """
    Prints the shape of the provided PyTorch dataloaders.

    Usage:

    ```python
    from random_functions.pytorch.utils import check_dataloaders

    check_dataloaders(dataloader1, dataloader2, dataloader3)
    ```
    """

    for i, dl in enumerate(args):
        print(f"Dataloader {i+1}")
        print(next(iter(dl))[0].shape)

def seed_everything(seed: int) -> None:
    """
    This function sets the seed value for random number generator, 
    numpy, torch and cuda(if one is available).

    Usage:

      ```python
      from random_functions.pytorch.utils import seed_everything

      seed_everything(seed=999)
      ```

    Args:
      seed (int): This value is set as the seed for reproducing the results

    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
