from .j2scr import J2Scr

state = J2Scr()


def __getattr__(name):
    if hasattr(state, name):
        attr = getattr(state, name)
        return attr
    raise AttributeError(f"module {__name__} has no attribute '{name}'")
