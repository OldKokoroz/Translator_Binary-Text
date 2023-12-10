
import time
import sys


def encode():
    message = input("\nWhat is the message you want to convert? : ")

    time.sleep(1)

    binary = " ".join(format(ord(char), "b") for char in message)

    time.sleep(1)

    print(f"\nMessage     : {message} \n\nBinary Code : {binary}")


def decode():
    binary_text = input("\nWhat is the code you want to decode? : ")

    time.sleep(1)

    if binary_text is int:
        time.sleep(1)

        normal = "".join(chr(int(k, 2)) for k in binary_text.split(" "))

        time.sleep(1.5)

        print(f"\nBinary Code : {binary_text} \n\nMessage     : {normal}")

    else:
        time.sleep(1)
        print("\nPlease Give a Binary Code !!")


time.sleep(1)

print("\n#____________________________START____________________________#")

time.sleep(1)

x = input("""\nModes: \n
    E  -->  Encode    |    D  -->  Decode    |    Q  -->  Exit
    ---------------        ---------------        -------------
\nChoice : """)

x = x.lower()


if x == "e":
    time.sleep(1)
    print("\n------ Encoder Started -----")
    time.sleep(1)
    encode()

elif x == "d":
    time.sleep(1)
    print("\nDecoder Started")
    time.sleep(1)
    decode()

elif x == "q":
    time.sleep(1)
    print("\nDecoder Started")
    time.sleep(1)
    sys.exit(1)

else:
    time.sleep(1)
    print("\nInvalid Input")

print("\n#_____________________________END_____________________________#\n")
