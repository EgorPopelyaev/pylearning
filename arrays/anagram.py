

def anagram(s1, s2):
    ar1 = s1.replace(' ', '').lower()
    ar2 = s2.replace(' ', '').lower()

    print sorted(ar1)
    print sorted(ar2)

    if sorted(ar1) == sorted(ar2):
        print "We have an anagram"
        return True
    else:
        print "We don't hav an anagram"
        return False

anagram('clint eastwood','old west action')