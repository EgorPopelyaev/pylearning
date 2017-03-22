def uni_char(s):
    length = len(s)

    i = 1
    while i < length:

        if s[i] == s[i - 1]:
            print "Non unique symbols were found!"
            return False
        i += 1

    return True


"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'


# Run Tests
t = TestUnique()
t.test(uni_char)