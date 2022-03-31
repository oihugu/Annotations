# _0. PyTorch for ML::EDx Questions

## What is true about the following lines of code?
```python
class linear_regression(nn.Module):

    def __init__(self,input_size,output_size):

    super(linear_regression,self).__init__()

    self.linear=nn.Linear(input_size,output_size)

    def forward(self,x):

    yhat=self.linear(x)

    return yhat

model=linear_regression(3,10)
```
[] The output of the model will have 10 rows
[] The output of the model will have 10 columns

%

The output of the model will have 10 columns


## How many bias parameters will object model have?
```python
class linear_regression(nn.Module):

    def __init__(self,input_size,output_size):

    super(linear_regression,self).__init__()

    self.linear=nn.Linear(input_size,output_size)

    def forward(self,x):

    yhat=self.linear(x)

    return yhat

model=linear_regression(3,10)
```

%

10

## What parameters do you have to change to the method backwards() when you train Multiple Output Linear Regression compared to regular Linear Regression?

None of them