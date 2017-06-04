str1 = "TestString"
print(str1[::-1])  # Reverse string
# gnirtStseT
print(str1 * 3)
# TestStringTestStringTestString
str1 = str1[0:4] + "New" + str1[4:]
print(str1)  # Add line into string
# TestNewString

str2 = "11121111311141112112"
print(str2.find('2'), str2.rfind('2'))  # find first enter and last enter
# 3 19
# print(str2.index('NotExistingString')) # ValueError - not found

print(str2.index('11'), str2.rindex('11'))  # Find first substring in string and last
# 0 17

str2.replace('111', '444')  # Not changes value, must change it directly
print(str2)
# 11121111311141112112
print(str2.replace('111', '444'))  # Creates new output
# 44424441344444442112

print(str2.split('2', 2))  # Split by Value ('2') and max = 2 splits
# ['111', '111131114111', '112']

print(str2.isdigit(), str1.isdigit())  # Check if string is a number only
# True False

print(str1.isalpha(), str2.isalpha())  # Check if string only literals
# True False

print(str1.isalnum(), str2.isalnum(), '#$#'.isalnum())  # Check if there are any num or literal
# True True False

print("STR".isupper(), "STR".islower(), "str".islower())  # UP, LOW-register check
# True False True

print("    \n".isspace(), " str ".isspace())  # Check if there are just spaces and newlines

print('not title'.istitle(), 'Title'.istitle())  # Check if starts with Big literal
# False True

print(str1.upper(), str1.lower())  # Soft get uppered, lowered str
# TESTNEWSTRING testnewstring

print("Start".startswith("St"), "Start".startswith("rt", 3))  # Check if string starts at X via ("str")
# True True
print("End".endswith("d"))  # Check if at end any ("string")
# True

print(", ".join(['spisok', 'iz', 'strok']))  # List with separator before (sep).join
# spisok, iz, strok

print("thIS TEXt caNt be CooL caUSe of THOSe LiteRALs".capitalize())  # Translate to readable text type
# This text cant be cool cause of those literals

print("you are TILTED ME OUT!".title())  # Transform like capitalize but every word starts with Upcase
# You Are Tilted Me Out!

print("Test string for example of center function".center(70, '~'))  # Center string of X points via filling
# ~~~~~~~~~~~~~~Test string for example of center function~~~~~~~~~~~~~~

print("Super count can be count from the counters of count countcount".count("count"))  # Count of subs
# 6

print("Tab\tMeeeeeeeeeeeeee\tHard\tAs\tYou\tWish".expandtabs())  # 8 spaces by tag \t, and 1 space if exceeds
# Tab     Meeeeeeeeeeeeee Hard    As      You     Wish

print(' !BANG! '.lstrip(' '), ' !BANG! '.rstrip(), ' !BANG! '.strip(' !BN'))  # Delete spaces
# Remove all spaces from left, right and both sides one by one (chars to remove)
# !BANG!   !BANG! ANG

print("WHAT IS THIS IS !".partition(' IS '))  # Takes substr and left and right substr from it
# ('WHAT', ' IS ', 'THIS IS !')
print("WHAT IS THIS IS !".rpartition(' IS '))  # Reverse partition
# ('WHAT IS THIS', ' IS ', '!')

print("mUST BE NOT THAT BIG!".swapcase())  # Swap lower and up - case
# Must be not that big!

print("whaaat?".zfill(20))  # Fill string at start wia ZEROS! to needed width
# 0000000000000whaaat?

print("again?".ljust(20, '3'), "again?".rjust(20, '3'))  # Fill from l/r side via choosen literal
# again?33333333333333 33333333333333again?