## Challenge: better dancing critters
To make the legs look more attached to the body, decide how high and low you want them to be.

## Step 1
`print()` the `leg_y` value to see it in the **text output**.

### Now run your code 
Use the numbers from the **text output** as the highest or lowest values in your code. 

## Step 2
Use `if` to limit how the legs move.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 20-28
---
    # Draw legs
    leg_x = 150 # starting position
    gap = 80 
    leg_y = mouse_y
    print(mouse_y)
    
    # Highest
    if leg_y < 200:
        leg_y = 200

    # Lowest    
    if leg_y > 310:
        leg_y = 310

    for i in range(4):
--- /code ---
</div>

### Now run your code 
See the legs ony move to the highest and lowest positions.

<div class="c-project-output">
![visual output window with printed number in the text output and critter and moving legs](images/step8.gif)
</div>






