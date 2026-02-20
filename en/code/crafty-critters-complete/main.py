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
    #legs
    leg_x = 150
    gap = 80
    #leg_y = mouse_y  
    #if leg_y < 200:
    #    leg_y = 200   
    #if leg_y > 310:
    #    leg_y = 310
    #print(mouse_y)
   
    for i in range(4):
        image(leg, leg_x, 300);
        leg_x = leg_x + gap
    
    #body
    image(body, 275, 150);

    #eyes
    image(eye, 300, 120);
    image(eye, 450, 100);

        
run() # Keep this to run your code
