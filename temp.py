import bpy

data = bpy.context.active_object.data
mat = bpy.context.active_object.matrix_world
LV = len(data.vertices)
LE = len(data.edges)
LF = len(data.polygons)

temp = True
name = []
for i in bpy.data.objects:
	if data.name == i.data.name:
		continue
	if len(i.data.vertices) == LV and len(i.data.edges) == LE and len(i.data.polygons) == LF:
		for j in i.data.vertices:
			if j.co != data.vertices[j.index].co:
				temp = False
				continue
		if temp:
			name.append(i.name)

bpy.ops.object.select_all(action='DESELECT')

for i in name:
	bpy.data.objects[i].select = True

bpy.ops.object.make_links_data(type='OBDATA')
bpy.context.active_object.select = True
bpy.ops.object.select_linked(type='OBDATA')


import bpy

name = []
temp_name = None
count = 0
for i in bpy.data.objects:
	temp_name = i.data.name
	for j in bpy.data.objects:
		if i.name == j.name:
			continue
		elif i.data.name == j.data.name:
			count += 1
	
	if count == 0:
		name.append(i.name)
	else:
		count = 0
		continue
for i in bpy.data.objects:
	if i.name in name:
		i.select = True
	
import bpy
mesh = []
for i in bpy.context.visible_objects:
	if i.data.name not in mesh:
		i.select = True
		mesh.append(i.data.name)
