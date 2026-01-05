#!/usr/bin/env python3


__description__ = 'Tool to decode veginere ciphers'
__author__      = 'Kevin Haug'
__version__     = '0.1'
__date__        = '2025/12/26'

"""
Tool to decode veginere ciphers.
"""


# ---- imports ----
import numpy as np
from pathlib import Path


# ---- Global / initial values ----
max_key_length = 50
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_file = "cipher-text.txt"
ioc_english = 0.0686
threshold = 0.003
ioc_english_min_th = round(ioc_english - threshold, 3) # Min threshold: 0.066
ioc_english_max_th = round(ioc_english + threshold, 3) # Max threshold: 0.072

# ---- Functions ----

# Calculate the Index of Coincidence for a given string
# THANKS: Based on https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC.html
def calculate_ioc(string):
        letter_frequency = np.zeros(len(alphabet), dtype=int)
        occurrences = 0
        N = len(string)
        #print(letter_frequency) # Debugging
        for i in range(len(alphabet)):
                #print(i, ":\t", alphabet[i], "\t", string.count(alphabet[i])) # Debugging      
                letter_frequency[i] = string.count(alphabet[i])
        #print("New letter frequency: ", letter_frequency) # Debugging
        #    letter_frequency[i] = string.count(alphabet[i])
        #print("Letter frequency: ", letter_frequency) # Debugging        

        for i in range(len(alphabet)):
                char_occurrence = letter_frequency[i]
                occurrences += char_occurrence * (char_occurrence - 1)

        #print("Occurrences: ", occurrences) # Debugging

        result = occurrences / (N * (N - 1))
        #print("IOC result: ", result) # Debugging
        return result


""" Check if a value is in between two thresholds """
def inbetween(value, min_threshold, max_threshold):
        return min_threshold <= value <= max_threshold


""" Split text into blocks based on key length """

def split_into_blocks(text, key_length):
        blocks = ['' for _ in range(key_length)]
        for index, char in enumerate(text):
            blocks[index % key_length] += char
        return blocks


def no_ioc_found():
    print("No IOC found within the English thresholds for any key length up to ", max_key_length)


def ioc_found(key_length, cipher_blocks):
        print("IoC detected for key length: ", key_length)
        cipher_keys = np.full(key_length, '_', dtype='U1')
        #for i in range(len(cipher_blocks)):
        #    pass # TODO:

# ---- Main code ----

# Prepares the ciphertext to a string-format
if not Path(encrypted_file).is_file():
    raise FileNotFoundError(f"Missing file: {encrypted_file}")
#raise TypeError("Only integers are allowed lolollolol")


with open(encrypted_file, 'r', encoding='utf-8') as file:
    ciphertext_raw = file.read()
    ciphertext = ciphertext_raw.lower()

#print(type(ciphertext))    # Debugging
#print(ciphertext)          # Debugging


# Run the function
ioc_values = np.zeros(max_key_length)
ioc_detected = False

for i in range(max_key_length):
    blocks = split_into_blocks(ciphertext, i+1)
    arr = np.zeros(len(blocks))

    for j in range(len(blocks)):
        #print("Key length ", i+1, " Block ", j, " : ", blocks[j])  # Debugging
        arr[j] = calculate_ioc(blocks[j])

    ioc_values[i] = np.mean(arr)
    if inbetween(ioc_values[i], ioc_english_min_th, ioc_english_max_th):
        #print("Key length ", i+1, " has an IOC within the English threshold: ", ioc_values[i])
        ioc_detected = True
        break

    
if not ioc_detected:
    no_ioc_found()
else:
    ioc_found(i+1, blocks)

print("Done.")