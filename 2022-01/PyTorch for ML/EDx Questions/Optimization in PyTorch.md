# _0. PyTorch for ML::EDx Questions

## What does the followling line of code do?
```python
optimizer.step()
```

%

## Makes an update to its parameters
```python
yhat=model(x)
loss=criterion(yhat,y)
loss.backward()
optimizer.step()
```

%

Does not clear the gradient

## What's wrong with the following lines of code?
```python
optimizer = optim.SGD(model.parameters(), lr = 0.01)

model=linear_regression(1,1)
```

%

The model object has not been created. As such, the argument that specifies what Tensors should be optimized does not exist