class ArmoredShooter():

    speed = 8
    diameter = 50
    c = color(0, 0, 255)
    mark = 0
    wait = 1000
    go = True

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
