import random
import math
import particle

"""
En cada lugar de interaccion vamos a definir un particle source, y ver
cuales van a sobrevivir

"""

class Particle_Source:

    def __init__(self, position, N):

        self.position = position
        self.N = N
        self.particles = []

        for n in range(N):

            # damos una distribucion inicial con mu_z = 1
            # es decir voy a poner el detector sobre el eje z
            # para simplificar las cosas

            phi = 2*math.pi*random.random()
            cos_theta = 1 - 2*random.random()
            sin_theta = math.sqrt(1- cos_theta**2)

            mu_x = sin_theta*math.cos(phi)
            mu_y = sin_theta*math.sin(phi)
            mu_z = cos_theta

            tmp_particle = particle.Particle(n,self.position, [mu_x, mu_y, mu_z], 10)

            self.particles.append(tmp_particle)
