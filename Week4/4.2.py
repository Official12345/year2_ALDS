from random import random

def find_fraction_with_same_hash():
    hashes = dict()
    while True:
        new_number = random()
        new_hash = hash(new_number)%(2**32)
        if new_hash in hashes:
            print(repr(new_number), "==", hashes[new_hash], '==', repr(hash(new_number)))
            return
        else:
            hashes[new_hash] = new_number

find_fraction_with_same_hash()