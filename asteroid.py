from circleshape import *
from constants import *
import random
random_angle = random.uniform(20,50)
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen,white,self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_vec_1 = self.velocity.rotate_rad(random_angle)
            new_vec_2 = self.velocity.rotate_rad(0-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position,self.position,new_radius)
            asteroid_2 = Asteroid(self.position,self.position,new_radius)
            asteroid_1.velocity = new_vec_1*1.2
            asteroid_2.velocity = new_vec_2*1.2

