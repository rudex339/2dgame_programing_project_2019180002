world = [[],[],[]]
collision_group = dict()

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

def add_collision_pairs(a,b,group):
    if group not in collision_group:
        print('add new group')
        collision_group[group]=[[],[]]
    if a:
        if type(a) == list:
            collision_group[group][0]+=a
        else:
            collision_group[group][0].append(a)
    if b:
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)
def all_collision_pairs():
    for group, pairs in collision_group.items(): #키 벨류를 모두 가져옴
        for a in pairs[0]:
            for b in pairs[1]:
                yield a,b,group

def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]: pairs[0].remove(o)
        elif o in pairs[1]: pairs[1].remove(o)