import particle as p
import detector as dct
import particle_source as ps
import cross_sections as xs
import numpy as np
import matplotlib.pyplot as plt
import random

class Simulation(object):
    """docstring for ."""

    def __init__(self, T, dt, detector, particle_source):

        self.T = T
        self.dt = dt

        if not isinstance(detector,  dct.Detector):
            raise TypeError("Detector is not Detector class")

        self.detector = detector

        if not isinstance(particle_source, ps.Particle_Source):
            raise TypeError("Particle source is not Particle Source Class")

        self.p_source = particle_source



    def gen_flight_distance(self, particle):

        r = random.random()
        return -np.log(r)


    def evolve(self):
        pass
