import math


# program use for reverse the character in string or paragraph like a to z, b to y,c to x ..... y to b, z to a
# like aedz = zvwa
# we can use this for encryption.

def encryption(data):
    splited_Data = list(data)
    reverser = [chr(abs(ord(i)-96-27)+96) if i.isalpha()else i for i in splited_Data ]
    print("".join(reverser))

if __name__ == '__main__':
    print("Enter the data you want to encrypt:")
    data= input()
    encryption(data=data)