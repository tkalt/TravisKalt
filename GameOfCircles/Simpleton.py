import SpriteManager

class PeaShooter: 
    wait = 1000
    mark = 0
    
    def __init__(self, handler):
        self.handler = handler
    
        
        def shoot(self, vector):
            if(millis() - self.mark > self.wait):
                pea = Pea(self.handler.x, self.handler.y, vector, slef.handler.team) 
                SpriteManager.spawn(pea) 
            
