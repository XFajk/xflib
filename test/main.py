from build.lib import xflib
import pygame
import time
import random as rnd


def change_color(dt, args):
    return rnd.randint(100, 255), rnd.randint(100, 255), rnd.randint(100, 255)


def main():
    pygame.init()

    ZOOM = 1
    WS = (800, 600)
    DS = (WS[0] / ZOOM, WS[1] / ZOOM)
    window = pygame.display.set_mode(WS, vsync=1)
    display = pygame.Surface(DS)
    clock = pygame.time.Clock()

    # fonts

    # entities
    button = xflib.ui.Button(
        [DS[0] / 2, DS[1] / 2], "Hello world!", pygame.font.Font(None, 32),
        (255, 0, 0), (255, 255, 255),
        True
    )
    button.flags["shadow"] = xflib.construct_shadow_flag(True, 3)
    button.flags["expand"] = xflib.construct_expand_flag(True, 1)
    button.flags["change_color"] = xflib.construct_change_color_flag(True, (255, 0, 0), (100, 0, 0))

    background_color = (255, 255, 0)

    # timer
    last_time = time.time()

    done = False
    while not done:

        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        mouse_input = pygame.mouse.get_pressed()
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

        # logic
        button.update(dt, (int(mouse_pos.x), int(mouse_pos.y)), mouse_input[0], (0,), change_color)
        if button.result is not None:
            background_color = button.result

        if button.pressed:
            button.rerender_text(str(rnd.randbytes(10)), (255, 255, 255), True)

        # drawing
        display.fill(background_color)

        button.draw(display)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.set_caption(f"FPS: {round(clock.get_fps(), 2)}")

        surf = pygame.transform.scale(display, WS)
        window.blit(surf, (0, 0))
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
