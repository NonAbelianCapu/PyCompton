import math
import numpy as np
import matplotlib.pyplot as plt

alpha = 1
r_e = 1

def low_photo(Z,k):

    # valid only for k < 0.9

    C = (16/3)*np.sqrt(2)*np.pi*(r_e**2)*alpha**4
    return C*(Z**4)/(k**(3.5))

def high_photo(Z,k):

    pass


def low_compton(Z,k):

    # valid for k < 0.2

    C = (8/3)*np.pi*Z*r_e**2
    sum = (1/(1+2*k)**2)*(1+ 2*k + (6/5)*k**2)

    return C*sum


def high_compton(Z,k):

    C = 2*np.pi*Z*r_e**2
    T1 = ((1+k)/(k**2))*(2*((1+k)/(1+2*k)) - np.log(1+2*k)/k)
    T2 = np.log(1 + 2*k)/(2*k) - (1 + 3*k)/(1 + 2*k)**2

    return C*(T1 + T2)


def total_compton(Z,k):
    k_values = []
    for value in k:
        if value < 0.2:
            k_values.append(low_compton(Z,value))
        else:
            k_values.append(high_compton(Z,value))

    return k_values



def compton_abs(Z,k):

    C = 2*np.pi*Z*r_e**2
    T1 = (2*(1+k)**2)/((k**2)*(1 + 2*k)) - (1 + 3*k)/((1 + 2*k)**2)
    T2 = -((1 + k)/(k**2))*((2*k**2 - 2*k - 1)/(1 + 2*k)**2) - (4*k**2)/(3*(1+2*k)**3)
    T3 = -((1+k)/(k**3) - 1/(2*k) + 1/(2*k**3))*np.log(1 + 2*k)

    return C*(T1 + T2 + T3)


def scatter_compton(Z,k):

    return (total_compton(Z,k) - compton_abs(Z,k))


k = np.linspace(0.1,1,1000)
plt.plot(k, low_photo(6,k))
plt.show()

plt.plot(k,total_compton(6,k), label="total")
plt.plot(k, compton_abs(6,k), label="abs")
plt.plot(k, scatter_compton(6,k), label="scatter")
plt.legend()
plt.show()


plt.plot(k, compton_abs(6,k)/total_compton(6,k),label="p_abs")
plt.plot(k, scatter_compton(6,k)/total_compton(6,k),label="p_scat")
plt.legend()
plt.show()
