import pyautogui
import time

# Function to continuously track cursor position
def track_cursor():
    try:
        while True:
            # Get the current position of the cursor
            x, y = pyautogui.position()
            
            # Print the cursor's position
            print(f"Cursor position: X={x}, Y={y}")
            
            # Wait for a short period before checking again
            time.sleep(0.1)  # 100ms delay
    except KeyboardInterrupt:
        print("\nTracking stopped.")

# Start tracking cursor
track_cursor()