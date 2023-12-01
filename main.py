import time, sys

x = input("\n\nWould you like to Encode (e) or Decode (d) ? :  ")


def encode():
    message = input("\nWhat is the message you want to convert? : ")

    time.sleep(1)

    binary = " ".join(format(ord(char), "b") for char in message)

    time.sleep(1)

    print(f"\nMessage : {message} \nBinary Code : {binary}")


def decode():
    binary_text = input("\nWhat is the code you want to decode? : ")

    time.sleep(1)

    normal = "".join(chr(int(k, 2)) for k in binary_text.split(" "))

    time.sleep(1)

    print(f"\nBinary Code : {binary_text} \nMessage : {normal}")


if x == "e":
    print("\nEncoder Started")
    time.sleep(1)
    encode()

elif x == "d":
    print("\nDecoder Started")
    time.sleep(1)
    decode()

else:
    time.sleep(1)
    print("\nPlease enter e or d")

print("\n#_____________________________END________________________________________#")
