# XFLIB

<p>A particle system, ui and game dev util library</p>

[documentation of the xflib library](https://github.com/XFajk/xflib/wiki)

# Welcome to the xflib library

So what is xfps about?
It is a library used to add particles to games made in pygame in the most simple and flexible way.
The library is intended for those who need a more simple way of making particles.
other features are planned to be added like more visual effects, UI and utilities

## Download
to download the library you can use

`pip install xflib`

## Showcase
so how simple is xflib for making particle effect like this

![gif](https://github.com/XFajk/xflib/blob/main/showcase/gifs/particle_showcase.gif)

to make particles like this you need to import the library like this 

`import xflib`

after that, you can store the result of this line `ShapeParticles("circle", 0.05)` in a variable like `particles` before the main while loop. But what are the arguments we put into the constructor? Let's break it down so we can see what do the arguments mean.

<p></p>

    def ShapeParticles(shape_type, gravity=0.0):
* The `shape_type` parameter can be one of two things `"circle"` or `"rectangle"` note that it has to be a string and this tells the particle system what shape should it use for the particle. _its type is `string`_
* The `gravity` parameter just adds gravity to the particles _its type is `float`_

<p> </p>

Then in the main loop, you can add a particle to the particle system with this command `particles.add(pygame.Vector2(250, 175), random.randint(-135, -45), random.randint(1, 5) / 2, 5, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 0.05)` so let's break this method down.

<p></p>

    def add(loc, angle, speed, size, color, dis_amount):

* The `loc` parameter stands for location and it tells the particle where to appear. _its type can be a `list` or a `pygame.Vector2`_
* The `angle` parameter tells the particle in what direction should the particle go in. The angle is in degrees. _its type is `float`_
* The `speed` parameter tells the particle how fast it should move in the direction of the angle. _its type is `float`_
* The `size` parameter is the size of the particle. _its type is `float`_
* The `color` parameter is the color of the particle. _its type can be a `tuple[int, int, int]` or `pygame.Color`_
* The `dis_amount` parameter tells the particle by what amount should the particle get smaller. _its type is `float`_

<p></p>

Then lastly to see and update the particles that we added to the system we need to use the `use()` method like this, `particles.use(display, dt)` again let's break this method down

<p></p>

    def use(surf, dt=1.0, operation=lambda x, dt: x):

* The `surf` parameter is the surface we want to draw on. _its type is `pygame.Surface`_
* The `dt` parameter is the delta time that is used for every operation of the method. _its type is `float`_
* The `operation` parameter is a function that needs to take two arguments an x that represents the particle and the delta time so it can then adjust the operation to the frame rate. We added this parameter to increase the flexibility of the framework and to give the user more control over the behavior _its type is `function` that can only have two parameters representation of the particle and the delta time_

**! Additionally, there is a `use_with_light()` method that works the same as the `use()` method but gives the particle a glow around it like in the gif**

**if you want to see the whole code you can find it here: [link to the source](https://github.com/XFajk/xflib/blob/main/showcase/basic_particles/main.py)**

**if you want more information about the library you can navigate to the Particle Types of the wiki: [particle types](https://github.com/XFajk/xflib/wiki/Particle-Types)**

