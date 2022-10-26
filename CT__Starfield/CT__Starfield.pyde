from star import Star

stars = []

def setup():
    size(400, 400)
    for i in range(400):
        stars.append(Star())
        
def draw():
    background(0)
    speed = map(mouseX, 0, width, 0, 50)
    translate(width/2, height/2)
    for s in stars:
        s.update(speed)
        s.show()
