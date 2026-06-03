class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs,]

        def bagOfWords(string: str) -> List[int]:
            output = [0]*26
            for i in string:
                output[ord(i) - 97] += 1
            return output

        hashMap = {}
        for words in strs:
            bOW = tuple(bagOfWords(words))
            if bOW not in hashMap:
                hashMap[bOW] = [words,]
            else:
                hashMap[bOW].append(words)
        
        return list(hashMap.values())

        