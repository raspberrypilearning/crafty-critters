from p5 import *
from random import randint

def setup():
    size(400, 400)
    image_mode(CENTER)
    global body, eye, leg
    body = load_image('body1.png')
    leg = load_image('leg1.png')
    eye = load_image('leg1.png')

def draw():
    background(220, 30, 124);
    image(leg, 150, 320);
    image(leg, 250, 300);
    image(leg, 350, 320);
    image(leg, 450, 330);
    image(body, width / 2, 200, 500);
    image(eye, 350, 120, 200);
    image(eye, 500, 100, 200);

run() # Keep this to run your code
