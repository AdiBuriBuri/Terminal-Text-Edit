color_red = '\033[31m'
color_green = '\033[32m'
color_blue = '\033[34m'
color_yellow = '\033[33m'
color_magenta = '\033[35m'
color_cyan = '\033[36m'
color_white = '\033[37m'
color_reset = '\033[0m'

bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"

fg_red = "\033[91m"
fg_green = "\033[92m"
fg_yellow = "\033[93m"
fg_blue = "\033[94m"
fg_magenta = "\033[95m"
fg_cyan = "\033[96m"

font_bold = "\033[1m"
font_italic = "\033[3m"
font_underline = "\033[4m"
font_reset = "\033[0m"

print(f"""
{fg_cyan}
**************************************************************************************************{color_reset}{color_magenta}
*     ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗    ████████╗██████╗               *
*     ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝    ╚══██╔══██╔═══██╗              *
*     ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗         ██║  ██║   ██║              *
*     ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝         ██║  ██║   ██║              *
*     ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗       ██║  ╚██████╔╝              *
*                                                                                                *{color_reset}{color_green}
*     ██╗═╝╚══█████╗███╗═══████████╗╝╚════██████╗███████╗════█████████████████╗══██████████╗     *
*     ██║    ██╔══██████╗  ████╔══██╗    ██╔═══████╔════╝    ╚══██╔══██╔════╚██╗██╔╚══██╔══╝     *
*     ██║    █████████╔██╗ ████║  ██║    ██║   ███████╗         ██║  █████╗  ╚███╔╝   ██║        *
*     ██║    ██╔══████║╚██╗████║  ██║    ██║   ████╔══╝         ██║  ██╔══╝  ██╔██╗   ██║        *
*     █████████║  ████║ ╚██████████╔╝    ╚██████╔██║            ██║  █████████╔╝ ██╗  ██║        *
*     ╚══════╚═╝  ╚═╚═╝  ╚═══╚═════╝      ╚═════╝╚═╝            ╚═╝  ╚══════╚═╝  ╚═╝  ╚═╝        *{color_reset}{fg_cyan}
**************************************************************************************************{color_reset}
{color_reset}
""")
input_from_user = input(f"{bg_blue}{font_bold}{color_white} Enter Text: {color_reset} ")

while True:

    print(f"{bg_magenta}{font_bold}Your Styled Text[Current]:{color_reset} {input_from_user}\n")

    print(f"\n{bg_cyan}{font_bold}{color_white} Choose color of FG for your text: {color_reset}")
    print(f"1. {font_italic}{color_blue}Blue{color_reset}")
    print(f"2. {font_italic}{color_red}Red{color_reset}")
    print(f"3. {font_italic}{color_green}Green{color_reset}")
    print(f"4. {font_italic}{color_yellow}Yellow{color_reset}")
    print(f"5. {font_italic}{color_magenta}Magenta{color_reset}")
    print(f"6. {font_italic}{color_cyan}Cyan{color_reset}")
    print(f"7. {font_italic}{color_white}White{color_reset}")

    color_choice = input(f"\n{bg_magenta}{font_bold}{color_white} Enter FG choice: {color_reset} ")

    if color_choice == "1":
        selected_color = color_blue
    elif color_choice == "2":
        selected_color = color_red
    elif color_choice == "3":
        selected_color = color_green
    elif color_choice == "4":
        selected_color = color_yellow
    elif color_choice == "5":
        selected_color = color_magenta
    elif color_choice == "6":
        selected_color = color_cyan
    elif color_choice == "7":
        selected_color = color_white
    else:
        print(f"{color_red}Invalid choice! Defaulting to white.{color_reset}")
        selected_color = color_white

    lines_to_clear = 11  
    print(f"\033[{lines_to_clear}A", end="")  
    for _ in range(lines_to_clear):
        print("\033[K") 
    print(f"\033[{lines_to_clear - 1}A", end="") 

    print(f"{bg_magenta}{font_bold}Your Styled Text[Current]:{color_reset} {selected_color} {input_from_user} {color_reset}\n")

    print(f"\n{bg_cyan}{font_bold}{color_white} Choose BG color for your text: {color_reset}")
    print(f"1. {font_italic}{bg_blue}Blue{color_reset}")
    print(f"2. {font_italic}{bg_red}Red{color_reset}")
    print(f"3. {font_italic}{bg_green}Green{color_reset}")
    print(f"4. {font_italic}{bg_yellow}Yellow{color_reset}")
    print(f"5. {font_italic}{bg_magenta}Magenta{color_reset}")
    print(f"6. {font_italic}{bg_cyan}Cyan{color_reset}")
    print(f"7. {font_italic}{bg_white}White{color_reset}")

    bg_color = input(f"{font_bold}Enter Bg color: {color_reset}")

    if bg_color == "1":
        bg_choice = bg_blue
    elif bg_color == "2":
        bg_choice = bg_red
    elif bg_color == "3":
        bg_choice = bg_green
    elif bg_color == "4":
        bg_choice = bg_yellow
    elif bg_color == "5":
        bg_choice = bg_magenta
    elif bg_color == "6":
        bg_choice = bg_cyan
    elif bg_color == "7":
        bg_choice = bg_white
    else:
        print(f"{color_red}Invalid choice! Defaulting to white.{color_reset}")
        bg_choice = color_white

    lines_to_clear = 11  
    print(f"\033[{lines_to_clear}A", end="")  
    for _ in range(lines_to_clear):
        print("\033[K") 
    print(f"\033[{lines_to_clear - 1}A", end="") 

    print(f"{bg_magenta}{font_bold}Your Styled Text[Current]:{color_reset} {bg_choice}{selected_color} {input_from_user} {color_reset}\n")

    print(f"\n{bg_cyan}{font_bold}{color_white} Choose BG color for your text: {color_reset}")
    print(f"1. {font_bold}BOLD{font_reset}")
    print(f"2. {font_italic}Italic{font_reset}")
    print(f"3. {font_underline}Underline{font_reset}")

    tex_style_input = input(f"{font_bold}Enter Font style: {font_reset}")

    if tex_style_input == "1":
        font_choice = font_bold
    elif tex_style_input == "2":
        font_choice = font_italic
    elif tex_style_input == "3":
        font_choice = font_underline
    else:
        print(f"{color_red}Invalid choice! Defaulting to white.{color_reset}")
        bg_choice = color_white

    lines_to_clear = 11  
    print(f"\033[{lines_to_clear}A", end="")  
    for _ in range(lines_to_clear):
        print("\033[K") 
    print(f"\033[{lines_to_clear - 1}A", end="") 

    print(f"Your Styled Text:{bg_choice}{font_choice}{selected_color} {input_from_user} {color_reset}\n")
    choice = input("Do u want to change the text style [Yes/No]: ")
    if choice == 'no' or choice == 'No':
        break
    else:
        print("Modify Text Again:\n")
    
print(f"Your Styled Text:{bg_choice}{font_choice}{selected_color} {input_from_user} {color_reset}\n")
