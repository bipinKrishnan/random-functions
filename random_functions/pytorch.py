def check_dataloaders(*args):
    for i, dl in enumerate(args):
        print(f"Dataloader {i+1}")
        print(next(iter(dl))[0].shape)
