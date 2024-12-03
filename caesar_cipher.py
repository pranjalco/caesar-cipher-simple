from art import logo

"""
# Project 5: Caesar Cipher
### Description:
A Python program that implements the Caesar Cipher for encoding and decoding messages. Users can input text,
choose shift numbers, and decide whether to encode or decode. Includes a user-friendly loop for multiple operations
in one run.

A Python program that encodes and decodes messages using the Caesar Cipher technique.

### Features:
    - Encode or decode messages based on user choice.
    - Input custom text and shift numbers.
    - Loop for performing multiple operations in one session.

# Level: Simple
Author: Pranjal Sarnaikpi
Date: 2024-12-03
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    if encode_or_decode == "encode" or encode_or_decode == "decode":
        for letter in original_text:

            if letter in alphabet:

                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]

            else:
                output_text += letter

        print(f"Here is the {encode_or_decode}d result: {output_text}")

    else:
        print("Error: please enter valid input 'encode' or 'decode'")


game_on = True
while game_on:

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            if shift >= 0:
                break
            else:
                print("Please enter positive number greater than 0")

        except ValueError:
            print("Error: Please enter positive number greater than 0")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    continue_or_not = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")

    if continue_or_not == "yes":
        print("\n"*30)
        continue
    elif continue_or_not == "no":
        game_on = False
        print("Goodbye! 👋")
    else:
        print("Error: please enter 'yes' or 'no', quiting Caesar Cipher.")
        game_on = False
