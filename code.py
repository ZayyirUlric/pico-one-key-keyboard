import rotaryio
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)
button = DigitalInOut(board.GP4)
button.switch_to_input(pull=Pull.UP)
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
last_position = None

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
keymap = {
    (0): ([Keycode.A]),
    (1): ([Keycode.B]),
    (2): ([Keycode.C]),
    (3): ([Keycode.D]),
    (4): ([Keycode.E]),
    (5): ([Keycode.F]),
    (6): ([Keycode.G]),
    (7): ([Keycode.H]),
    (8): ([Keycode.I]),
    (9): ([Keycode.J]),
    (10): ([Keycode.K]),
    (11): ([Keycode.L]),
    (12): ([Keycode.M]),
    (13): ([Keycode.N]),
    (14): ([Keycode.O]),
    (15): ([Keycode.P]),
    (16): ([Keycode.Q]),
    (17): ([Keycode.R]),
    (18): ([Keycode.S]),
    (19): ([Keycode.T]),
    (20): ([Keycode.U]),
    (21): ([Keycode.V]),
    (22): ([Keycode.W]),
    (23): ([Keycode.X]),
    (24): ([Keycode.Y]),
    (25): ([Keycode.Z]),
    (26): ((Keycode.SHIFT, Keycode.A)),
    (27): ((Keycode.SHIFT, Keycode.B)),
    (28): ((Keycode.SHIFT, Keycode.C)),
    (29): ((Keycode.SHIFT, Keycode.D)),
    (30): ((Keycode.SHIFT, Keycode.E)),
    (31): ((Keycode.SHIFT, Keycode.F)),
    (32): ((Keycode.SHIFT, Keycode.G)),
    (33): ((Keycode.SHIFT, Keycode.H)),
    (34): ((Keycode.SHIFT, Keycode.I)),
    (35): ((Keycode.SHIFT, Keycode.J)),
    (36): ((Keycode.SHIFT, Keycode.K)),
    (37): ((Keycode.SHIFT, Keycode.L)),
    (38): ((Keycode.SHIFT, Keycode.M)),
    (39): ((Keycode.SHIFT, Keycode.N)),
    (40): ((Keycode.SHIFT, Keycode.O)),
    (41): ((Keycode.SHIFT, Keycode.P)),
    (42): ((Keycode.SHIFT, Keycode.Q)),
    (43): ((Keycode.SHIFT, Keycode.R)),
    (44): ((Keycode.SHIFT, Keycode.S)),
    (45): ((Keycode.SHIFT, Keycode.T)),
    (46): ((Keycode.SHIFT, Keycode.U)),
    (47): ((Keycode.SHIFT, Keycode.V)),
    (48): ((Keycode.SHIFT, Keycode.W)),
    (49): ((Keycode.SHIFT, Keycode.X)),
    (50): ((Keycode.SHIFT, Keycode.Y)),
    (51): ([Keycode.ZERO]),
    (52): ([Keycode.ONE]),
    (53): ([Keycode.TWO]),
    (54): ([Keycode.THREE]),
    (55): ([Keycode.FOUR]),
    (56): ([Keycode.FIVE]),
    (57): ([Keycode.SIX]),
    (58): ([Keycode.SEVEN]),
    (59): ([Keycode.EIGHT]),
    (60): ([Keycode.NINE]),
    (61): ((Keycode.SHIFT, Keycode.ZERO)),
    (62): ((Keycode.SHIFT, Keycode.ONE)),
    (63): ((Keycode.SHIFT, Keycode.TWO)),
    (64): ((Keycode.SHIFT, Keycode.THREE)),
    (65): ((Keycode.SHIFT, Keycode.FOUR)),
    (66): ((Keycode.SHIFT, Keycode.FIVE)),
    (67): ((Keycode.SHIFT, Keycode.SIX)),
    (68): ((Keycode.SHIFT, Keycode.SEVEN)),
    (69): ((Keycode.SHIFT, Keycode.EIGHT)),
    (70): ((Keycode.SHIFT, Keycode.NINE)),
    (71): ([Keycode.SPACE]),
    (72): ([Keycode.ENTER]),
    (73): ([Keycode.PERIOD]),
    (74): ([Keycode.COMMA]),
    (75): ((Keycode.SHIFT, Keycode.FORWARD_SLASH)),
    (76): ((Keycode.SHIFT,)),
}  # 0 to 76
pointer = 0
while True:
    led.value = not button.value
    position = encoder.position
    if button.value == False:
        kbd.press(Keycode.SPACEBAR)
        kbd.release(Keycode.SPACEBAR)
        time.sleep(0.5)
    if last_position is None or position != last_position:
        try:
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            if int(position) > int(last_position):
                pointer += 1
                if pointer > 76:
                    pointer = 0
                else:
                    pass
            else:
                pointer -= 1
                if pointer < 0:
                    pointer = 76
                else:
                    pass
            print(keymap[pointer])
            kbd.press(*keymap[pointer])
            kbd.release(*keymap[pointer])
            last_position = position
        except:
            pass
    last_position = position
