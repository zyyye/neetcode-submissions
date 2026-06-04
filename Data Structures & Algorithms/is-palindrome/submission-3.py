class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(x: int) -> bool:
            return (48 <= x and x <= 57) or \
                (65 <= x and x <= 90) or \
                (97 <= x and x <= 122)
        string = ""
        for char in s:
            if isAlphaNum(ord(char)):
                string += char.lower()
        return string == string[::-1]

        