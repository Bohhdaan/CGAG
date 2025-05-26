import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab 4 – 2D Об’єкти")

clock = pygame.time.Clock()

current_shape = 'circle'
angle = 0
scale = 1.0

def draw_circle(center, scale):
    radius = int(50 * scale)
    pygame.draw.circle(screen, (0, 200, 255), center, radius)

def draw_square(center, angle, scale):
    size = 100 * scale
    points = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    rotated = []
    for x, y in points:
        x *= size / 2
        y *= size / 2
        rx = x * math.cos(angle) - y * math.sin(angle)
        ry = x * math.sin(angle) + y * math.cos(angle)
        rotated.append((center[0] + rx, center[1] + ry))
    pygame.draw.polygon(screen, (255, 100, 100), rotated)

def draw_triangle(center, angle, scale):
    size = 120 * scale
    points = [(0, -1), (1, 1), (-1, 1)]
    rotated = []
    for x, y in points:
        x *= size / 2
        y *= size / 2
        rx = x * math.cos(angle) - y * math.sin(angle)
        ry = x * math.sin(angle) + y * math.cos(angle)
        rotated.append((center[0] + rx, center[1] + ry))
    pygame.draw.polygon(screen, (100, 255, 100), rotated)

def draw_shape():
    center = (WIDTH // 2, HEIGHT // 2)
    if current_shape == 'circle':
        draw_circle(center, scale)
    elif current_shape == 'square':
        draw_square(center, angle, scale)
    elif current_shape == 'triangle':
        draw_triangle(center, angle, scale)

# Main loop
running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = 'circle'
            elif event.key == pygame.K_2:
                current_shape = 'square'
            elif event.key == pygame.K_3:
                current_shape = 'triangle'
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                scale += 0.1
            elif event.key == pygame.K_MINUS:
                scale = max(0.1, scale - 0.1)
            elif event.key == pygame.K_LEFT:
                angle -= 0.1
            elif event.key == pygame.K_RIGHT:
                angle += 0.1

    draw_shape()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
