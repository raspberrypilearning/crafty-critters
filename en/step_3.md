## Make them look
Add eyes to your critter 👀

<div class="c-project-callout c-project-callout--tip">

### Tip

The screen is like a grid, and each image has an x and y position, for example `image(eye, x, y)`. 

</div>

## Step 1
Add the code below. Use the image you want by changing the file name in `load_image()`.

## Step 2
There are two eyes, so `image()` is written twice with a small difference in the x and y to change the position. Move your eyes to a different position by changing the x and y numbers in the code.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8, 10, 18-20
---
    # Add images
    global body, eye
    body = load_image('body1.png')
    eye = load_image('eye1.png')
    
def draw():
    background(220, 30, 124);
    
    # Draw body
    image(body, 275, 150);

    # Draw eyes
    image(eye, 300, 120);
    image(eye, 450, 100);

run() # Keep this to run your code
--- /code ---
</div>

### Now run your code
Test that your eyes are in the right place, and edit the code if they need to change.

<div class="c-project-output">
![visual output window with shell and fish eyes](images/step4.png)
</div>








