# PyBrailleArt
This library can transform unicode-art made up of braille characters. It can invert, rotate and mirror any given unicode-braille-art string.

## Usage
Include both files *braille.py* and *braille_data.py* and import the functions with `from braille import *`. All functions take two parameters: 
 * input (*string*)
     * for best results every line should have an even amount of characters
     * the lines should be separated by spaces or newlines
 * [optional] dot_for_blank (*boolean*)
     * explained further below


## Invert
For example this:

<p>⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠋⠉⠉⠙⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⣿⣿⣿⠿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠻⣿⣿⣿⣿⣿ <br> 
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢻⣿⣿⣿ <br> 
⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⢀⣔⢤⣄⡀⠄⡄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿ <br> 
⠏⠄⠄⠄⠄⠄⠄⠄⢀⣀⣨⣵⣿⣿⣿⣿⣧⣦⣤⣀⣿⣷⡐⠄⠄⠄⠄⠄⢿⣿ <br> 
⠄⠄⠄⠄⠄⠄⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⢚⣿ <br> 
⣆⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⡿⠛⠛⠛⠛⣿⢿⣿⣿⣿⡿⢟⣻⣄⣤⣮⡝⣿ <br> 
⣿⠆⠄⠄⠄⠄⠄⠄⠄⠄⠉⠘⣿⡗⡕⣋⢉⣩⣽⣬⣭⣶⣿⣿⣿⣿⣝⣻⣷⣿ <br> 
⣿⣦⡀⠄⠄⠠⢀⠄⠄⠁⠄⠄⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿ <br> 
⣿⣿⣿⡆⠄⠄⠰⣶⡗⠄⠄⠄⣿⣿⣿⣿⣦⣌⠙⠿⣿⣿⣿⣿⣿⣿⣿⡛⠱⢿ <br> 
⣿⣿⣿⣿⡀⠄⠄⠿⣿⠄⠄⠄⠨⡿⠿⠿⣿⣟⣿⣯⣹⣿⣿⣿⣿⣿⣿⣿⣦⡀ <br> 
⣿⣿⣿⣿⣷⠄⠄⠄⢷⣦⠄⠄⠐⢶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ <br> 
⣿⣿⣿⣿⣿⣧⡄⠄⠄⠉⠄⠄⠄⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄ <br> 
⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠈⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄ <br> 
⣿⠿⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⢿⣿⣿⣿⣿⣿⠿⠋⠄⠄⠄⠄</p> 

can be converted to this:

<p>⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣶⣶⣶⣶⣴⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄⠄⠄ ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣴⣶⣶⣦⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀ <br> 
⠄⠄⠄⠄⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⠄⠄⠄⠄⠄ ⠀⠀⠀⠀⣀⣴⣾⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣷⣶⣄⠀⠀⠀⠀⠀ <br> 
⠄⠄⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠄⠄⠄ ⠀⠀⢠⣾⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣦⡄⠀⠀⠀ <br> 
⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⡛⠻⢿⣿⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄ ⠀⣰⣻⣻⣻⣻⣻⣻⣻⣻⡿⠫⡛⠻⢿⣻⢻⢿⣻⣻⣻⣻⣻⣻⣻⣻⣻⡄⠀⠀ <br> 
⣰⣿⣿⣿⣿⣿⣿⣿⡿⠿⠗⠊⠄⠄⠄⠄⠘⠙⠛⠿⠄⠈⢯⣿⣿⣿⣿⣿⡀⠄ ⣰⣻⣻⣻⣻⣻⣻⣻⡿⠿⠗⠊⠀⠀⠀⠀⠘⠙⠛⠿⠀⠈⢯⣻⣻⣻⣻⣻⡀⠀ <br> 
⣿⣿⣿⣿⣿⣿⣯⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⡥⠄ ⣻⣻⣻⣻⣻⣻⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣻⣻⣻⡥⠀ <br> 
⠹⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⢀⣤⣤⣤⣤⠄⡀⠄⠄⠄⢀⡠⠄⠻⠛⠑⢢⠄ ⠹⣻⣻⣻⣻⣻⣻⡄⠀⠀⠀⠀⢀⣤⣤⣤⣤⠀⡀⠀⠀⠀⢀⡠⠄⠻⠛⠑⢢⠀ <br> 
⠄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣶⣧⠄⢨⢪⠴⡶⠖⠂⠓⠒⠉⠄⠄⠄⠄⠢⠄⠈⠄ ⠀⣹⣻⣻⣻⣻⣻⣻⣻⣻⣶⣧⠀⢨⢪⠴⡶⠖⠂⠓⠒⠉⠀⠀⠀⠀⠢⠄⠈⠀ <br> 
⠄⠙⢿⣿⣿⣟⡿⣿⣿⣾⣿⣿⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄ ⠀⠙⢿⣻⣻⣟⡿⣻⣻⣾⣻⣻⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀ <br> 
⠄⠄⠄⢹⣿⣿⣏⠉⢨⣿⣿⣿⠄⠄⠄⠄⠙⠳⣦⣀⠄⠄⠄⠄⠄⠄⠄⢤⣎⡀ ⠀⠀⠀⢹⣻⣻⣏⠉⢨⣻⣻⣻⠀⠀⠀⠀⠙⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⢤⣎⡀ <br> 
⠄⠄⠄⠄⢿⣿⣿⣀⠄⣿⣿⣿⣗⢀⣀⣀⠄⠠⠄⠐⠆⠄⠄⠄⠄⠄⠄⠄⠙⢿ ⠀⠀⠀⠀⢿⣻⣻⣀⠀⣻⣻⣻⣗⢀⣀⣀⠀⠠⠀⠐⠆⠀⠀⠀⠀⠀⠀⠀⠙⢿ <br> 
⠄⠄⠄⠄⠈⣿⣿⣿⡈⠙⣿⣿⣯⡉⡁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸ ⠀⠀⠀⠀⠈⣻⣻⣻⡈⠙⣻⣻⣯⡉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ <br> 
⠄⠄⠄⠄⠄⠘⢻⣿⣿⣶⣿⣿⣿⡶⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿ ⠀⠀⠀⠀⠀⠘⢻⣻⣻⣶⣻⣻⣻⡶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣻ <br> 
⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿ ⠀⠀⠀⠀⠀⣠⣴⣻⣻⣻⣻⣻⣻⣷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣻⣻ <br> 
⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⡀⠄⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⠀⣀⣤⣶⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣧⣀⡀⠀⠀⠀⠀⠀⣀⣴⣻⣻⣻⣻ </p>  

The right-hand outcome is the default option. Giving a `True` boolean for `dot_for_blank` to the function will convert blank braille characters to single dot braille characters, giving the left-hand outcome. <br><br>
Due to the blank braille character being more narrow than the other braille characters, some lines can differ in length. Putting the option will combat this, but the look of the outcome may differ, especially when rotating. But generally, either option can look better depending on the input.

## Rotate
This script also allows an unicode-art string to be rotated 90°, 180° and 270°. <br>
*(Note that after rotating any newlines in the string won't be preserved, instead the output will be separated by spaces)* <br><br>
For example, 90°:

<p>⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⠟⠫⠁⠨⠀⠨⠙⠻⢿⣿⣿⣿⣿⣿⣿ <br> 
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠡⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠉⠻⣿⣿⣿⣿ <br> 
⠨⠀⠻⣿⣿⠿⠻⠋⠡⠀⠨⠀⢈⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠘⢿⣿⣿ <br> 
⠨⠀⠠⠙⠩⠀⠨⠀⢨⣤⣴⡆⠢⠀⠨⠀⣈⣤⣤⣦⠨⠀⠨⠀⠨⠀⠠⠈⢿⣿ <br> 
⠨⠀⠨⠀⠈⢠⣾⠏⠻⠛⠩⠋⠈⠠⠨⠀⣿⣿⣿⣿⡆⠀⠨⠀⠨⠀⠨⠀⠈⣿ <br> 
⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠀⣘⣿⣿⣿⣿⣷⡰⡦⡀⠨⠀⠨⠀⠀⢸ <br> 
⠨⠀⠈⢀⡈⢠⣠⡆⢴⣴⣿⣿⣿⣿⠿⡿⠙⣿⣿⣿⣿⣿⡾⠀⠨⠀⠨⠀⠀⢸ <br> 
⠨⠀⢠⣿⣿⣾⣾⣷⢸⣿⣿⣿⣿⣧⡍⢮⠀⣿⣿⣿⣿⣿⠡⠀⠨⠀⠨⠀⠀⢹ <br> 
⢠⣶⣼⣿⣿⣿⣿⣿⡿⣿⡿⢁⣿⣿⣆⢸⣤⣿⣿⣿⣿⠍⠍⠀⠨⠀⠨⠀⠀⣸ <br> 
⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⢠⣾⣿⣿⣿⢚⣾⣿⣿⣿⡟⠀⠨⠀⠨⠀⠨⠀⠀⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⡿⠨⠀⠨⠀⠨⠀⢰⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⣿⣿⠟⠡⠂⠨⠀⠨⠀⠀⢰⣾⣿ <br> 
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠛⠡⠀⠨⠀⠨⠀⠈⣠⣴⣿⣿⣿ <br> 
⠨⠀⠙⢿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣏⣾⣿⢄⠨⠀⠨⠀⣈⣤⣶⣿⣿⣿⣿⣿ <br> 
⠨⠀⠨⠀⠨⠛⠿⠿⠟⠁⣰⣮⣭⣿⣿⣯⣭⣾⣦⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿ </p> 

180°:

<p>⠐⠐⠐⠐⣠⣶⣿⣿⣿⣿⣿⣷⣶⡄⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⣀⣤⣶⣿ <br> 
⠐⠐⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⡀⠐⠐⠐⠐⠐⠐⣠⣴⣿⣿⣿⣿⣿ <br> 
⠐⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣁⠐⠐⠐⣀⠐⠐⠘⢻⣿⣿⣿⣿⣿ <br> 
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠷⠄⠐⠐⠻⢷⠐⠐⠐⢿⣿⣿⣿⣿ <br> 
⠈⠻⣿⣿⣿⣿⣿⣿⣿⣏⣻⣿⣽⣿⣶⣶⣾⡂⠐⠐⠐⣿⣶⠐⠐⠈⣿⣿⣿⣿ <br> 
⣷⢆⣬⣿⣿⣿⣿⣿⣿⣿⣶⣄⡙⠻⣿⣿⣿⣿⠐⠐⠐⢼⠿⠆⠐⠐⠸⣿⣿⣿ <br> 
⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⠐⠐⢀⠐⠐⠁⠂⠐⠐⠈⠻⣿ <br> 
⣿⢿⣯⣝⣿⣿⣿⣿⠿⣛⡛⣟⣋⣁⣩⢜⢼⣿⡄⣀⠐⠐⠐⠐⠐⠐⠐⠐⠰⣿ <br> 
⣿⣜⡻⠛⠙⣯⣵⣾⣿⣿⣿⣷⣿⣤⣤⣤⣤⣾⣿⣿⣿⣿⣧⠐⠐⠐⠐⠐⠐⠹ <br> 
⣿⡥⠐⠐⠐⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠐⠐⠐⠐⠐⠐ <br> 
⣿⣷⠐⠐⠐⠐⠐⠌⢿⣿⠉⠛⠻⢻⣿⣿⣿⣿⢟⡋⠉⠁⠐⠐⠐⠐⠐⠐⠐⣰ <br> 
⣿⣿⣧⠐⠐⠐⠐⠐⠐⠐⠐⠐⠈⠘⠐⠈⠙⠓⠝⠁⠐⠐⠐⠐⠐⠐⠐⠐⣰⣿ <br> 
⣿⣿⣿⣧⣄⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⢀⣼⣿⣿ <br> 
⣿⣿⣿⣿⣿⣦⣀⡀⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⢀⣠⣶⣿⣿⣿⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣄⣀⣀⣠⣀⣀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿ </p>

270°:

<p>⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠻⡿⣛⣻⣿⣿⣛⡻⠏⢀⣴⣶⣶⣤⡂⠀⡂⠀⡂ <br> 
⣿⣿⣿⣿⣿⠿⠛⡉⠀⡂⠀⡂⠑⣿⡿⣹⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣄⠀⡂ <br> 
⣿⣿⣿⠟⠋⡀⠀⡂⠀⡂⠀⢂⣤⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄ <br> 
⣿⡿⠇⠀⠀⡂⠀⡂⠠⢂⣴⣿⣿⣎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⠇⠀⡂⠀⡂⠀⡂⣾⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⠀⠀⡂⠀⡂⠀⡂⠀⣼⣿⣿⣿⡿⡥⣿⣿⣿⡿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿ <br> 
⡏⠀⠀⡂⠀⡂⠀⣐⣐⣿⣿⣿⣿⠛⡇⠹⣿⣿⢁⣾⣿⣾⣿⣿⣿⣿⣿⡟⠿⠃ <br> 
⣇⠀⠀⡂⠀⡂⠀⢂⣿⣿⣿⣿⣿⠀⡳⣘⢻⣿⣿⣿⣿⡇⢿⡿⡿⣿⣿⠃⠀⡂ <br> 
⡇⠀⠀⡂⠀⡂⠀⡾⣿⣿⣿⣿⣿⣄⣾⣶⣿⣿⣿⣿⠟⠗⠸⠋⠃⡈⠁⡀⠀⡂ <br> 
⡇⠀⠀⡂⠀⡂⠈⠺⠎⢿⣿⣿⣿⣿⡍⠀⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂ <br> 
⣿⡀⠀⡂⠀⡂⠀⡂⠀⠸⣿⣿⣿⣿⠀⡂⠂⡀⣠⣂⣤⣦⣰⡿⠃⡀⠀⡂⠀⡂ <br> 
⣿⣷⡀⠂⠀⡂⠀⡂⠀⡂⠻⠛⠛⡉⠀⡂⠀⠢⠸⠟⠛⡃⠀⡂⠀⣂⣄⠂⠀⡂ <br> 
⣿⣿⣷⡄⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡁⠀⡂⠀⢂⣠⣦⣶⣿⣿⣦⠀⡂ <br> 
⣿⣿⣿⣿⣦⣀⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⢂⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀ <br> 
⣿⣿⣿⣿⣿⣿⣷⣦⣄⡂⠀⡂⢀⣢⣴⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧ </p>

Like the invert function, these functions have the `dot_for_blank` option to replace blank braille characters with single dot braille characters. 
<br><br>
Every line should have an even amount of characters. If not, the last single character of each line will get ignored and will not show up in the end result.

## Mirror
The mirror function mirrors the input string horizontally. <br>
Example: 
<p>⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠋⠉⠉⠙⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿ <br>
⣿⣿⣿⣿⣿⠟⠉⠁⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠈⠙⠿⣿⣿⣿⣿ <br>
⣿⣿⣿⡟⠋⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠈⢻⣿⣿ <br>
⣿⣿⡟⠠⠠⠠⠠⠠⠠⠠⠠⠠⢀⢠⠠⢀⣠⡤⣢⡀⠠⠠⠠⠠⠠⠠⠠⠠⠹⣿ <br>
⣿⡿⠠⠠⠠⠠⠠⢂⣾⣿⣀⣤⣴⣼⣿⣿⣿⣿⣮⣅⣀⡀⠠⠠⠠⠠⠠⠠⠠⠹ <br>
⣿⡓⠠⠠⠠⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠠⠠⠠⠠⠠⠠ <br>
⣿⢫⣵⣤⣠⣟⡻⢿⣿⣿⣿⡿⣿⠛⠛⠛⠛⢿⣿⣿⣿⣿⡟⠠⠠⠠⠠⠠⠠⣰ <br>
⣿⣾⣟⣫⣿⣿⣿⣿⣶⣭⣥⣯⣍⡉⣙⢪⢺⣿⠃⠉⠠⠠⠠⠠⠠⠠⠠⠠⠰⣿ <br>
⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠠⠠⠈⠠⠠⡀⠄⠠⠠⢀⣴⣿ <br>
⡿⠎⢛⣿⣿⣿⣿⣿⣿⣿⠿⠋⣡⣴⣿⣿⣿⣿⠠⠠⠠⢺⣶⠆⠠⠠⢰⣿⣿⣿ <br>
⢀⣴⣿⣿⣿⣿⣿⣿⣿⣏⣽⣿⣻⣿⠿⠿⢿⠅⠠⠠⠠⣿⠿⠠⠠⢀⣿⣿⣿⣿ <br>
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⡶⠂⠠⠠⣴⡾⠠⠠⠠⣾⣿⣿⣿⣿ <br>
⠠⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡉⠠⠠⠠⠉⠠⠠⢠⣼⣿⣿⣿⣿⣿ <br>
⠠⠠⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠁⠠⠠⠠⠠⠠⠠⠙⠻⣿⣿⣿⣿⣿ <br>
⠠⠠⠠⠠⠙⠿⣿⣿⣿⣿⣿⡿⠿⠃⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠉⠛⠿⣿ </p>
