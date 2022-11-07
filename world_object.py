world = [[],[],[]]

def add_object(o,depth):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
def all_object():
    for layer in world:
        for o in layer:
            yield o
def clear():
    for o in all_object():
        del o
    for layer in world:
        layer.clear