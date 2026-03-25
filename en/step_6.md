<h2 class="c-project-heading--task">Challenge: dancing critters</h2>
--- task ---

Use the mouse or trackpad to make the critter dance.

--- /task ---

--- task ---

Add `leg_y` and make it the same as the y value on the mouse or trackpad. 

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 19, 22
---
    # Draw legs
    leg_x = 150 # starting position
    gap = 80 
    leg_y = mouse_y
    
    for i in range(4):
        image(leg, leg_x, leg_y);
        leg_x = leg_x + gap
--- /code ---
--- task ---

Click **run** to see the legs move with the curser.

--- /task ---  
</div>

<div class="c-project-output">
![visual output window with critter and moving legs](images/step7.gif)
</div>






