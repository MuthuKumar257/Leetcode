# 32. Longest Valid Parentheses

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit400:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result32. Longest Valid ParenthesesSolvedHardTopicsCompaniesGiven a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".


Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".


Example 3:

Input: s = ""
Output: 0


 
Constraints:


	0 <= s.length <= 3 * 104
	s[i] is '(', or ')'.

 Seen this question in a real interview before?1/6YesNoAccepted1,225,767/3MAcceptance Rate40.2%TopicsStringDynamic ProgrammingStackBracket SequencesCompaniesSimilar QuestionsValid ParenthesesEasyDiscussion (250)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestPranay_ReddyJun 22, 2025Here you go :
"()(()"
"((("
")))"
"()()()"
"(()()())()()))()()(((()))))"
""
"()(()()"
"())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))("
Do upvote to make it more visible! Read more2371ReubenAug 22, 2023When I see parentheses, I think of stack. Read more1792AditiJun 08, 2025Sending a little hate to the person who added "()(()". Read more2128dj_ios1988Oct 13, 2018from the description:
Input: "(()"
Output: 2
and in the testcase
Input: “"()(()"”
Output: 4
Expected :2
why these two have diferent answer of "(()" ? Read more10214Vinoth NJul 20, 2024This question is asked in Zoho interview round 2 during July 2024 college placements. Read more1302Muzahid HussainJul 01, 2025This question was asked during Round 2 of the Microsoft SDE Intern interview for the 2025 summer internship. Read more904euniceFeb 04, 2025 Read more512Pulkit MittalJan 15, 2025This question was asked in VISA interview in Jan 2025 Read more36viocostDec 07, 2018The description only shows example with ()() sequences being correct.
How about this: (()()) or this ((()(())))? Are they correct? Read more416av9ashMay 27, 2018()(() how is this the longest valid parentheses? Answer is 4 I think its 2
Can someone please explain Read more3610123426Copyright © 2026 LeetCode. All rights reserved.13.6K2503570 Online
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

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoC#RustTypeScriptPHPKotlinSwiftRubyScalaDartElixirMS SQL ServerStackStringDynamic ProgrammingBracket SequencesTwo PointersArrayGreedyMonotonic StackRecursionMathSliding WindowSortingIteratorCountingQueueString MatchingMemoizationDepth-First SearchHash TableBacktrackingDivide and ConquerPrefix SumLinked ListBinary SearchBit ManipulationBrainteaserTreeSimulationDoubly-Linked ListEnumerationOrdered MapYour last submission beat 75% of other submissions' runtime.Share my solutionLeetCode・ Open・Dec 23, 2016Longest Valid ParenthesesEditorial573621.1K256Ashok Varma・ Open・6 hours agoStack of Indexes | Easy Intuition | Step by Step GIF Visualization | Java, C++, Python, JSStringDynamic ProgrammingStackPython5+733.4K4eunice・ Open・8 hours agoStack + Two Pass Counting | Parentheses Matching | Linear Time | with O(1) SpaceStringStackPythonC++4+726.3K6TCZON・ Open・7 hours ago🚀 Optimal Approach | 🎯 0ms | Beats 100% | ✅ Easy solution | 💯 Three-Line SolutionStringStackPythonC++6+151.6K4An-Wen Deng・ Open・7 hours agostack+DP|beats 100%Dynamic ProgrammingStackC++Bracket Sequences148406Pratulssingh・ Open・an hour agoA Unique SolutionTwo PointersC++Bracket Sequences10419Md Aarzoo Islam・ Open・5 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringDynamic ProgrammingStackC++6+126212NEXUS・ Open・4 hours ago⚡ 0ms | 100% Beats 🚀 — Longest Valid Parentheses | Optimized Two-Pass O(1) Space SolutionStringDynamic ProgrammingPythonC++4+81150Dhanush Rajulapati・ Open・7 hours agoStack Solution | Java, Python, C++, JavaScript | O(n) Time | O(n) SpaceStringStackPythonC++2+73081Aryan Kumar Shaw Halwai・ Open・5 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | StackStringDynamic ProgrammingStackPython4+6610Mayank Jha・ Open・3 hours agoOne Stack, One Pass | The Boundary Trick Behind Longest Valid ParenthesesC++5282Shakti Pravesh・ Open・4 hours agoSimple to Understand | Interview friendly | Beast 100% StringDynamic ProgrammingStackC5+5900Jordinario・ Open・7 hours agoBranchless O(1) space solution in a single loopArrayBit ManipulationGo31102Satyam Singh・ Open・an hour agoTwo-Pass Counter | Forward + Backward Scan | O(1) SpaceArrayStringDivide and ConquerDynamic Programming6+4120Kostiantyn Lazukin・ Open・6 hours agoBranchless O(N) O(1)C++3812All Solutions🚀 Optimal Approach | 🎯 0ms | Beats 100% | ✅ Easy solution | 💯 Three-Line SolutionTCZON1.6K7 hours agoStringStackPythonC++6+Given a string of ( and ), find the length of its longest contiguous valid parentheses substring. A valid substring has matching pairs in the correct order.
For example, in s = "(()", the whole string is incomplete, but the final "()" is valid. The answer is 2.

Concepts used
1. Parentheses balance
While reading a substring from left to right, keep a balance:

Add 1 for (.
Subtract 1 for ).

A substring is valid exactly when its balance finishes at 0 and never becomes negative along the way. A negative balance means a ) appeared without an earlier ( to match it.
2. Starting positions and contiguous substrings
Every possible substring has a starting index. We can try each starting index, extend to the right, and track its balance. This gives a direct baseline: examine all relevant substrings and keep the greatest valid length.
3. Scanning in both directions
A left-to-right scan can find valid stretches using only two counters. If closing parentheses outnumber opening parentheses, no valid substring can cross that point, so the counters reset.
One left-to-right scan is insufficient: in "(()", its extra ( prevents the counters from becoming equal after the "()" suffix. A right-to-left scan handles this opposite case. Together, the two scans find the answer in linear time and constant extra space.

Approach 1: Optimal - Two Directional Counter Scans [No Extra Space]
Intuition
Instead of reconsidering the same characters from every starting index, scan the string once in each direction.
In the left-to-right scan, count opening and closing parentheses. When the counts are equal, the current stretch is valid. When closing parentheses outnumber opening parentheses, reset: that unmatched ) cannot belong to a valid substring crossing it.
This scan can miss a valid suffix hidden behind extra opening parentheses. For "(()", it never reaches equal counts for the final "()". The right-to-left scan solves that case. From this direction, reset when opening parentheses outnumber closing parentheses.
Algorithm

Scan from left to right with open = 0 and close = 0:

Increment the appropriate counter.
If open == close, update the answer with 2 * close.
If close > open, reset both counters.


Reset the counters and scan from right to left:

Increment the appropriate counter.
If open == close, update the answer with 2 * open.
If open > close, reset both counters.


Return the answer.

Why both passes work: A valid substring has equal numbers of ( and ). An excess ) blocks a valid stretch when scanning forward; an excess ( blocks one when scanning backward. Resets discard only stretches that cannot be valid across that blocking character. If extra ( prevents the forward pass from recognizing a valid substring, the backward pass can recognize it after discarding that excess; the symmetric case is covered by the forward pass.
For s = ")()())", the forward pass resets at the first ), then reaches equal counts after "()" and again after "()()". It records 4.
The approach removes the baseline’s repeated scan from every starting position. Each character is visited only twice, and no array or stack is needed.
Code Implementation
C++PythonJavaJavaScriptGoRustclass Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        opening = closing = 0

        for ch in s:
            if ch == "(":
                opening += 1
            else:
                closing += 1

            if opening == closing:
                answer = max(answer, 2 * closing)
            elif closing > opening:
                opening = closing = 0

        opening = closing = 0
        for ch in reversed(s):
            if ch == "(":
                opening += 1
            else:
                closing += 1

            if opening == closing:
                answer = max(answer, 2 * opening)
            elif opening > closing:
                opening = closing = 0

        return answer
Complexity

Time: O(n). Each of the two scans visits every character once, giving 2n visits.
Space: O(1) auxiliary space, excluding the input and output. Only a few counters are stored.
Why this is optimal: Determining the answer requires examining the input characters, so the worst-case time has a lower bound of Ω(n). This approach meets that bound.

For Detailed Analysis - TCZON.
Takeaway: Balance identifies valid parentheses. Scanning in both directions catches valid substrings obscured by unmatched parentheses on either side.

Approach 2: The Altitude Ledger
Imagine ( as one step uphill and ) as one step downhill. Starting at altitude 0, the string becomes a walk through integer heights.
A substring is valid when its walk returns to its starting altitude without ever going below it. This suggests a different question:

At each altitude, how far back can we start and still reach the current position without dipping below that altitude?

Intuition
Keep an earliest position for each altitude. It records the earliest visit to that altitude since the walk last went below it.
If the current position has altitude h, a valid substring can start at an earlier position with altitude h. Using the earliest eligible position gives the longest valid substring ending here.
The unusual part is how little bookkeeping this needs:

On (, we arrive at a higher altitude from below. Any old record at that altitude is unusable, so replace it with the current position.
On ), we leave the old altitude by going below it. Invalidate that altitude’s record. At the new altitude, compare with its earliest eligible position.

Every nonempty valid parentheses substring ends with ), so checking lengths on downward steps is enough.
Example: s = "(()"








































Prefix positionStepAltitudeEarliest eligible position hereBest length0—0001(1102(2203)112
At position 3, the walk returns to altitude 1. Positions 1 through 3 describe the substring "()", so its length is 3 - 1 = 2.
Code Implementation
Altitudes range from -n to n. The implementations use an array of size 2n + 1 and shift each altitude by n to make it a valid array index.
C++PythonJavaJavaScriptGoRustclass Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        vector<int> earliest(2 * n + 1, -1);
        int height = 0;
        int answer = 0;

        earliest[n] = 0;

        for (int position = 1; position <= n; ++position) {
            if (s[position - 1] == '(') {
                ++height;
                earliest[height + n] = position;
            } else {
                earliest[height + n] = -1;
                --height;

                int& start = earliest[height + n];
                if (start == -1) {
                    start = position;
                } else {
                    answer = max(answer, position - start);
                }
            }
        }

        return answer;
    }
};
Complexity

Time: O(n). Each character updates one or two array entries; initializing the array also takes O(n).
Space: O(n) auxiliary space for the altitude ledger, excluding input and output storage.

For Detailed Analysis - TCZON.

Bonus: Three-Line Stack Solution
Keep indices of unmatched ( on a stack. The initial -1 marks the boundary before the string. When a ) arrives, pop once; if the stack becomes empty, that ) becomes the new boundary. Otherwise, the current valid length is the distance to the index on top.
Python
Pythonclass Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, answer = [-1], 0
        for i, ch in enumerate(s): stack.append(i) if ch == '(' else stack.pop(); stack.append(i) if not stack else None; answer = max(answer, i - stack[-1])
        return answer
JavaScript
JavaScript/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
    let stack = [-1],
        answer = 0;
    for (let i = 0; i < s.length; i++) {
        s[i] === "(" ? stack.push(i) : stack.pop();
        if (!stack.length) stack.push(i);
        answer = Math.max(answer, i - stack[stack.length - 1]);
    }
    return answer;
};
Complexity: O(n) time and O(n) auxiliary space, excluding input and output storage. The compact lines perform the same stack steps as a longer implementation; they do not change the algorithm.
 PreviousStack + Two Pass Counting | Parentheses Matching | Linear Time | with O(1) SpaceNextstack+DP|beats 100%Comments (4)Sort by:BestCommentTCZON6 hours agoIf you found this solution helpful, please UPVOTE, FOLLOW, and ADD TO ⭐. Happy Coding, and keep grinding! 🚀 Read more3Jiacheng Gu3 hours agohow this guy gets 26 upvotes with only <300 views? Read moreRead more11Cassie3 hours agoEasiest Code and Explanation https://leetcode.com/problems/longest-valid-parentheses/solutions/8552851/stack-indices-easy-solution-cpp-python-j-v1gs/ Read more11154Python3Auto17181920212223242526272829        opening = closing = 0        for ch in reversed(s):            if ch == "(":                opening += 1            else:                closing += 1            if opening == closing:                answer = max(answer, 2 * opening)            elif opening > closing:                opening = closing = 0        return answerSavedLn 29, Col 22AcceptedRuntime: 0 msCase 1Case 2Case 3Inputs ="(()"Output2Expected2Contribute a testcaseInput9123›"(()"")()())"""Output9123›240Expected9123›240 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 03, 2026 12:30AnalysisSolutionCodePython31class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        answer = 0
4        opening = closing = 0
5
6        for ch in s:
7            if ch == "(":
8                opening += 1
9            else:
10                closing += 1
11
12            if opening == closing:
13                answer = max(answer, 2 * closing)
14            elif closing > opening:
15                opening = closing = 0
16
17        opening = closing = 0
18        for ch in reversed(s):
19            if ch == "(":
20                opening += 1
21            else:
22                closing += 1
23
24            if opening == closing:
25                answer = max(answer, 2 * opening)
26            elif opening > closing:
27                opening = closing = 0
28
29        return answerView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
