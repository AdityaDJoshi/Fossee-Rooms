from unittest import result


def calculate_average(a, b):

    avg = (a+b)/2
    return round(avg, 2)


def counta(s):
    s = s.lower()
    return s.count("a")


def oddsum(s):
    odd_total = 0
    for i in s:
        if i % 2 == 1:
            odd_total += i
    return odd_total


def caesar_cipher(s, n):
    l = [ord(i)+n for i in s]
    for i in range(len(l)):
        if l[i] > ord('z'):
            l[i] = l[i] - ord('z')+ord('a')-1
        l[i] = chr(l[i])
    return ''.join(l)


def remove_spaces(s):
    s = s.lstrip()
    s = s.rstrip()
    # print(s)
    return " ".join(s.split())


# calculate_average(5, 6.5)
# print(counta("All apps"))
# print(oddsum([1, 2, 3, 1, 4]))
# print(ord('a'))
# print(ord('z'))
# print(caesar_cipher("wxyz", 2))
# print(caesar_cipher("bbbb", 26))
# print(caesar_cipher("mnop", 14))
# print(caesar_cipher("abcd", 1))
print(remove_spaces('  Hello    Hi!'))
