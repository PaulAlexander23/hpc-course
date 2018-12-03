"""Final project, part 2"""
import numpy as np
import matplotlib.pyplot as plt
#from m1 import bmodel as bm #assumes p2.f90 has been compiled with: f2py -c p2.f90 -m m1


def simulate_jacobi(n,input_num=(10000,1e-8),input_mod=(1,1,1,2,1.5),display=False):
    """ Solve contamination model equations with
        jacobi iteration.
        Input:
            input_num: 2-element tuple containing kmax (max number of iterations
                        and tol (convergence test parameter)
            input_mod: 5-element tuple containing g,k_bc,s0,r0,t0 --
                        g: bacteria death rate
                        k_bc: r=1 boundary condition parameter
                        s0,r0,t0: source function parameters
            display: if True, a contour plot showing the final concetration field is generated
        Output:
            C,deltac: Final concentration field and |max change in C| each iteration
    """
    #Set model parameters------

    kmax,tol = input_num
    g,k_bc,s0,r0,t0 = input_mod
    #-------------------------------------------
    #Set Numerical parameters
    Del = np.pi/(n+1)
    r = np.linspace(1,1+np.pi,n+2)
    t = np.linspace(0,np.pi,n+2) #theta
    tg,rg = np.meshgrid(t,r) # r-theta grid

    #Factors used in update equation
    rinv2 = 1.0/(rg*rg)
    fac = 1.0/(2 + 2*rinv2+Del*Del*g)
    facp = (1+0.5*Del/rg)*fac
    facm = (1-0.5*Del/rg)*fac
    fac2 = fac*rinv2

    #set initial condition/boundary conditions
    C = (np.sin(k_bc*tg)**2)*(np.pi+1.-rg)/np.pi

    #set source function, Sdel2 = S*del^2*fac
    Sdel2 = s0*np.exp(-20.*((rg-r0)**2+(tg-t0)**2))*(Del**2)*fac

    deltac = []
    Cnew = C.copy()

    #Jacobi iteration
    for k in range(kmax):
        #Compute Cnew
        Cnew[1:-1,1:-1] = Sdel2[1:-1,1:-1] + C[2:,1:-1]*facp[1:-1,1:-1] + C[:-2,1:-1]*facm[1:-1,1:-1] + (C[1:-1,:-2] + C[1:-1,2:])*fac2[1:-1,1:-1] #Jacobi update
        #Compute delta_p
        deltac += [np.max(np.abs(C-Cnew))]
        C[1:-1,1:-1] = Cnew[1:-1,1:-1]
        if k%1000==0: print("k,dcmax:",k,deltac[k])
        #check for convergence
        if deltac[k]<tol:
            print("Converged,k=%d,dc_max=%28.16f " %(k,deltac[k]))
            break

    deltac = deltac[:k+1]

    if display:
        plt.figure()
        plt.contour(t,r,C,50)
        plt.xlabel('theta')
        plt.ylabel('r')
        plt.title('Final concentration field')

    return C,deltac



def simulate(n,input_num=(10000,1e-8),input_mod=(1,1,1,2,1.5)):
    """ Solve contamination model equations with
        OSI method, input/output same as in simulate_jacobi above
    """
    #Set model parameters------

    kmax,tol = input_num
    g,k_bc,s0,r0,t0 = input_mod

    #Add code here


    C,deltac = None,None #Must be replaced
    return C,deltac


def performance():
    """Analyze performance of simulation codes
    Add input/output variables as needed.
    """

    return None


def analyze():
    """Analyze influence of modified
    boundary condition on contamination dynamics
        Add input/output variables as needed.
    """

    return None


if __name__=='__main__':
    #Add code below to call performance and analyze
    #and generate figures you are submitting in
    #your repo.
    input=()
