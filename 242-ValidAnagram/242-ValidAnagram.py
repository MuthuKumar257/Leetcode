# Last updated: 8/11/2026, 6:46:04 PM
class Solution(object):
    def isAnagram(self, s, t):
        ana1={}
        ana2={}
        for i in s:
            if i in ana1:
                ana1[i]+=1
            else:
                ana1[i]=1
        
        for i in t:
            if i in ana2:
                ana2[i]+=1
            else:
                ana2[i]=1
        return ana1==ana2