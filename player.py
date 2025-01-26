from circleshape import *
from constants import *
from shot import *
class Player(CircleShape):
    def __init__(self, x , y):
        radius= PLAYER_RADIUS
        super().__init__(x,y,radius)
        self.rotation = 0
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.polygon(screen,white,self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(0-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(0-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            shot = Shot(self.position, self.position, SHOT_RADIUS)
            shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED)
            self.timer = PLAYER_SHOT_CD


    
