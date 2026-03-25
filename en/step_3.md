<h2 class="c-project-heading--task">Make them look</h2>
--- task ---

Add eyes to your critter 👀

--- /task ---

--- task ---

There are two eyes, so `image()` is written twice with a small difference in the x and y to change the position.

--- /task ---

<div class="c-project-callout c-project-callout--tip">

### Tip

The screen is like a grid, and each image has an x and y position, for example `image(eye, x, y)`. 

</div>

--- task ---

Add the code below. Use the image you want by changing the file name in `load_image()`.

--- /task ---

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
--- task ---

Click **run** to see the eye you chose. Move your eyes by changing the x and y numbers in the code.

--- /task ---  
</div>

<div class="c-project-output">
![visual output window with shell and fish eyes](images/step4.png)
</div>








