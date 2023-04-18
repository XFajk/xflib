import pygame


def construct_shadow_flag(add_shadow: bool = False, shadow_offset: int = 0, shadow_color: tuple = (0, 0, 0)) -> dict:
    return {
        "add_shadow": add_shadow,
        "shadow_offset": shadow_offset,
        "shadow_color": shadow_color
    }


def construct_expand_flag(add_expand: bool = False, expand_speed: float = 0) -> dict:
    return {
        "add_expand": add_expand,
        "expand_speed": expand_speed
    }


def construct_change_color_flag(add_change_color: bool = False, primary_color: tuple = (0, 0, 0), secondary_color: tuple = (0, 0, 0)) -> dict:
    return {
        "add_change_color": add_change_color,
        "primary_color": primary_color,
        "secondary_color": secondary_color

    }


class Button:
    def __init__(self, position: list[float], text: str, font: pygame.font.Font,
                 color: tuple[int, int, int] | list[int, int, int],
                 secondary_color: tuple[int, int, int] | list[int, int, int],
                 text_color: tuple[int, int, int] | list[int, int, int], antialias: bool):
        self.position = pygame.Vector2((position[0], position[1]))
        self.text = text
        self.font = font
        self.rendered_text = self.font.render(self.text, antialias, text_color)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.rendered_text.get_width() + 10,
                                self.rendered_text.get_height() + 10)
        self.color = color
        self.secondary_color = secondary_color
        self.flags = {
            "expand": False,
            "change_color": False,
            "shadow": construct_shadow_flag(False)
        }

        self.pressed = False

    def draw(self, surf: pygame.Surface):
        if self.flags["shadow"]["add_shadow"]:
            pygame.draw.rect(surf, self.flags["shadow"]["shadow_color"], (
                self.rect.x - self.rect.w / 2 + self.flags["shadow"]["shadow_offset"],
                self.rect.y - self.rect.h / 2 + self.flags["shadow"]["shadow_offset"], self.rect.w, self.rect.h))

        pygame.draw.rect(surf, self.color,
                         (self.rect.x - self.rect.w / 2, self.rect.y - self.rect.h / 2, self.rect.w, self.rect.h))
        surf.blit(
            self.rendered_text,
            (
                self.position.x - self.rendered_text.get_width() / 2,
                self.position.y - self.rendered_text.get_height() / 2
            )
        )

    def update(self, dt, operation=lambda dt: 1):
        pass


class TextArea:
    pass
