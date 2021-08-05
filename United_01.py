def morse_cr(letters):
    letter_morse = {"a":".-", "b":"-.-.", "c":"-...", "d":"-..",
                    "e":".", "f":"..-.", "g":"--.",
                    "h":"....", "i":"..", "j":".---", "k":"-.-",
                    "l":".-..", "m":"--", "n":"-.",
                    "o":"---", "p":".--.", "q":"--.-",
                    "r":".-.", "s":"...", "t":"-",
                    "u":"..-", "v":"...-", "w":".--",
                    "x":"-..-", "y":"-.--", "z":"--..",
                    " ":"  "}
    msg = ""
    letters = letters.lower()
    for letter in letters:
        if letter not in letter_morse:
            msg += letter
        elif letter in letters:
            msg += letter_morse[letter] + ' '
    return msg
