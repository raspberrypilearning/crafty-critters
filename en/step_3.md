<h2 class="c-project-heading--task">Add the body</h2>
--- task ---

Add an image for the body of the critter.

--- /task ---

--- task ---

Click the image gallery icon to see all the image files in this project. There are different bodies you can use. 

--- /task ---

--- task ---

Add the image file first in teh `setup()`. Then show the image in `draw()`

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-9, 15
---
from p5 import *

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
--- /code ---
--- task ---

Click **run** to see the background in the visual output window.

--- /task ---  
</div>

<div class="c-project-output">
![ADD](images/robotrumps-yellow.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip
Change the file name in `load_image()` to the body you want to use.
 
</div>







