import PIL
from PIL import ImageGrab
from PIL import Image
import keyboard


# Capture the entire screen
#screenshot = ImageGrab.grab()

# Save the screenshot as an image file
#screenshot.save("screenshot.png")

# Optionally, display the screenshot
# Define the coordinates of the area you want to capture
left =1500  # X-coordinate of the top-left corner of the area
top = 1030   # Y-coordinate of the top-left corner of the area
right = left+140 # X-coordinate of the bottom-right corner of the area
bottom = top+110 # Y-coordinate of the bottom-right corner of the area

# Capture the screenshot of the specified area
while True:
    if keyboard.KEY_DOWN:
        if keyboard.is_pressed('p'):
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
            print("img taken")
            #screenshot.show()
            #screenshot.save("test.png")
           
            img = Image.open(r"C:\Users\zerod\Desktop\prog\python\holocheat\test.png")
            intmage = Image.Image.getcolors(img)
            intshot = Image.Image.getcolors(screenshot)
            for x in range(len(intmage)-1):
                for y in range(len(intmage[x])-1):
                    if (intshot[x] != intmage[x]):
                        screenshot.putpixel((x,y),(255,255,255))
            screenshot.show()
        if keyboard.is_pressed("o"):
            break
    
print("a plus")
# Close the screenshot object
screenshot.close()


"""
 part of the screen
im=screenshot.grab(bbox=(10,10,500,500))
im.show()

"""