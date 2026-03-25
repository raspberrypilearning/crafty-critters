## More challenges

## Move the whole critter
Try making the whole critter move by adding `leg_y` to y position of the eye and body. You will need to adjust the numbers until it looks right.


## Change the look
You can change the size of images by adding a `width` and `height`. Experiment with `image(x, y, width, height)` to change the look of your critter.


## Make it random
Add some randomness in the `setup()` of your critter. Here is some starter code with `randint()` for you to experiment with.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: false
---
from p5 import *
from random import randint

def setup():
    size(600, 400)
    image_mode(CENTER)
    global body, eye, leg

    rand_body = str(randint(1,3))
    rand_eye = str(randint(1,3))
    rand_leg = str(randint(1,3))
    body = load_image('body' + rand_body + '.png')
    eye = load_image('eye' + rand_eye + '.png')
    leg = load_image('leg' + rand_leg + '.png')

def draw():
    background(220, 30, 124);
--- /code ---
</div>






