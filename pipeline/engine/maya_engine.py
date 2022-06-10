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
        objs_in_scene = scene_obj_name.split(", ")
        root_obj = ''
        for abc_obj in objs_in_scene:
            root_obj = root_obj + f' -root {abc_obj}'

        command = f'-frameRange {start} {end} -uvWrite -writeFaceSets -worldSpace -writeUVSets -stripNamespaces' \
                  f'{root_obj} -file {final_save}'

        cmds.AbcExport(j=command)

    def get_selection(self):
        # selected_objs = cmds.ls(selection=True, tail=1)
        selected_objs = cmds.ls(selection=True)
        return selected_objs

    def export_path_generator(self, root, save_name, extension):
        path = Path(root)
        name_ext_combination = save_name + extension
        return path / name_ext_combination

    # Just to test window
    def import_asset_ue(self, import_file_name, destination_path, dcc_save_name, save_after_every_import,
                        replace_existing):
        print_statement = f'The file import name is {import_file_name}, the destination path is ' \
                          f'{destination_path}, the dcc save name is {dcc_save_name}, it saves after every ' \
                          f'import {save_after_every_import} and it replaces existing {replace_existing}'
        print(print_statement)
