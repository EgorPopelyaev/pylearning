def compress(s):
    length = len(s)

    i = 1
    counter = 1
    compressed_string = ""

    while i < length:
        if s[i] == s[i - 1]:
            counter += 1

        else:
            compressed_string += s[i - 1] + str(counter)
            counter = 1
        i += 1

    compressed_string += s[i - 1] + str(counter)

    print compressed_string
    return compressed_string


compress('AAAAABBBBCCCC')
