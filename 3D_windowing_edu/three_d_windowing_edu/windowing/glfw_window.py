import glfw

if not glfw.init():
    raise Exception("glfw can not be initialized!")


def tdd_true():
    return True
