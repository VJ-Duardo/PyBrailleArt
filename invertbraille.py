# -*- coding: utf-8 -*-

braille_str_invert = "⠀⣿⠁⣾⠂⣽⠃⣼⠄⣻⠅⣺⠆⣹⠇⣸⠈⣷⠉⣶⠊⣵⠋⣴⠌⣳⠍⣲⠎⣱⠏⣰⠐⣯⠑⣮⠒⣭⠓⣬⠔⣫⠕⣪⠖⣩⠗⣨⠘⣧" \
                     "⠙⣦⠚⣥⠛⣤⠜⣣⠝⣢⠞⣡⠟⣠⠠⣟⠡⣞⠢⣝⠣⣜⠤⣛⠥⣚⠦⣙⠧⣘⠨⣗⠩⣖⠪⣕⠫⣔⠬⣓⠭⣒⠮⣑⠯⣐⠰⣏⠱⣎" \
                     "⠲⣍⠳⣌⠴⣋⠵⣊⠶⣉⠷⣈⠸⣇⠹⣆⠺⣅⠻⣄⠼⣃⠽⣂⠾⣁⠿⣀⡀⢿⡁⢾⡂⢽⡃⢼⡄⢻⡅⢺⡆⢹⡇⢸⡈⢷⡉⢶⡊⢵" \
                     "⡋⢴⡌⢳⡍⢲⡎⢱⡏⢰⡐⢯⡑⢮⡒⢭⡓⢬⡔⢫⡕⢪⡖⢩⡗⢨⡘⢧⡙⢦⡚⢥⡛⢤⡜⢣⡝⢢⡞⢡⡟⢠⡠⢟⡡⢞⡢⢝⡣⢜" \
                     "⡤⢛⡥⢚⡦⢙⡧⢘⡨⢗⡩⢖⡪⢕⡫⢔⡬⢓⡭⢒⡮⢑⡯⢐⡰⢏⡱⢎⡲⢍⡳⢌⡴⢋⡵⢊⡶⢉⡷⢈⡸⢇⡹⢆⡺⢅⡻⢄⡼⢃" \
                     "⡽⢂⡾⢁⡿⢀"

braille_str_180 = "⠁⢀⠂⠠⠃⢠⠄⠐⠅⢐⠆⠰⠇⢰⠈⡀⠉⣀⠊⡠⠋⣠⠌⡐⠍⣐⠎⡰⠏⣰⠑⢄⠒⠤⠓⢤⠔⠔⠕⢔⠖⠴⠗⢴⠘⡄⠙⣄⠚⡤⠛⣤" \
                  "⠜⡔⠝⣔⠞⡴⠟⣴⠡⢂⠢⠢⠣⢢⠥⢒⠦⠲⠧⢲⠨⡂⠩⣂⠪⡢⠫⣢⠬⡒⠭⣒⠮⡲⠯⣲⠱⢆⠳⢦⠵⢖⠶⠶⠷⢶⠸⡆⠹⣆⠺⡦" \
                  "⠻⣦⠼⡖⠽⣖⠾⡶⠿⣶⡁⢈⡃⢨⡅⢘⡇⢸⡈⡈⡉⣈⡊⡨⡋⣨⡌⡘⡍⣘⡎⡸⡏⣸⡑⢌⡓⢬⡕⢜⡗⢼⡙⣌⡚⡬⡛⣬⡜⡜⡝⣜" \
                  "⡞⡼⡟⣼⡡⢊⡣⢪⡥⢚⡧⢺⡩⣊⡪⡪⡫⣪⡭⣚⡮⡺⡯⣺⡱⢎⡳⢮⡵⢞⡷⢾⡹⣎⡻⣮⡽⣞⡾⡾⡿⣾⢁⢁⢃⢡⢅⢑⢇⢱⢉⣁" \
                  "⢋⣡⢍⣑⢏⣱⢓⢥⢕⢕⢗⢵⢙⣅⢛⣥⢝⣕⢟⣵⢣⢣⢧⢳⢩⣃⢫⣣⢭⣓⢯⣳⢷⢷⢹⣇⢻⣧⢽⣗⢿⣷⣉⣉⣋⣩⣍⣙⣏⣹⣛⣭" \
                  "⣝⣝⣟⣽⣫⣫⣯⣻⣿⣿"


def create_braille_dic(braille_str):
    braille_dic = {}
    for i in range(0, len(braille_str), 2):
        braille_dic[braille_str[i]] = braille_str[i + 1]
        braille_dic[braille_str[i + 1]] = braille_str[i]

    return braille_dic


def replace_str_chars(input_str, braille_dic):
    new_str = ""
    for i in range(0, len(input_str), 1):
        try:
            new_str += braille_dic[input_str[i]]
        except KeyError:
            new_str += input_str[i]

    return new_str


def invert(input_str):
    braille_dic_invert = create_braille_dic(braille_str_invert)

    # you may want to comment these out if you want to have '⣿' be replaced with an invisible '⠀' character instead of '⠄'
    braille_dic_invert['⣿'] = '⠄'
    braille_dic_invert['⠄'] = '⣿'

    result_str = replace_str_chars(input_str, braille_dic_invert)

    return result_str


def turn(input_str):
    braille_dic_180 = create_braille_dic(braille_str_180)

    replaced_str = replace_str_chars(input_str, braille_dic_180)

    line_arr = replaced_str.split(" ")
    result_str = ""
    for i in range(len(line_arr) - 1, 0 - 1, -1):
        reversed_line = line_arr[i][len(line_arr[i])::-1]
        result_str += reversed_line + " "

    return result_str


braille_input_str = """⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠋⠉⠉⠙⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⠿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠻⣿⣿⣿⣿⣿ ⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢻⣿⣿⣿ ⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⢀⣔⢤⣄⡀⠄⡄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿  ⠏⠄⠄⠄⠄⠄⠄⠄⢀⣀⣨⣵⣿⣿⣿⣿⣧⣦⣤⣀⣿⣷⡐⠄⠄⠄⠄⠄⢿⣿ ⠄⠄⠄⠄⠄⠄⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⢚⣿ ⣆⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⡿⠛⠛⠛⠛⣿⢿⣿⣿⣿⡿⢟⣻⣄⣤⣮⡝⣿  ⣿⠆⠄⠄⠄⠄⠄⠄⠄⠄⠉⠘⣿⡗⡕⣋⢉⣩⣽⣬⣭⣶⣿⣿⣿⣿⣝⣻⣷⣿ ⣿⣦⡀⠄⠄⠠⢀⠄⠄⠁⠄⠄⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿ ⣿⣿⣿⡆⠄⠄⠰⣶⡗⠄⠄⠄⣿⣿⣿⣿⣦⣌⠙⠿⣿⣿⣿⣿⣿⣿⣿⡛⠱⢿  ⣿⣿⣿⣿⡀⠄⠄⠿⣿⠄⠄⠄⠨⡿⠿⠿⣿⣟⣿⣯⣹⣿⣿⣿⣿⣿⣿⣿⣦⡀ ⣿⣿⣿⣿⣷⠄⠄⠄⢷⣦⠄⠄⠐⢶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ ⣿⣿⣿⣿⣿⣧⡄⠄⠄⠉⠄⠄⠄⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄ ⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠈⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄ ⣿⠿⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⢿⣿⣿⣿⣿⣿⠿⠋⠄⠄⠄⠄ """

print(invert(braille_input_str))
print(turn(braille_input_str))