import numpy as np
import matplotlib.pyplot as plt
import warnings
from enum import Enum

class Detector_types(Enum):

	RECTANGULAR = "rec"
	SPHERE = "sph"

class Detector:

	def __init__(self, geometry, params, position):


		if not isinstance(geometry, Detector_types):

			# Si la geometria esta mal pasamos a una geometria
			# por defecto, es decir rectangular

			self.geometry_type = Detector_types.RECTANGULAR
			# WARNING:
			warning.warn("Geometry not specified, using default")

		self.parameters = parameters
		self.position = position
		self.efficiency = 1


	def parametric_check(self, position):

		# implementar funciones para chequear
		# si esta en el volumen 

		pass
