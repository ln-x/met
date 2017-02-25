__author__ = 'lnx'

#from ps6 import *

def apply_shift(self, shift):


        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #alphabet = build_shift_dict(shift)
        alphabet = {'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
        message_shifted = ''
        for i in self:
            if i in alphabet:
                message_shifted += alphabet[i]
            else:
                message_shifted += i

        return message_shifted

print apply_shift('acb',2)

print apply_shift("we are taking 6.00.1x",2) #zh duh wdnlqj 6.00.1a

print apply_shift("th!s is Problem Set 6?",2) #ma!l bl Ikhuexf Lxm 6?

print apply_shift("TESTING.... so many words we are testing out your code: last one",2) #ALZAPUN.... zv thuf dvykz dl hyl alzapun vba fvby jvkl: shza vul
