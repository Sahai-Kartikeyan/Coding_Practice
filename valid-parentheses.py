class Solution(object):
    def isValid(self, s):

        paren = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        ans = True

        for i in range(0,len(s)-1,2):
            
            if s[i+1] != paren[s[i]]:
                ans = False

        
        return ans

roman = "()[]{}"

a = Solution()
print(a.isValid(roman))


'''
while roman != 'n':
    roman = input('enter roman: ')
    a = Solution()

    print(a.longestCommonPrefix(roman))
'''
