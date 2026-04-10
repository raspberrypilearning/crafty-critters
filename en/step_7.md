### Challenge: Improve the dancing critter
To make the legs look more attached to the body, decide how high and low you want them to be.

## Step 1
`print()` the `mouse_y` value to see it in the **Text output**.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 20
---
    # Draw legs
    leg_x = 150 # starting position
    gap = 80 
    leg_y = mouse_y
    print(mouse_y)
    
    for i in range(4):
--- /code ---
</div>

### Now run your code 
You can use the numbers from the **Text output** as the highest or lowest values in your code. 

## Step 2
Use `if` to limit how the legs move.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 22-28
---
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
See the legs only move between the highest and lowest positions.

<div class="c-project-output">
![The Visual output window with the critter with legs moving up and down from the bottom of the snail shell with the cursor, and the Text output window with numbers being printed.](images/step8.gif)
</div>






