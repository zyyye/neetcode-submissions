class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastMap = {}
        for i, char in enumerate(s):
            lastMap[char] = i

        res = []
        index = lastMap[s[0]]
        prevEnd = -1
        for i, char in enumerate(s):
            if index == i:
                res.append(index - prevEnd)
                if i+1 == len(s):
                    break
                index = lastMap[s[i+1]]
                prevEnd = i
            else:
                index = max(index, lastMap[s[i]])

        return res

        