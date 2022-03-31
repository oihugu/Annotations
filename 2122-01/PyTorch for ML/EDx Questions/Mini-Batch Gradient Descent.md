# _0. PyTorch for ML::EDx Questions

## You have 100 samples of data and your batch size is 25. How many iterations will it take to go through 1 epoch?

4

## You have 100 samples of data and your batch size is 50. How many iterations will it take to go through 1 epoch?

2

## Consider the dataset class Data(). How would you create a data loader object trainloader with a batch size of 3?

```python
data_set=Data()

trainloader=DataLoader(dataset=data_set,batch_size=3)
```

## Consider the dataset class Data(). How would you create a data loader object trainloader with a batch size of 5?

```python
data_set=Data()

trainloader=DataLoader(dataset=data_set,batch_size=5)
```
