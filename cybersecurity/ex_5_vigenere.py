# TODO implement
# Recall the Vigenere cipher from the lecture. Write a function vigenere_encrypt(message: str, key: str) -> str that given a key and a message message in lowercase encrypts it using the Vigenere cipher.
# For this you have to use cycle function from itertools and the builtin zip function. Please import cycle as from itertools import cycle. You are free to import strings.
from itertools import cycle
import string


def vigenere_encrypt(message: str, key: str) -> str:
    alphabet = string.ascii_lowercase
    size = len(alphabet)

    encrypted = []

    for i, key_char in zip(message, cycle(key)):
        if i in alphabet:
            index = alphabet.index(i)
            key_index = alphabet.index(key_char)
            encrypted_index = (index + key_index) % size
            encrypted.append(alphabet[encrypted_index])
        else:
            encrypted.append(i)

    return ''.join(encrypted)
