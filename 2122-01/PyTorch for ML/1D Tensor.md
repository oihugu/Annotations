# _0. PyTorch for ML

## What are pythorch tensors?
Data Strucktures that generalize numbers and arrays
[#1D Tensor]()

## What opperations are permited in pythorch tensors?
Operations with matrices and vectors, multiplication, addition...
[#1D Tensor]()

## What is the role of gradients and derivatives?
They are used to train a model.
[#1D Tensor]()

## What is a 0D Tensor?
A 0D tensor is a number.
[#1D Tensor]()

## What is a 1D Tensor?
A 1D tensor is a vector, can be a Time Series, a line in a DB, a row in a CSV, a column in a matrix, and his has to be the same type.
[#1D Tensor]()

## What is a 2D Tensor?
A 2D tensor is a matrix.
[#1D Tensor]()
 
## What happens if we change an element in a np array that was used to create a pytorch tensor?
The tensor will be changed too. Pytorch only create a link to the array.
[#1D Tensor]()

## How to create a pytorch tensor from a pandas dataframe?
We have to use the torch.from_numpy() function, and the pandas .items() method.
[#1D Tensor]()

## How tensor addition works in pytorch?
The addition of two vectors is the addition of the corresponding elements.
```python
u = torch.tensor([1,2,3])
v = torch.tensor([4,5,6])
u + v == tensor([5, 7, 9])
```
[#1D Tensor]()

## How to create a pytorch tensor from a numpy array?
We have to use the torch.from_numpy() function.
[#1D Tensor]()

## How product of two tensor works in pytorch?
The multiplication of two vectors is the multiplication of the corresponding elements.
```python
u = torch.tensor([1,2,3])
v = torch.tensor([4,5,6])
u * v == tensor([4, 10, 18])
```
This can be called Hadamard product.
[#1D Tensor]()

## How multiplication of a tensor by a scalar works in pytorch?
The multiplication of a vector by a scalar is the multiplication of the corresponding elements by the scalar.
```python
u = torch.tensor([1,2,3])
2 * u == tensor([2, 4, 6])
```
[#1D Tensor]()

## How the dot product of two tensors works in pytorch?
The dot product of two vectors is the sum of the multiplication of the corresponding elements.
```python
v = torch.tensor([4,5,6])
u = torch.tensor([1,2,3])
torch.dot(u,v) == tensor(32)
```
[#1D Tensor]()

## How torch.linspace works in pytorch?
The linspace function creates a tensor with a sequence of numbers.
```python
torch.linspace(start, end, steps)
```
[#1D Tensor]()
