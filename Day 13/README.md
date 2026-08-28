# Day 13 — Neural Network Regularization with PyTorch

## Overview

Day 13 focuses on reducing neural network overfitting using **Batch Normalization** and **Dropout** in PyTorch.

The Day 12 baseline Multi-Layer Perceptron (MLP) was upgraded to a regularized architecture, and both models were trained and compared using training and validation loss.

## Objectives

* Reuse the PyTorch `train_loader` and `val_loader` created in Day 12.
* Create a regularized MLP using `torch.nn.Module`.
* Add `BatchNorm1d` layers between Linear and ReLU layers.
* Add Dropout with `p=0.3`.
* Train both baseline and regularized models for 30 epochs.
* Use the Adam optimizer.
* Track training and validation loss.
* Compare baseline and regularized loss curves.
* Analyze overfitting and generalization.

## Model Architecture

### Baseline MLP

The baseline model uses Linear layers with ReLU activations and an output layer.

### Regularized MLP

The regularized model adds:

* `BatchNorm1d`
* `ReLU`
* `Dropout(p=0.3)`

between the Linear transformations.

## Training Configuration

| Configuration   | Value             |
| --------------- | ----------------- |
| Framework       | PyTorch           |
| Optimizer       | Adam              |
| Learning Rate   | 0.001             |
| Epochs          | 30                |
| Dropout         | 0.3               |
| Loss Function   | CrossEntropyLoss  |
| Random Seed     | 42                |
| Training Data   | Day 12 DataLoader |
| Validation Data | Day 12 DataLoader |

## Regularization Concepts

### Dropout

Dropout randomly deactivates neurons during training. With `p=0.3`, 30% of activations are dropped.

PyTorch uses inverted dropout scaling:

$$
\hat{x} = \frac{x \odot r}{1-p}
$$

For `p=0.3`, retained activations are scaled by:

$$
\frac{1}{0.7} \approx 1.4286
$$

This preserves the expected activation magnitude during training.

Dropout helps prevent overfitting by reducing dependence on specific neurons and encouraging more distributed representations.

### Batch Normalization

Batch Normalization normalizes activations using mini-batch statistics and then applies learnable scale and shift parameters:

$$
y = \gamma\hat{x}+\beta
$$

where:

* \(\gamma\) is the learnable scale parameter.
* \(\beta\) is the learnable shift parameter.

Batch Normalization helps stabilize training by keeping intermediate activations better controlled.

## Training and Validation

Both models were trained for 30 epochs using native PyTorch training loops.

The experiment explicitly uses:

* `model.train()` during training.
* `model.eval()` during validation.
* `torch.no_grad()` during validation.

Training and validation losses were recorded for both models.

A 2×1 Matplotlib figure was created to compare:

1. Baseline MLP training and validation loss.
2. Regularized MLP training and validation loss.

## Dropout as an Implicit Ensemble

Dropout can be viewed as training many different smaller subnetworks because different neurons are randomly deactivated during different training steps.

This prevents the network from relying on a fixed set of neurons and encourages robust feature learning.

## Results

The baseline and regularized models were compared using:

* Best validation loss.
* Best validation-loss epoch.
* Final training loss.
* Final validation loss.
* Training-validation loss gap.
* Training and validation loss curves.

The final conclusion is based on the observed experimental results rather than assuming that regularization will always produce better performance.

## Technologies

* Python
* PyTorch
* Matplotlib
* Jupyter Notebook

## Key Learning Outcomes

* Implemented neural network regularization using PyTorch.
* Applied Batch Normalization using `nn.BatchNorm1d`.
* Applied Dropout using `nn.Dropout(p=0.3)`.
* Understood inverted dropout scaling.
* Understood BatchNorm's learnable gamma and beta parameters.
* Compared regularized and unregularized neural networks.
* Analyzed training and validation loss to evaluate generalization.
