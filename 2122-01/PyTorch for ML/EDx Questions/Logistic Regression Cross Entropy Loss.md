# _0. PyTorch for ML::EDx Questions

## What cost function should be used for logistic regression?

Cross Entropy

## What's the problem with obtaining the parameters for Logistic Regression and mean sqaured error?

During training, you may not reach the minimum of the cost surface

## What is the PyTorch function you would use for training Logistic Regression with Cross Entropy

nn.BCELoss()

## What fucntion does the following line of code perform?

```python
def criterion(yhat,y):
    out = - 1 * torch.mean(y * torch.log(yhat) + (1 - y) * torch.log(1 - yhat))
    return out
```

%

Calculate the Cross Entropy loss or cost.