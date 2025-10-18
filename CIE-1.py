a = input("Enter a name: ")
rev = a[::-1]
print(f"The reversed name is: {rev}")

if a == rev:
    print("The name is a palindrome")
else:
    print("The name is not a palindrome")
