<h2 class="c-project-heading--task">Loop the legs</h2>
--- task ---

Add four legs by using a loop.

--- /task ---

--- task ---

**Delete** the `image()` code for the leg, and replace it with a loop. The loop runs four times, one for each leg. 

--- /task ---

--- task ---

Instead of writing a number `leg_x` is used as the starting position, and changed each time the loop runs. The `gap` is the number it changes by.  

--- /task ---

--- task ---

Experiment with the code to change the number of legs, and their positions.

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 17-21
---
    # Add images
    global body, eye, leg
    body = load_image('body1.png')
    eye = load_image('eye1.png')
    leg = load_image('leg1.png')
    
def draw():
    background(220, 30, 124);

    # Draw legs
    leg_x = 150 # starting position
    gap = 80 
    for i in range(4):
        image(leg, leg_x, 300);
        leg_x = leg_x + gap
    
    # Draw body
    image(body, 275, 150);

    # Draw eyes
    image(eye, 300, 120);
    image(eye, 450, 100);

run() # Keep this to run your code
--- /code ---
--- task ---

Click **run** to see your critter! 

--- /task ---  
</div>

<div class="c-project-output">
![ADD](images/robotrumps-yellow.png)
</div>






