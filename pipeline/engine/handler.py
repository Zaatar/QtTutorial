import sys


def choose_handler():
    if 'maya' in sys.executable:
        from pipeline.engine.maya_engine import MayaEngine
        return MayaEngine()
    elif 'houdini' in sys.executable:
        from pipeline.engine.houdini_engine import HoudiniEngine
        return HoudiniEngine()
    else:
        return None
    # elif 'Unreal' in sys.executable:
    # Use Unreal Engine
