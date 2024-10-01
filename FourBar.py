import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin, atan2


def FourBarCode(zeroth_side, first_side,second_side,third_side, rotation_number, velocity, XLim, YLim):

    """
    Simulates the motion of a four-bar linkage mechanism and plots it.

    Parameters:
    zeroth_side (float): Length of the fixed ground link (side 0).
    first_side (float): Length of the crank link (side 1).
    second_side (float): Length of the coupler link (side 2).
    third_side (float): Length of the output link (side 3).
    rotation_number (int): Number of complete rotations of the crank (side 1).
    velocity (float): Determines the resolution of the crank's motion (smaller values give finer simulation).
    XLim (list): Tuple defining the x-axis limits for the plot (e.g., (-10, 10)).
    YLim (list): Tuple defining the y-axis limits for the plot (e.g., (-10, 10)).

    """

    #Constants 
    a0 = zeroth_side;
    a1 = first_side;
    a2 = second_side;
    a3 = third_side;

    #Input theta_12
    input_angles = np.linspace(pi,rotation_number*2*pi, int(1/velocity*rotation_number*2*pi))
    X = []
    Y = []

    #Calculations
    for theta_12 in input_angles:

        A = 2*a0*a3 - 2*a1*a3*cos(theta_12)
        B = -2*a1*a3*sin(theta_12)
        C = a2**2-a0**2-a3**2-a1**2+2*a0*a1*cos(theta_12)
        t = (B - (B**2 - C**2 + A**2)**0.5)/(C + A)
        theta_14 = atan2(2*t/(1+t**2),(1-t**2)/(1+t**2))

        C_theta_13 = (a0 - a1*cos(theta_12) + a3*cos(theta_14)) / a2
        S_theta_13 = (-a1*sin(theta_12) + a3*sin(theta_14)) / a2
        theta_13 = atan2(S_theta_13, C_theta_13)

        X_coordinates = [0, a1*cos(theta_12), a1*cos(theta_12) + a2*cos(theta_13), a0]
        Y_coordinates = [0, a1*sin(theta_12), a1*sin(theta_12) + a2*sin(theta_13), 0]
        X.append(X_coordinates)
        Y.append(Y_coordinates)


    for i in range(0,len(X)):
        plt.xlim(XLim)
        plt.ylim(YLim)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.plot(X[i],Y[i])
        plt.show(block=False)
        plt.pause(0.001)
        plt.clf()

#Example Use
FourBarCode(25, 40, 40, 40, 3, 0.5, [-40,65], [-55,50])


