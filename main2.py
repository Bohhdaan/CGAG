import pygame
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дерево Мандельброта")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mu = 0.6
depth = 6
angle = math.radians(45)

def draw_branch(x1, y1, length, direction, depth):
    if depth == 0:
        return
    x2 = x1 + length * math.cos(direction)
    y2 = y1 - length * math.sin(direction)
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)
    draw_branch(x2, y2, length * mu, direction + angle, depth - 1)
    draw_branch(x2, y2, length * mu, direction - angle, depth - 1)

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BLACK)
        x0, y0 = width // 2, height - 50
        length = 100
        draw_branch(x0, y0, length, math.radians(90), depth)
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
