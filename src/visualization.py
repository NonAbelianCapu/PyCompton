from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
import particle
import particle_source
import detector

# genero las particulas y los detectores

new_particle_source = particle_source.Particle_Source([0,0,0],100)
new_type = detector. Detector_types.RECTANGULAR
new_detector = detector.Detector(new_type, [0,0,5])
print(new_detector.get_mesh())


x_cords = []
y_cords = []
z_cords = []

for p in new_particle_source.particles:

    x = []
    y = []
    z = []

    t_max = 35
    t = 0

    while t < t_max:

        xs = p.position[0]
        ys = p.position[1]
        zs = p.position[2]

        x.append(xs)
        y.append(ys)
        z.append(zs)

        p.evolve_particle(0.3)

        t = t + 1



    x_cords.append(x)
    y_cords.append(y)
    z_cords.append(z)

# hacemos la clase de visualizacion
verts = new_detector.get_mesh()[0]
faces = new_detector.get_mesh()[1]
colors = new_detector.get_mesh()[2]
"""
## Mesh item will automatically compute face normals.

"""

class Visualizer(object):

    def __init__(self):

        self.traces = dict()
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 60
        self.w.setWindowTitle('pyqtgraph example: GLLinePlotItem')
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.show()

        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.w.addItem(gz)

        m1 = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False)
        m1.translate(0, 10, 0)
        m1.setGLOptions('additive')
        self.w.addItem(m1)

        self.n = new_particle_source.N

        for i in range(self.n):

            pts = np.vstack([x_cords[i], y_cords[i], z_cords[i]]).transpose()
            self.traces[i] = gl.GLLinePlotItem(pos=pts, antialias=True)
            self.w.addItem(self.traces[i])

    def start(self):

        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()



## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    v = Visualizer()
    v.start()
