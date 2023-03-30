import pygame


def surf_circle(r: float, color: tuple | pygame.Color) -> pygame.Surface:
    surf = pygame.Surface((r * 2, r * 2)) if r > 0 else pygame.Surface((0, 0))
    pygame.draw.circle(surf, color, (r, r), r)
    surf.set_colorkey((0, 0, 0))

    return surf


def surf_rect(w: float, h: float, color: tuple | pygame.Color) -> pygame.Surface:
    surf = pygame.Surface((w, h)) if w > 0 and h > 0 else pygame.Surface((0, 0))
    surf.fill(color)

    return surf
