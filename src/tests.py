import particle
import particle_source
import detector

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt

new_type = detector. Detector_types.RECTANGULAR
new_detector = detector.Detector(new_type, [0,0,5])

print("Position:",new_detector.position)
print("L:",new_detector.L)
print("eff:", new_detector.density)

new_particle_source = particle_source.Particle_Source([0,0,0],10)
new_particle_source_1 = particle_source.Particle_Source([0,0,5],10)

# estos no deberian estar en el detector

for p in new_particle_source.particles:
    p.pprint()
    if new_detector.parametric_check(p):
        print("Is in detector")


# estos deberian estar en el detector

for p in new_particle_source_1.particles:
    p.pprint()
    if new_detector.parametric_check(p):
        print("Is in detector")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


t_max = 75
t = 0

while t < t_max:

    for p in new_particle_source.particles:

        xs = p.position[0]
        ys = p.position[1]
        zs = p.position[2]

        ax.scatter(xs,ys,zs)

        if new_detector.parametric_check(p):
            print("{} Is in detector".format(p.id))

        p.evolve_particle(0.3)

    t = t + 1

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
