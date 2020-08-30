import numpy as np

# sigmoid function


def nonlin(x, deriv=False):
    if deriv == True:
        print(1 * (1 - x))
    return 1 / (1 + np.exp(-x))


# input data
x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output data
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)

# weights = synapses arrow 1 & 2
sy0 = 2 * np.random.random((3, 4)) - 1   #two neurons 
sy1 = 2 * np.random.random((4, 1)) - 1

for j in range(60000):

    # layers
    l0 = x
    l1 = nonlin(np.dot(l0, sy0))
    l2 = nonlin(np.dot(l1, sy1))
# Error layer 2
    l2_error = y - l2
    if(j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
# Error layer 1
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(sy1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

# update weight or synapses

    sy1 += l1.T.dot(l2_delta)
    sy0 += l0.T.dot(l1_delta)

print("output after training ")
print(l2)
