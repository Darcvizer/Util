import bpy
#########################################################################################
#             This addon is made on the basis of the MultiEdit and uses it.             #
#     The authors of the adage are the MultiEdit Antonis Karvelas, Dimitris Chloyupis.  #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#########################################################################################
bl_info = {
	"name": "Quick access to edit mode :)",
	"location": "View3D > Add > Mesh > Quick access to edit mode,",
	"description": "Quick access to edit mode",
	"author": "Vladislav Kindushov",
	"version": (1),
	"blender": (2, 7, 9),
	"category": "Mesh",
}


def SaveSelection(context):
	sel = bpy.context.selected_objects
	st = 'Multy_Object_Edit,'
	st = (st + bpy.context.active_object.name) + ','
	for i in sel:
		st = (st + i.name) + ','

	return st


def ReturnSelection(context,st):
	object = ''
	act = False
	for i in st[18:]:
		object += i
		if i == ',':
			object = object[:-1]
			if act == False:
				bpy.context.scene.objects.active = bpy.data.objects[object]
				act = True
			bpy.data.objects[object].select = True
			object = ''




class fast_to_vertex(bpy.types.Operator):
	bl_idname = "mesh.fast_to_vertex"
	bl_label = "fast_to_vertex"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return (context.mode == "OBJECT") or (context.mode == "EDIT_MESH")

	def execute(self, context):
		if context.mode == "OBJECT":
			sel = bpy.context.selected_objects
			if len(sel) > 1:
				st = SaveSelection(context)
				bpy.data.objects.new(st, None)
				bpy.ops.objects.multiedit_enter_operator()
				bpy.context.tool_settings.mesh_select_mode = (True, False, False)
			else:
				bpy.ops.object.mode_set(mode='EDIT')
				bpy.context.tool_settings.mesh_select_mode = (True, False, False)

		else:
			bpy.context.tool_settings.mesh_select_mode = (True, False, False)

		return {'FINISHED'}


class fast_to_edge(bpy.types.Operator):
	bl_idname = "mesh.fast_to_edge"
	bl_label = "fast_to_edge"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return (context.mode == "OBJECT") or (context.mode == "EDIT_MESH")

	def execute(self, context):
		if context.mode == "OBJECT":
			sel = bpy.context.selected_objects
			if len(sel) > 1:
				st = SaveSelection(context)
				bpy.data.objects.new(st, None)
				bpy.ops.objects.multiedit_enter_operator()
				bpy.context.tool_settings.mesh_select_mode = (False, True, False)
			else:
				bpy.ops.object.mode_set(mode='EDIT')
				bpy.context.tool_settings.mesh_select_mode = (False, True, False)

		else:
			bpy.context.tool_settings.mesh_select_mode = (False, True, False)

		return {'FINISHED'}


class fast_to_face(bpy.types.Operator):
	bl_idname = "mesh.fast_to_face"
	bl_label = "fast_to_face"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return (context.mode == "OBJECT") or (context.mode == "EDIT_MESH")

	def execute(self, context):
		if context.mode == "OBJECT":
			sel = bpy.context.selected_objects
			if len(sel) > 1:
				st = SaveSelection(context)
				bpy.data.objects.new(st, None)
				bpy.ops.objects.multiedit_enter_operator()
				bpy.context.tool_settings.mesh_select_mode = (False, False, True)
			else:
				bpy.ops.object.mode_set(mode='EDIT')
				bpy.context.tool_settings.mesh_select_mode = (False, False, True)

		else:
			bpy.context.tool_settings.mesh_select_mode = (False, False, True)

		return {'FINISHED'}

class fast_to_mode(bpy.types.Operator):
	bl_idname = "mesh.fast_to_mode"
	bl_label = "fast_to_mode"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return (context.mode == "OBJECT") or (context.mode == "EDIT_MESH")

	def execute(self, context):
		if context.mode == "OBJECT":
			sel = bpy.context.selected_objects
			if len(sel) > 1:
				bpy.ops.objects.multiedit_enter_operator()
			else:
				bpy.ops.object.mode_set(mode='EDIT')
		else:
			for i in reversed(bpy.data.objects):
				if i.name[:17] == 'Multy_Object_Edit':
					bpy.ops.objects.multiedit_exit_operator()
					ReturnSelection(context, i.name)
					bpy.data.objects.remove(bpy.data.objects[i.name], True)
					print(i.name)
					break
				else:
					bpy.ops.object.mode_set(mode='OBJECT')

		return {'FINISHED'}


def register():
	bpy.utils.register_class(fast_to_vertex)
	bpy.utils.register_class(fast_to_edge)
	bpy.utils.register_class(fast_to_face)
	bpy.utils.register_class(fast_to_mode)

	kc = bpy.context.window_manager.keyconfigs.addon

	if kc:
		km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
		kmi = km.keymap_items.new('mesh.fast_to_vertex', 'ONE', 'PRESS', )
		kmi = km.keymap_items.new('mesh.fast_to_edge', 'TWO', 'PRESS', )
		kmi = km.keymap_items.new('mesh.fast_to_face', 'THREE', 'PRESS', )
		kmi = km.keymap_items.new('mesh.fast_to_mode', 'FOUR', 'PRESS', )


def unregister():
	bpy.utils.unregister_class(fast_to_vertex)
	bpy.utils.unregister_class(fast_to_edge)
	bpy.utils.unregister_class(fast_to_face)
	bpy.utils.unregister_class(fast_to_mode)

	kc = bpy.context.window_manager.keyconfigs.addon
	if kc:
		km = kc.keymaps["3D View"]
		for kmi in km.keymap_items:
			if kmi.idname == 'mesh.fast_to_vertex':
				km.keymap_items.remove(kmi)
				break
		for kmi in km.keymap_items:
			if kmi.idname == 'mesh.fast_to_edge':
				km.keymap_items.remove(kmi)
				break
		for kmi in km.keymap_items:
			if kmi.idname == 'mesh.fast_to_face':
				km.keymap_items.remove(kmi)
				break
		for kmi in km.keymap_items:
			if kmi.idname == 'mesh.fast_to_mode':
				km.keymap_items.remove(kmi)
				break


if __name__ == "__main__":
	register()