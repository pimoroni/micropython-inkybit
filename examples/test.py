from microbit import *
import inkybit

x = 0
y = 0

for x in range(inkybit.HEIGHT):
    inkybit.set_pixel(x, x, 1)
for x in range(inkybit.HEIGHT):
    inkybit.set_pixel(inkybit.HEIGHT - x, x, 1)
for x in range(inkybit.HEIGHT):
    inkybit.set_pixel(inkybit.HEIGHT, x, 1)
    
inkybit.draw_icon(10, 10, Image.ARROW_E, 1)
inkybit.draw_icon(20, 10, Image.GHOST, 1)
    
inkybit.draw_icon(30, 10, Image.GIRAFFE, 1, double=True)

inkybit.set_pixel(0, 0, 1)
inkybit.set_pixel(inkybit.WIDTH - 1, 0, 1)
inkybit.set_pixel(inkybit.WIDTH - 1, inkybit.HEIGHT - 1, 1)
inkybit.set_pixel(0, inkybit.HEIGHT - 1, 1)

inkybit.write(10, 30, "The quick brown fox jumps over the lazy dog!", 1)
inkybit.write(10, 50, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!", 1)

inkybit.write(10, 90, "EPIC BIG TEXT", 1, double=True)
inkybit.write(10, 102, "EPIC BIG COLOR TEXT", 2, double=True)

inkybit.show()