# _0. PyTorch for ML::EDx Questions

## Early stopping is best described as?
not performing all the iterations of gradient descent

## How would you save the model object ```model```?
```python
torch.save(model.state_dict(), 'best_model.pt')
```