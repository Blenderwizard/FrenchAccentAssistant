# Import modules
from pynput.keyboard import Key, Controller
from pynput import keyboard
import time

#Creates a keyboard controller
keyControl = Controller()

# Defining variables
lastKeys = ["",""] # Defines last 2 keysisShiftHeld = False # If shift key is being held, evaluate true
isShiftHeld = False # Flag if Shift is currently pressed
isCapsHeld = False # Flag if Caps is was pressed during program runtime

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
        if (isShiftHeld or isCapsHeld):
            if (isShiftHeld):
                lastKeys[1] = '{0}'.format(key.char).upper()
                for i in range(10): # Number keys compiled
                    if (str(i) == '{0}'.format(key.char)):
                        lastKeys[1] = capVar[i]
                if ('`' == '{0}'.format(key.char)):
                    lastKeys[1] = '~'
                elif ('-' == '{0}'.format(key.char)):
                    lastKeys[1] = '_'
                elif ('=' == '{0}'.format(key.char)):
                    lastKeys[1] = '+'
                elif ('[' == '{0}'.format(key.char)):
                    lastKeys[1] = '{'
                elif (']' == '{0}'.format(key.char)):
                    lastKeys[1] = '}'
                elif (';' == '{0}'.format(key.char)):
                    lastKeys[1] = ':'
                elif ('\'' == '{0}'.format(key.char)):
                    lastKeys[1] = '"'
                elif (',' == '{0}'.format(key.char)):
                    lastKeys[1] = '<'
                elif ('.' == '{0}'.format(key.char)):
                    lastKeys[1] = '>'
                elif ('/' == '{0}'.format(key.char)):
                    lastKeys[1] = '?'
                elif ('\\' == '{0}'.format(key.char)):
                    lastKeys[1] = '|'
            else:
                lastKeys[1] = '{0}'.format(key.char).upper()
        else:
            lastKeys[1] = '{0}'.format(key.char)
        
    except AttributeError:
        # Edits the shift and capslock flags, omits in lastkeypressed item
        if ('{0}'.format(key) == 'Key.caps_lock' or '{0}'.format(key) == 'Key.shift'):
            if ('{0}'.format(key) == 'Key.caps_lock' and isCapsHeld == False):
                isCapsHeld = True
            elif ('{0}'.format(key) == 'Key.shift'):
                isShiftHeld = True
            else:
                isCapsHeld = False
        else:
            # Edits last 2 key pressed info
            lastKeys[0] = lastKeys[1]
            lastKeys[1] = '{0}'.format(key)
        
    #Check keys if combo exist, then replaces with letter  
    if(lastKeys[0] == '\''):
        if (lastKeys[1] == 'e'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('é')
            keyControl.release('é')
        elif (lastKeys[1] == 'E'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('É')
            keyControl.release('É')
    elif(lastKeys[0] == '`'):
        if (lastKeys[1] == 'a'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('à')
            keyControl.release('à')
        elif (lastKeys[1] == 'A'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('À')
            keyControl.release('À')
        elif (lastKeys[1] == 'e'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('è')
            keyControl.release('è')
        elif (lastKeys[1] == 'E'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('È')
            keyControl.release('È')
        elif (lastKeys[1] == 'u'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ù')
            keyControl.release('ù')
        elif (lastKeys[1] == 'U'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ù')
            keyControl.release('Ù')
    elif(lastKeys[0] == ':'):
        if (lastKeys[1] == 'e'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ë')
            keyControl.release('ë')
        elif (lastKeys[1] == 'E'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ë')
            keyControl.release('Ë')
        elif (lastKeys[1] == 'i'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ï')
            keyControl.release('ï')
        elif (lastKeys[1] == 'I'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ï')
            keyControl.release('Ï')
        elif (lastKeys[1] == 'u'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ü')
            keyControl.release('ü')
        elif (lastKeys[1] == 'U'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ü')
            keyControl.release('Ü')
    elif(lastKeys[0] == '^'):
        if (lastKeys[1] == 'a'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('â')
            keyControl.release('â')
        elif (lastKeys[1] == 'A'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Â')
            keyControl.release('Â')
        elif (lastKeys[1] == 'e'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ê')
            keyControl.release('ê')
        elif (lastKeys[1] == 'E'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ê')
            keyControl.release('Ê')
        elif (lastKeys[1] == 'i'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('î')
            keyControl.release('î')
        elif (lastKeys[1] == 'I'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Î')
            keyControl.release('Î')
        elif (lastKeys[1] == 'o'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ô')
            keyControl.release('ô')
        elif (lastKeys[1] == 'O'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ô')
            keyControl.release('Ô')
        elif (lastKeys[1] == 'u'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('û')
            keyControl.release('û')
        elif (lastKeys[1] == 'U'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Û')
            keyControl.release('Û')
    elif(lastKeys[1] == '+'):
        if (lastKeys[0] == 'a'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('æ')
            keyControl.release('æ')
        elif (lastKeys[0] == 'A'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Æ')
            keyControl.release('Æ')
        elif (lastKeys[0] == 'o'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('œ')
            keyControl.release('œ')
        elif (lastKeys[0] == 'O'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Œ')
            keyControl.release('Œ')
    elif(lastKeys[0] == '<'):
        if (lastKeys[1] == '<'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('«')
            keyControl.release('«')
    elif(lastKeys[0] == '>'):
        if (lastKeys[1] == '>'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('»')
            keyControl.release('»')
    elif(lastKeys[0] == ','):
        if (lastKeys[1] == 'c'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('ç')
            keyControl.release('ç')
        elif (lastKeys[1] == 'C'):
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press(Key.backspace)
            keyControl.release(Key.backspace)
            keyControl.press('Ç')
            keyControl.release('Ç')
    
        

# Function find keys on release
def on_release(key):
    global isShiftHeld
    
    # Sees if the key is released
    if ('{0}'.format(key) == 'Key.shift'):
        isShiftHeld = False


# Collect events until released (Till program termination)
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
