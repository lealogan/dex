from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

deck = 60
hand = 7
#numlands = 26
for numlands in range(18,29):
    [M, n, N] = [deck, hand, numlands]
    rv = stats.hypergeom(M, n, N)
    x = np.arange(0, n+1)
    pmf_dogs = rv.pmf(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, pmf_dogs, 'bo')
    ax.vlines(x, 0, pmf_dogs, lw=2)
    ax.set_xlabel('# lands in starting hand')
    ax.set_ylabel('hypergeom PMF')
    #plt.show()
    plt.savefig('lands{}.png'.format(numlands))
