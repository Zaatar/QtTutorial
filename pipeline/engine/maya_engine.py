from pipeline.engine.engine import Engine
import six

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

try:
    import maya.cmds as cmds
except:
    cmds = None


class MayaEngine(Engine):
    def __init__(self):
        self.implements = ['Open', 'Save', 'Export As Alembic']

    def open(self, file):
        cmds.file(file, open=True)

    def save(self, file, file_name):
        cmds.file(rename=file_name)
        cmds.file(file, save=True)

    def reference(self, path):
        cmds.file(path, reference=True)

    def alembic_export(self, start, end, root, save_name, scene_obj_name):
        final_save = self.export_path_generator(root, save_name, '.abc')
        command = f'-frameRange {start} {end} -uvWrite -worldSpace -root {scene_obj_name} -file {final_save}'
        cmds.AbcExport(j=command)

    def get_selection(self):
        selected_objs = cmds.ls(selection=True, tail=1)
        return selected_objs

    def export_path_generator(self, root, save_name, extension):
        path = Path(root)
        name_ext_combination = save_name + extension
        return path / name_ext_combination


