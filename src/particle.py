import numpy as np
import matplotlib.pyplot as plt
import random
import detector as dct

class Particle:

    def __init__(self,id,pos,mu,energy):

        self.id = id

        self.__x = pos[0]
        self.__y = pos[1]
        self.__z = pos[2]


        self.__mu_x = mu[0]
        self.__mu_y = mu[1]
        self.__mu_z = mu[2]

        self.__energy = 0
        self.__weight = 1
        self.__is_alive = True


    @property
    def mu(self):

        return [self.__mu_x,self.__mu_y, self.__mu_z]

    @property
    def position(self):

        return [self.__x, self.__y, self.__z]

    @property
    def energy(self):
        return self.__energy

    @property
    def is_alive(self):
        return self.__is_alive

    @position.setter
    def position(self, value):

        self.__x = value[0]
        self.__y = value[1]
        self.__z = value[2]

    @energy.setter
    def energy(self, value):
        self.__energy = value

    def pprint(self):
        print(self.__x,self.__y,self.__z,self.__mu_x,self.__mu_y, self.__mu_z)

    def gen_random_angles(self):

        angle_data = {}
        zeta = random.random()
        phi = 2*np.pi*zeta

        angle_data["cos_theta"] = 2*zeta - 1
        angle_data["sin_theta"] = np.sqrt(1 - angle_data["cos_theta"]**2)
        angle_data["cos_phi"] = np.cos(phi)
        angle_data["sin_phi"] = np.sin(phi)

        return angle_data

    def update_weight(self,mu_t,mu_a):

        treshold = 0.2

        self.__weight = self.__weight*(1- mu_a/mu_t)

        if self.__weight < treshold:

            self.__is_alive = False

    def is_in_detector(self,detector):

        # check if the particle is in the detector

        if isinstance(detector, dct.Detector):
            if detector.parametric_check(self):
                return True
            else:
                return False

        else:
            raise Warning("Volume is not a detector")

    def evolve(self,s):

        self.__x = self.__x + self.__mu_x*s
        self.__y = self.__y + self.__mu_y*s
        self.__z = self.__z + self.__mu_z*s

    def update_energy(self, cos_theta):

        pass

    def update_cosines(self, sin_theta, cos_theta, sin_phi, cos_phi):

        # we update to the new cosines after interaction

        self.__mu_x = sin_theta*(self.__mu_x*self.__mu_z - self.__mu_y*sin_phi)/(np.sqrt(1 - self.__mu_z**2)) + self.__mu_x*cos_theta
        self.__mu_y = sin_theta*(self.__mu_y*self.__mu_z + self.__mu_x*sin_phi)/(np.sqrt(1 - self.__mu_z**2)) + self.__mu_y*cos_theta
        self.__mu_z = -sin_theta*cos_phi*np.sqrt(1 - self.__mu_z**2) + self.__mu_z*cos_theta
