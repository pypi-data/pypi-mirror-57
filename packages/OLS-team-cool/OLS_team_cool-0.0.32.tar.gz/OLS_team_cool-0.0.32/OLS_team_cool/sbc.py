import numpy as np
import scipy.stats as st
import statsmodels.api as sm
from OLS_team_cool import OLS
import matplotlib.pyplot as plt


N = 1000
p = 2
cf = 0.95
k = 10000

def sbc(model = "OLS",N,p,cf,k):

# Draw from a prior for the model parameters beta
    if model == "OLS":
        beta = np.sqrt(2) * np.random.randn(p,1)
        sigma = np.exp(np.random.randn(1))

# Step 3:
        x = np.random.randn(N,p)
        eps = np.random.normal(0,sigma,(N,1))
        y = (beta.T @ x.T).reshape(N,1) + eps

# Step 4:
        result = OLS(y,x,cf)
        beta_hat = result.get("Beta").reshape(-1,1)
        se_hat = result.get("Standard Error").reshape(-1,1)
        beta_distribut = np.ones((k,p)) * beta_hat.T + np.random.randn(k,p) * se_hat.T

        port_less = (beta_distribut - beta.T.reshape)


plt.hist(beta_distribut[:,1])
beta.shape

beta.T.reshape(k,p)
sigma
