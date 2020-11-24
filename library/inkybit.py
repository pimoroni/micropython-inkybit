from microbit import *
from micropython import const

COLS = const(136)
ROWS = const(250)
OFFSET_X = const(0)
OFFSET_Y = const(6)

WIDTH = const(250)
HEIGHT = const(122)

DRIVER_CONTROL = const(0x01)
GATE_VOLTAGE = const(0x03)
SOURCE_VOLTAGE = const(0x04)
DISPLAY_CONTROL = const(0x07)
NON_OVERLAP = const(0x0B)
BOOSTER_SOFT_START = const(0x0C)
GATE_SCAN_START = const(0x0F)
DEEP_SLEEP = const(0x10)
DATA_MODE = const(0x11)
SW_RESET = const(0x12)
TEMP_WRITE = const(0x1A)
TEMP_READ = const(0x1B)
TEMP_CONTROL = const(0x1C)
TEMP_LOAD = const(0x1D)
MASTER_ACTIVATE = const(0x20)
DISP_CTRL1 = const(0x21)
DISP_CTRL2 = const(0x22)
WRITE_RAM = const(0x24)
WRITE_ALTRAM = const(0x26)
READ_RAM = const(0x25)
VCOM_SENSE = const(0x28)
VCOM_DURATION = const(0x29)
WRITE_VCOM = const(0x2C)
READ_OTP = const(0x2D)
WRITE_LUT = const(0x32)
WRITE_DUMMY = const(0x3A)
WRITE_GATELINE = const(0x3B)
WRITE_BORDER = const(0x3C)
SET_RAMXPOS = const(0x44)
SET_RAMYPOS = const(0x45)
SET_RAMXCOUNT = const(0x4E)
SET_RAMYCOUNT = const(0x4F)
NOP = const(0xFF)

spi_dc = pin12
spi_cs = pin8
reset = pin2
busy = pin16

CS_ACTIVE = const(0)
CS_INACTIVE = const(0)

TEXT_TINY = const(1)
TEXT_NORMAL = const(2)
TEXT_MEDIUM = const(3)
TEXT_LARGE = const(4)

WHITE = const(0)
BLACK = const(1)
ACCENT = const(2)

LUTS_BLACK = bytearray([
    0x02, 0x02, 0x01, 0x11, 0x12, 0x12, 0x22, 0x22, 0x66, 0x69,
    0x69, 0x59, 0x58, 0x99, 0x99, 0x88, 0x00, 0x00, 0x00, 0x00,
    0xF8, 0xB4, 0x13, 0x51, 0x35, 0x51, 0x51, 0x19, 0x01, 0x00
])

_icons = [getattr(Image, x) for x in dir(Image) if hasattr(getattr(Image, x), 'get_pixel')]


def icon_format(text):
    replace = {}
    for attr_name in dir(Image):
        attr = getattr(Image, attr_name)
        if attr in _icons and attr_name in text:
            replace[attr_name] = chr(128 + _icons.index(attr))

    return text.format(**replace)


def char_len(char, text_size=TEXT_NORMAL):
    if char in b"\"*+-0123<=>ABCDEFHKLOPQSUXZ[]^bcdefghjklnopqrsxz{":
        return 4 * text_size
    if char in b"!'.:i|":
        return 2 * text_size
    if char in b" (),;I`}":
        return 3 * text_size
    return 5 * text_size


def text_len(text, text_size=TEXT_NORMAL):
    return sum(char_len(c, text_size=text_size) + text_size for c in text)


def write(text, x, y, color=1, text_size=TEXT_NORMAL):
    image = None
    for letter in text:
        image = None
        letter_width = char_len(letter, text_size=text_size)

        if letter != " " and (x + letter_width) >= 1:
            if ord(letter) > 127:
                image = _icons[ord(letter) - 128]
            else:
                try:
                    image = Image(letter)
                except:
                    pass

        if image is not None:
            if not draw_image(image, x, y, color, text_size=text_size):
                return

        x += letter_width + text_size

    del image


def draw_image(icon, x, y, color=1, text_size=TEXT_NORMAL):
    cols = 5 * text_size
    rows = 5 * text_size
    for ox in range(cols):
        if x + ox < 0:
            continue
        if x + ox >= WIDTH:
            return False
        for oy in range(rows):
            if not icon.get_pixel(ox // text_size, oy // text_size):
                continue
            try:
                set_pixel(ox + x, oy + y, color)
            except IndexError:
                pass
    return True


def set_pixel(x, y, color=1):
    y += OFFSET_Y
    y = COLS - 1 - y
    shift = 7 - y % 8
    y //= 8

    offset = x * (COLS // 8) + y

    if offset >= len(buf_b):
        return

    byte_b = buf_b[offset] | (0b1 << shift)
    byte_r = buf_r[offset] & ~(0b1 << shift)

    if color == 2:
        # Set a bit to set as red/yellow
        byte_r |= 0b1 << shift
    if color == 1:
        # Mask *out* a bit to set as black
        byte_b &= ~(0b1 << shift)

    buf_b[offset] = byte_b
    buf_r[offset] = byte_r


def draw_line(x0, y0, x1, y1, color=1):
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1

    err = dx + dy
    while True:
        set_pixel(x0, y0, color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def draw_rectangle(x, y, width, height, color=1, filled=False):
    width -= 1
    height -= 1

    draw_line(x, y, x + width, y, color)
    draw_line(x, y, x, y + height, color)
    draw_line(x + width, y, x + width, y + height, color)
    draw_line(x, y + height, x + width, y + height, color)

    if filled:
        x += 1
        y += 1
        width -= 1
        height -= 1
        for px in range(width):
            for py in range(height):
                set_pixel(x + px, y + py, color)


def clear():
    global buf_b, buf_r
    buf_b = bytearray(b'\xFF' * (COLS // 8) * ROWS)
    buf_r = bytearray((COLS // 8) * ROWS)


def _busy_wait():
    while busy.read_digital():
        v = busy.read_digital()
        print(v)
        sleep(500)


def _spi_cmd(command, data=None):
    """Send command over SPI.
    :param command: command byte
    :param data: optional list of values
    """
    spi_cs.write_digital(CS_ACTIVE)
    spi_dc.write_digital(0)
    spi.write(bytearray([command]))
    if data is not None:
        spi_dc.write_digital(1)
        spi.write(bytearray(data))
    spi_cs.write_digital(CS_INACTIVE)


def _spi_data(data):
    spi_cs.write_digital(CS_ACTIVE)
    spi_dc.write_digital(1)
    spi.write(bytearray(data))
    spi_cs.write_digital(CS_INACTIVE)


def show():
    spi.init()
    reset.write_digital(0)
    sleep(500)
    reset.write_digital(1)
    sleep(500)

    _spi_cmd(0x12)
    sleep(1000)
    _busy_wait()

    _spi_cmd(DRIVER_CONTROL, [ROWS - 1, (ROWS - 1) >> 8, 0x00])
    _spi_cmd(WRITE_DUMMY, [0x1B])
    _spi_cmd(WRITE_GATELINE, [0x0B])
    _spi_cmd(DATA_MODE, [0x03])
    _spi_cmd(SET_RAMXPOS, [0x00, COLS // 8 - 1])
    _spi_cmd(SET_RAMYPOS, [0x00, 0x00, (ROWS - 1) & 0xFF, (ROWS - 1) >> 8])
    _spi_cmd(WRITE_VCOM, [0x70])
    _spi_cmd(WRITE_LUT, LUTS_BLACK)
    _spi_cmd(SET_RAMXCOUNT, [0x00])
    _spi_cmd(SET_RAMYCOUNT, [0x00, 0x00])

    _spi_cmd(WRITE_RAM)
    _spi_data(buf_b)

    _spi_cmd(WRITE_ALTRAM)
    _spi_data(buf_r)

    _busy_wait()
    _spi_cmd(MASTER_ACTIVATE)


clear()