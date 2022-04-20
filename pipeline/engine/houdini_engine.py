from pipeline.engine.engine import Engine

try:
    import hou
except:
    hou = None


class HoudiniEngine(Engine):
    def __init__(self):
        self.implements = ['Open', 'Save', 'Merge']

    def open(self, file):
        hou.hipFile.load(file)

    def save(self, file_name):
        hou.hipFile.save(file_name)

    def merge(self, file_name):
        hou.hipFile.merge(file_name)
