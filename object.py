class Box:
    def __init__(self,top,bottom,left,right,state):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.state = state
        pass
    def hit_check(self,object,mx,my):
        x, y, wid, hei = object.return_position()
        right, left, top, bottom = x+wid+mx, x-wid+mx, y+hei+my, y-hei+my
        if right > self.left and left < self.right and bottom < self.top and top > self.bottom:
            object.input_jump(0)
            if self.state == 'ground':
                if bottom+top < self.top+self.bottom:
                    return 0,self.bottom - top
                else:
                    return 0, self.top - bottom
            elif self.state == 'wall':
                if left+right > self.left+self.right:
                    return self.right - left,0
                else:
                    return self.left - right,0
        return 0, 0