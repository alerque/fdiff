ansicolors = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "BOLD": "\033[1m",
    "RESET": "\033[0m",
}

green_start = ansicolors["GREEN"]
red_start = ansicolors["RED"]
cyan_start = ansicolors["CYAN"]
reset = ansicolors["RESET"]


def color_unified_diff_line(line):
    if line[0:2] == "+ ":
        return f"{green_start}{line}{reset}"
    elif line[0:2] == "- ":
        return f"{red_start}{line}{reset}"
    elif line[0:3] == "@@ ":
        return f"{cyan_start}{line}{reset}"
    elif line[0:4] == "--- ":
        return f"{red_start}{line}{reset}"
    elif line[0:4] == "+++ ":
        return f"{green_start}{line}{reset}"
    else:
        return line
