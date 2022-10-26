class Star:
    
    def __init__(self):
        self.x = random(-width, width)
        self.y = random(-height, height)
        self.z = random(width)
        self.pz = self.z
        
    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.z = width
            self.x = random(-width, width)
            self.y = random(-height, height)
            self.pz = self.z
            
    def show(self):
        fill(255)
        noStroke()
        sx = map(self.x/self.z, 0, 1, 0, width)
        sy = map(self.y/self.z, 0, 1, 0, height)
        r = map(self.z, 0, width, 16, 0)
        
        # ellipse(sx, sy, r, r)
        
        px = map(self.x/self.pz, 0, 1, 0, width)
        py = map(self.y/self.pz, 0, 1, 0, height)
        
        self.pz = self.z
        
        stroke(255)
        line(px, py, sx, sy)
