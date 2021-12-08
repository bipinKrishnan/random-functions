def check_dataloaders(*args) -> None:
    """
    Checks if there are any errors in the provided PyTorch dataloaders
    and prints the shape of it.

    Usage:

    ```python
    from random_functions.pytorch.utils import check_dataloaders

    check_dataloaders(dataloader1, dataloader2, dataloader3)
    ```
    """

    for i, dl in enumerate(args):
        print(f"Dataloader {i+1}")
        print(next(iter(dl))[0].shape)