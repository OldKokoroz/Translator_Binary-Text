
import time
import sys


def encode():
    message = input("\nWhat is the message you want to convert? : ")

    time.sleep(1)

    binary = " ".join(format(ord(char), "b") for char in message)

    time.sleep(1)

    enc_out = f"\nMessage     : {message} \n\nBinary Code : {binary}"

    print(enc_out)


def decode():
    binary_text = input("\nWhat is the code you want to decode? : ")

    time.sleep(1)

    normal = "".join(chr(int(k, 2)) for k in binary_text.split(" "))

    time.sleep(1.5)

    dec_out = f"\nBinary Code : {binary_text} \n\nMessage     : {normal}"

    print(dec_out)


def file_encode():
    time.sleep(1)

    fil_en = input("\nPath of the file : ")

    file_to_encode = open(fil_en, "r")
    char_as_text = file_to_encode.read()

    normal_in = " ".join(format(ord(char), "b") for char in char_as_text)

    out_choice_en = input("\nPath of the output file : ")

    out_en = open(out_choice_en, 'w')
    out_en.write(normal_in)

    print("PROCESS DONE !")


def file_decode():
    time.sleep(1)

    fil_de = input("\nPath of the file : ")

    file_to_decode = open(fil_de, "r")
    char_as_text = file_to_decode.read()

    normal_out = "".join(chr(int(k, 2)) for k in char_as_text.split(" "))

    out_choice_de = input("\nPath of the output file : ")

    out_de = open(out_choice_de, 'w')
    out_de.write(normal_out)

    print("PROCESS DONE !")


time.sleep(1)


print("\n#____________________________START____________________________#")

time.sleep(1)

while True:
    start = input('''
|----------MODES----------|
| 1 - Encode              |
| 2 - Decode              |
| 3 - File Encode         |
| 4 - File Decode         |
| 5 - Exit                |
|-------------------------|
|-> ''')

    if start == "1":
        time.sleep(1)
        print("\n------ Encoder Started ------")
        time.sleep(1)
        encode()

    elif start == "2":
        time.sleep(1)
        print("\n------ Decoder Started ------")
        time.sleep(1)
        decode()

    elif start == "3":
        time.sleep(1)
        print("\n------ File Encoder Started ------")
        time.sleep(1)
        file_encode()

    elif start == "4":
        time.sleep(1)
        print("\n------ File Decoder Started ------")
        time.sleep(1)
        file_decode()

    elif start == "5":
        time.sleep(1)
        print("\n#_____________________________END_____________________________#\n")
        time.sleep(1)
        sys.exit(0)

    else:
        time.sleep(1)
        print("\nInvalid Input")
        break
