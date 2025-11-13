str1 = input("Enter some words: ")
str2 = input("Enter the word you find: ")

first_pos = str1.find(str2)
last_pos = str1.rfind(str2)

if first_pos != -1:
    print(f'First occurrence of "{str2}" at index: {first_pos}')
    print(f'Last occurrence of "{str2}" at index: {last_pos}')
else:
    print(f'"{str2}" not found in the sentence.')
