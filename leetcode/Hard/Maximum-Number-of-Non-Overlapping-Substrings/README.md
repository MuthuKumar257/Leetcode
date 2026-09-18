# 1520. Maximum Number of Non-Overlapping Substrings

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsJudging...Judging...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1520. Maximum Number of Non-Overlapping SubstringsHardTopicsCompaniesHintGiven a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:


	The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
	A substring that contains a certain character c must also contain all occurrences of c.


Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 
Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.


Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.


 
Constraints:


	1 <= s.length <= 105
	s contains only lowercase English letters.

 Seen this question in a real interview before?1/6YesNoAccepted57,365/101.3KAcceptance Rate56.6%TopicsSenior StaffHash TableStringGreedySortingWeekly Contest 198CompaniesHint 1Notice that it's impossible for any two valid substrings to overlap unless one is inside another.Hint 2We can start by finding the starting and ending index for each character.Hint 3From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).Hint 4Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.Similar QuestionsMaximum Number of Non-overlapping Palindrome SubstringsHardDiscussion (92)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestDeepanshu ChauhanJun 15, 2026I wish everyone who comes across this message attains their dream job in 2026! Read more3097SAAHIL SABU HAMEEDOct 18, 2023What tf do you mean ??????????? Read more113Jaimie Rosal9 hours ago Read moreRead more481SANSKAR GUPTAMay 11, 2026Why all the super hard questions are string + graph ?? :) Read moreFeedback283Yuting ZhongJul 19, 2020????????????????? Read more381Utkarsh_SAug 15, 2025I hope I am not being asked this in an interview or OA Read more191DIVITE DINESHApr 23, 2024Input
s =
"abab"
Output
["aba"]
Expected
["abab"] Read more154PrishaJul 17, 2023SAD: Even after knowing the that the graph concept of maximum number of connected components has to be used , could not apply that :(. But did it with some other method. need to practise graphs Read more124Lourdu RadjouFeb 20, 2024I got the intuition it is graph but can't get it,, so watched the solution took 2 hrs to understand and code but fails and fails but finally i myself found the error and debug it and that feeling my god😊. Even though it took 3 hrs i feel it is worth. Read more111ds1ayerJul 13, 2026Congrats whoever made it this far into striver's sheet and solved this problem. Read more143123410Copyright © 2026 LeetCode. All rights reserved.1.1K922426 Online
@property --beam-angle-_r_7o_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7o_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7o_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7o_"][data-active] {
  animation:
    beam-spin-_r_7o_ 1.96s linear infinite,
    beam-fade-in-_r_7o_ 0.6s ease forwards;
}

[data-beam="_r_7o_"][data-fading] {
  animation:
    beam-spin-_r_7o_ 1.96s linear infinite,
    beam-fade-out-_r_7o_ 0.5s ease forwards;
}

[data-beam="_r_7o_"][data-active]::after,
[data-beam="_r_7o_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7o_),
        transparent 0%, transparent 54%,
        rgba(0, 0, 0, 0.08) 57%,
        rgba(0, 0, 0, 0.2) 60%,
        rgba(0, 0, 0, 0.4) 63%,
        rgba(0, 0, 0, 0.55) 66%,
        rgba(0, 0, 0, 0.4) 69%,
        rgba(0, 0, 0, 0.2) 72%,
        rgba(0, 0, 0, 0.08) 75%,
        transparent 78%, transparent 100%
      ),radial-gradient(ellipse 9px 18px at 2% 68%, rgb(60, 140, 200), transparent),
    radial-gradient(ellipse 4px 8px at 2% 68%, rgb(50, 120, 180), transparent),
    radial-gradient(ellipse 59px 9px at 72% -3%, rgb(100, 80, 220), transparent),
    radial-gradient(ellipse 42px 7px at 74% 100%, rgb(80, 100, 255), transparent),
    radial-gradient(ellipse 10px 17px at 100% 27%, rgb(120, 70, 240), transparent),
    radial-gradient(ellipse 10px 18px at 100% 27%, rgb(90, 80, 220), transparent),
    radial-gradient(ellipse 5px 10px at 100% 27%, rgb(70, 110, 255), transparent),
    radial-gradient(ellipse 11px 12px at 100% 27%, rgb(110, 90, 230), transparent);
  -webkit-mask:
    conic-gradient(
      from var(--beam-angle-_r_7o_),
      transparent 0%, transparent 30%,
      rgba(255, 255, 255, 0.1) 36%, rgba(255, 255, 255, 0.35) 44%,
      white 52%, white 80%,
      rgba(255, 255, 255, 0.35) 86%, rgba(255, 255, 255, 0.1) 92%,
      transparent 95%, transparent 100%
    ),
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: source-in, xor;
  mask:
    conic-gradient(
      from var(--beam-angle-_r_7o_),
      transparent 0%, transparent 30%,
      rgba(255, 255, 255, 0.1) 36%, rgba(255, 255, 255, 0.35) 44%,
      white 52%, white 80%,
      rgba(255, 255, 255, 0.35) 86%, rgba(255, 255, 255, 0.1) 92%,
      transparent 95%, transparent 100%
    ),
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  mask-composite: intersect, exclude;
  pointer-events: none;
  z-index: 2;
  opacity: calc(var(--beam-opacity-_r_7o_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7o_"][data-active]::before,
[data-beam="_r_7o_"][data-fading]::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  clip-path: inset(0 round 9999px);
  background: radial-gradient(ellipse 9px 18px at 2% 68%, rgba(60, 140, 200, 0.5), transparent),
    radial-gradient(ellipse 4px 8px at 2% 68%, rgba(50, 120, 180, 0.45), transparent),
    radial-gradient(ellipse 59px 9px at 72% -3%, rgba(100, 80, 220, 0.35), transparent),
    radial-gradient(ellipse 42px 7px at 74% 100%, rgba(80, 100, 255, 0.35), transparent),
    radial-gradient(ellipse 10px 17px at 100% 27%, rgba(120, 70, 240, 0.3), transparent),
    radial-gradient(ellipse 10px 18px at 100% 27%, rgba(90, 80, 220, 0.4), transparent),
    radial-gradient(ellipse 5px 10px at 100% 27%, rgba(70, 110, 255, 0.3), transparent),
    radial-gradient(ellipse 11px 12px at 100% 27%, rgba(110, 90, 230, 0.3), transparent);
  box-shadow: inset 0 0 5px 1px rgba(0, 0, 0, 0.14);
  -webkit-mask-image: conic-gradient(
    from var(--beam-angle-_r_7o_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7o_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7o_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7o_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7o_),
        transparent 0%, transparent 58%,
        rgba(0, 0, 0, 0.02) 62%,
        rgba(0, 0, 0, 0.08) 65%,
        rgba(0, 0, 0, 0.2) 67%,
        rgba(0, 0, 0, 0.4) 69%,
        rgba(0, 0, 0, 0.6) 70%,
        rgba(0, 0, 0, 0.6) 70.5%,
        rgba(0, 0, 0, 0.4) 71.5%,
        rgba(0, 0, 0, 0.2) 73%,
        rgba(0, 0, 0, 0.08) 75%,
        rgba(0, 0, 0, 0.02) 78%,
        transparent 82%
      );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  padding: 1px;
  filter: blur(8px) brightness(1.30) saturate(0.96);
  pointer-events: none;
  z-index: 3;
  opacity: 0;
}

[data-beam="_r_7o_"][data-active] [data-beam-bloom],
[data-beam="_r_7o_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7o_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7o_ {
  to { --beam-angle-_r_7o_: 360deg; }
}

@keyframes beam-fade-in-_r_7o_ {
  to { --beam-opacity-_r_7o_: 1; }
}

@keyframes beam-fade-out-_r_7o_ {
  from { --beam-opacity-_r_7o_: 1; }
  to { --beam-opacity-_r_7o_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonCJavaScriptRustGoKotlinTypeScriptPHPSwiftC#RubyElixirDartErlangRacketScalaPandasGreedyStringSortingHash TableTwo PointersGraph TheoryDynamic ProgrammingDepth-First SearchSliding WindowArrayStrongly Connected ComponentBacktrackingBinary SearchKosaraju's AlgorithmHeap (Priority Queue)Union-FindQueueStackOrdered SetMonotonic StackMemoizationOrdered MapDirected Acyclic GraphTarjan's SCC AlgorithmTopological SortBitmaskSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 09, 2026Maximum Number of Non-Overlapping SubstringsEditorial910.6K6Long Nguyen・ Open・9 hours ago100% - [Hard Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+8510.2K1Aura Farming・ Open・11 hours agoᯓ★ Trust me it's not Hard! • Sorting → Greedy | Visual Flow ⚡︎ • Easy Explanation!✈︎GreedySortingC++Java1+402.3K4Ritik Saini・ Open・13 hours agoMost easy to understand solution || With explanation || SortingHash TableStringGreedySorting1+192.4K2Aryan Kumar Shaw Halwai・ Open・10 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Greedy + First/Last OccurenceHash TableStringGreedySorting4+138452Muthu Vrn・ Open・5 hours agoGod is Great 467Python38220Coding_Ghost・ Open・8 hours ago100 % beats solutionC++51252Manjeet Dhayal・ Open・6 hours agoObservation | Greedy or DP | focus on character occurance (first, last) | Explained Hash TableStringDynamic ProgrammingGreedy2+4740Ankit Mishra・ Open・13 hours agoGreedy + Interval Expansion | The Trick Behind This Hard Problem | O(n) | C++ Java Python JSGreedyPythonC++Java1+58450Vinay kumar・ Open・9 hours ago🏆⚡ 2 Approaches • Expand Intervals + Greedy • O(N) 🚀🔥Hash TableStringGreedySorting3+3991A S T A・ Open・6 hours ago💡 Hard made easy ❤️ — A step-by-step, intuition-based approach.  ⏱️ TC: O(n) | 💾 SC: O(1)Java3490Aryan Yadav・ Open・12 hours agoSImple and short ---- Beat 99%Python334900Magudarena・ Open・12 hours agoGreedy O(N) | Range Expansion + End-Time Sorting | All 19 LanguagesSwiftPHPScalaRust6+31730Sukhmanpreet Singh・ Open・5 hours agoEasy Solution | Broken into Functions for UnderstandingHash TableStringGreedySliding Window2+2112Prashant Singh・ Open・12 hours agoClingy Characters: Grow, Nest, Swap — O(26n)Two PointersStringGreedyJava2571All Solutions100% - [Hard Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS Long Nguyen10.2K9 hours agoCC++JavaTypeScript2+Intuition
A valid substring must contain every occurrence of every character that appears inside it.
For each character, we can record:

Its first occurrence.
Its last occurrence.
Its total frequency.

These values describe the interval that must be covered if that character belongs to a selected substring.
The key observation is that an interval [left, right] is complete when the total number of occurrences of the characters collected inside it equals:
right - left + 1
This means every position inside the interval belongs to those characters, and all occurrences of those characters are contained inside the interval.
We can process characters in first-occurrence order and use a queue to build these valid intervals greedily.
Approach


Count the frequency of every character in s.


For every character, store:


first[c] = first occurrence of c
last[c]  = last occurrence of c
count[c] = total occurrences of c


Process the distinct characters in the order of their first appearance.


For each character, add its information to the front of the queue:


[first[c], last[c], count[c]]

Scan the current queue and maintain:

left  = minimum first occurrence
right = maximum last occurrence
total = total frequency

After adding each queued character, check:

total == right - left + 1
If this is true, [left, right] forms a complete valid substring.

Add:

s[left:right + 1]
to the result.


Clear the queue after selecting a valid substring so the next selected substring starts independently and does not overlap it.


Continue processing the remaining characters.


Return all selected substrings.


Complexity

Time complexity:

O(n)
Building the frequency, first occurrence, and last occurrence information requires O(n) time.
There are at most 26 distinct lowercase English letters, so all queue operations and scans are bounded by a constant.
Therefore, the overall time complexity is:
O(n)

Space complexity:

O(n)
The character information and queue contain at most 26 entries, which is O(1) auxiliary space.
However, the returned substrings can contain up to O(n) total characters.
Therefore, including the output:
O(n)
Auxiliary space excluding the output is:
O(1)
Code
Python3C++CJavaJavaScriptTypeScriptclass Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        counts = Counter(s)
        first = {c: s.find(c) for c in counts}
        last = {c: s.rfind(c) for c in counts}

        res = []
        queue = deque()

        for c in counts:
            queue.appendleft([first[c], last[c], counts[c]])

            left = inf
            right = -inf
            total = 0

            for x, y, z in queue:
                total += z
                left = min(left, x)
                right = max(right, y)

                if total == right - left + 1:
                    break

            if total == right - left + 1:
                res.append(s[left:right + 1])
                queue.clear()

        return res PreviousMaximum Number of Non-Overlapping SubstringsNextᯓ★ Trust me it's not Hard! • Sorting → Greedy | Visual Flow ⚡︎ • Easy Explanation!✈︎Comments (1)Sort by:BestCommentAWVB6 minutes agoThanks for the solution! However, I don't understand why the python solution is not written as:
def maxNumOfSubstrings(self, s: str) -> list[str]:
counts = Counter(s)
first = {c: s.find(c) for c in counts}
last = {c: s.rfind(c) for c in counts}
res = []
queue = deque()
    for c in counts:
        queue.appendleft([first[c], last[c], counts[c]])
        left = inf
        right = -inf
        total = 0

        for x, y, z in queue:
            total += z
            left = min(left, x)
            right = max(right, y)

            if total == right - left + 1:
                res.append(s[left:right + 1])
                queue.clear()
                break
           
    return res Read more01851Python3Auto1234567891011121314class Solution:    def maxNumOfSubstrings(self, s: str) -> list[str]:        counts = Counter(s)        first = {c: s.find(c) for c in counts}        last = {c: s.rfind(c) for c in counts}        res = []        queue = deque()        for c in counts:            queue.appendleft([first[c], last[c], counts[c]])            left = inf            right = -infSavedLn 29, Col 19Case 1Case 2s ="adefaddaccc"912›"adefaddaccc""abbaccd"SourceAcceptedRuntime: 0 msCase 1Case 2Inputs ="adefaddaccc"Output["e","f","ccc"]Expected["e","f","ccc"]Contribute a testcaseInput912›"adefaddaccc""abbaccd"Output912›["e","f","ccc"]["bb","cc","d"]Expected912›["e","f","ccc"]["d","bb","cc"] All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 18, 2026 18:29AnalysisSolutionCodePython31class Solution:
2    def maxNumOfSubstrings(self, s: str) -> list[str]:
3        counts = Counter(s)
4        first = {c: s.find(c) for c in counts}
5        last = {c: s.rfind(c) for c in counts}
6
7        res = []
8        queue = deque()
9
10        for c in counts:
11            queue.appendleft([first[c], last[c], counts[c]])
12
13            left = inf
14            right = -inf
15            total = 0
16
17            for x, y, z in queue:
18                total += z
19                left = min(left, x)
20                right = max(right, y)
21
22                if total == right - left + 1:
23                    break
24
25            if total == right - left + 1:
26                res.append(s[left:right + 1])
27                queue.clear()
28
29        return resView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
