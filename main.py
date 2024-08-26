# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    keepGameRunning=True    
    delta_time = pygame.time.Clock()
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)       
    dt = 0
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    asteroidfield1 = AsteroidField()
    updatable.add(player1)
    updatable.add(asteroidfield1)
    drawable.add(player1)
    
    
    while keepGameRunning:              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        for item in drawable:
            item.draw(screen)        
        for item in updatable:
            item.update(dt)
        for item in asteroids:            
            if item.check_collision(player1):
                print("Game  over!")
                raise SystemExit              
        pygame.display.flip() 
        dt = delta_time.tick(60) / 1000              

if __name__ == "__main__":
    main()