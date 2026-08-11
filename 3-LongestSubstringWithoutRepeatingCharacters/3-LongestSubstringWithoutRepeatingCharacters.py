# Last updated: 8/11/2026, 6:52:11 PM
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         a=[0]
#         for j in range(len(s)):
#             temp=s[j]
#             for i in range(j+1,len(s)):
#                 if s[i] in temp:
#                     a.append(len(temp))
#                     temp=s[i]
#                     break
#                 temp=temp+s[i]
#             a.append(len(temp))
#         return max(a)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        