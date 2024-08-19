#!/usr/bin/python3
""" validUTF8 """


def validUTF8(data):
    """
    """
    status = 0

    for number in data:
        binary_data = bin(number).replace('0b', '').rjust(8, '0')[-8:]
        if status == 0:
            if binary_data.startswith('110'):
                status = 1
            if binary_data.startswith('1110'):
                status = 2
            if binary_data.startswith('11110'):
                status = 3
            if binary_data.startswith('10'):
                return False
        else:
            if not binary_data.startswith('10'):
                return False
            status -= 1

    if status != 0:
        return False

    return True
