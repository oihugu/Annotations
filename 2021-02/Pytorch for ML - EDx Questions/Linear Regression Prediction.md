# _0. PyTorch for ML::EDx Questions

## Consider the following lines of code. How many Parameters does the object model have?
```python
from torch.nn import Linear model=Linear(in_features=1,out_features=1)
```

%

2

## What is wrong with the following class:
```python
class LR():
    # Constructor
    def __init__(self, input_size, output_size)::
        # Inherit from parent
        super(LR, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    # Prediction function
    def forward(self, x):
        out = self.linear(x)
        return out
```

%

It is missing nn.Module

## What is wrong with the following class or custom module:
```python
class LR(nn.Module):
    # Constructor
    def __init__(self, input_size, output_size)::
        # Inherit from parent
        super(LR, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    # Prediction function
    def forward(self, x):
        out = linear(x)
        return out
```

%

"linear" should be self.linear

## What is wrong with the following class or custom module:
```python
class LR(nn.Module):
    # Constructor
    def __init__(self, input_size, output_size)::
        # Inherit from parent
        super(dog, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    # Prediction function
    def forward(self, x):
        out = self.linear(x)
        return out
```

%

super(dog,self) should be super(LR,self)

## Consider the following lines of code. How many Parameters does the object model have?
```python
from torch.nn import Linear

model=Linear(in_features=1,out_features=1)
```

%

2