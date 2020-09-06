import particle
import warnings
from enum import Enum
import numpy as np

class Detector_types(Enum):

	RECTANGULAR = "Rec"
	SPHERE = "Sph"
	CUSTOM = "Cst"

class Detector:

	def __init__(self, geometry, position):


		if not isinstance(geometry, Detector_types):

			# Si la geometria esta mal pasamos a una geometria
			# por defecto, es decir rectangular

			self.geometry_type = Detector_types.RECTANGULAR
			# WARNING:
			warning.warn("Geometry not specified, using default (Rectangular)")

			self.L = 3
			self.H = 3
			self.D = 2

		if geometry == Detector_types.RECTANGULAR:

			self.geometry_type = Detector_types.RECTANGULAR
			self.L = 3
			self.H = 3
			self.D = 2


		self.position = position
		self.density = 1
		self.efficiency = 1

		# aca van a ir todas las energias depositadas, que eventualmente voy a tener
		# que discretizar para poder hacer histogramas con una precision parecida a un MCA

		self.deposited_energy = []

	def parametric_check(self, p):

		# implementar funciones para chequear
		# si esta en el volumen

		if isinstance(p, particle.Particle):

			pos = p.position

			x = pos[0]
			y = pos[1]
			z = pos[2]

			if (x <= self.position[0] + self.L/2 and x >= self.position[0] - self.L/2):
				if (y <= self.position[1] + self.H/2 and y >= self.position[1] - self.H/2):
					if (z <= self.position[2] + self.D/2 and z >= self.position[2] - self.D/2):

						return True

					else:
						return False
				else:
					return False

			else:
				return False

		else:
			raise TypeError("Particle is not a particle class")



	def deposit_energy(self, p):

		if isinstance(p, particle.Particle):

			# aca voy a tener que depositar la energia del electron si es compton
			# o depositar la energia total si fue foto-electrico

			pass

		else:
			raise TypeError("Particle is not a particle class")


	def get_mesh(self):

		verts = np.array([
		[self.L/2, -self.H/2, -self.D/2],
		[self.L/2, self.H/2, -self.D/2],
		[-self.L/2, -self.H/2, -self.D/2],
		[-self.L/2, self.H/2, -self.D/2],
		[self.L/2, -self.H/2, self.D/2],
		[self.L/2, self.H/2, self.D/2],
		[-self.L/2, -self.H/2, self.D/2],
		[-self.L/2, self.H/2, self.D/2]])


		faces = np.array([
		[0,1,3], [0,1,2],
		[0,1,5], [0,4,5],
		[0,2,4], [2,4,6],
		[3,2,7], [2,6,7],
		[1,3,5], [3,5,7],
		[4,5,6], [5,6,7]])


		colors = np.array([
		    [1, 0, 0, 0.5],
		    [0, 0, 0, 0.5],
		    [1, 0, 0, 0.5],
			[1, 0, 0, 0.5],
			[1, 0, 0, 0.5],
			[1, 0, 1, 0.5],
			[1, 0, 0, 0.5],
		    [1, 0, 0, 0.5],
		    [1, 0, 0, 0.5],
			[1, 0, 0, 0.5],
			[1, 0, 0, 0.5],
			[1, 0, 0, 0.5]

		])

		# Aca voy a tener que armar el mesh para pasar a OpenGL
		# y poder graficar

		return (verts, faces, colors)



class Rectangular_Detector(Detector):

	def parametric_check(self, position):

		pass

class Spherical_Detector(Detector):

	def parametric_check(self, position):

		pass
