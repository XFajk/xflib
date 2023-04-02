from build.lib.xfps import *
import pygame
import time
import random as rnd

def main():
    pygame.init()

    ZOOM = 1
    WS = (800, 600)
    DS = (WS[0] / ZOOM, WS[1] / ZOOM)
    window = pygame.display.set_mode(WS)
    display = pygame.Surface(DS)
    clock = pygame.time.Clock()

    # fonts

    # entities
    particles = ShapeParticles("rectangle", 0.1)

    # timer
    last_time = time.time()

    done = False
    while not done:

        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        keys = pygame.key.get_pressed()
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

        # logic
        particles.add(pygame.Vector2(400, 300), rnd.randint(-135, -45), rnd.randint(1, 5) / 2, 64,
                      (rnd.randint(100, 255), rnd.randint(100, 255), rnd.randint(100, 255)), 0.5)

        # drawing
        display.fill((0, 0, 0))

        particles.use_with_light(display, dt)

        pygame.draw.circle(display, (255, 0, 0), (400, 300), 2)

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
