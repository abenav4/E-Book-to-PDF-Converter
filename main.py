from PIL import Image, ImageGrab
from pyautogui import press
import time
import multiprocessing

n = int(input("How many pages are in your pdf?: "))

x = int(input("Specify x-pixel-coordinate of top-left of screenshot: "))
y =  int(input("Specify y-pixel-coordinate of top-left of screenshot: "))
x2 = int(input("Specify x-pixel-coordinate of bottom-right of screenshot: "))
y2 = int(input("Specify y-pixel-coordinate of bottom-right of screenshot: "))

cover_image = input("Specify cover-image file name: ")

count = multiprocessing.cpu_count()
sleepTime = 2;
if count>4:
    sleepTime = 1;

time.sleep(10)

box = (x, y, x2, y2)
images = []
firstPage = Image.open(cover_image).convert("RGB")

for i in range(0, n):
    press("down")
    time.sleep(1)
    im = ImageGrab.grab(bbox=box).convert('RGB')
    images.append(im)

firstPage.save("outputPDF.pdf", "PDF", resolution=100.0, save_all=True, append_images=images)