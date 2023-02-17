#enter the serial number of the finger and determine its name

finger_number = int(input("Enter the serial number of the finger: "))
if finger_number == 1:
    print("This is a thumb")
elif finger_number == 2:
    print("This is the index finger")
elif finger_number == 3:
    print("This is a middle finger")
elif finger_number == 4:
    print("This is a ring finger")
elif finger_number == 5:
    print("This is a little finger")
else:
    print("No name")
