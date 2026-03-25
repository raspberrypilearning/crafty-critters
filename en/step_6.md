## Challenge: dancing critters
Use the mouse or trackpad to make the critter dance.

Add `leg_y` and make it the same as the y value on the mouse or trackpad. 

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
</div>

### Now run your code 
The legs should move with the curser.

<div class="c-project-output">
![visual output window with critter and moving legs](images/step7.gif)
</div>






