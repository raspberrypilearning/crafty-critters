## Make them look
Add eyes to your critter 👀

<div class="c-project-callout c-project-callout--tip">

### Tip

- The screen is like a grid, and each image has an x and y position, for example, `image(eye, x, y)` 
- The critter has two eyes, so you need to write `image()` twice with a small difference in the x and y values to change the positions

</div>

## Step 1
Add the code below. To use the image you want, change the file name in `load_image()`.

## Step 2
To move the eyes to different positions, change the x and y numbers in the code.

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
    background(220, 30, 124)
    
    # Draw body
    image(body, 275, 150)

    # Draw eyes
    image(eye, 300, 120)
    image(eye, 450, 100)

run() # Keep this to run your code
--- /code ---
</div>

### Now run your code
Test that the eyes are in the right place, and edit the code if you need to move them.

<div class="c-project-output">
![The Visual output window with a snail shell with two fish eyes towards the front.](images/step3.png)
</div>








