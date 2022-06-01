import sys


def choose_handler():
    if 'maya' in sys.executable:
        from pipeline.engine.maya_engine import MayaEngine
        return MayaEngine()
    elif 'houdini' in sys.executable:
        from pipeline.engine.houdini_engine import HoudiniEngine
        return HoudiniEngine()
    elif 'UnrealEngine' in sys.executable:
        from pipeline.engine.unreal_engine import UnrealEngine
        return UnrealEngine()
    else:
        return None
    # elif 'Unreal' in sys.executable:
    # Use Unreal Engine
