"""Lab 2 Task 2
This module contains functions for simulating Brownian motion
and analyzing the results
"""
import numpy as np
import matplotlib.pyplot as plt

def brown1(Nt,M,dt=1):
    """Run M Brownian motion simulations each consisting of Nt time steps
    with time step = dt
    Returns: X: the M trajectories; Xm: the mean across these M samples; Xv:
    the variance across these M samples
    """
    from numpy.random import randn

    #Initialize variable
    X = np.zeros((M,Nt+1))

    #1D Brownian motion: X_j+1 = X_j + sqrt(dt)*N(0,1)
    for i in range(M):
        for j in range(Nt):
            X[i,j+1] = X[i,j] + np.sqrt(dt)*randn(1)

    Xm = np.mean(X,axis=0)
    Xv = np.var(X,axis=0)
    return X,Xm,Xv


def plot_position_vs_time(X,dt=1):
    Nt = X.shape[1] - 1
    t = np.arange(0, (Nt + 1) * dt, dt)
    plt.plot(t, np.transpose(X))
    plt.show()


def plot_std_vs_time(Xv,dt=1):
    Nt = Xv.shape[0] - 1
    t = np.arange(0, (Nt + 1) * dt, dt)
    plt.plot(t, Xv)
    plt.show()


def analyze(display=False):
    """Complete this function to analyze simulation error
    """
    dt = 1
    Nt = int(np.ceil(100/dt))
    Mvalues = np.logspace(0,10,11,base=2).astype(int)
    var = np.zeros(11)
    error = np.zeros(11)
    for n in range(Mvalues.shape[0]):
        _,_,Xv = brown1(Nt,Mvalues[n],dt)
        var[n] = Xv[Nt+1]
        error[n] = np.abs(Nt*dt - var[n])
    return Mvalues,var,error
