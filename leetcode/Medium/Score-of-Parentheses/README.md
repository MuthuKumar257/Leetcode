# 856. Score of Parentheses

- **Difficulty:** Medium
- **Language:** Java
- **LeetCode Link:** [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

## Solution

See [`solution.java`](./solution.java).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result856. Score of ParenthesesMediumTopicsCompaniesGiven a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:


	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.


 
Example 1:

Input: s = "()"
Output: 1


Example 2:

Input: s = "(())"
Output: 2


Example 3:

Input: s = "()()"
Output: 2


 
Constraints:


	2 <= s.length <= 50
	s consists of only '(' and ')'.
	s is a balanced parentheses string.

 Seen this question in a real interview before?1/6YesNoAccepted290,677/450.2KAcceptance Rate64.6%TopicsStaffStringStackBracket SequencesWeekly Contest 90CompaniesDiscussion (186)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:Bestnpestov9Mar 13, 2024what are these example test cases???? Could you have picked any worse ones Read more1756eunice16 hours ago Read more13511Eddie LAug 24, 2024These examples are absolute garbage. Read more156Akash_ChitaleAug 12, 2025Test Cases -------------->
If you find these test cases helpful, an upvote would be appreciated.
"((()()()))"
"(()(()))"
"()()()()()()()(((())))"
"((((((()))((()))))))"
"(()()(((())(((()))))))"
"(((((((((()()()))))((((())))))(((((((())))))))))))"
UPVOTE Read more1821user6982nzJul 02, 2023What does "AB" has score of A + B mean? Read more651Veron Nica14 hours agoWho would have thought it's another parenthesis problem
🤔🤔 Read more501Mohit SainiAug 09, 2025Guys try hard.
If I can then you definitely can solve this.
We will use stack. And we compute something and push back to the stack. Read moreTip416chirag c14 hours agoAt this point its too much parentheses Read more391David YeeJul 20, 2023I don't think the description is explained well... why is the output expected to be 6 instead of 8 when s = "(()(()))"? Read more2610Amrutham MohanJun 03, 2024because () = 1, so (()) = 21 and AB = A+B
Here ()(()) = 1 + 2 = 3
Finally (()(())) = 2(1+(21)) = 23 = 6 Read more502123419Copyright © 2026 LeetCode. All rights reserved.5.9K1863482 Online
@property --beam-angle-_r_30_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_30_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_30_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_30_"][data-active] {
  animation:
    beam-spin-_r_30_ 1.96s linear infinite,
    beam-fade-in-_r_30_ 0.6s ease forwards;
}

[data-beam="_r_30_"][data-fading] {
  animation:
    beam-spin-_r_30_ 1.96s linear infinite,
    beam-fade-out-_r_30_ 0.5s ease forwards;
}

[data-beam="_r_30_"][data-active]::after,
[data-beam="_r_30_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_30_),
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
      from var(--beam-angle-_r_30_),
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
      from var(--beam-angle-_r_30_),
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
  opacity: calc(var(--beam-opacity-_r_30_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_30_"][data-active]::before,
[data-beam="_r_30_"][data-fading]::before {
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
    from var(--beam-angle-_r_30_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_30_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_30_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_30_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_30_),
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

[data-beam="_r_30_"][data-active] [data-beam-bloom],
[data-beam="_r_30_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_30_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_30_ {
  to { --beam-angle-_r_30_: 360deg; }
}

@keyframes beam-fade-in-_r_30_ {
  to { --beam-opacity-_r_30_: 1; }
}

@keyframes beam-fade-out-_r_30_ {
  from { --beam-opacity-_r_30_: 1; }
  to { --beam-opacity-_r_30_: 0; }
}

LeetSort byAllMy SolutionJavaC++Python3CPythonJavaScriptGoRustC#SwiftTypeScriptKotlinRubyScalaPHPMySQLDartRacketStackStringBracket SequencesRecursionMathBit ManipulationIteratorSimulationDivide and ConquerGreedyMonotonic StackDynamic ProgrammingDepth-First SearchArrayCountingTreeQueueLinked ListMemoizationBrainteaserSliding WindowBitmaskOrdered SetTwo PointersMonotonic QueueHash TableSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Jun 24, 2018Score of ParenthesesEditorial179140.4K47Irmhild Rupprecht・ Open・13 hours agoDivide and Conquer / Recursion ➠ Stack ➠ Counting Cores ➠ Super EasyStringDivide and ConquerStackGreedy6+10613.7K7Md Aarzoo Islam・ Open・12 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringStackC++Java5+678.4K7Ashok Varma・ Open・9 hours ago✅2 Method's || Stack of Score Boxes | Step by Step GIF Visualization | Java, C++, Python, JSStringStackPythonC++4+743.2K2Muthu Vrn・ Open・12 hours agoGod is Great 484Python3291160NEXUS・ Open・13 hours ago⚡ 0ms | 100% Beats 🚀 — Score of Parentheses | Stack Magic for Nested Scores 🧠🔥StringStackPythonC++5+261.7K2An-Wen Deng・ Open・14 hours agoGreedy branchless loop|beats 100%GreedyBitmaskC++Python31+165923Dhanush Rajulapati・ Open・14 hours agoStack Solution | Java, Python, C++, JavaScript | O(n) Time | O(n) SpaceStringStackPythonC++3+152K3Rohitttt・ Open・14 hours ago🔥 🚀  0ms Beats 100% Runtime & 95.79% Memory | O(1) Space Depth Counting ⚡ 💡StringStackC++Bracket Sequences121.3K6TCZON・ Open・14 hours ago🚀 Optimal Approach | 🎯 0ms | Beats 100% | ✅ Easy solution | 🔥 2-Line SolutionStackPythonC++Java5+98791Aryan Kumar Shaw Halwai・ Open・12 hours agoGreedy Approach🔥| Beats 100 %✅ | No BS + Easy Solution 💯StringStackPythonC++3+82090Adityaraj210711・ Open・12 hours agoBeats 100% in O(n)💪🏻C++42171MikPosp・ Open・4 hours ago✅ One Line SolutionStringPythonPython3Bracket Sequences41220Manjeet Dhayal・ Open・8 hours agoObservation | Stack | Track score at each level StackMonotonic StackJava4830AATHTHI PANDI・ Open・9 hours agoSimple O(n) Python Solution | Replace "()" with 1 | Depth Multiplier, No StackPython341120All Solutions0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Md Aarzoo Islam8.4K12 hours agoStringStackC++Java5+

Approach

Start with score = 0 and depth = 0.
Go through the string from left to right.

( → increase depth.
) → decrease depth.


After seeing ), check whether the previous character was (.

If yes, we found ().
Add 2^depth to score.


Return score.

Here, 1 << depth is simply another way to calculate 2^depth.

Code
C++JavaJavaScriptTypeScriptPython3goclass Solution {
    public int scoreOfParentheses(String s) {
        int score = 0, depth = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                ++depth;
            } else {
                --depth;
                if (s.charAt(i - 1) == '(') {
                    score += 1 << depth;
                }
            }
        }
        return score;
    }
}

 PreviousDivide and Conquer / Recursion ➠ Stack ➠ Counting Cores ➠ Super EasyNext✅2 Method's || Stack of Score Boxes | Step by Step GIF Visualization | Java, C++, Python, JSComments (7)Sort by:BestCommentMd Aarzoo Islam12 hours agoComplexity
Time Complexity: O(n) where n is the length of the string, because I examine each character exactly once.
Space Complexity: O(1) because I only use a handful of integer variables and never allocate any extra data structures. Read more8keshav_jha8 hours agointeresting the way you handled 2^depth Read more2stasf2537 minutes agoCOOL !!!
7 lines: simplest stack Read more1Maria4 hours agoOne line solution for this task Read more1Uyu Milk2 hours agoIt didn't really explain why it works. thanks anyway Read more0Ramakrishna8 hours agonice Read more0Irmhild Rupprecht11 hours ago3 Approach => https://leetcode.com/problems/score-of-parentheses/solutions/8556204/1-by-flerkeen-2mdi Read more01677JavaAuto45678910111213141516        for (int i = 0; i < s.length(); ++i) {            if (s.charAt(i) == '(') {                ++depth;            } else {                --depth;                if (s.charAt(i - 1) == '(') {                    score += 1 << depth;                }            }        }        return score;    }}SavedLn 16, Col 2AcceptedRuntime: 0 msCase 1Case 2Case 3Inputs ="()"Output1Expected1Contribute a testcaseInput9123›"()""(())""()()"Output9123›122Expected9123›122 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 05, 2026 19:45AnalysisSolutionCodeJava1class Solution {
2    public int scoreOfParentheses(String s) {
3        int score = 0, depth = 0;
4        for (int i = 0; i < s.length(); ++i) {
5            if (s.charAt(i) == '(') {
6                ++depth;
7            } else {
8                --depth;
9                if (s.charAt(i - 1) == '(') {
10                    score += 1 << depth;
11                }
12            }
13        }
14        return score;
15    }
16}View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize
- **Memory:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result856. Score of ParenthesesMediumTopicsCompaniesGiven a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:


	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.


 
Example 1:

Input: s = "()"
Output: 1


Example 2:

Input: s = "(())"
Output: 2


Example 3:

Input: s = "()()"
Output: 2


 
Constraints:


	2 <= s.length <= 50
	s consists of only '(' and ')'.
	s is a balanced parentheses string.

 Seen this question in a real interview before?1/6YesNoAccepted290,677/450.2KAcceptance Rate64.6%TopicsStaffStringStackBracket SequencesWeekly Contest 90CompaniesDiscussion (186)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:Bestnpestov9Mar 13, 2024what are these example test cases???? Could you have picked any worse ones Read more1756eunice16 hours ago Read more13511Eddie LAug 24, 2024These examples are absolute garbage. Read more156Akash_ChitaleAug 12, 2025Test Cases -------------->
If you find these test cases helpful, an upvote would be appreciated.
"((()()()))"
"(()(()))"
"()()()()()()()(((())))"
"((((((()))((()))))))"
"(()()(((())(((()))))))"
"(((((((((()()()))))((((())))))(((((((())))))))))))"
UPVOTE Read more1821user6982nzJul 02, 2023What does "AB" has score of A + B mean? Read more651Veron Nica14 hours agoWho would have thought it's another parenthesis problem
🤔🤔 Read more501Mohit SainiAug 09, 2025Guys try hard.
If I can then you definitely can solve this.
We will use stack. And we compute something and push back to the stack. Read moreTip416chirag c14 hours agoAt this point its too much parentheses Read more391David YeeJul 20, 2023I don't think the description is explained well... why is the output expected to be 6 instead of 8 when s = "(()(()))"? Read more2610Amrutham MohanJun 03, 2024because () = 1, so (()) = 21 and AB = A+B
Here ()(()) = 1 + 2 = 3
Finally (()(())) = 2(1+(21)) = 23 = 6 Read more502123419Copyright © 2026 LeetCode. All rights reserved.5.9K1863482 Online
@property --beam-angle-_r_30_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_30_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_30_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_30_"][data-active] {
  animation:
    beam-spin-_r_30_ 1.96s linear infinite,
    beam-fade-in-_r_30_ 0.6s ease forwards;
}

[data-beam="_r_30_"][data-fading] {
  animation:
    beam-spin-_r_30_ 1.96s linear infinite,
    beam-fade-out-_r_30_ 0.5s ease forwards;
}

[data-beam="_r_30_"][data-active]::after,
[data-beam="_r_30_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_30_),
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
      from var(--beam-angle-_r_30_),
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
      from var(--beam-angle-_r_30_),
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
  opacity: calc(var(--beam-opacity-_r_30_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_30_"][data-active]::before,
[data-beam="_r_30_"][data-fading]::before {
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
    from var(--beam-angle-_r_30_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_30_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_30_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_30_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_30_),
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

[data-beam="_r_30_"][data-active] [data-beam-bloom],
[data-beam="_r_30_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_30_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_30_ {
  to { --beam-angle-_r_30_: 360deg; }
}

@keyframes beam-fade-in-_r_30_ {
  to { --beam-opacity-_r_30_: 1; }
}

@keyframes beam-fade-out-_r_30_ {
  from { --beam-opacity-_r_30_: 1; }
  to { --beam-opacity-_r_30_: 0; }
}

LeetSort byAllMy SolutionJavaC++Python3CPythonJavaScriptGoRustC#SwiftTypeScriptKotlinRubyScalaPHPMySQLDartRacketStackStringBracket SequencesRecursionMathBit ManipulationIteratorSimulationDivide and ConquerGreedyMonotonic StackDynamic ProgrammingDepth-First SearchArrayCountingTreeQueueLinked ListMemoizationBrainteaserSliding WindowBitmaskOrdered SetTwo PointersMonotonic QueueHash TableSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Jun 24, 2018Score of ParenthesesEditorial179140.4K47Irmhild Rupprecht・ Open・13 hours agoDivide and Conquer / Recursion ➠ Stack ➠ Counting Cores ➠ Super EasyStringDivide and ConquerStackGreedy6+10613.7K7Md Aarzoo Islam・ Open・12 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringStackC++Java5+678.4K7Ashok Varma・ Open・9 hours ago✅2 Method's || Stack of Score Boxes | Step by Step GIF Visualization | Java, C++, Python, JSStringStackPythonC++4+743.2K2Muthu Vrn・ Open・12 hours agoGod is Great 484Python3291160NEXUS・ Open・13 hours ago⚡ 0ms | 100% Beats 🚀 — Score of Parentheses | Stack Magic for Nested Scores 🧠🔥StringStackPythonC++5+261.7K2An-Wen Deng・ Open・14 hours agoGreedy branchless loop|beats 100%GreedyBitmaskC++Python31+165923Dhanush Rajulapati・ Open・14 hours agoStack Solution | Java, Python, C++, JavaScript | O(n) Time | O(n) SpaceStringStackPythonC++3+152K3Rohitttt・ Open・14 hours ago🔥 🚀  0ms Beats 100% Runtime & 95.79% Memory | O(1) Space Depth Counting ⚡ 💡StringStackC++Bracket Sequences121.3K6TCZON・ Open・14 hours ago🚀 Optimal Approach | 🎯 0ms | Beats 100% | ✅ Easy solution | 🔥 2-Line SolutionStackPythonC++Java5+98791Aryan Kumar Shaw Halwai・ Open・12 hours agoGreedy Approach🔥| Beats 100 %✅ | No BS + Easy Solution 💯StringStackPythonC++3+82090Adityaraj210711・ Open・12 hours agoBeats 100% in O(n)💪🏻C++42171MikPosp・ Open・4 hours ago✅ One Line SolutionStringPythonPython3Bracket Sequences41220Manjeet Dhayal・ Open・8 hours agoObservation | Stack | Track score at each level StackMonotonic StackJava4830AATHTHI PANDI・ Open・9 hours agoSimple O(n) Python Solution | Replace "()" with 1 | Depth Multiplier, No StackPython341120All Solutions0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Md Aarzoo Islam8.4K12 hours agoStringStackC++Java5+

Approach

Start with score = 0 and depth = 0.
Go through the string from left to right.

( → increase depth.
) → decrease depth.


After seeing ), check whether the previous character was (.

If yes, we found ().
Add 2^depth to score.


Return score.

Here, 1 << depth is simply another way to calculate 2^depth.

Code
C++JavaJavaScriptTypeScriptPython3goclass Solution {
    public int scoreOfParentheses(String s) {
        int score = 0, depth = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                ++depth;
            } else {
                --depth;
                if (s.charAt(i - 1) == '(') {
                    score += 1 << depth;
                }
            }
        }
        return score;
    }
}

 PreviousDivide and Conquer / Recursion ➠ Stack ➠ Counting Cores ➠ Super EasyNext✅2 Method's || Stack of Score Boxes | Step by Step GIF Visualization | Java, C++, Python, JSComments (7)Sort by:BestCommentMd Aarzoo Islam12 hours agoComplexity
Time Complexity: O(n) where n is the length of the string, because I examine each character exactly once.
Space Complexity: O(1) because I only use a handful of integer variables and never allocate any extra data structures. Read more8keshav_jha8 hours agointeresting the way you handled 2^depth Read more2stasf2537 minutes agoCOOL !!!
7 lines: simplest stack Read more1Maria4 hours agoOne line solution for this task Read more1Uyu Milk2 hours agoIt didn't really explain why it works. thanks anyway Read more0Ramakrishna8 hours agonice Read more0Irmhild Rupprecht11 hours ago3 Approach => https://leetcode.com/problems/score-of-parentheses/solutions/8556204/1-by-flerkeen-2mdi Read more01677JavaAuto45678910111213141516        for (int i = 0; i < s.length(); ++i) {            if (s.charAt(i) == '(') {                ++depth;            } else {                --depth;                if (s.charAt(i - 1) == '(') {                    score += 1 << depth;                }            }        }        return score;    }}SavedLn 16, Col 2AcceptedRuntime: 0 msCase 1Case 2Case 3Inputs ="()"Output1Expected1Contribute a testcaseInput9123›"()""(())""()()"Output9123›122Expected9123›122 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 05, 2026 19:45AnalysisSolutionCodeJava1class Solution {
2    public int scoreOfParentheses(String s) {
3        int score = 0, depth = 0;
4        for (int i = 0; i < s.length(); ++i) {
5            if (s.charAt(i) == '(') {
6                ++depth;
7            } else {
8                --depth;
9                if (s.charAt(i - 1) == '(') {
10                    score += 1 << depth;
11                }
12            }
13        }
14        return score;
15    }
16}View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
