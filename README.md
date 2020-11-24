# MicroPython inky:bit library for the BBC micro:bit

This library works with micro:bit V2 only. V1 just doesn't have enough RAM to store the display buffer. Sorry!

# Using inky:bit

## python.microbit.org

If you're using the online editor - https://python.microbit.org/v/2.1 - you must make sure you include the `inkybit.py` library:

1. Save `inkybit.py` somewhere memorable - right-click, save-as: https://raw.githubusercontent.com/pimoroni/micropython-inkybit/master/library/inkybit.py
2. Go to python.microbit.org
3. Click "Load/Save"
4. Expand the Project Files by clicking "Show Files"
5. Click "Add file"
6. Select the `inkybit.py` file that you saved
7. Now you can `import inkybit` and get programming!

## Mu

First, install the Mu micropython editor from https://codewith.mu/ by following the instructions online.

Copy the code from library/inkybit.py into your "mu_code" folder by pasting it into the blank file in the Mu editor and saving it as "inkybit.py". The folder might be in:

* C:\Users\YourUserName\mu_code on Windows
* /Users/YourUserName/mu_code on macOS

Create a new blank file in Mu for your project, leave it blank and Flash it to your micro:bit with the Flash button. You can close this for now.

Create another new file, save this one as "main.py" and keep it open.

Now open the "Files" dialog (you might have to close the "Repl" first) and drag and drop main.py and inkybit.py from the right pane, to the left pane.

When you reset your micro:bit, it will load main.py- so you can "import inkybit" and start writing your code here!

# Function Reference

## Colours and Text Sizes

inky:bit includes constants for the three available colours (White, Black, Red) and four text sizes (Tiny, Normal, Medium, Large):

#### Colours

```python
inkybit.WHITE
inkybit.BLACK
inkybit.ACCENT
```

#### Text Sizes

The four available text sizes work by changing the size of each pixel to 1x1, 2x2, 3x3 or 4x4:

```python
inkybit.TEXT_TINY    # Text/icons are 5px tall
inkybit.TEXT_NORMAL  # Text/icons are 10px tall (default, easier to read)
inkybit.TEXT_MEDIUM  # Text/icons are 15px tall
inkybit.TEXT_LARGE   # Text/icons are 20px tall
```

## Draw text to your inky:bit

`inkybit.write(text, x, y, color=inkybit.BLACK, text_size=inkybit.TEXT_NORMAL)`

Text will be written starting from `x,y`.

## Draw an icon to your inky:bit

`inkybit.draw_icon(icon, x, y, color=inkybit.BLACK, text_size=inkybit.TEXT_NORMAL)`

`icon` must be a micro:bit `Image` such as `Image.GHOST`.

## Draw a line on your inky:bit

`inkybit.draw_line(x0, y0, x1, y1, color=inkybit.BLACK)`

Draws a line from `x0,y0` to `x1,y1` in your chosen colour.

## Draw a rectangle on your inky:bit

`inkybit.draw_rectangle(x, y, width, height, color=inkybit.BLACK, filled=False)`

Draws a rectangle of your chosen width/height at `x,y`.

If `filled` is `True` then the rectangle will be solid. Otherwise it's just a 1px outline.

## Set an image to your inky:bit

`inkybit.draw_bin("filename.bin")`

Use the `image-to-raw.py` file to convert an 8bit PNG file with White, Black and Red colours only into a raw image suitable for inky:bit. You'll need to add that raw image to your project with the same method you used to add `inkybit.py`.
