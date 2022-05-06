import matplotlib.pyplot as plt

fac_table = {}


def fac(x):
    if (x == 0):
        return 1
    if (x in fac_table):
        return fac_table[x]
    y = x * fac(x-1)
    fac_table[x] = y
    return y


def choose(n, r):
    return fac(n) / (fac(r) * fac(n-r))


def act_marks(X, n, pos_marks, neg_marks):
    return pos_marks * X - neg_marks * (n - X)


def binomial_distrib(x, n, p, q):
    return choose(n, x) * p**x * q**(n-x)


if __name__ == "__main__":
    # number of questions
    n = 10
    # number of options
    Q = 4
    # positive marks
    pos_marks = 3
    # negative marks
    neg_marks = 1

    data = [(act_marks(X, n, pos_marks, neg_marks), binomial_distrib(X, n, 1/Q, 1-(1/Q)))
            for X in range(0, n+1)]

    x = []
    y = []

    total_prob = 0
    for d in data:
        print(d)
        j, k = d
        total_prob += k
        x.append(j)
        y.append(k)

    # print("total prob =", total_prob)
    print("error", total_prob - 1.0)

    plt.plot(x, y)
    plt.show()
