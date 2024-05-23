# let's decide a equation of x = [3, 6, 9, 12, ]

import numpy as np;

def ImplementGradientDescent(x, y, iterations, a, b):
    m = len(x);
    lr = 0.01;
    for i in range(iterations):
        y_preds = a + b*x;
        error = y_preds - y;
        error_a = np.sum(error)/m;
        error_b = np.sum(error*x)/m;
        a = a - lr*error_a;
        b = b - lr*error_b;
    print(f"after {iterations} value of a is {a}")
    print(f"after {iterations} value of b is {b}")
    # print(f"after {iterations} error is {}")

if __name__ == "__main__":
    x = []
    y = []
    for i in range(200):
        x.append(i*3)
        y.append(i*3 + 2);
    print(x)
    print(y)
    ImplementGradientDescent(np.array(x), np.array(y), 1000, 1, 1);


