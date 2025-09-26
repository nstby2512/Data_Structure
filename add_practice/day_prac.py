# class Solution:
#     def findOcurrences(self, text: str, first: str, second: str) :
#         text.split()
#         print(text)
def findOcurrences(text: str, first: str, second: str) :
        t = list(text.split())
        ans = []
        for w in range(len(t)) :
            if t[w] == first:
                if t[w + 1] and t[w + 2]and t[w + 1]== second:
                    ans.append(t[w+2])
        return ans


     
