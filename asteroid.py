import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angel = random.uniform(20,50)
            unit_vector = self.position
            rotated_vector = unit_vector.rotate(random_angel)
            other_rotated_vector = unit_vector.rotate(-random_angel)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_asteroid.velocity = rotated_vector * 1.2
            second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_asteroid.velocity = other_rotated_vector * 1.2