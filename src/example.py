import particle_source

source = particle_source.Particle_Source([0,0,0],10)
source_particles = source.particles

for p in source_particles:
    p.pprint()
