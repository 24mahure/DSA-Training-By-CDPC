inp = 'helpforcode'

count_vowels = 0
count_consonants = 0

for i in inp:
    if i in 'aeiouAEIOU':
        count_vowels += 1

    elif i.isalpha():
        count_consonants += 1

print("Number of vowels:", count_vowels)
print("Number of consonants:", count_consonants)