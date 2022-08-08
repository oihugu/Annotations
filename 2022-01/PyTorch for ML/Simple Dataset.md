# _0. Pytorch for ML

## What is the python class used to chreate pytorch datasets?
torch.utils.Dataset
[Simple Dataset]()[PyTorch]()

## What methods do we need to overwrite in the Dataset class in order to create our own dataset?
- \_\_init\_\_ 
- \_\_getitem\_\_
- \_\_len\_\_
[Simple Dataset]()[PyTorch]()

## How do we apply a trasnform in a pytorch dataset?
We need to create a class for each transformation, with an \_\_init\_\_ e \_\_call\_\_, beeing \_\_call\_\_ the proper transformation.
For apply more than one transform we utilize the _transforms.Compose([1° Transform(), 2° Transform(), ...])
[Simple Dataset]()[PyTorch]()
