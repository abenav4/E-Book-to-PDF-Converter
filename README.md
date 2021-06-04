# E-Book-to-PDF-Converter

Make sure you have the latest version of Python, Pillow and PyAutoGUI installed.

To run the program, open a command prompt, navigate to the root folder of this directory, and enter:

`python -i main.py`

If you want a custom first page (such as a cover page) of the E-Book, include it in the root folder of this directory. Otherwise, simply type `default.png` when prompted, as a first page image file is provided in the directory.

When asked to specify the next-page button for the E-Book, common values include: `down` `PgDn` `right`.
After entering this value, you'll have ten seconds to open up your E-Book application. Do not unfocus the E-Book application while the program flips through the pages.

The final output file will be called `outputPDF.pdf` and it will be located in the root folder of the directory.

Example program output: 
```
python -i main.py
How many pages are in your pdf?: 4
Specify x-pixel-coordinate of top-left of page: 25
Specify y-pixel-coordinate of top-left of page: 25
Specify x-pixel-coordinate of bottom-right of page: 800
Specify y-pixel-coordinate of bottom-right of page: 800
Specify cover-image file name and type: default.png
Specify next-page button for E-Book: right
Page capture will start in 10 seconds, please click on the E-Book app.
Operation successful, check root folder for output.
```
