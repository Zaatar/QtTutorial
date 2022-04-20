from pipeline.engine.engine import Engine

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

    def alembic_export(self, start, end, root, save_name):
        command = f'-frameRange {start} {end} -uvWrite -worldSpace {root} -file {save_name}'
        cmds.AbcExport(j=command)