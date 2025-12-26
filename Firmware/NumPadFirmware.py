# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner # or use MatrixScanner if you have rows/cols
from kmk.keys import KC
from kmk.modules.macros import Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension (needed for Num Lock toggle behavior)
macros = Macros()
keyboard.modules.append(macros)

# --- Define your pins here! ---
# You must replace these with the actual GPIO pins your board uses.
# The number of pins depends on how your numpad hardware is wired.
# This example assumes a simple 17-pin direct wiring (KeysScanner), 
# which is common for simple projects like the Hack Club Hackpad.

PINS = [
    board.D0, board.D1, board.D2, board.D3, 
    board.D4, board.D5, board.D6, board.D7, 
    board.D8, board.D9, board.D10, board.D11, 
    board.D12, board.D13, board.D14, board.D15, 
    board.D16
]

# Tell kmk we are using a simple keypad scanner with 17 pins
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, # Change to True if your circuit uses pull-down resistors
)

# --- Define the keymap based on the numpad image ---
# The keys correspond to the PINS list in order.
# When Num Lock is OFF, the arrow/navigation keys (Home, PgUp, arrows, End, PgDn, Ins, Del) are active.
# When Num Lock is ON, the numbers (0-9) and symbols (/, *, -, +) are active.

keyboard.keymap = [
    [
        KC.NUM_LOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
        KC.KP_HOME, KC.KP_UP, KC.KP_PGUP, KC.KP_PLUS,
        KC.KP_LEFT, KC.KP_5, KC.KP_RIGHT, KC.KP_PLUS, # Note: KP_PLUS spans two spots
        KC.KP_END, KC.KP_DOWN, KC.KP_PGDN, KC.KP_ENTER,
        KC.KP_INS, KC.KP_0, KC.KP_DOT, KC.KP_ENTER # Note: KP_0 and KP_ENTER span two spots
    ]
]

# The layout above assumes the following physical wiring order for a standard 4-column numpad:
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
# 17 18 19 20 (Note: The visual layout is a 4x5 grid with some multi-key spans)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()