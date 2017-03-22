
def rev_word(s):

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])

        i += 1

    j = 0
    reverted_words = []
    word_len = len(words)
    while j < word_len:
        reverted_words.append(words.pop())
        j += 1

    return " ".join(reverted_words)

rev_word('Hi John,   are you ready to go?')

from nose.tools import assert_equal


class ReversalTest(object):
    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print "ALL TEST CASES PASSED"


# Run and test
t = ReversalTest()
t.test(rev_word)