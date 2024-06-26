class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)):
            return False

        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for i in range(len(letters)):
            if (letters[i] != 0):
                return False

        return True


