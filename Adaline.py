import numpy as np

# Input for AND gate
X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

# Target output (bipolar: 1 = True, -1 = False)
T = np.array([1, -1, -1, -1])

# Initialize weights and bias
weights = np.zeros(X.shape[1])
bias = 0.1

# Hyperparameters
alpha = 0.1  # learning rate
epochs = 10  # number of training iterations

# Training Adaline
print("Training Adaline Model for AND Gate\n")
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")
    for i in range(len(X)):
        x_i = X[i]
        t_i = T[i]

        # Net input
        y_in = np.dot(weights, x_i) + bias

        # Output (linear activation)
        y = y_in

        # Error and MSE for this sample
        error = t_i - y
        mse = error ** 2

        # Update rule
        weights += alpha * error * x_i
        bias += alpha * error

        print(f"Input: {x_i}, Target: {t_i}, Output: {y:.2f}, Error: {error:.2f}, MSE: {mse:.4f}, Weights: {weights}, Bias: {bias:.2f}")
