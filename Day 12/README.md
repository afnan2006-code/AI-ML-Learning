# Day 12 — PyTorch Mini-Batch Training with DataLoader and Adam

## Project Objective

The objective of Day 12 was to upgrade the PyTorch Deep Learning model developed on Day 11 by introducing `TensorDataset`, `DataLoader`, mini-batch training, validation loss tracking, and the Adam optimizer.

The model was trained using native PyTorch without Scikit-Learn or the `.fit()` method.

## Technologies Used

- Python
- PyTorch
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## Dataset

The PyTorch tensors created during Day 11 were reused for this task.

The training and validation data were wrapped using PyTorch's `TensorDataset`.

## DataLoader Configuration

The training and validation datasets were converted into DataLoaders.

### Training DataLoader

- Batch size: 64
- Shuffle: True

### Validation DataLoader

- Batch size: 64
- Shuffle: False

Mini-batch processing allows the model to process a smaller number of samples at a time instead of processing the entire dataset in a single training step. This helps reduce peak RAM usage and allows more frequent parameter updates.

## Model

The existing Multi-Layer Perceptron (MLP) architecture from Day 11 was continued for Day 12.

The model was trained using PyTorch's native training process:

1. Forward pass
2. Loss calculation
3. Backpropagation
4. Adam optimizer update

## Loss Function

`CrossEntropyLoss` was used for classification.

```python
criterion = nn.CrossEntropyLoss()
