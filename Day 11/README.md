# Day 11 — Deep Learning Baseline with PyTorch

## Project Overview

This project begins the Deep Learning journey by implementing a baseline Multi-Layer Perceptron (MLP) using PyTorch for loan default classification.

## Dataset

The project uses the cleaned and balanced loan default dataset from the previous project.

## Model Architecture

The MLP contains:

- Input Layer
- Hidden Layer with 64 neurons
- Hidden Layer with 32 neurons
- ReLU activation
- Output Layer

## Training

The model was trained for 20 epochs using a manual PyTorch training loop.

The training loop performs:

1. Zero gradients
2. Forward pass
3. Loss calculation
4. Backpropagation
5. Optimizer step

## Results

The training loss was tracked across 20 epochs and visualized using Matplotlib.

Test Accuracy: `ADD YOUR ACTUAL ACCURACY HERE`

## Key Learning

This project demonstrated how PyTorch tensors, neural-network layers, ReLU activation, loss functions, backpropagation, and optimizers are used to build a basic deep-learning model.