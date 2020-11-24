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

inkybit.draw_rectangle(125, 0, 25, 20, inkybit.BLACK)

inkybit.draw_rectangle(152, 0, 1, 1, inkybit.BLACK)
inkybit.draw_rectangle(155, 0, 2, 2, inkybit.BLACK)
inkybit.draw_rectangle(160, 0, 4, 4, inkybit.BLACK)

inkybit.draw_rectangle(210, 0, 25, 20, inkybit.BLACK, True)
inkybit.draw_rectangle(210, 0, 25, 20, inkybit.ACCENT)
    
inkybit.draw_image(Image.ARROW_E, 10, 10, 1, text_size=inkybit.TEXT_TINY)
inkybit.draw_image(Image.GHOST, 20, 10, 1, text_size=inkybit.TEXT_TINY)

inkybit.draw_image(Image.GIRAFFE, 30, 10, 1)
inkybit.draw_image(Image.GIRAFFE, 50, 10, 1, text_size=inkybit.TEXT_MEDIUM)
inkybit.draw_image(Image.GIRAFFE, 70, 10, 1, text_size=inkybit.TEXT_LARGE)

inkybit.set_pixel(0, 0, 1)
inkybit.set_pixel(inkybit.WIDTH - 1, 0, 1)
inkybit.set_pixel(inkybit.WIDTH - 1, inkybit.HEIGHT - 1, 1)
inkybit.set_pixel(0, inkybit.HEIGHT - 1, 1)

inkybit.write("The quick brown fox jumps over the lazy dog!", 10, 30, 1, text_size=inkybit.TEXT_TINY)
inkybit.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!", 10, 50, 1, text_size=inkybit.TEXT_TINY)

inkybit.write("EPIC BIG TEXT", 10, 75, 1, text_size=inkybit.TEXT_MEDIUM)
inkybit.write("EPIC COLOR TEXT", 10, 102, 2, text_size=inkybit.TEXT_MEDIUM)

inkybit.show()