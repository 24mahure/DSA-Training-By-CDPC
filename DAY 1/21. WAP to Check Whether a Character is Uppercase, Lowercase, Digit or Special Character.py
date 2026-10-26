chr = input("Enter a single character: ")

if chr.isupper():
    print("The character is in uppercase.")

elif chr.islower():
    print("The character is in lowercase.")

elif chr.isdigit():
    print("The character is a digit.")

else:
    print("The character is a special character.")