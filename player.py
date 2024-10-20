import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.player_lives = PLAYER_LIVES
        self.invincible_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        self.invincible_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
    
    # Wrap around the screen vertically
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT


    def shoot(self):
        if self.shoot_timer >0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def collissions(self,second):   
        distance = pygame.math.Vector2.distance_to(self.position,second.position)
        if self.radius + second.radius >= distance and self.player_lives <= 0:
            return True
        elif self.radius + second.radius >= distance and self.player_lives > 0 and self.invincible_timer <= 0:
            self.player_lives -= 1
            self.invincible_timer = INVINCIBILITY_DURATION
            if self.player_lives >= 1:    
                print(f"You have {self.player_lives} life left")
        return False