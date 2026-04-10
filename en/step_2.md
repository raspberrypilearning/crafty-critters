## Add a body
Add an image for the body of the critter.

## Step 1
Click on the **Image gallery** icon to see all the image files in this project. Choose the body you want to use.

## Step 2
Add the code below and change the file name in `load_image()` to the body you want to use.


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 7-9, 14-15
---
def setup():
    size(600, 400)
    image_mode(CENTER)
    
    # Add images
    global body
    body = load_image('body1.png')
    
def draw():
    background(220, 30, 124);
    
    # Draw body
    image(body, 275, 150);

run() # Keep this to run your code
--- /code ---
</div>

### Now run your code
See the body you chose in the **Visual output**.


<div class="c-project-output">
![The Visual output window with a snail shell.](images/step3.png)
</div>






