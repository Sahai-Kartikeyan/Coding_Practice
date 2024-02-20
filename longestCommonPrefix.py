class Solution(object):
    def longestCommonPrefix(self, strs):
        lcp = strs[0]
        check= ""
          
        for i in strs[1:]:
            #print(i)
            for j in range(0,len(lcp)):
                
                if j == len(i):
                    break
                elif lcp[j] == i[j]:
                    #print(lcp[j] + ' - ' + i[j])
                    check = check + lcp[j]
            #print('lcp='+lcp)
            lcp = check
            check = ""
            
        return(lcp)


roman =["flower","flow","flight"]

a = Solution()
print(a.longestCommonPrefix(roman))


'''
while roman != 'n':
    roman = input('enter roman: ')
    a = Solution()

    print(a.longestCommonPrefix(roman))
'''
