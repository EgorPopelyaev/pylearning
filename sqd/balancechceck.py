from sqd.stackimpl import Stack


def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening_paranth = set('[({')
    matches = {('(', ')'), ('[', ']'), ('{', '}')}

    stack = Stack()

    for char in s:

        if char in opening_paranth:
            stack.push(char)

        else:

            if stack.size() == 0:
                return False

            last_open = stack.pop()

            if (last_open, char) not in matches:
                return False

    return stack.size() == 0


# print balance_check('[]')

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}))(('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print 'ALL TEST CASES PASSED'


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
