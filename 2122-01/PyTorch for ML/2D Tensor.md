# _0. PyTorch for ML

## What can be a 2D Tensors?
Images can be represented in a 2D tensors in grey scale
[2D Tensor]()

## What can be a 3D Tensors?
Images can be represented in a 3D tensors in RGB
[2D Tensor]()

## What methods are available in pytorch for 2D Tensors?
Addition, Multiplications with scalar, hadamard product, identical to 1D tensors
[2D Tensor]()

## How matrix multiplication works in pytorch?
The multiplication of two matrices works with the rule:

[$$]
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13}\\\\
a_{21} & a_{22} & a_{23}
\end{bmatrix}

B = \begin{bmatrix}
b_{11} & b_{12} \\\\
b_{21} & b_{22} \\\\
b_{31} & b_{32}
\end{bmatrix}
[/$$]

$$
torch.mm(A,B) = \begin{bmatrix}
A[0,:].dot(B[:,0]) & A[0,:].dot(B[:,1])\\\\
A[1,:].dot(B[:,0]) & A[1,:].dot(B[:,1])
\end{bmatrix}
$$

```python
A = torch.tensor([[1,2,3],[4,5,6]])
B = torch.tensor([[1,2,3],[4,5,6]])
torch.mm(A,B) == tensor([[22, 28], [49, 64]])
```
[2D Tensor]()

