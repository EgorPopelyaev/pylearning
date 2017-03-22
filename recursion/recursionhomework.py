def rec_sum(n):

    if n == 0:
        return 0

    return n + rec_sum(n - 1)

print "Rec func: %d" % rec_sum(4)


def sum_func(n):

    if n == 0:
        return 0

    i = n % 10
    j = n / 10

    return n % 10 + sum_func(n / 10)

print "Sum func: %d" % sum_func(4321)


def words_split(phrase, list_of_words, output = None):

    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):

            output.append(word)

            return words_split(phrase[len(word):], list_of_words, output)

    return output

print words_split('themanran',['the','ran','man'])