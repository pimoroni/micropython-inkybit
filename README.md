# MicroPython inky:bit library for the BBC micro:bit

# Installing

First, install the Mu micropython editor from https://codewith.mu/ by following the instructions online.

Copy the code from library/inkybit.py into your "mu_code" folder by pasting it into the blank file in the Mu editor and saving it as "inkybit.py". The folder might be in:

* C:\Users\YourUserName\mu_code on Windows
* /Users/YourUserName/mu_code on macOS

Create a new blank file in Mu for your project, leave it blank and Flash it to your micro:bit with the Flash button. You can close this for now.

Create another new file, save this one as "main.py" and keep it open.

Now open the "Files" dialog (you might have to close the "Repl" first) and drag and drop main.py and inkybit.py from the right pane, to the left pane.

When you reset your micro:bit, it will load main.py- so you can "import inkybit" and start writing your code here!


# Function Reference

## Draw text to your inky:bit

`inkybit.write(text, x, y, color=1, double=False)`

Text will be written starting from `x,y`. If `double` is `False` then characters will be 5 pixels tall and suitable for close reading. Setting `double` to `True` will double the size of text, making it easier to read from a distance.

## Draw an icon to your inky:bit

`inkybit.draw_icon(icon, x, y, color=1, double=False)`

`icon` must be a micro:bit `Image` such as `Image.GHOST`.

