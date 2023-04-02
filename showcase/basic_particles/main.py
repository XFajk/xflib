import xfps
import pygame
import time
import random as rnd

"""
 this file shows a demonstration
 of how easy it is to use the xfps library width pygame 
 to run this file you need to have pygame and xfps installed with pip
"""


def main():
    pygame.init()

    WS = (800, 600)
    window = pygame.display.set_mode(WS)
    clock = pygame.time.Clock()

    # entities
    particles = xfps.ShapeParticles("circle", 0.05)  # creates the particle system

    last_time = time.time()
    done = False
    while not done:

        # calculates the delta time between the two frames
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        particles.add(  # adds one particle to the particle system
            pygame.Vector2(400, 300),  # initial the position of the particle
            rnd.randint(-135, -45),  # the angle that represents direction of the particle
            rnd.randint(1, 5) / 2,  # speed is which the particle should move in into the given direction
            10,  # size
            (rnd.randint(100, 255), rnd.randint(100, 255), rnd.randint(100, 255)),  # color
            0.1  # the amount by which we decrease the size of the particle
        )

        window.fill((0, 0, 0))

        particles.use_with_light(window, dt)  # draws and updates every particle that is in the particle system

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.set_caption(f"FPS: {round(clock.get_fps(), 2)}")  # prints out the FPS to the caption

        clock.tick(60)  # caps the fps to 60

    pygame.quit()


if __name__ == '__main__':
    main()
