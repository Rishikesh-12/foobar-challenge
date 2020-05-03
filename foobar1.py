# Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions.
# But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station.
# You figure printing out Braille signs will help them, and – since you’ll be promoting efficiency at the same time – increase your chances of a promotion.
# Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2×3 grid, where each dot can either be a bump or be flat (no bump).
# You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda’s command can feel the bumps on the signs and “read” the text with their touch.
# The special printer which can print the bumps onto the signs expects the dots in the following order:


def solution(plaintext):
   
    switcher = {
        "a": "100000",
        "b": "110000",
        "c": "100100",
        "d": "100110",
        "e": "100010",
        "f": "110100",
        "g": "110110",
        "h": "110010",
        "i": "010100",
        "j": "010110",
        "k": "101000",
        "l": "111000",
        "m": "101100",
        "n": "101110",
        "o": "101010",
        "p": "111100",
        "q": "111110",
        "r": "111010",
        "s": "011100",
        "t": "011110",
        "u": "101001",
        "v": "111001",
        "w": "010111",
        "x": "101101",
        "y": "101111",
        "z": "101011",
        "1": "100000",
        "2": "110000",
        "3": "100100",
        "4": "100110",
        "5": "100010",
        "6": "110100",
        "7": "110110",
        "8": "110010",
        "9": "010100",
        "0": "010110",
        ".": "010011",
        "-": "010010",
        ",": "010000",
        "!": "011010",
        "?": "011001",
        ":": "010010",
        "(": "011011",
        ")": "011011",
        "/": "001100",
        "#": "001111",
        ";": "011000",
        "[": "000001011011",
        "]": "011011001000",
        "capital": "000001",
        "_": "001001001001001001",
        "'": "001000",
        "+": "011010",
        "*": "011001",
        ">": "101010",
        "<": "010101",
        "@": "001110",
        "%": "010110001011",
        " ": "000000"
    }
    result = ""
    lastCharIsDigit = False
    for l in plaintext:
        if l.isdigit():
            if not lastCharIsDigit:
                lastCharIsDigit = True
                result += switcher.get("#", "")
        else:
            lastCharIsDigit = False
            if l.isupper():
                result += switcher.get("capital", "")

        result += switcher.get(l.lower(), "")
    print(result)
