# _0. PyTorch for ML::EDx Questions

## Consider the following code, including the bias. How many parameters does the object model have?
```python
model=nn.Linear(4,1)
```

%

5

## Consider the following code, including the bias. How many parameters does the object model have?
```python
model=nn.Linear(6,1)
```

%

7

## How would you create a lienar object with ten input features?

model=nn.Linear(10,1)

## Consider the following line of code. How many rows and columns does the tensor yhat contain?
```python
X=torch.tensor([[1.0,1.0,1],[1.0,2.0,1],[1.0,3.0,1],[1.0,3.0,1]])

model=nn.Linear(3,1)

yhat=model(X)
```

%

4,1

## If the input to our linear regression object is 10 dimensions, including the bias, how many variables does our cost or total loss function contain?

11

## How do you calculate the gradient and perform the update for Multiple Linear Regression with 10 input variables

```python
loss.backward()
optimizer.step()
```