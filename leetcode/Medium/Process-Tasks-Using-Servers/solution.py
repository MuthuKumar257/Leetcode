"""
LeetCode: Process Tasks Using Servers
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/process-tasks-using-servers/
"""

heappop(busy_servers)

            if free_servers == []:
                sec, wgt, idx = heappop(busy_servers)
                heappush(busy_servers, (sec + task, wgt, idx))

            else:
                wgt, idx = heappop(free_servers)
                heappush(busy_servers, (time + task, wgt, idx))
                
            ans.append(idx)

        return ans
