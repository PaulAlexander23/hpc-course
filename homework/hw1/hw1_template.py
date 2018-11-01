"""M3C 2018 Homework 1
"""
import numpy as np
import matplotlib.pyplot as plt


def simulate1(N,Nt,b,e):
    """Simulate C vs. M competition on N x N grid over
    Nt generations. b and e are model parameters
    to be used in fitness calculations
    Output: S: Status of each gridpoint at tend of somulation, 0=M, 1=C
    fc: fraction of villages which are C at all Nt+1 times
    Do not modify input or return statement without instructor's permission.
    """
    #Set initial condition
    S  = np.ones((N,N),dtype=int) #Status of each gridpoint: 0=M, 1=C
    j = int((N-1)/2)
    S[j-1:j+2,j-1:j+2] = 0

    fc = np.zeros(Nt+1) #Fraction of points which are C
    fc[0] = S.sum()/(N*N)

    return S,fc

def plot_S(S):
    """Simple function to create plot from input S matrix
    """
    ind_s0 = np.where(S==0) #C locations
    ind_s1 = np.where(S==1) #M locations
    plt.plot(ind_s0[1],ind_s0[0],'rs')
    plt.hold(True)
    plt.plot(ind_s1[1],ind_s1[0],'bs')
    plt.hold(False)
    plt.show()
    plt.pause(0.05)
    return None


def simulate2(N,Nt,b,e):
    """Simulation code for Part 2, add input variables as needed
    """


def analyze():
    """ Add input variables as needed
    """



if __name__ == '__main__':
    #The code here should call analyze and generate the
    #figures that you are submitting with your code
    output = analyze()
