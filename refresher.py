import pyautogui
import time
import keyboard

# Function to click at the given position (x, y)
def click_at_position(x, y):
    # Move the cursor to the specified position (x, y)
    pyautogui.moveTo(x, y)
    print(f"Cursor moved to position: ({x}, {y})")
    
    # Click the mouse at the position
    pyautogui.click()
    print("Clicked at the position")

# Function to simulate Ctrl+E, Ctrl+V, and Enter
def press_ctrl_e_v_enter():
    # Press Ctrl + E
    keyboard.press_and_release('ctrl+e')
    print("Pressed Ctrl + E")

    # Wait for a brief moment before pressing Ctrl + V
    time.sleep(0.5)
    
    # Press Ctrl + V
    keyboard.press_and_release('ctrl+v')
    print("Pressed Ctrl + V")

    # Wait a moment before pressing Enter
    time.sleep(0.5)
    
    # Press Enter
    keyboard.press_and_release('enter')
    print("Pressed Enter")

# Main function to perform the actions
def perform_actions(x, y):
    time.sleep(5)
    # Step 1: Click at the defined position
    click_at_position(x, y)
    
    # Step 2: Simulate Ctrl + E, Ctrl + V, and Enter
    press_ctrl_e_v_enter()

# Example usage
x = 500  # Define the x-axis position
y = 300  # Define the y-axis position

# Perform the actions
perform_actions(x, y)
