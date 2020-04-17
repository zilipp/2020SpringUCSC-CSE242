import numpy as np

'''
Implementation of MSE as shown in above derivation.
'''
def mse(X, y, h):
    n = len(X)
    return 0.5 * (1 / n) * np.sum((y - h) ** 2)


'''
Implementation of the derivative of MSE as shown in above derivation.
'''
def compute_gradient(X, y, h):
    n = len(X)
    res = 1 / n * np.dot((h - y), X)
    return res

'''
Gradient descent step. 
Takes X, y, current theta_0 & theta_1, and alpha. 
Returns an updated theta_0 & theta_1.
'''
def gradient_descent_step(X, y, theta_0, theta_1, alpha):
    n = len(X)
    # First compute h (y_pred)
    h =  theta_0 + theta_1 * X
    delta_h = compute_gradient(X, y, h)

    # Then compute theta_0's update step
    theta_0 -= alpha * 1 / n * np.dot((h - y),  np.array([[1] * n]).T)

    # Finally compute theta_1's update step
    theta_1 -= alpha * delta_h

    return theta_0, theta_1


'''
Linear regression algorithm.
'''
def linear_regression(X, y, epochs=100000, alpha=0.02):
    theta_0 = 0
    theta_1 = 0
    n = len(X)
    for epoch in range(epochs):
        theta_0, theta_1 = gradient_descent_step(X, y, theta_0, theta_1, alpha)
        if epoch % (epochs / 10) == 0:
            h = theta_0 + theta_1 * X
            loss = mse(X, y, h)
            print('{} done. theta_0: {} theta_1: {} Loss {}'.format(100 * (epoch + (epochs / 10)) / epochs, theta_0, theta_1, loss))
    return theta_0, theta_1


if __name__ == '__main__' :
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.asarray([8, 14, 20, 26, 32])
    linear_regression(X.flatten(), y.flatten())
