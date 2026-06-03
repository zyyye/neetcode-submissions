class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for st in strs:
            for char in st:
                output += str(ord(char)) + "_"
            output += " "
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        currWord = ""
        currNum = ""
        for char in s:
            if char == " ":
                output.append(currWord)
                currWord = ""
            elif char == "_":
                currWord += chr(int(currNum))
                currNum = ""
            else:
                currNum += char
        return output
            