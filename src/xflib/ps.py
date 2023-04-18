import pygame
import math
from typing import Callable
from .utils import surf_circle, surf_rect, surf_polygon


class ShapeParticles:
    def __init__(self, shape_type: str, gravity: float = 0.0):
        self.shape_type = shape_type
        self.gravity = gravity
        self.objects = []

    def add(self, loc: list | pygame.Vector2, angle: float, speed: float, size: float, color: tuple | pygame.Color,
            dis_amount: float):
        vel = [math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed]
        self.objects.append(
            {
                "loc": loc,
                "vel": vel,
                "size": size,
                "color": color,
                "dis_amount": dis_amount,
            }
        )

    def use(self, surf: pygame.Surface, dt: float, operation: Callable[[dict, float], any]):
        if self.shape_type == "circle":
            for i, p in sorted(enumerate(self.objects), reverse=True):
                p["loc"][0] += p["vel"][0] * dt
                p["loc"][1] += p["vel"][1] * dt
                p["size"] -= p["dis_amount"] * dt
                p["vel"][1] += self.gravity * dt
                operation(p, dt)
                pygame.draw.circle(surf, p["color"], p["loc"], p["size"])
                if p["size"] <= 0:
                    self.objects.pop(i)

        elif self.shape_type == "rectangle":
            for i, p in sorted(enumerate(self.objects), reverse=True):
                p["loc"][0] += p["vel"][0] * dt
                p["loc"][1] += p["vel"][1] * dt
                p["size"] -= p["dis_amount"] * dt
                p["vel"][1] += self.gravity * dt
                operation(p, dt)
                pygame.draw.rect(surf, p["color"], (p["loc"][0]-p["size"]/2, p["loc"][1]-p["size"]/2, p["size"], p["size"]))
                if p["size"] <= 0:
                    self.objects.pop(i)
        else:
            raise TypeError(f"{self.shape_type} is an invalid shape type you can use circle or rectangle")

    def use_with_light(self, surf: pygame.Surface, dt: float, operation: Callable[[dict, float], any]):
        if self.shape_type == "circle":
            for i, p in sorted(enumerate(self.objects), reverse=True):
                p["loc"][0] += p["vel"][0] * dt
                p["loc"][1] += p["vel"][1] * dt
                p["size"] -= p["dis_amount"] * dt
                p["vel"][1] += self.gravity * dt
                operation(p, dt)
                light_surf = surf_circle(p["size"] * 2, (p["color"][0] / 3, p["color"][1] / 3, p["color"][2] / 3))
                surf.blit(light_surf,
                          (p["loc"][0] - int(light_surf.get_width() / 2), p["loc"][1] - int(light_surf.get_height() / 2)),
                          special_flags=pygame.BLEND_RGB_ADD)
                pygame.draw.circle(surf, p["color"], p["loc"], p["size"])
                if p["size"] <= 0:
                    self.objects.pop(i)

        elif self.shape_type == "rectangle":
            for i, p in sorted(enumerate(self.objects), reverse=True):
                p["loc"][0] += p["vel"][0] * dt
                p["loc"][1] += p["vel"][1] * dt
                p["size"] -= p["dis_amount"] * dt
                p["vel"][1] += self.gravity * dt
                operation(p, dt)
                light_surf = surf_rect(p["size"] * 2, p["size"] * 2, (p["color"][0] / 3, p["color"][1] / 3, p["color"][2] / 3))
                surf.blit(light_surf,
                          (p["loc"][0] - int(light_surf.get_width() / 4)-p["size"]/2, p["loc"][1] - int(light_surf.get_height() / 4)-p["size"]/2),
                          special_flags=pygame.BLEND_RGB_ADD)
                pygame.draw.rect(surf, p["color"], (p["loc"][0]-p["size"]/2, p["loc"][1]-p["size"]/2, p["size"], p["size"]))
                if p["size"] <= 0:
                    self.objects.pop(i)
        else:
            raise TypeError(f"{self.shape_type} is an invalid shape type you can use circle or rectangle")


class SparkParticles:
    def __init__(self, gravity: float = 0.0):
        self.gravity = gravity
        self.objects = []

    def add(self, loc: list | pygame.Vector2, angle: float, speed: float, scale: float, color: tuple | pygame.Color,
            dis_amount: float):
        self.objects.append(Spark(loc, math.radians(angle), speed, color, scale, dis_amount))

    def use(self, surf: pygame.Surface, dt: float, operation: Callable[[dict, float], any]):
        for i, s in sorted(enumerate(self.objects), reverse=True):
            s.move(dt, self.gravity)
            operation(s, dt)
            s.draw(surf)
            if not s.alive:
                self.objects.pop(i)

    def use_with_light(self, surf: pygame.Surface, dt: float, operation: Callable[[dict, float], any]):
        for i, s in sorted(enumerate(self.objects), reverse=True):
            s.move(dt, self.gravity)
            operation(s, dt)
            s.draw(surf)
            scale = s.scale * 3
            points = [
                [s.loc[0] + math.cos(s.angle) * s.speed * scale,
                 s.loc[1] + math.sin(s.angle) * s.speed * scale],
                [s.loc[0] + math.cos(s.angle + math.pi / 2) * s.speed * scale * 0.3,
                 s.loc[1] + math.sin(s.angle + math.pi / 2) * s.speed * scale * 0.3],
                [s.loc[0] - math.cos(s.angle) * s.speed * scale * 3.5,
                 s.loc[1] - math.sin(s.angle) * s.speed * scale * 3.5],
                [s.loc[0] + math.cos(s.angle - math.pi / 2) * s.speed * scale * 0.3,
                 s.loc[1] - math.sin(s.angle + math.pi / 2) * s.speed * scale * 0.3],
            ]
            light_surf, new_points = surf_polygon(points, (s.color[0] / 3, s.color[1] / 3, s.color[2] / 3), True)

            new_loc = [
                new_points[0][0] - math.cos(s.angle) * s.speed * scale,
                new_points[0][1] - math.sin(s.angle) * s.speed * scale
            ]

            surf.blit(light_surf, (s.loc[0] - new_loc[0], s.loc[1] - new_loc[1]), special_flags=pygame.BLEND_RGB_ADD)
            if not s.alive:
                self.objects.pop(i)


class ImgParticles:
    def __init__(self, img: pygame.Surface, gravity: float = 0.0, give_color_key: bool = False, color_key: tuple | pygame.Color = (0, 0, 0)):
        self.img = img
        if give_color_key:
            self.img.set_colorkey(color_key)
        self.gravity = gravity
        self.objects = []

    def add(self, loc: list | pygame.Vector2, angle: float, speed: float, size: float, color: tuple | pygame.Color,
            dis_amount: float, rot_amount_deg: float = 0.0):
        vel = [math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed]
        self.objects.append(
            {
                "loc": loc,
                "vel": vel,
                "size": size,
                "color": color,
                "dis_amount": dis_amount,
                "rot_amount_deg": rot_amount_deg,
                "rotation": 0
            }
        )

    def use(self, surf: pygame.Surface, dt: float, operation: Callable[[dict, float], any]):
        for i, p in sorted(enumerate(self.objects), reverse=True):
            p["loc"][0] += p["vel"][0] * dt
            p["loc"][1] += p["vel"][1] * dt
            p["size"] -= p["dis_amount"] * dt
            p["vel"][1] += self.gravity * dt
            operation(p, dt)
            p_img = pygame.transform.scale(self.img, (p["size"], p["size"]))
            if p["rot_amount_deg"] > 0:
                p["rotation"] += p["rot_amount_deg"]
                p_img_rot = pygame.transform.rotate(p_img, p["rotation"])
                surf.blit(p_img_rot, (p["loc"][0] - int(p_img_rot.get_width() / 2) + p["size"] / 2,
                                      p["loc"][1] - int(p_img_rot.get_height() / 2) + p["size"] / 2))
            else:
                surf.blit(p_img, (p["loc"][0] - p["size"] / 2, p["loc"][1] - p["size"] / 2))
            if p["size"] <= 0:
                self.objects.pop(i)


class Spark:
    def __init__(self, loc: list | tuple | pygame.Vector2, angle: float, speed: float, color: tuple = (255, 255, 255),
                 scale: float = 1,
                 dis_amount: float = 0.25):
        self.loc = loc
        self.angle = angle
        self.speed = speed
        self.scale = scale
        self.color = color
        self.dis_amount = dis_amount
        self.alive = True

    def calculate_movement(self, dt: float):
        return [math.cos(self.angle) * self.speed * dt, math.sin(self.angle) * self.speed * dt]

    def velocity_adjust(self, friction, force, terminal_velocity, dt):
        movement = self.calculate_movement(dt)
        movement[1] = min(terminal_velocity, movement[1] + force * dt)
        movement[0] *= friction
        self.angle = math.atan2(movement[1], movement[0])

    def move(self, dt: float, gravity: float = 0.0):
        movement = self.calculate_movement(dt)
        self.loc[0] += movement[0]
        self.loc[1] += movement[1]
        if gravity > 0:
            self.velocity_adjust(0.975, gravity, 8, dt)

        self.speed -= self.dis_amount * dt

        if self.speed <= 0:
            self.alive = False

    def draw(self, surf):
        if self.alive:
            points = [
                [self.loc[0] + math.cos(self.angle) * self.speed * self.scale,
                 self.loc[1] + math.sin(self.angle) * self.speed * self.scale],
                [self.loc[0] + math.cos(self.angle + math.pi / 2) * self.speed * self.scale * 0.3,
                 self.loc[1] + math.sin(self.angle + math.pi / 2) * self.speed * self.scale * 0.3],
                [self.loc[0] - math.cos(self.angle) * self.speed * self.scale * 3.5,
                 self.loc[1] - math.sin(self.angle) * self.speed * self.scale * 3.5],
                [self.loc[0] + math.cos(self.angle - math.pi / 2) * self.speed * self.scale * 0.3,
                 self.loc[1] - math.sin(self.angle + math.pi / 2) * self.speed * self.scale * 0.3],
            ]
            pygame.draw.polygon(surf, self.color, points)
