print("Enter the String:")
text = str(input())
print("Enter a Character:")
char = input()
textLen = len(text)
for i in range(textLen):
    if char==text[i]:
        if text[i]>='a' and text[i]<='z':
            ascVal = ord(text[i])
            ascVal = ascVal-32
            ascVal = chr(ascVal)
            index = i
            text = text[:index] + ascVal + text[index+1:]
print("\nThe New String is:")
print(text)