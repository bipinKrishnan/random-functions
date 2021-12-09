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