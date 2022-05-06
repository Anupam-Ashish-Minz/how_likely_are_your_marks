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


def comb(n, r):
    return fac(n) / (fac(r) * fac(n-r))

def act_marks(X, n, plus_marks, neg_marks):
    return plus_marks * X - neg_marks * (n - X)

if __name__ == "__main__":
    n = 10
    Q = 4

    # data = [(i, comb(10, i)/(2**10)) for i in range(0, 11)]

    # 3 marks positive for each right answer and 1 marks negative for each
    # wrong answer
    data = [(act_marks(X, n, 1, 0), comb(n, X) * (((1/Q)**X * ((Q-1)/Q)**(n-X))))
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

    print("total prob =", total_prob)

    plt.plot(x, y)
    # plt.xticks(x)
    # plt.yticks(y)
    plt.show()
