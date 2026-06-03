class Solution:
    def checkValidString(self, s: str) -> bool:
        left, asterisk = [], []
        for i, symbol in enumerate(s):
            if symbol == "(": left.append(i)
            elif symbol == "*": asterisk.append(i)
            else: 
                if len(left) == 0 and len(asterisk) == 0:
                    return False
                if len(left) != 0: left.pop()
                else: asterisk.pop()
        
        while len(left) and len(asterisk):
            if left[-1] > asterisk[-1]: return False
            left.pop()
            asterisk.pop()

        return len(left) == 0