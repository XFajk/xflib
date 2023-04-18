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


def construct_change_color_flag(add_change_color: bool = False, primary_color: tuple = (0, 0, 0),
                                secondary_color: tuple = (0, 0, 0)) -> dict:
    return {
        "add_change_color": add_change_color,
        "primary_color": primary_color,
        "secondary_color": secondary_color
    }


class Button:
    def __init__(self, position: list[float], text: str, font: pygame.font.Font,
                 color: tuple[int, int, int] | list[int, int, int],
                 text_color: tuple[int, int, int] | list[int, int, int], antialias: bool):
        self.position = pygame.Vector2((position[0], position[1]))
        self.text = text
        self.font = font
        self.rendered_text = self.font.render(self.text, antialias, text_color)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.rendered_text.get_width() + 10,
                                self.rendered_text.get_height() + 10)
        self.normal_wh = (self.rect.w, self.rect.h)
        self.expanded_wh = (self.rect.w+10, self.rect.h+10)
        self.color = color
        self.flags = {
            "expand": construct_expand_flag(False),
            "change_color": construct_change_color_flag(False),
            "shadow": construct_shadow_flag(False)
        }

        self.pressed = False
        self.result = None

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

    def update(self, dt: float, cursor_position: list[int, int] | tuple[int, int], click_input: bool,
               operation_args: tuple, operation=lambda dt, args: 1):
        rect = pygame.Rect(self.rect.x - self.rect.w / 2, self.rect.y - self.rect.h / 2, self.rect.w, self.rect.h)
        if rect.collidepoint(cursor_position):
            if self.flags["change_color"]["add_change_color"]:
                self.color = self.flags["change_color"]["secondary_color"]

            if self.flags["expand"]["add_expand"]:
                if self.rect.w < self.expanded_wh[0]:
                    self.rect.w += self.flags["expand"]["expand_speed"]*dt
                if self.rect.h < self.expanded_wh[1]:
                    self.rect.h += self.flags["expand"]["expand_speed"]*dt

            if click_input and not self.pressed:
                self.pressed = True
                self.result = operation(dt, operation_args)
        else:
            if self.flags["change_color"]["add_change_color"]:
                self.color = self.flags["change_color"]["primary_color"]

            if self.flags["expand"]["add_expand"]:
                if self.rect.w > self.normal_wh[0]:
                    self.rect.w -= self.flags["expand"]["expand_speed"]*dt
                if self.rect.h > self.normal_wh[1]:
                    self.rect.h -= self.flags["expand"]["expand_speed"]*dt

        if not click_input and self.pressed:
            self.pressed = False


class TextArea:
    pass
