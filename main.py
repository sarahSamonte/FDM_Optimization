import numpy
import math
from stl import mesh


def rotate(mesh, axis, angle):
	mesh.rotate(axis, math.radians(angle))
	return mesh

filepath = 'stl/Part1.stl'
#open stl file
mesh = mesh.Mesh.from_file(filepath)
angle = 30
nameAngle = 30

for i in range(12):
	#rotate in y axis 
	mesh = rotate(mesh, [0.5, 0.0, 0.0], angle)
	mesh.save("stl/x" + str(nameAngle) + ".stl")
	nameAngle += 30
	
nameAngle = 30	
for i in range(12):
	#roate in x axis
	mesh = rotate(mesh, [0.0, 0.5, 0.0], angle)
	mesh.save("stl/y" + str(nameAngle) + ".stl")
	nameAngle += 30
