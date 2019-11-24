bl_info = {
    "name": "Sort Bones Alphabetically",
    "blender": (2, 80, 0),
    "author": "Lars Wobus",
    "category": "Rigging"
}

import bpy
from collections import deque

class BoneSorting(bpy.types.Operator):
    """Sort bones of active armature alphabetically"""
    bl_idname = "armature.bone_sorting"
    bl_label = "Sort Bones Alphabetically"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
      bpy.ops.object.mode_set(mode='EDIT', toggle=True)
      bpy.ops.armature.select_all(action='DESELECT')

      armature_id = bpy.context.active_object.id_data.name
      edit_bones = bpy.context.active_object.data.edit_bones

      queue = deque([]) 

      for name in sorted (edit_bones.keys()) :
        queue.append(name) 
        bone = edit_bones[name]
        edit_bones.active = bone
        edit_bones.active.select = True
        edit_bones.active.select_head = True
        edit_bones.active.select_tail = True
        bpy.ops.armature.duplicate()
        edit_bones.active.select = False
        edit_bones.active.select_head = False
        edit_bones.active.select_tail = False
        edit_bones.remove(bone)
        
      for name in sorted (edit_bones.keys()) :
        edit_bones[name].name = queue.popleft()
        
      bpy.ops.object.mode_set(mode='OBJECT', toggle=True)

      return {'FINISHED'}

def menu_func(self, context):
  self.layout.operator(BoneSorting.bl_idname)
      
def register():
    bpy.utils.register_class(BoneSorting)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BoneSorting)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
