import numpy as np
import matplotlib.pyplot as plt
import detector

class Particle:

	def __init__(self,pos,mu,energy):

		self.__x = pos[0]
		self.__y = pos[1]
		self.__z = pos[2]


		self.__mu_x = mu[0]
		self.__mu_y = mu[1]
		self.__mu_z = mu[2]

		self.energy = 0
		self.__weight = 1
		self.__is_alive = True


	@property
	def mu(self):

		return [self.__mu_x,self.__mu_y, self.__mu_z]

	@property
	def position(self):

		return [self.__x, self.__y, self.__z]


	def pprint(self):
		print(self.__x,self.__y,self.__z,self.__mu_x,self.__mu_y, self.__mu_z)

	def update_weight(self,mu_t,mu_a):

		treshold = 0.2

		self.weight = self.weight*(1- mu_a/mu_t)

		if self.weight < treshold:

			self.is_alive = False

	def is_in_detector(self,detector):

		if isinstance(volume, detector.Detector):
			volume.parametric_check(self.position)

		else:
			raise Warning("Volume is not a detector")



	def update_position(self,s):

		self.x = self.x + self.mu_x*s
		self.y = self.y + self.mu_y*s
		self.z = self.z + self.mu_z*s

	def update_energy(self):
		pass 

	def update_cosines(self):

		pass
