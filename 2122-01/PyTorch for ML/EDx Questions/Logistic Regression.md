# _0. PyTorch for ML::EDx Questions

## Will the following line of code run:
```python
model = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())

x = torch.tensor([[1.0]])
yhat = model(x)
```

%

No

## What line of code is equivalent to:
```python
class logistic_regression(nn.Module):

    # Constructor
    def __init__(self, n_inputs):

        super(logistic_regression, self).__init__()

        self.linear = nn.Linear(n_inputs, 1)

    # Prediction
    def forward(self, x):

        yhat = torch.sigmoid(self.linear(x))

        return yhat

model = logistic_regression(1)
```

%

```python
model = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())
```

## How many parameters does the following model have:
```python
model = nn.Sequential(nn.Linear(1, 1), nn.Sigmoid())
```

%

2

## How would you apply the sigmoid function to the tensor z
```python
z=torch.arange(-100,100,0.1).view(-1, 1)
```

%

```python
sig=nn.Sigmoid()
yhat=sig(z)
```
