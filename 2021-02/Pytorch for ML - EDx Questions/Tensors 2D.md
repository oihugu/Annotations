# _0. PyTorch for ML::EDx Questions

## Consider the following code:

```python
a=torch.tensor([[0,1,1],[1,0,1]])
```
What is the output of a.size() and a.ndimension()?

%

(2, 3), 2

## How do you convert the following Pandas Dataframe to a tensor
```python
df = pd.DataFrame({'A':[11, 33, 22],'B':[3, 3, 2]})
```

%

torch.tensor(df.values)

## What is the result of the following:
```python
X = torch.tensor([[1, 0], [0, 1]])
Y = torch.tensor([[2, 1], [1, 2]]) 
X_times_Y = X * Y
```

%

tensor([[2, 0],[0, 2]])

## What is the result of the following:
```python
A = torch.tensor([[0, 1, 1], [1, 0, 1]])
B = torch.tensor([[1, 1], [1, 1], [-1, 1]])
A_times_B = torch.mm(A,B)
```

%

tensor([[0, 2], [0, 2]])
