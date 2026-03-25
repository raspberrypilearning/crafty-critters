## Add the body
Add an image for the body of the critter.

## Step 1
Click the image gallery icon to see all the image files in this project. There are different bodies you can use. 

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
See the body you chose in the visual output.


<div class="c-project-output">
![visual output window with snail shell](images/step3.png)
</div>






