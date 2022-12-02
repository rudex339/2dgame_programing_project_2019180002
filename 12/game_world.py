world = [[],[],[],[],[]]
collision_group = dict()

def add_object(o,depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        try:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
        except:
            pass
    raise ValueError('Trying destroy non existing object')
def all_object():
    for layer in world:
        for o in layer:
            yield o

def all_objects():
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
    if a != None:
        if type(a) == list:
            collision_group[group][0]+=a
        else:
            collision_group[group][0].append(a)
    if b != None:
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


class box:
    def __init__(self,left,bottom,right,top):
        self.left,self.bottom,self.right,self.top = left,bottom,right,top
        self.event = []
        pass
    def get_bb(self):
        return self.left,self.bottom,self.right,self.top
    def handle_collision(self, other, group):
        self.event.append([other,group])
        pass
    def all_collision(self):
        for o in self.event:
            other, group = o
            yield other, group
        self.event.clear()
    def move_box(self,dx,dy):
        self.left, self.right = self.left+dx, self.right+dx
        self.bottom, self.top = self.bottom+dy, self.top+dy
    def change_box(self,left,bottom,right,top):
        self.left,self.bottom,self.right,self.top = left,bottom,right,top
    def compatible(self):
        self.left, self.bottom, self.right, self.top = self.right, self.bottom, self.top, self.left
        pass