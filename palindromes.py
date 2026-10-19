seq = "03022030"
seq_1 = "racecar"
seq_2 = "kayak"

list = []
for letter in seq:
    list.append(letter)

reverselist = list.copy()
reverselist.reverse()

counter = 0
for x in list:
    #print(x)
    #print(reverselist[counter])
    if x == reverselist[counter]:
        counter = counter + 1
        if counter == len(list):
            print("Congrats, it's a palindrome!")
            break
    else: 
        print("not a pal, pal")
        break

# another version
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

# and another one
if seq == seq[::-1]:
    print("hurra")
else:
    print("meh")