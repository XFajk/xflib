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


def surf_polygon(points: list[list], color: tuple | pygame.Color, return_points: bool = False) -> pygame.Surface | tuple:
    smallest_position_x = min(row[0] for row in points)
    smallest_position_y = min(row[1] for row in points)

    if smallest_position_x != 0:
        offset = 0 - smallest_position_x
        for pair in points:
            pair[0] += offset

    if smallest_position_y != 0:
        offset = 0 - smallest_position_y
        for pair in points:
            pair[1] += offset

    biggest_position_x = max(row[0] for row in points)
    biggest_position_y = max(row[1] for row in points)

    surf = pygame.Surface((biggest_position_x, biggest_position_y))
    surf.set_colorkey((0, 0, 0))

    pygame.draw.polygon(surf, color, points)

    if return_points:
        return surf, points
    else:
        return surf
