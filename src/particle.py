import numpy as np
import matplotlib.pyplot as plt
import detector

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

	def update_weight(self,mu_t,mu_a):

		treshold = 0.2

		self.__weight = self.__weight*(1- mu_a/mu_t)

		if self.__weight < treshold:

			self.__is_alive = False

	def is_in_detector(self,detector):

		# check if the particle is in the detector

		if isinstance(volume, detector.Detector):
			if volume.parametric_check(self):
				return True
			else:
				return False

		else:
			raise Warning("Volume is not a detector")

	def evolve_particle(self,s):

		self.__x = self.__x + self.__mu_x*s
		self.__y = self.__y + self.__mu_y*s
		self.__z = self.__z + self.__mu_z*s

	def update_energy(self):
		pass

	def update_cosines(self):

		pass
