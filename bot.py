import pyautogui
import time
import keyboard

# List of x and y coordinates
x = [370, 900, 1400, 370, 900, 1400]
y = [300, 300, 300, 700, 700, 700]

#time interval
time_seconds = 60

yt_link = "https://www.youtube.com/@cla_sterling8633/shorts"

# Function to move cursor and scroll
def move_and_scroll_down():
    # Loop through the list of coordinates
    # Wait for 1 minute before moving to the next position
    print(f"Waiting for 1 minute before moving to position")
    time.sleep(time_seconds)  # Wait for 1 minute
    for i in range(len(x)):        
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i], y[i])
        print(f"Cursor moved to position: ({x[i]}, {y[i]})")
        
        # Scroll down
        pyautogui.scroll(-300)  # Negative value to scroll down
        print("Scrolled down")
        
        # Small delay after scrolling
        time.sleep(0.5)

def move_and_scroll_up():
    # Loop through the list of coordinates
    # Wait for 1 minute before moving to the next position
    print(f"Waiting for 1 minute before moving to position")
    time.sleep(time_seconds)  # Wait for 1 minute
    for i in range(len(x)):        
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i], y[i])
        print(f"Cursor moved to position: ({x[i]}, {y[i]})")
        
        # Scroll up
        pyautogui.scroll(300)  # Positive value to scroll up
        print("Scrolled up")
        
        # Small delay after scrolling
        time.sleep(0.5)

def refresher():
    # Move the cursor to the specified position (x, y)
    for i in range(len(x)):        
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i], y[i])
        print(f"Cursor moved to position: ({x[i]}, {y[i]})")
        time.sleep(0.5)

        # Click the mouse at the position
        pyautogui.click()
        print("Clicked at the position")
        time.sleep(0.5)

        # Press Ctrl + E
        keyboard.press_and_release('ctrl+e')
        print("Pressed Ctrl + E")

        time.sleep(0.5)

        keyboard.press_and_release('backspace')
        print("Backspace pressed")

        # Wait for a brief moment before pressing Ctrl + V
        time.sleep(0.5)
        
        # write the link
        keyboard.write(yt_link)
        print("link pasted")

        # Wait a moment before pressing Enter
        time.sleep(0.5)
        
        # Press Enter
        keyboard.press_and_release('enter')
        print("Pressed Enter")
        
    time.sleep(60)

    #click page
    for i in range(3):        
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i], y[i] - 100)
        print(f"Cursor moved to position: ({x[i] - 200}, {y[i] + 150})")
        time.sleep(0.5)

        # Click the mouse at the position
        pyautogui.click()
        print("Clicked at the position")
        time.sleep(0.5)

    time.sleep(1)

    #click a short
    for i in range(3):        
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i] - 200, y[i] + 150)
        print(f"Cursor moved to position: ({x[i] - 200}, {y[i] + 150})")
        time.sleep(0.5)

        # Click the mouse at the position
        pyautogui.click()
        print("Clicked at the position")
        time.sleep(0.5)

    #scroll and click a short
    for i in range(3, 6):  # Start from index 3 to 5 (items 4-6)
        # Move the cursor to the specified position (x[i], y[i])
        pyautogui.moveTo(x[i], y[i] + 150)
        print(f"Cursor moved to position: ({x[i]}, {y[i] + 150})")
        time.sleep(0.5)

        # Scroll down
        pyautogui.scroll(-600)  # Negative value to scroll down
        print("Scrolled down")

        # Click the mouse at the position
        pyautogui.click()
        print("Clicked at the position")
        time.sleep(0.5)

# Run the sequence 6 times: move and scroll down, then up

time.sleep(5)
refresher()

while True:
    for _ in range(1):
        for _ in range(6):
            move_and_scroll_down()

        for _ in range(6):
            move_and_scroll_up()
    time.sleep(5)
    refresher()

# After finishing one full cycle (down + up), it will reset and repeat