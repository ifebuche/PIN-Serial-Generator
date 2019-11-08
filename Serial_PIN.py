from random import randint
import os

def random_with_N_digits(n):
    """
    Random integer PIN generation
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

welcome = "Welcome to Serial-PIN generator v1. by Fesh. \nThis script generates 1000 PINs and serial number"
decor = "#" * 45
print(decor, "\n", welcome, "\n", decor)
print("\n", "How long do you want the pin to be?")
pin_length = input(">>> ")

try:
    pin_length = int(pin_length)
    pins = [random_with_N_digits(pin_length) for line in range(1000)]
    print("enerating {} digit PINs...".format(pin_length))
    
    serial = []
    for i, pin in enumerate(pins, 1):
        if len(str(i)) == 1:
            serial.append("00"+str(i))
            #print("00"+str(i), pin)
        elif len(str(i)) == 2:
            serial.append("0"+str(i))
            #print("0"+str(i), pin)
        else:
            serial.append(str(i))
            #print(i, pin)
    print("Choose a name to save the file with.")
    namer = input(">>> ")
    filename = namer+".csv"
    
    with open(filename, "w") as file:
        for ser, pin in zip(serial, pins):
            file.write(str(ser) + "," + str(pin) + "\n")
    
    print("File saved in this location. {}".format(os.getcwd()))
    
    #open the folder
    os.startfile(os.getcwd())
except:
    print("{} is not an integer. Try '1' or '2' without the quotation marks".format(pin_length))
    print("Please restart the script.")