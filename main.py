import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рух кіл по основі радіуса R")
clock = pygame.time.Clock()

R = 200
r1 = 40
r2 = 60
center = WIDTH // 2, HEIGHT // 2

theta1 = 0
theta2 = math.pi
speed = 0.01

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    theta1 += speed
    theta2 -= speed

    x1 = center[0] + (R - r1) * math.cos(theta1)
    y1 = center[1] + (R - r1) * math.sin(theta1)
    x2 = center[0] + (R - r2) * math.cos(theta2)
    y2 = center[1] + (R - r2) * math.sin(theta2)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), center, R, 2)
    pygame.draw.circle(screen, (0, 0, 255), (int(x1), int(y1)), r1)
    pygame.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), r2)

    dx = x1 - x2
    dy = y1 - y2
    dist = math.hypot(dx, dy)
    if dist <= r1 + r2:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.time.wait(2000)
pygame.quit()
