import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1280, height=720, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, sorted_numbers, target, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found
    # Generate a list with random numbers
    numbers = random.sample(range(1, 31), 30)
    random.shuffle(numbers)  # Shuffle for linear search
    numbers.sort() # Sort for binary search
    target = random.choice(numbers) # Target number to search for

    # Reset search variables
    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  # Initialize searches

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found

    # Update linear search
    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == target:
            linear_found = True
        else:
            linear_index += 1

    # Update binary search
    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == target:
            binary_found = True
        elif numbers[binary_mid] < target:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.R: # Press 'R' key to restart the program
        reset_searches()
    elif symbol == pyglet.window.key.SPACE: # Press 'Space' key to start the program
        pyglet.clock.schedule_interval(update_searches, 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 47.5
        y_linear = window.height // 2 + 120
        y_binary = window.height // 2 + 10
        width = 28
        height = 28

        # Linear search boxes (Top half)
        if linear_found and i == linear_index:
            color_linear = (0, 255, 0) 
        elif i == linear_index: 
            color_linear = (255, 0, 0) 
        else: 
            color_linear = (200, 200, 200)

        pyglet.shapes.Rectangle(x-2, y_linear-2, width+4, height+4, color=color_linear, batch=batch).draw()
        pyglet.shapes.Rectangle(x, y_linear, width, height, color=(0, 0, 0), batch=batch).draw()
        label = pyglet.text.Label(str(number), font_size=12, x=x+width//2-1, y=y_linear+height//2+3, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

        # Binary search boxes (bottom half)
        if binary_found and i == binary_mid:
            color_binary = (0, 255, 0)
        elif binary_left <= i <= binary_right:
            color_binary = (255, 0, 0)
        else:
            color_binary = (200, 200, 200)
        pyglet.shapes.Rectangle(x-2, y_binary-2, width+4, height+4, color=color_binary, batch=batch).draw()
        pyglet.shapes.Rectangle(x, y_binary, width, height, color=(0, 0, 0), batch=batch).draw()
        label = pyglet.text.Label(str(number), font_size=12, x=x+width//2-1, y=y_binary+height//2+3, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

        # Draw the target number box
        target_x, target_y = window.width//2, 180 # Target number position

        if linear_found and binary_found == True:
            target_color = (0, 255, 0) # Target number box turn green when program found the target number
        else:
            target_color = (255, 0, 0) 

        pyglet.shapes.Rectangle((target_x-5)-12, target_y-5, width+20, height+20, color=target_color).draw()
        pyglet.shapes.Rectangle((target_x)-12, target_y, width+10, height+10, color=(0, 0, 0)).draw()
        pyglet.text.Label(str(target), font_size=20, x=target_x+height//2-7, y=target_y+height//2+11, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label(str('Target number is'), font_size=24, x=target_x, y=280, anchor_x='center', anchor_y='center').draw()

pyglet.app.run()