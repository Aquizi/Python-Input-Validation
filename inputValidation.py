# This program says hello and asks for my name.

print('What is your name?')

name = input()
while not name.isalpha():
    print("Please enter a valid name.")
    name = input()
    continue

print('What is your age?')

while True:
    try:
        age = int(input())
        break
    except ValueError:
        print('Please enter a valid age.')

print('It is good to meet you, ' + name)
print('The length of your name is: ' + str((len(name))))
print('You will be ' + str(age + 1) + ' in one year.')