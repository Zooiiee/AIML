import numpy as np

# Define the input for AND Gate
x = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

# Define the target output for AND Gate
t = np.array([1, -1, -1, -1])
weights = np.array([0.0, 0.0])
bias = 0.0
alpha = 1  # learning rate
theta = 0  # threshold


def activation(yin):
    if yin > theta:
        return 1
    elif yin < -theta:
        return -1
    else:
        return 0

epochs = 10

for e in range(epochs):
    print(f"\nEpoch {e + 1}")
    for i in range(len(x)):
        x1 = x[i]
        t1 = t[i]
        yin = np.dot(weights, x1) + bias
        y = activation(yin)
        error = t1 - y
        if error != 0:
            weights += alpha * t1 * x1
            bias += alpha * t1

        print(f"Input: {x1}, Target: {t1}, Output: {y}, Weights: {weights}, Bias: {bias}")
