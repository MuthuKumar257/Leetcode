# 1541. Minimum Insertions to Balance a Parentheses String

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit400:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1541. Minimum Insertions to Balance a Parentheses StringMediumTopicsCompaniesHintGiven a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:


	Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
	Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.


In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.


	For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.


You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 
Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.


Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.


Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.


 
Constraints:


	1 <= s.length <= 105
	s consists of '(' and ')' only.

 Seen this question in a real interview before?1/6YesNoAccepted94,861/172.9KAcceptance Rate54.9%TopicsStaffStringStackGreedyBracket SequencesBiweekly Contest 32CompaniesHint 1Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.Hint 2If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.Similar QuestionsMinimum Number of Swaps to Make the String BalancedMediumDiscussion (79)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestchrisTrisAug 08, 2020For test case "(()))(()))()())))" expected is 4
but consider steps
(()))(()))()()))) => Removing all ()) => ()()()))
()()())) => Removing ()) => ()())
()()) => Removing ()) => ()
() => insert ) => ()) => "" Read more984Lincoln OsirisDec 13, 2023This is balanced, no?  ( * ) ( * ) Read more321Justin Wu3 hours ago Read moreRead more282KublaiFeb 27, 2022A bit confused about the question.
For test case "(()))(()))()())))" why is the answer 4, not 1 ?
It seems to me that I can insert ')' to the end and make it balanced. That is: "(()))(()))()())))" + ')' = "(()))(()))()()))))"
which will satisfy the two criterions:


Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.


Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.


================================
"(()))(()))()()))))"
->
"(()))(()))())))"
->
"(()))(()))))"
->
"(()))()))"
->
"(())))"
->
"())"
->
""
-> balanced Read more222loshmiFeb 28, 2024What a lame assignment. Its hard to even understand what exactly do they want. And examples present are not even showcasing the most ridiculous aspect of the assignment. That is the the closing parenthesis have to be consecutive.
Meaning  "()()))" is not valid. Yes, the inner ()) is balanced (chars 2-4), but even after that "()___)" is not considered balanced, because the  two ")" are not next to each other in the original string.
So the answer to ()())) is 3. You need 1 closing for () and one open and one closing for the opening bracket ) at the end. That is 3.
I hope this saves people some time. Read more162Diyan3 hours agoDay 12 of solving this Parentheses shit Read more13gamefanaFeb 05, 2024What exactly is the point of this problem? It doesn't add any learning value at all over the single ")" one. There is no special technique or theory that can be generalized to any other problem. Read more111deleted_userNov 23, 2023You don't need the stack for storage ;). It is helpful though, but after you solve it with a stack, you should ask - what am I really using it for, and can I achieve this with constant storage instead? Read more9Krishna MavuluriApr 22, 2023Read This Statement Carefully Before Solving it .
" corresponding two  CONSECUTIVE right parenthesis "
For  This Testcase  "(()))(()))()())))" answer is 4 . Read more81Vaibhav AggarwalAug 08, 2020"(()))(()))()())))"
Thanks in advance Read more912348Copyright © 2026 LeetCode. All rights reserved.1.3K791694 Online
@property --beam-angle-_r_7k_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7k_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7k_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7k_"][data-active] {
  animation:
    beam-spin-_r_7k_ 1.96s linear infinite,
    beam-fade-in-_r_7k_ 0.6s ease forwards;
}

[data-beam="_r_7k_"][data-fading] {
  animation:
    beam-spin-_r_7k_ 1.96s linear infinite,
    beam-fade-out-_r_7k_ 0.5s ease forwards;
}

[data-beam="_r_7k_"][data-active]::after,
[data-beam="_r_7k_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7k_),
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
      from var(--beam-angle-_r_7k_),
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
      from var(--beam-angle-_r_7k_),
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
  opacity: calc(var(--beam-opacity-_r_7k_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7k_"][data-active]::before,
[data-beam="_r_7k_"][data-fading]::before {
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
    from var(--beam-angle-_r_7k_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7k_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7k_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7k_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7k_),
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

[data-beam="_r_7k_"][data-active] [data-beam-bloom],
[data-beam="_r_7k_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7k_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7k_ {
  to { --beam-angle-_r_7k_: 360deg; }
}

@keyframes beam-fade-in-_r_7k_ {
  to { --beam-opacity-_r_7k_: 1; }
}

@keyframes beam-fade-out-_r_7k_ {
  from { --beam-opacity-_r_7k_: 1; }
  to { --beam-opacity-_r_7k_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++CPythonJavaScriptGoC#TypeScriptRustSwiftKotlinScalaDartRubyStackStringGreedyBracket SequencesCountingMathSimulationArrayIteratorMonotonic StackBit ManipulationTwo PointersSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・21 hours agoMinimum Insertions to Balance a Parentheses StringEditorial33K2Ashok Varma・ Open・2 hours agoCount the Waiting ( | Pairs of )) | Easy Intuition | Step by Step GIF VisualizationStringStackGreedyPython5+417191An-Wen Deng・ Open・an hour ago2 Greedy C++|beats 100%GreedyC++Bracket Sequences211.1K2Md Aarzoo Islam・ Open・2 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringStackGreedyC++6+159451Vaibhav Raj Singh・ Open・2 hours agoEasy Balancing ApproachMathStringC++121K1Dhanush Rajulapati・ Open・3 hours agoStack + Greedy Solution | Java, Python, C++, JavaScript | O(n) Time | O(n) SpaceStringStackGreedyPython4+139222Vaibhav Raj Singh・ Open・3 hours agoEasy Balancing ApproachMathStringC++166291TCZON・ Open・3 hours ago✅ 2 Methods | 🚀 Stack → Greedy Counter | 🎯O(n) Time | Pair Matching → Minimum Insertion | 2-LinerStringStackGreedyC++6+42321DHRUVIK・ Open・25 minutes agoSimple Observation + Easy Explanation | Greedy ApproachC++380aatifa_mugheer・ Open・2 hours agoEasy C++ Solution | Greedy C++3310Ajay Choudhary・ Open・3 hours agopython3Python331540An-Wen Deng・ Open・3 hours agoGreedy Branchless|0msGreedyC++Bracket Sequences141962Aryan Kumar Shaw Halwai・ Open・an hour agoGreedy 🔥| Easiest Solution with Step by Step Breakdown💯StringStackGreedyPython4+2201venkadasesan・ Open・3 hours agoBeats 100% | Ultimate O(N) Time / O(1) Space Greedy Solution / C, C++, Java, Python3CC++JavaPython321310Prabhas Sharma・ Open・an hour ago1541. Minimum Insertions to Balance a Parentheses StringPython3181All Solutions0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Md Aarzoo Islam9462 hours agoStringStackGreedyC++6+

Approach

Use two counters: ans for insertions and x for unmatched '('.
Traverse the string:

If the current character is '(', increment x.
If it is ')', check the next character:

If the next character is also ')', skip it and treat them as a pair.
Otherwise, increment ans to insert the missing ')'.


If x == 0, insert a missing '(' and increment ans. Otherwise, decrement x.


After the loop, each unmatched '(' needs two ')', so add 2 * x to ans.
Return ans.


Code
C++JavaJavaScriptTypeScriptPython3goclass Solution:
    def minInsertions(self, s: str) -> int:
        ans = x = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                x += 1
            else:
                if i < n - 1 and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1
                if x == 0:
                    ans += 1
                else:
                    x -= 1
            i += 1
        ans += x << 1
        return ans

 Previous2 Greedy C++|beats 100%NextEasy Balancing ApproachComments (1)Sort by:BestCommentMd Aarzoo Islam2 hours agoComplexity
Time Complexity: O(n) where n is the length of the input string s, because I examine each character a constant number of times.
Space Complexity: O(1) because I only use a few integer variables; no extra arrays or stacks are needed. Read more21151Python3Auto7891011121314654312                x += 1            else:                if i < n - 1 and s[i + 1] == ')':                    i += 1                else:                    ans += 1                if x == 0:                    ans += 1            if s[i] == '(':        while i < n:        i, n = 0, len(s)        ans = x = 0class Solution:    def minInsertions(self, s: str) -> int:SavedLn 19, Col 19AcceptedRuntime: 0 msCase 1Case 2Case 3Inputs ="(()))"Output1Expected1Contribute a testcaseInput9123›"(()))""())""))())("Output9123›103Expected9123›103 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 09, 2026 08:57AnalysisSolutionCodePython31class Solution:
2    def minInsertions(self, s: str) -> int:
3        ans = x = 0
4        i, n = 0, len(s)
5        while i < n:
6            if s[i] == '(':
7                x += 1
8            else:
9                if i < n - 1 and s[i + 1] == ')':
10                    i += 1
11                else:
12                    ans += 1
13                if x == 0:
14                    ans += 1
15                else:
16                    x -= 1
17            i += 1
18        ans += x << 1
19        return ansView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
