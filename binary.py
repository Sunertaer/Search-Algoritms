import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1280, height=720, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list
numbers = sorted(random.sample(range(1, 11), 10))
target = random.choice(numbers) # Target number to search for

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == target:
            found = True
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE: # Press 'Space' key to start the program
        pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)
# Schedule the linear search to run every 0.5 seconds

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 120 + 55
        y = window.height // 2 + 90
        width = 80
        height = 80

        # Draw the box
        if left <= i <= right and not search_complete:
            color = (100, 100, 255)  # Blue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 0, 0)  # Red for the middle element
        elif found and i == mid:
            color = (0, 255, 0)  # Green if target number is found
        else:
            color = (200, 200, 200)  # Grey for eliminated elements
        
        pyglet.shapes.Rectangle(x-10, y-10, width+20, height+20, color=color, batch=batch).draw()
        pyglet.shapes.Rectangle(x, y, width, height, color=(0, 0, 0), batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), font_size=30, x=x+width//2, y=y+height//2+4, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

        # Draw the target number box
        target_x, target_y = window.width//2, 180 # Target number position

        if search_complete == True:
            target_color = (0, 255, 0) # Target number box turn green when program found the target number
        else:
            target_color = (255, 0, 0) 

        pyglet.shapes.Rectangle(target_x-52, target_y-10, width+20, height+20, color=target_color).draw()
        pyglet.shapes.Rectangle(target_x-42, target_y, width, height, color=(0, 0, 0)).draw()
        pyglet.text.Label(str(target), font_size=30, x=target_x+height//2-42, y=target_y+height//2+4, anchor_x='center', anchor_y='center').draw()
        pyglet.text.Label(str('Target number is'), font_size=30, x=target_x, y=330, anchor_x='center', anchor_y='center').draw()

pyglet.app.run()
