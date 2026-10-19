# userinput in terminal
text = input("Enter your message: ")

# method for forcing number range input
def shift_value_validation():
    shift_value = int(input("Enter a shift number from 1 to 25: "))
    if shift_value >= 1 and shift_value <= 25:
        print("thanks for your collaboration")
        return shift_value
    else:
        print("please, pick a valid number")
        return shift_value_validation()

# method for encoding the text
def encode_text(shift_value):
    #storing the encoded text
    cipher = ''
    # every letter gets checked and changed
    for char in text:
        # add without change whatever is NOT a letter
        if not char.isalpha():
            cipher += char
            continue
        else:
            # shift first, add up letter number (unicode) and shiftnumber
            code = ord(char) + shift_value
            # check if the input letter was capital 
            if char.isupper():
                # and if shifted value is a higher number than Z 
                if code > ord('Z'):
                    # storing the new shift value, aca how far the shifted
                    # character is behind Z
                    other_shift = code - ord('Z')
                    # we used one step already to go from A to Z thats why -1
                    code = ord('A') + other_shift -1
            else: 
                if code > ord('z'):
                    other_shift = code - ord('z')
                    code = ord('a') + other_shift - 1

            # now into the variable from above
            # ord() number needs to be onverted back into letter chr()
            cipher += chr(code)
    return cipher


# call method
print(encode_text(shift_value_validation()))

# maybe for another day we could try if we can reverse the string


def check_palindrome(seq):
    letters = list(seq)
    reverselist = letters.copy()
    reverselist.reverse()

    mismatch = False

    for index, x in enumerate(letters):
        if x != reverselist[index]:
            mismatch = True
            break

    if mismatch == False:
        print("hurra — it is a palindrome!")
    else:
        print("it is not a palindrome.")

check_palindrome("kayak")
check_palindrome("hello")