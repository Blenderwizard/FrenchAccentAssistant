# Import modules
import time
from pynput.keyboard import Key, Controller
from pynput import keyboard

#Creates a keyboard controller
keyControl = Controller()

# Defining variables
lastKeys = ["",""] # Defines last 2 keysisShiftHeld = False # If shift key is being held, evaluate true
isShiftHeld = False # Flag if Shift is currently pressed
isCapsHeld = False # Flag if Caps is was pressed during program runtime


def emulate_keypress(to_press):
    keyControl.press(Key.backspace)
    keyControl.release(Key.backspace)
    keyControl.press(Key.backspace)
    keyControl.release(Key.backspace)
    keyControl.press(to_press)
    keyControl.release(to_press)

# Function finds keys on press
def on_press(key):
    # Get the global shift and capslock flags
    global isShiftHeld
    global isCapsHeld

    capVar = [')','!','@','#','$','%','^','&','*','('] # number capitals

    try:
        # Tests for if key is alphanumeric, AttributeError thrown if key is not alphanumeric
        'alphanumeric key {0} pressed'.format(key.char)

        #Edits last 2 key pressed info, need logic for shift cases because upper no work on all characters
        lastKeys[0] = lastKeys[1]
        if isShiftHeld or isCapsHeld:
            if isShiftHeld:
                lastKeys[1] = '{0}'.format(key.char).upper()
                for i in range(10): # Number keys compiled
                    if str(i) == '{0}'.format(key.char):
                        lastKeys[1] = capVar[i]
                if '{0}'.format(key.char) == '`':
                    lastKeys[1] = '~'
                elif  '{0}'.format(key.char) == '-':
                    lastKeys[1] = '_'
                elif '{0}'.format(key.char) == '=':
                    lastKeys[1] = '+'
                elif '{0}'.format(key.char) == '[':
                    lastKeys[1] = '{'
                elif '{0}'.format(key.char) == ']':
                    lastKeys[1] = '}'
                elif '{0}'.format(key.char) == ';':
                    lastKeys[1] = ':'
                elif '{0}'.format(key.char) == '\'':
                    lastKeys[1] = '"'
                elif '{0}'.format(key.char) == ',':
                    lastKeys[1] = '<'
                elif '{0}'.format(key.char) == '.':
                    lastKeys[1] = '>'
                elif '{0}'.format(key.char) == '/':
                    lastKeys[1] = '?'
                elif '{0}'.format(key.char) == '\\':
                    lastKeys[1] = '|'
            else:
                lastKeys[1] = '{0}'.format(key.char).upper()
        else:
            lastKeys[1] = '{0}'.format(key.char)

    except AttributeError:
        # Edits the shift and capslock flags, omits in lastkeypressed item
        if ('{0}'.format(key) == 'Key.caps_lock' or '{0}'.format(key) == 'Key.shift'):
            if ('{0}'.format(key) == 'Key.caps_lock' and not isCapsHeld):
                isCapsHeld = True
            elif '{0}'.format(key) == 'Key.shift':
                isShiftHeld = True
            else:
                isCapsHeld = False
        else:
            # Edits last 2 key pressed info
            lastKeys[0] = lastKeys[1]
            lastKeys[1] = '{0}'.format(key)

    #Check keys if combo exist, then replaces with letter
    if lastKeys[0] == '\'':
        if lastKeys[1] == 'e':
            emulate_keypress('é')
        elif lastKeys[1] == 'E':
            emulate_keypress('É')
    elif lastKeys[0] == '`':
        if lastKeys[1] == 'a':
            emulate_keypress('à')
        elif lastKeys[1] == 'A':
            emulate_keypress('À')
        elif lastKeys[1] == 'e':
            emulate_keypress('è')
        elif lastKeys[1] == 'E':
            emulate_keypress('È')
        elif lastKeys[1] == 'u':
            emulate_keypress('ù')
        elif lastKeys[1] == 'U':
            emulate_keypress('Ù')
    elif lastKeys[0] == ':':
        if lastKeys[1] == 'e':
            emulate_keypress('ë')
        elif lastKeys[1] == 'E':
            emulate_keypress('Ë')
        elif lastKeys[1] == 'i':
            emulate_keypress('ï')
        elif lastKeys[1] == 'I':
            emulate_keypress('Ï')
        elif lastKeys[1] == 'u':
            emulate_keypress('ü')
        elif lastKeys[1] == 'U':
            emulate_keypress('Ü')
    elif lastKeys[0] == '^':
        if lastKeys[1] == 'a':
            emulate_keypress('â')
        elif lastKeys[1] == 'A':
            emulate_keypress('Â')
        elif lastKeys[1] == 'e':
            emulate_keypress('ê')
        elif lastKeys[1] == 'E':
            emulate_keypress('Ê')
        elif lastKeys[1] == 'i':
            emulate_keypress('î')
        elif lastKeys[1] == 'I':
            emulate_keypress('Î')
        elif lastKeys[1] == 'o':
            emulate_keypress('ô')
        elif lastKeys[1] == 'O':
            emulate_keypress('Ô')
        elif lastKeys[1] == 'u':
            emulate_keypress('û')
        elif lastKeys[1] == 'U':
            emulate_keypress('Û')
    elif lastKeys[1] == '+':
        if lastKeys[0] == 'a':
            emulate_keypress('æ')
        elif lastKeys[0] == 'A':
            emulate_keypress('Æ')
        elif lastKeys[0] == 'o':
            emulate_keypress('œ')
        elif lastKeys[0] == 'O':
            emulate_keypress('Œ')
    elif lastKeys[0] == '<':
        if lastKeys[1] == '<':
            emulate_keypress('«')
    elif lastKeys[0] == '>':
        if lastKeys[1] == '>':
            emulate_keypress('»')
    elif lastKeys[0] == ',':
        if lastKeys[1] == 'c':
            emulate_keypress('ç')
        elif lastKeys[1] == 'C':
            emulate_keypress('Ç')



# Function find keys on release
def on_release(key):
    global isShiftHeld

    # Sees if the key is released
    if '{0}'.format(key) == 'Key.shift':
        isShiftHeld = False


# Collect events until released (Till program termination)
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
