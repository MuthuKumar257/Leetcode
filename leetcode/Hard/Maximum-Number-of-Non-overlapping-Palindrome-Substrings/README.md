# 2472. Maximum Number of Non-overlapping Palindrome Substrings

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit10300:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsJudging...Judging...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result2472. Maximum Number of Non-overlapping Palindrome SubstringsHardTopicsCompaniesHintYou are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:


	The length of each substring is at least k.
	Each substring is a palindrome.


Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 
Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.


Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.


 
Constraints:


	1 <= k <= s.length <= 2000
	s consists of lowercase English letters.

 Seen this question in a real interview before?1/6YesNoAccepted39,133/77.2KAcceptance Rate50.7%TopicsSenior StaffTwo PointersStringDynamic ProgrammingGreedyWeekly Contest 319CompaniesHint 1Try to use dynamic programming to solve the problem.Hint 2let dp[i] be the answer for the prefix s[0…i].Hint 3The final answer to the problem will be dp[n-1]. How do you compute this dp?Similar QuestionsLongest Palindromic SubstringMediumPalindrome PartitioningMediumPalindrome Partitioning IIHardPalindrome Partitioning IIIHardMaximum Number of Non-Overlapping SubstringsHardPalindrome Partitioning IVHardDiscussion (38)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestKardboardCodeMar 09, 2024I got this on my PhonePe interview Read more391Aura Farming2 hours agoLeetCode really wakes up every morning and asks: Overlap or non-overlap bro? 💀
Happy Engineer’s Day! 👨‍💻😂
Hope we all get placed before GTA 6 drops! 💼🥲 Read more31ngocbaoMar 13, 2024Greedy works fine with this problem. You don't need DP. Read moreTip164anoob375 hours agoClosing this tab like I never saw it. See you guys tomorrow when LeetCode decides to love us again Read more95vivek781113Aug 29, 2025Greedy works

You can jump immeditely by k steps to find the next valid palindrome
Can be solved in O(n * k)
 Read moreTip5rajeshswamiDec 05, 2024I got this question in my crickbuzz HackerRank test Read more5Juvy3 hours agoI didnt expect a hard one after an easy
definitely a storm after the calm Read more3AutumnKeeperOct 20, 2024The "non-overlapping" in question means non-overlapping in the position of letter.
E.g. "aaaa" can be divided into 'aa' & 'aa'. The valid substrings can be the same.
However 'aaa' & 'aaa' is not allowed. Because in this case they share one 'overlapping' letter Read more3Aditya KumarSep 25, 2024no way i myself came up with greedy solution feel so good now Read more31ArthurNov 13, 2022I wrote two versions of the same code - once in Py and another in CPP. The Py version will  time out but CPP will pass :(
I think Big O wise, the code should be fine. I think the Py time limits should be extended.
`class Solution {
public:
int maxPalindromes(string s, int k) {
vector<vector> is_pal(s.size(),vector(s.size(), false));
for(int l = 0;l<s.size();l++){
for(int start = 0;start<s.size();start++){
auto end = start + l;
if(end >= s.size()){
break;
}else if (start == end || start + 1 == end){
// cout << start << " " << end << endl;
is_pal[start][end] = s[start] == s[end];
} else{
// cout << start << " " << end << endl;
is_pal[start][end] = (s[start] == s[end] && is_pal[start+1][end-1]);
}
}
}
vector dp(s.size()+1, 0);
for(int i = 0;i<s.size();i++){
dp[i+1] = max(dp[i], dp[i+1]);
for(int end = i+k-1;end<s.size();end++){
if(is_pal[i][end]){
// t << i << " " << end << endl;
dp[end+1] = max(dp[end+1], dp[i]+1);
break;
}
}
    } 
    // t << dp.size() << endl;
    return dp[s.size()];
}
};`
`class Solution:
def maxPalindromes(self, s: str, k: int) -> int:
is_pal = [[False] * len(s) for let in s]
for l in range(len(s)):
for start in range(len(s)):
end = start + l
if end >= len(s):
break
elif start == end or start+1 == end:
is_pal[start][end] = s[start] == s[end]
else:
is_pal[start][end] = s[start] == s[end] and is_pal[start+1][end-1]
    dp = [0] * (len(s) + 1)
    for i in range(len(s)):
        dp[i+1] = max(dp[i], dp[i+1]) 
        
        for end in range(i+k-1, len(s)):
            if is_pal[i][end]:
                # print("Found", start, end)
                dp[end+1] = max(dp[end+1], dp[i] + 1)
                break
    
    # print(dp)
    return dp[-1]` Read more311234Copyright © 2026 LeetCode. All rights reserved.576383700 Online
@property --beam-angle-_r_7p_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7p_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7p_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7p_"][data-active] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-in-_r_7p_ 0.6s ease forwards;
}

[data-beam="_r_7p_"][data-fading] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-out-_r_7p_ 0.5s ease forwards;
}

[data-beam="_r_7p_"][data-active]::after,
[data-beam="_r_7p_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"][data-active]::before,
[data-beam="_r_7p_"][data-fading]::before {
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
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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

[data-beam="_r_7p_"][data-active] [data-beam-bloom],
[data-beam="_r_7p_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7p_ {
  to { --beam-angle-_r_7p_: 360deg; }
}

@keyframes beam-fade-in-_r_7p_ {
  to { --beam-opacity-_r_7p_: 1; }
}

@keyframes beam-fade-out-_r_7p_ {
  from { --beam-opacity-_r_7p_: 1; }
  to { --beam-opacity-_r_7p_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoC#RustKotlinTypeScriptRubySwiftScalaPHPRacketElixirDartErlangDynamic ProgrammingGreedyStringTwo PointersMemoizationRecursionRolling HashManacherDepth-First SearchSimulationArraySortingBinary TreeSliding WindowHeap (Priority Queue)BacktrackingBrute-Force SearchSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 08, 2026Maximum Number of Non-overlapping Palindrome SubstringsEditorial45K5eunice・ Open・5 hours agoGreedy | Sliding Window | Two-Pointers | Palindrome Core | Beats 100%Two PointersStringGreedyPython4+272.5K1Aura Farming・ Open・2 hours agoᯓ★ Trust me it's not Hard! 100% Beats • TwoPointer's ⚡︎ Easiest Approach with Image's ✈︎Two PointersStringGreedyC++2+197064An-Wen Deng・ Open・4 hours agoGreedy sliding window|beats 100%Two PointersGreedyC++117086Bijoy Sing・ Open・4 hours ago✅ Simple & Easy Solution | 🚫 No DP | C++ | Python | Java | JavaScript | GoTwo PointersStringGreedyPython5+76141Md Aarzoo Islam・ Open・3 hours ago163ms | Beats 50.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Two PointersStringDynamic ProgrammingGreedy6+101731Aryan Kumar Shaw Halwai・ Open・2 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Palindrome DP + 1D DPTwo PointersStringDynamic ProgrammingGreedy1+5600VIVEK_KUMAR・ Open・4 hours ago✅✅Greedy Center Expansion || O(N²) || ❌DPStringGreedyC++Java1+43242Jordinario・ Open・4 hours ago[0 ms] Please help me prove this is not quadraticStringGreedyGo2643EdgeCaseOffByOne・ Open・an hour agoThe DP Behind Non-Overlapping PalindromesTwo PointersStringDynamic ProgrammingC++3240Long Nguyen・ Open・3 hours ago100% - [Hard Problem with Easy Approach] 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+21102Kostiantyn Lazukin・ Open・4 hours agoSimple solution using O(1) spaceC++2751Ujjawal・ Open・2 hours agoSolution that Beats 100%Two PointersStringDynamic ProgrammingGreedy1+2240Ajay Choudhary・ Open・4 hours agopython3Python321370Pallab Nath・ Open・24 minutes agoSimple Expand Around Centre + Interval Scheduling || O(n^2) Solution || Simple ExplanationC++130Harsh Chhallani・ Open・an hour agoRolling Hash + DP . Dynamic ProgrammingRolling HashJava1130Suraj Darade・ Open・an hour ago[BEATS 100%🔥] THIS PALINDROME DP TRICK IS CRAZY SIMPLE 🤯🧠 | MEMOIZATION MAGIC 🪄🚀StringDynamic ProgrammingMemoizationPython2+1130light-y_・ Open・an hour ago100% Beat | O(nk) | simpleTwo PointersStringC++160Naman Sharma・ Open・an hour agoSimple Java Code Java1140Sonam Narula・ Open・an hour agoNo DP Needed! 🧠 $O(1)$ Space Greedy Trick for Non-Overlapping PalindromeTwo PointersStringDynamic ProgrammingGreedy1+120Rahul Patil・ Open・an hour ago💾 Low Memory Magic! Greedy Slidings Window Beats 88.66% Memory ⚡🧠Two PointersStringPythonPython31130Yash Fadadu・ Open・2 hours ago🧠💹Optimized Solution | 100% Beats | Easy Memorization🧠💹Python31120Ayush Dalal・ Open・2 hours ago🚀 Very Easy & Short Solution | Java & JavaScript | Palindrome SubstringsTwo PointersStringDynamic ProgrammingGreedy2+190Seither・ Open・2 hours agoGreedy Palindrome Expansion from Every Center | O(n²) Time, O(1) SpaceTwo PointersStringGreedyPython31140Vedansh Rathod・ Open・3 hours ago⚡ Two DP Layers, One Maximum | 🧠 Palindrome Detection + Interval Selection | 🚀 O(n²) SolutionTwo PointersStringDynamic ProgrammingPython3130Prabhas Sharma・ Open・3 hours ago2472. Maximum Number of Non-overlapping Palindrome SubstringsPython31120Unstbl・ Open・3 hours agoSimple O(n) Solution with IntutionTwo PointersStringDynamic ProgrammingGreedy3+1210Sai Vishal Matcha・ Open・4 hours agoMaximum Number of Non-overlapping Palindrome SubstringsPython31120Magudarena・ Open・4 hours agoSimple O(N⋅K) DP | Clean Substring Checking | All 19 Languages Included 🚀CPHPGoScala6+1450Ajay Choudhary・ Open・4 hours agoC#C#1180All Solutionspython3Ajay Choudhary1374 hours agoPython3Code
Python3class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = s[left] == s[right] and (
                    length <= 2 or is_palindrome[left + 1][right - 1]
                )

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if is_palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n] Discover moreTechnical skill assessmentsNextMaximum Number of Non-overlapping Palindrome SubstringsComments (0)Sort by:BestCommentNo comments yet.20Python3Auto7891011121314151617181920            for left in range(n - length + 1):                right = left + length - 1                is_palindrome[left][right] = s[left] == s[right] and (                    length <= 2 or is_palindrome[left + 1][right - 1]                )        dp = [0] * (n + 1)        for i in range(1, n + 1):            dp[i] = dp[i - 1]            for j in range(i - k + 1):                if is_palindrome[j][i - 1]:                    dp[i] = max(dp[i], dp[j] + 1)        return dp[n]SavedLn 20, Col 21AcceptedRuntime: 0 msCase 1Case 2Inputs ="abaccdbbd"k =3Output2Expected2Contribute a testcaseInput91234›"abaccdbbd"3"adbcda"2Output912›20Expected912›20 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 15, 2026 10:20AnalysisSolutionCodePython31class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        n = len(s)
4        is_palindrome = [[False] * n for _ in range(n)]
5
6        for length in range(1, n + 1):
7            for left in range(n - length + 1):
8                right = left + length - 1
9                is_palindrome[left][right] = s[left] == s[right] and (
10                    length <= 2 or is_palindrome[left + 1][right - 1]
11                )
12
13        dp = [0] * (n + 1)
14        for i in range(1, n + 1):
15            dp[i] = dp[i - 1]
16            for j in range(i - k + 1):
17                if is_palindrome[j][i - 1]:
18                    dp[i] = max(dp[i], dp[j] + 1)
19
20        return dp[n]View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize
- **Memory:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit10300:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsJudging...Judging...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result2472. Maximum Number of Non-overlapping Palindrome SubstringsHardTopicsCompaniesHintYou are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:


	The length of each substring is at least k.
	Each substring is a palindrome.


Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 
Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.


Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.


 
Constraints:


	1 <= k <= s.length <= 2000
	s consists of lowercase English letters.

 Seen this question in a real interview before?1/6YesNoAccepted39,133/77.2KAcceptance Rate50.7%TopicsSenior StaffTwo PointersStringDynamic ProgrammingGreedyWeekly Contest 319CompaniesHint 1Try to use dynamic programming to solve the problem.Hint 2let dp[i] be the answer for the prefix s[0…i].Hint 3The final answer to the problem will be dp[n-1]. How do you compute this dp?Similar QuestionsLongest Palindromic SubstringMediumPalindrome PartitioningMediumPalindrome Partitioning IIHardPalindrome Partitioning IIIHardMaximum Number of Non-Overlapping SubstringsHardPalindrome Partitioning IVHardDiscussion (38)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestKardboardCodeMar 09, 2024I got this on my PhonePe interview Read more391Aura Farming2 hours agoLeetCode really wakes up every morning and asks: Overlap or non-overlap bro? 💀
Happy Engineer’s Day! 👨‍💻😂
Hope we all get placed before GTA 6 drops! 💼🥲 Read more31ngocbaoMar 13, 2024Greedy works fine with this problem. You don't need DP. Read moreTip164anoob375 hours agoClosing this tab like I never saw it. See you guys tomorrow when LeetCode decides to love us again Read more95vivek781113Aug 29, 2025Greedy works

You can jump immeditely by k steps to find the next valid palindrome
Can be solved in O(n * k)
 Read moreTip5rajeshswamiDec 05, 2024I got this question in my crickbuzz HackerRank test Read more5Juvy3 hours agoI didnt expect a hard one after an easy
definitely a storm after the calm Read more3AutumnKeeperOct 20, 2024The "non-overlapping" in question means non-overlapping in the position of letter.
E.g. "aaaa" can be divided into 'aa' & 'aa'. The valid substrings can be the same.
However 'aaa' & 'aaa' is not allowed. Because in this case they share one 'overlapping' letter Read more3Aditya KumarSep 25, 2024no way i myself came up with greedy solution feel so good now Read more31ArthurNov 13, 2022I wrote two versions of the same code - once in Py and another in CPP. The Py version will  time out but CPP will pass :(
I think Big O wise, the code should be fine. I think the Py time limits should be extended.
`class Solution {
public:
int maxPalindromes(string s, int k) {
vector<vector> is_pal(s.size(),vector(s.size(), false));
for(int l = 0;l<s.size();l++){
for(int start = 0;start<s.size();start++){
auto end = start + l;
if(end >= s.size()){
break;
}else if (start == end || start + 1 == end){
// cout << start << " " << end << endl;
is_pal[start][end] = s[start] == s[end];
} else{
// cout << start << " " << end << endl;
is_pal[start][end] = (s[start] == s[end] && is_pal[start+1][end-1]);
}
}
}
vector dp(s.size()+1, 0);
for(int i = 0;i<s.size();i++){
dp[i+1] = max(dp[i], dp[i+1]);
for(int end = i+k-1;end<s.size();end++){
if(is_pal[i][end]){
// t << i << " " << end << endl;
dp[end+1] = max(dp[end+1], dp[i]+1);
break;
}
}
    } 
    // t << dp.size() << endl;
    return dp[s.size()];
}
};`
`class Solution:
def maxPalindromes(self, s: str, k: int) -> int:
is_pal = [[False] * len(s) for let in s]
for l in range(len(s)):
for start in range(len(s)):
end = start + l
if end >= len(s):
break
elif start == end or start+1 == end:
is_pal[start][end] = s[start] == s[end]
else:
is_pal[start][end] = s[start] == s[end] and is_pal[start+1][end-1]
    dp = [0] * (len(s) + 1)
    for i in range(len(s)):
        dp[i+1] = max(dp[i], dp[i+1]) 
        
        for end in range(i+k-1, len(s)):
            if is_pal[i][end]:
                # print("Found", start, end)
                dp[end+1] = max(dp[end+1], dp[i] + 1)
                break
    
    # print(dp)
    return dp[-1]` Read more311234Copyright © 2026 LeetCode. All rights reserved.576383700 Online
@property --beam-angle-_r_7p_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7p_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7p_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7p_"][data-active] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-in-_r_7p_ 0.6s ease forwards;
}

[data-beam="_r_7p_"][data-fading] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-out-_r_7p_ 0.5s ease forwards;
}

[data-beam="_r_7p_"][data-active]::after,
[data-beam="_r_7p_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"][data-active]::before,
[data-beam="_r_7p_"][data-fading]::before {
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
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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

[data-beam="_r_7p_"][data-active] [data-beam-bloom],
[data-beam="_r_7p_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7p_ {
  to { --beam-angle-_r_7p_: 360deg; }
}

@keyframes beam-fade-in-_r_7p_ {
  to { --beam-opacity-_r_7p_: 1; }
}

@keyframes beam-fade-out-_r_7p_ {
  from { --beam-opacity-_r_7p_: 1; }
  to { --beam-opacity-_r_7p_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoC#RustKotlinTypeScriptRubySwiftScalaPHPRacketElixirDartErlangDynamic ProgrammingGreedyStringTwo PointersMemoizationRecursionRolling HashManacherDepth-First SearchSimulationArraySortingBinary TreeSliding WindowHeap (Priority Queue)BacktrackingBrute-Force SearchSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 08, 2026Maximum Number of Non-overlapping Palindrome SubstringsEditorial45K5eunice・ Open・5 hours agoGreedy | Sliding Window | Two-Pointers | Palindrome Core | Beats 100%Two PointersStringGreedyPython4+272.5K1Aura Farming・ Open・2 hours agoᯓ★ Trust me it's not Hard! 100% Beats • TwoPointer's ⚡︎ Easiest Approach with Image's ✈︎Two PointersStringGreedyC++2+197064An-Wen Deng・ Open・4 hours agoGreedy sliding window|beats 100%Two PointersGreedyC++117086Bijoy Sing・ Open・4 hours ago✅ Simple & Easy Solution | 🚫 No DP | C++ | Python | Java | JavaScript | GoTwo PointersStringGreedyPython5+76141Md Aarzoo Islam・ Open・3 hours ago163ms | Beats 50.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Two PointersStringDynamic ProgrammingGreedy6+101731Aryan Kumar Shaw Halwai・ Open・2 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Palindrome DP + 1D DPTwo PointersStringDynamic ProgrammingGreedy1+5600VIVEK_KUMAR・ Open・4 hours ago✅✅Greedy Center Expansion || O(N²) || ❌DPStringGreedyC++Java1+43242Jordinario・ Open・4 hours ago[0 ms] Please help me prove this is not quadraticStringGreedyGo2643EdgeCaseOffByOne・ Open・an hour agoThe DP Behind Non-Overlapping PalindromesTwo PointersStringDynamic ProgrammingC++3240Long Nguyen・ Open・3 hours ago100% - [Hard Problem with Easy Approach] 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+21102Kostiantyn Lazukin・ Open・4 hours agoSimple solution using O(1) spaceC++2751Ujjawal・ Open・2 hours agoSolution that Beats 100%Two PointersStringDynamic ProgrammingGreedy1+2240Ajay Choudhary・ Open・4 hours agopython3Python321370Pallab Nath・ Open・24 minutes agoSimple Expand Around Centre + Interval Scheduling || O(n^2) Solution || Simple ExplanationC++130Harsh Chhallani・ Open・an hour agoRolling Hash + DP . Dynamic ProgrammingRolling HashJava1130Suraj Darade・ Open・an hour ago[BEATS 100%🔥] THIS PALINDROME DP TRICK IS CRAZY SIMPLE 🤯🧠 | MEMOIZATION MAGIC 🪄🚀StringDynamic ProgrammingMemoizationPython2+1130light-y_・ Open・an hour ago100% Beat | O(nk) | simpleTwo PointersStringC++160Naman Sharma・ Open・an hour agoSimple Java Code Java1140Sonam Narula・ Open・an hour agoNo DP Needed! 🧠 $O(1)$ Space Greedy Trick for Non-Overlapping PalindromeTwo PointersStringDynamic ProgrammingGreedy1+120Rahul Patil・ Open・an hour ago💾 Low Memory Magic! Greedy Slidings Window Beats 88.66% Memory ⚡🧠Two PointersStringPythonPython31130Yash Fadadu・ Open・2 hours ago🧠💹Optimized Solution | 100% Beats | Easy Memorization🧠💹Python31120Ayush Dalal・ Open・2 hours ago🚀 Very Easy & Short Solution | Java & JavaScript | Palindrome SubstringsTwo PointersStringDynamic ProgrammingGreedy2+190Seither・ Open・2 hours agoGreedy Palindrome Expansion from Every Center | O(n²) Time, O(1) SpaceTwo PointersStringGreedyPython31140Vedansh Rathod・ Open・3 hours ago⚡ Two DP Layers, One Maximum | 🧠 Palindrome Detection + Interval Selection | 🚀 O(n²) SolutionTwo PointersStringDynamic ProgrammingPython3130Prabhas Sharma・ Open・3 hours ago2472. Maximum Number of Non-overlapping Palindrome SubstringsPython31120Unstbl・ Open・3 hours agoSimple O(n) Solution with IntutionTwo PointersStringDynamic ProgrammingGreedy3+1210Sai Vishal Matcha・ Open・4 hours agoMaximum Number of Non-overlapping Palindrome SubstringsPython31120Magudarena・ Open・4 hours agoSimple O(N⋅K) DP | Clean Substring Checking | All 19 Languages Included 🚀CPHPGoScala6+1450Ajay Choudhary・ Open・4 hours agoC#C#1180All Solutionspython3Ajay Choudhary1374 hours agoPython3Code
Python3class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = s[left] == s[right] and (
                    length <= 2 or is_palindrome[left + 1][right - 1]
                )

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if is_palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n] Discover moreTechnical skill assessmentsNextMaximum Number of Non-overlapping Palindrome SubstringsComments (0)Sort by:BestCommentNo comments yet.20Python3Auto7891011121314151617181920            for left in range(n - length + 1):                right = left + length - 1                is_palindrome[left][right] = s[left] == s[right] and (                    length <= 2 or is_palindrome[left + 1][right - 1]                )        dp = [0] * (n + 1)        for i in range(1, n + 1):            dp[i] = dp[i - 1]            for j in range(i - k + 1):                if is_palindrome[j][i - 1]:                    dp[i] = max(dp[i], dp[j] + 1)        return dp[n]SavedLn 20, Col 21AcceptedRuntime: 0 msCase 1Case 2Inputs ="abaccdbbd"k =3Output2Expected2Contribute a testcaseInput91234›"abaccdbbd"3"adbcda"2Output912›20Expected912›20 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 15, 2026 10:20AnalysisSolutionCodePython31class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        n = len(s)
4        is_palindrome = [[False] * n for _ in range(n)]
5
6        for length in range(1, n + 1):
7            for left in range(n - length + 1):
8                right = left + length - 1
9                is_palindrome[left][right] = s[left] == s[right] and (
10                    length <= 2 or is_palindrome[left + 1][right - 1]
11                )
12
13        dp = [0] * (n + 1)
14        for i in range(1, n + 1):
15            dp[i] = dp[i - 1]
16            for j in range(i - k + 1):
17                if is_palindrome[j][i - 1]:
18                    dp[i] = max(dp[i], dp[j] + 1)
19
20        return dp[n]View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
