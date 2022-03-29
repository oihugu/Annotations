# _0. Pytorch for ML

## What is torch.autograd?
torch.autograd is an automatic differentiation package, utilized to train neural networks.
[PyTorch Documentation]()[torch.autograd]()

## What are neural networks?
Neural networks are a series of nested functions, that are executed in some input, this functions are defined with the parameters(weights and bias) in pytorch they are stored as tensors.
[PyTorch Documentation]()[torch.autograd]()

## What is Forward Propagation?
Forward Propagation is the step on witch the neural netowrk does is best to try to predict the output, pass the input to each one of these functions to realize its guess.
[PyTorch Documentation]()[torch.autograd]()

## What is Backward Propagation?
The neural network ajust its parameters according to the error in its guesses, it does that by travessing backwards is functions, starting with the input, colecting the derivatives of the error, taking into account the parameters of the functions(gradients), and optmizing, utilizing the gradient descent.
[PyTorch Documentation]()[torch.autograd]()

## How the neural network keeps information about its tensors and operations?
It mantains all information about its tensors and operations, utilizing the DAG(Direct Aciclic Graph), in wich, leaves are the input tensors, roots are the output tensors, drawning a graph, starting from the leaves to the root, you can automatically compute the gradients utilizing the chain rule.
[PyTorch Documentation]()[torch.autograd]()

## What the Forward Pass does?
- It executes the operation and returns the result tensor
- They mantain the gradient of operations in DAG
[PyTorch Documentation]()[torch.autograd]()

## What the Backward Pass does?
- Computes the gradients for each .grad_fn
- Accumulate them into .grad
- Utilizing the chain rule, propagate them into the leaves
[PyTorch Documentation]()[torch.autograd]()

## What does "requires_grad=False" do in relation with DAG?
They exclude the tensor from the DAG, freezing the parameters.
[PyTorch Documentation]()[torch.autograd]()

## What the benefits from excluding a thensor from the DAG?
Freezing the parameters is util when you you dont will need the gradients, this will increasse the performance and its commum in the fine tuning fase.
[PyTorch Documentation]()[torch.autograd]()
