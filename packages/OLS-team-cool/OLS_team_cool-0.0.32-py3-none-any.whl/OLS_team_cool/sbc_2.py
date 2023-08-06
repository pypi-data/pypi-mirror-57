import numpy as np
import scipy.stats as st
import statsmodels.api as sm
from OLS_team_cool import OLS
import matplotlib.pyplot as plt

def demand(alpha,delta,p,xi_d):
    if delta <= 0 :
        q_d = alpha + delta * p + xi_d
    else:
        q_d = np.nan
        print("ERROR: delta should be less than 0.")

    return q_d


def supply(gamma, psi,p,xi_s):
    if psi >= 0:
        q_s = gamma + psi * p +  xi_s
    else:
        q_s = np.nan
        print("ERROR: psi should be greater than 0.")

    return q_s

N = 1000

def simulate(N):
    xi_d = np.random.normal(0,1,(N,1))
    xi_s = np.random.normal(0,1,(N,1))

    alpha = np.random.randn()
    delta = -np.random.exponential()
    gamma = np.random.randn()
    psi = np.random.exponential()
    p = np.zeros((N,1))

    q_d = demand(alpha,delta,p,xi_d)
    q_s = supply(gamma, psi,p,xi_s)

    while np.sum(abs(q_d - q_s)) > 0.01:
        p = p + 0.1 * (q_d - q_s)
        q_d = demand(alpha,delta,p,xi_d)
        q_s = supply(gamma, psi,p,xi_s)

plt.plot(xi_d,p,'.')
plt.plot(xi_s,p,'.')
