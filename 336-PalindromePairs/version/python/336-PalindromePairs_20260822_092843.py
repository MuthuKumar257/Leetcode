# Last updated: 8/22/2026, 9:28:43 AM
1class TrieNode:
2    def __init__(self):
3        self.children = dict()
4        self.end = False
5        self.idx = -1
6        self.palindromeIdxs = list()
7
8class Solution:
9    def __init__(self):
10        self.root = TrieNode()
11        
12    def palindromePairs(self, words: List[str]) -> List[List[int]]:
13        res = list()
14        
15        # populate the trie with
16        # the reverse of every word.
17        # once we're done inserting
18        # we're going to have 3 conditions
19        for i in range(len(words)):
20            cur = self.root
21            rWord = words[i][::-1]
22            for j in range(len(rWord)):
23                # if the current word (from j onwards)
24                # is a palindrome, add it's index to the trie node
25                # (palindromIdx list) we'll use it later on to find combinations
26                if self.isPalindrome(rWord[j:]):
27                    cur.palindromeIdxs.append(i)
28                    
29                if rWord[j] not in cur.children:
30                    cur.children[rWord[j]] = TrieNode()
31                cur = cur.children[rWord[j]]
32                
33            # once the word is done
34            # add it's index to the trie node
35            cur.end = True
36            cur.idx = i
37            
38        for i in range(len(words)):
39            self.search(words[i], i, res)
40            
41        return res
42        
43    # to find all pairse, we can have
44    # conditions:
45    # 1. exact match (abc, cba)
46    # 2. long word, short word in trie match (abbcc, a)
47    # 3. short word, long word in trie match (lls, sssll)
48    def search(self, word, idx, res):   
49        cur = self.root
50        for i in range(len(word)):
51            # 2. long word, short trie
52            # so the trie ended here and 
53            # we have matched till the ith
54            # character, so we check if the
55            # remaining of the word is also a
56            # palindrome, if yes, then we have a pair
57            # for e.g. word = abcdaa, trieWord = bcda
58            # we can make a pair like abcdaabcda
59            if cur.end and self.isPalindrome(word[i:]):
60                res.append([idx, cur.idx])
61                
62            if word[i] not in cur.children:
63                return
64            cur = cur.children[word[i]]        
65        
66        # 1. exact match
67        # in the given list, for that 
68        # we'll take every word and then
69        # check if the reverse of that
70        # word lies in the trie
71        # for e.g. for abc and cba
72        # the trie would have both c->b->a and a->b->c
73        # but when we take the first word (abc)
74        # we'll match this with a->b->c which is
75        # actually cba and so we found a match
76        if cur.end and cur.idx != idx:
77            res.append([cur.idx, idx])
78        
79        # 3. long trie, short word
80        # so the trie still has items (not cur.end)
81        # and the word has ended, it's the exact
82        # opposite of point 2
83        # for e.g. word=abcd trieWord=bcdaa
84        # we can have a pair bcdaaabcd
85        # and so we have a pair
86        for pIdx in cur.palindromeIdxs:
87            res.append([idx, pIdx])
88                
89        return
90        
91        
92    def isPalindrome(self, s):
93        return s == s[::-1]