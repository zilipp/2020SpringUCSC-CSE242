import numpy as np


X = np.array([[1, 1, 1], [0.25, 0.25, 0], [1, 2, 1], [2, 1, 1],
              [0, 0, 0], [2, 2, 1], [1, 0, 0], [1.5, 1.5, 1], [0, 1, 0]])

x1, x2 = [], []
for i in range(X.shape[0]):
    if X[i, 2] == 1:
        x1.append([X[i, 0], X[i, 1]])
    else:
        x2.append([X[i, 0], X[i, 1]])
x1, x2 = np.array(x1), np.array(x2)


def optimizer(x1, x2):
    w, b = 0, 0
    all_data = np.array([])
    for i in range(len(x1)):
        all_data = np.append(all_data, x1[i][0])
    for i in range(len(x2)):
        all_data = np.append(all_data, x2[i][0])
    max_x = max(all_data)
    min_x = min(all_data)
    learning_rate = [max_x * 0.1, max_x * 0.01, max_x * 0.001, ]

    opt_dict = {}
    transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    b_step_size = 5
    b_multiple = 5
    w_optimum = max_x * 10

    for lrate in learning_rate:
        w = np.array([w_optimum, w_optimum])
        optimized = False

        while not optimized:
            for b in np.arange(-1 * (max_x * b_step_size), max_x * b_step_size, lrate * b_multiple):
                for transformation in transforms:
                    w_t = w * transformation

                    correctly_classified = True
                    for i in range(len(x1)):
                        if not (np.dot(w_t, x1[i]) + b) >= 1:
                            correctly_classified = False
                    for i in range(len(x2)):
                        if not (np.dot(w_t, x2[i]) + b) <= -1:
                            correctly_classified = False

                    if correctly_classified:
                        opt_dict[np.linalg.norm(w_t)] = [w_t, b]  # store w, b for minimum magnitude

            if w[0] < 0:
                optimized = True
            else:
                w = w - lrate

        norms = sorted([n for n in opt_dict])
        if len(norms) > 0:
            opt_choice = opt_dict[norms[0]]
            w = opt_choice[0]
            b = opt_choice[1]

        w_optimum = opt_choice[0][0] + lrate * 2

    return w, b

w, b = optimizer(x1, x2)
print(w, b)