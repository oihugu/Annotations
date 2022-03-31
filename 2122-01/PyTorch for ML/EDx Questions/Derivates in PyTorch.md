# _0. PyTorch for ML::EDx Questions

## What task does the following lines of code perform?
```python
q=torch.tensor(1.0,requires_grad=True)
fq=2q**3+q
fq.backward()
q.grad
```

%

Determines the derivative of 2q**3+q at q=1

## What's wrong with the following lines of code?
```python
q=torch.tensor(1.0, requires_grad=False)
fq=2q**3+q
fq.backward()
q.grad
```

%

The parameter requires_grad should be set to True

## How would you determine the derivative of $ y = 2x^3+x $ at $x=1$

```python
x = torch.tensor(1.0, requires_grad=True)
y = 2 * x ** 3 + x
y.backward()
x.grad
```

## Try to determine partial derivative 𝑢u of the following function where 𝑢=2u=2 and 𝑣=1v=1: 𝑓=𝑢𝑣+(𝑢𝑣)**2

```python
u = torch.tensor(2.0, requires_grad = True)
v = torch.tensor(1.0, requires_grad = True)
f = u * v + (u * v) ** 2
f.backward()
print("The result is ", u.grad)
```