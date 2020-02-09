import numpy as np
import matplotlib.pyplot as plt


class Slot:
    def __init__(self, m):
        """
        init m with its own value.  this 'm' is meant to be hidden value to a player.
        :param m:
        """
        self.m = m
        self.mean = 0
        self.N = 0

    def pull(self):
        """
        return m + random number, it means return is close to m
        :return:
        """
        return np.random.randn() + self.m

    def update(self, x):
        """
        update mean with new value of x
        :param x: new value from pull()
        :return: update total N and mean
        """
        self.N += 1
        self.mean = (1-1.0/self.N) * self.mean + 1/self.N * x


def run_experiment(m1, m2, m3, eps, N):
    """
    run three different Slots with different hidden return values.
    :param m1: hidden return value
    :param m2: hidden return value
    :param m3: hidden return value
    :param eps: epsilon-greedy value
    :param N: number of plays per each Slots
    :return: cumulative average
    """
    bandits = [Slot(m1), Slot(m2), Slot(m3)]

    data = np.empty(N)

    for i in range(N):
        # epsilon greedy
        p = np.random.random()
        if p < eps:
            j = np.random.choice(3)
        else:
            j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        # for the plot
        data[i] = x
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    # plot moving average ctr
    plt.plot(cumulative_average)
    plt.plot(np.ones(N) * m1)
    plt.plot(np.ones(N) * m2)
    plt.plot(np.ones(N) * m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average


if __name__ == '__main__':
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000)
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)

    # log scale plot
    plt.plot(c_1, label='eps = 0.1')
    plt.plot(c_05, label='eps = 0.05')
    plt.plot(c_01, label='eps = 0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(c_1, label='eps = 0.1')
    plt.plot(c_05, label='eps = 0.05')
    plt.plot(c_01, label='eps = 0.01')
    plt.legend()
    plt.show()
