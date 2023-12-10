#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    if letter == " ":
        return " "
    elif 'A' <= letter <= 'Z':
        shifted_letter_code = (ord(letter) - ord('A') + shift) % 26 + ord('A')
        shifted_letter = chr(shifted_letter_code)
        return shifted_letter
    else:
        return letter

print(shift_letter("A", 0))  # Output: "A"
print(shift_letter("A", 2))  # Output: "C"
print(shift_letter("Z", 1))  # Output: "A"
print(shift_letter("X", 5))  # Output: "C"
print(shift_letter(" ", _))  # Output: " "


# In[17]:


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    shifted_message = ""
    for char in message:
        if 'A' <= char <= 'Z':
            shifted_code_point = (ord(char) - ord('A') + shift) % 26 + ord('A')
            shifted_message += chr(shifted_code_point)
        elif char == " ":
            shifted_message += " "
        else:
            shifted_message += char
    return shifted_message

print(caesar_cipher("HELLO WORLD", 3))
print(caesar_cipher("PYTHON IS FUN", 5))
print(caesar_cipher(" ", 2))


# In[18]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    if letter == " ":
        return " "
    elif 'A' <= letter <= 'Z' and 'A' <= letter_shift <= 'Z':
        shift_value = ord(letter_shift) - ord('A')
        shifted_code_point = (ord(letter) - ord('A') + shift_value) % 26 + ord('A')
        shifted_letter = chr(shifted_code_point)
        return shifted_letter
    else:
        return letter
    
print(shift_by_letter("A", "A"))
print(shift_by_letter("A", "C"))
print(shift_by_letter("B", "K"))
print(shift_by_letter(" ", _))


# In[19]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    key = key.replace(" ", "")
    extended_key = (key * (len(message) // len(key))) + key[:len(message) % len(key)]
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        if 'A' <= char <= 'Z':
            shift_value = ord(extended_key[i % len(extended_key)]) - ord('A')
            shifted_code_point = (ord(char) - ord('A') + shift_value) % 26 + ord('A')
            encrypted_message += chr(shifted_code_point)
        elif char == " ":
            encrypted_message += " "
        else:
            encrypted_message += char
    return encrypted_message

print(vigenere_cipher("A C", "KEY"))


# In[ ]:




