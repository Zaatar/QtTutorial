from pipeline.engine.engine import Engine

try:
    import unreal
except:
    unreal = None


class UnrealEngine(Engine):
    def __init__(self):
        self.implements = ['Import Alembic']

    def import_abc(self):
        pass
