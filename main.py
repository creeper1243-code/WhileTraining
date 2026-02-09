counter = 7
while counter > 0:
    print(counter)
    counter = counter - 1

print()

counter = 10
while counter > 0:
    print(counter, end=", ")
    counter = counter - 2

print()

while True:
    print("THIS IS AN INFINITE CYCLE")
    user_input = input("do you want to exit from infinite cycle? (y/n): ")
    if user_input == "y":
        print("CYCLE ENDED")
        break

print()

counter = 0
while counter < 10:
    print(counter)
    #counter = counter + 1
    counter += 1

print()

counter = 0
while counter < 1000:
    counter += 1
    if counter % 7 == 0:
        print(counter, end="*")