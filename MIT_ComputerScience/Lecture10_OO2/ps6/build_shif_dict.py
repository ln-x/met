__author__ = 'lnx'
import string

def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        pass

#def alphabet_shift(alphabet, shift):
        alphabet = string.ascii_uppercase
        alphabet2 = string.ascii_lowercase

        shifted1 = {}
        shifted2 = {}
        for i in range(len(alphabet)):
            if (i + shift + 1) >= len(alphabet):
                shifted1[alphabet[i]] = alphabet[i-len(alphabet)+shift]
            else:
                shifted1[alphabet[i]] = alphabet[i + shift]
        for i in range(len(alphabet2)):
            if (i + shift + 1) >= len(alphabet2):
                shifted2[alphabet2[i]] = alphabet2[i-len(alphabet2)+shift]
            else:
                shifted2[alphabet2[i]] = alphabet2[i + shift]
        for i in shifted2:
            shifted1[i] = shifted2[i]

        print (shifted1)

        return shifted1

print (build_shift_dict(2))
