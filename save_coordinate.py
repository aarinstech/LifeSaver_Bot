import pyautogui
import time

print("Move your mouse to the first position and wait for 12 seconds...")
print("And then move your mouse to the second position and again wait for 12 seconds...")
print("Press Enter to continue...")
temp = input()

time.sleep(10)
pos1 = pyautogui.position()
print(f"First position: {pos1}")

time.sleep(10)
pos2 = pyautogui.position()
print(f"Second position: {pos2}")

with open("temp.txt", "w") as f:
    f.write(f"{pos1.x}\n{pos1.y}\n")
    f.write(f"{pos2.x}\n{pos2.y}\n")

print("\nProcess Completed!")