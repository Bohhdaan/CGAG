import pygame
import sys

def draw_bresenham_quarter_circle(surface, center, radius, color, quadrant):
    x0, y0 = center
    x = 0
    y = radius
    d = 3 - 2 * radius

    while y >= x:
        if quadrant == 'tl':
            surface.set_at((x0 - x, y0 - y), color)
            surface.set_at((x0 - y, y0 - x), color)
        elif quadrant == 'tr':
            surface.set_at((x0 + x, y0 - y), color)
            surface.set_at((x0 + y, y0 - x), color)
        elif quadrant == 'bl':
            surface.set_at((x0 - x, y0 + y), color)
            surface.set_at((x0 - y, y0 + x), color)
        elif quadrant == 'br':
            surface.set_at((x0 + x, y0 + y), color)
            surface.set_at((x0 + y, y0 + x), color)
        x += 1
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6

def draw_rounded_rect(surface, rect, radius, color):
    x, y, w, h = rect

    pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, radius, h - 2 * radius))
    pygame.draw.rect(surface, color, (x + w - radius, y + radius, radius, h - 2 * radius))

    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius - 1, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + h - radius - 1), radius)
    pygame.draw.circle(surface, color, (x + w - radius - 1, y + h - radius - 1), radius)

    draw_bresenham_quarter_circle(surface, (x + radius, y + radius), radius, (0, 0, 0), 'tl')
    draw_bresenham_quarter_circle(surface, (x + w - radius - 1, y + radius), radius, (0, 0, 0), 'tr')
    draw_bresenham_quarter_circle(surface, (x + radius, y + h - radius - 1), radius, (0, 0, 0), 'bl')
    draw_bresenham_quarter_circle(surface, (x + w - radius - 1, y + h - radius - 1), radius, (0, 0, 0), 'br')

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Прямокутник із заокругленими кутами")

screen.fill((255, 255, 255))

rect = (100, 100, 300, 200)
radius = 40
color = (0, 0, 255)

draw_rounded_rect(screen, rect, radius, color)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
