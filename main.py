from PIL import Image, ImageGrab
from pyautogui import press
import time
import keyboard
import multiprocessing

n = int(input("How many pages are in your pdf?: "))

x = int(input("Specify x-pixel-coordinate of top-left of page: "))
y =  int(input("Specify y-pixel-coordinate of top-left of page: "))
x2 = int(input("Specify x-pixel-coordinate of bottom-right of page: "))
y2 = int(input("Specify y-pixel-coordinate of bottom-right of page: "))

cover_image = input("Specify cover-image file name and type: ")

#print("Press next-page button for E-Book: ")
#next_page = keyboard.read_key()
#comment the next line out and uncomment the last two if you want to manually press the next-page button.
next_page = input("Specify next-page button for E-Book: ")

print("Page capture will start in 10 seconds, please click on the E-Book app.")

count = multiprocessing.cpu_count()
sleepTime = 2;
if count>=4:
    sleepTime = 1;

time.sleep(10)

capture = (x, y, x2, y2)
images = []
firstPage = Image.open(cover_image).convert("RGB")

for i in range(0, n):
    press(next_page)
    time.sleep(1)
    im = ImageGrab.grab(bbox=capture).convert('RGB')
    images.append(im)

firstPage.save("outputPDF.pdf", "PDF", resolution=100.0, save_all=True, append_images=images)
print("Operation successful, check root folder for output.")
