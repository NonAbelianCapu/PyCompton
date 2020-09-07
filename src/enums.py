from enum import Enum

class Event(Enum):

    PHOTO = "photo_electric"
    COMPTON = "compton"
    PAIR = "pair_production"
    TRIPLE =  "triplet production"

class Detector_types(Enum):

	RECTANGULAR = "Rec"
	SPHERE = "Sph"
	CUSTOM = "Cst"
