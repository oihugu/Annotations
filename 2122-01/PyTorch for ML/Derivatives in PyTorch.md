# _0. Pytorch for ML

## How to instance a tensor that will be used in a derivative?
torch.tensor(x, requires_grad=True)
[Derivatives in PyTorch]()

## How to convert to numpy a cariable that was used in a derivative?
x.detach().numpy()
[Derivatives in PyTorch]()

## What method is used to calculate the derivatives in pytorch?
Pytorch uses a method called backwards graph.
[Derivatives in PyTorch]()
