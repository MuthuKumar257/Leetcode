"""
LeetCode: Count Zero Request Servers
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/count-zero-request-servers/
"""

if dico[serv]==0:
                    countNull-=1
                dico[serv]+=1
                right+=1
            while left+1<p and logs[left+1][1]<query-x:
                left+=1
                serv=logs[left][0]
                dico[serv]-=1
                if dico[serv]==0:
                    countNull+=1
            res[i]=countNull
        return res
