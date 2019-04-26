import SpriteManager

from Sprite import Sprite
from Bullet import Bullet
from Enemy import Enemy

class Spawner(Enemy):
    
    mark = 0
    wait = 1000
    mark2 = 0
    wait2 = 5000
    speed = 10
    diameter = 50
    
    def spawn(self):
        if millis() - self.mark2 > self.wait2:
            self.mark2 = millis()
            SpriteManager.spawn(Enemy(self.x, self.y, self.team))
        
    def move(self):
        self.spawn()
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
    
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)

    def aim(self, target):
        d = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** .5
        xComp = target.x - self.x
        yComp = target.y - self.y
        xVec = xComp / 2 * .1
        yVec = yComp / 2 * .1
        return PVector(xVec, yVec)

    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.mark = millis()
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
    

             
