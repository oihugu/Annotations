# _0. PyTorch for ML::EDx Questions

## Which of the following is the correct way to compose transforms?

transforms.Compose([add_mult(), mult()])

## Which of the following are the build-in functions you need to define while customizing the class for transforming?
[] \_\_init\_\_
[] np.array()
[] \_\_call\_\_

% 

[X] \_\_init\_\_
[] np.array()
[X] \_\_call\_\_

## What methods do you need in your data set class

\_\_init\_\_,\_\_getitem\_\_ and \_\_len\_\_

## What is wrong with the following class:

```python
class toy_set(Dataset):

    # Constructor with defult values

    def __init__(self, length = 100, transform = None):

        self.len = length

        self.x = 2 * torch.ones(length, 2)

        self.y = torch.ones(length, 1))

        self.transform = transform

    # Getter

    def __getitem__(self, index):

        sample = self.x[index], self.y[index]

        if self.transform:

        sample = self.transform(sample)

        return sample

    # Get Length

    def __len__(self):
```
%

The method \_\_len\_\_(self) does not return anything

