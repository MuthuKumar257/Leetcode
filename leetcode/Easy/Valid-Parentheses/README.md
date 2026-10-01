# 20. Valid Parentheses

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit200:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result20. Valid ParenthesesSolvedEasyTopicsCompaniesHintGiven a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:


	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.


 
Example 1:


Input: s = "()"

Output: true


Example 2:


Input: s = "()[]{}"

Output: true


Example 3:


Input: s = "(]"

Output: false


Example 4:


Input: s = "([])"

Output: true


Example 5:


Input: s = "([)]"

Output: false


 
Constraints:


	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

 Seen this question in a real interview before?1/6YesNoAccepted8,228,477/18.3MAcceptance Rate45.0%TopicsStringStackBracket SequencesCompaniesHint 1Use a stack of characters.Hint 2When you encounter an opening bracket, push it to the top of the stack.Hint 3When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.Similar QuestionsGenerate ParenthesesMediumLongest Valid ParenthesesHardRemove Invalid ParenthesesHardCheck If Word Is Valid After SubstitutionsMediumCheck if a Parentheses String Can Be ValidMediumMove Pieces to Obtain a StringMediumDiscussion (740)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestsunwangshuAug 02, 2017The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
From this problem description I cannot guess if [()]{} is valid or not.
But clearly from the answer it is valid.
Then I think the problem description should be updated. Read more2.4K40bryMay 27, 2019It's a really good problem. But I don't think it's appropriate to call it Easy. If you've never had a question like this before, and if you're new to python and programming - which is my guess the target audiance for easy questions - it's a little difficult. Read more79526tonybrasunasJun 05, 2017The description for this one should say ([]{}) is valid too. Otherwise it's not clear that validating nested parentheses is part of the requirements. Read more80113Saksham MaitriDec 03, 2023either i am dumb af or this is not easy Read more38812AlexApr 27, 2023Here is some tip:
The first line of the function uses a guard statement to check if the length of the input string is even. If the length is odd, the function returns false because it means that the brackets are not properly balanced.
The next line creates an empty stack of characters to store the opening brackets.
The function then loops through each character item in the input string s.
For each character item, the code checks whether it is an opening bracket: (, [, or {. If it is, the corresponding closing bracket is pushed onto the stack. For example, if the character is (, the character ) is pushed onto the stack.
If the character is a closing bracket: ), ], or }, the code checks whether the stack is empty. If the stack is empty, it means that there is no opening bracket to match the closing bracket, so the function returns false. If the stack is not empty, the last opening bracket is removed from the stack and checked against the current closing bracket. If the brackets do not match, the function returns false.
After looping through all the characters in the input string, the function checks whether the stack is empty. If it is, it means that all the opening brackets have been matched with their corresponding closing brackets, so the function returns true. If the stack is not empty, it means that there are unmatched opening brackets, so the function returns false. Read moreTip27514tryhard00Oct 13, 2022This problem could be considered easy but only if you realized the crux of it. If you tried to do it using pure conditionals, which I did for the first 3 hours, you're in for a very bad time. I finally gave up on conditionals when it had a nested within nested case. I was about to go 3d array to store each set but it was so logically complex I almost quit. Then I saw it. So this problem could considered medium if you didn't see the easy answer. Overall, a very clever question. It had so many caveats that I kept getting rejected and it was giving me pstd by the end. lol. For those who are stuck, the hint is what goes in last must come out first. Read more25518Alexander AkhilchenokJun 06, 2023Description is not good enough. Should be shown some more test cases as "( [ ) ]", because "Open brackets must be closed in the correct order" could be missunderstood. Read more1579Uday SinghNov 02, 2017I was asked to do this in o(1) memory in an interview! Anyone knows how to do that? Read more5332RamJan 01, 2021whats wrong with this TC "{[]}" in custom test cases run it succeed but it fails on submission.
" Read moreRead more5211raja shekar davalgariFeb 09, 2020for the string '(]' my code is working fine with python 3.7, but here its showing wrong output Read more4812123475Copyright © 2026 LeetCode. All rights reserved.28.6K7401571 Online
@property --beam-angle-_r_7g_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7g_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7g_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7g_"][data-active] {
  animation:
    beam-spin-_r_7g_ 1.96s linear infinite,
    beam-fade-in-_r_7g_ 0.6s ease forwards;
}

[data-beam="_r_7g_"][data-fading] {
  animation:
    beam-spin-_r_7g_ 1.96s linear infinite,
    beam-fade-out-_r_7g_ 0.5s ease forwards;
}

[data-beam="_r_7g_"][data-active]::after,
[data-beam="_r_7g_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7g_),
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
      from var(--beam-angle-_r_7g_),
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
      from var(--beam-angle-_r_7g_),
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
  opacity: calc(var(--beam-opacity-_r_7g_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7g_"][data-active]::before,
[data-beam="_r_7g_"][data-fading]::before {
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
    from var(--beam-angle-_r_7g_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7g_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7g_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7g_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7g_),
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

[data-beam="_r_7g_"][data-active] [data-beam-bloom],
[data-beam="_r_7g_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7g_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7g_ {
  to { --beam-angle-_r_7g_: 360deg; }
}

@keyframes beam-fade-in-_r_7g_ {
  to { --beam-opacity-_r_7g_: 1; }
}

@keyframes beam-fade-out-_r_7g_ {
  from { --beam-opacity-_r_7g_: 1; }
  to { --beam-opacity-_r_7g_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++JavaScriptPythonCC#GoTypeScriptSwiftKotlinRustPHPDartRubyScalaElixirRacketErlangMySQLHTMLPython MLStackStringHash TableArrayBracket SequencesQueueRecursionString MatchingIteratorOrdered MapLinked ListMonotonic StackMathDynamic ProgrammingTwo PointersHash FunctionBacktrackingOrdered SetGreedySimulationBinary SearchCombinatoricsDivide and ConquerBit ManipulationCountingSortingDesignBrainteaserSliding WindowEnumerationShortest PathMemoizationPersistent Data StructureDoubly-Linked ListBitmaskHeap (Priority Queue)Binary TreeGraph TheoryMonotonic QueueBreadth-First SearchProbability and StatisticsYour last submission beat 13% of other submissions' runtime.Share my solutionLeetCode・ Open・Jun 02, 2021Valid ParenthesesEditorial3371.4M474TripleTTT・ Open・3 hours agoIn-Place Stack with ASCII Bit Manipulation ||  O(1) SPACE || In-place C++StringStackC++Java1+179765Md Aarzoo Islam・ Open・an hour ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringStackC++Java5+113842An-Wen Deng・ Open・3 hours agoStack with an unordered_map/function|beats 100%StackHash FunctionC++Bracket Sequences81355Ashok Varma・ Open・Sep 25, 2026🎯 Beginner Friendly | Step-by-Step Visualization 🔍 | Stack (Java/C++/Python/C/JS) ✅StringStackPythonC++4+342K3Aryan Kumar Shaw Halwai・ Open・an hour agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Simple StackStringStackPythonC++3+5420TCZON・ Open・3 hours ago🚀 Brute Force → Optimal Approach | One-liner solution | Easy Solution | 0ms | Beats 100% ✅🔥StringStackPythonC++6+51050Dhanush Rajulapati・ Open・3 hours agoStack Solution | Java, Python, C++, JavaScript | O(n) Time | O(n) SpaceStringStackPythonC++3+4801Shakti Pravesh・ Open・2 hours agoJava | C++ | C | Python | Stack + HashMap | Easy Explanation | O(n) Time, O(n) SpaceStringStackCPython4+4120niits・ Open・Sep 07, 2026【Video】2 ways to solve this questionStringStackC++Java1+985.9K2Aishwarya・ Open・Aug 22, 2025100% Beats 0ms || Stack || Beginner Friendly || Python || Java || C++StringStackC++Java1+1.3K155.3K28EdgeCaseOffByOne・ Open・11 minutes agoEasy Solution With Video Explanation Do Like and Subscribe our ChannelStringStackC++Bracket Sequences450DHRUVIK・ Open・33 minutes agoSimple Stack ApproachC++380o_o・ Open・2 hours ago✅ 1-Line Solution Explained | 100%StringStackTypeScriptPython32+2452chaharharsh67・ Open・5 minutes agoVery Easy Solution Using StackJava230All SolutionsBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Simple StackAryan Kumar Shaw Halwai42an hour agoStringStackPythonC++3+Intuition

Whenever an opening bracket appears, its closing bracket is already known.
So instead of storing ( , { , or [ , store the closing bracket we expect. For example, if ( comes in, put ) into the stack.
When a closing bracket appears, it must match the bracket on top of the stack. If it doesn't match, the string is invalid.
At the end, the stack must be empty. That means every opening bracket found its correct closing bracket.
The even-length check is just a quick way to reject strings that can never be valid.
Approach

First, check whether the length of the string is odd. A valid parentheses string always has pairs, so an odd length can immediately return false.
Use an array as a stack.
For every character:

( → push )
{ → push }
[ → push ]
For a closing bracket, check whether it matches the bracket currently at the top of the stack.
If the stack is empty or the brackets don't match, return false.

After processing the whole string, return true only if the stack is empty.
The useful part of this implementation is that it doesn't need to store the opening bracket at all — it directly stores what closing bracket is expected.
Complexity

Time complexity:


O(n)

Space complexity:


O(n)
Code
JavaC++PythonJavaScriptclass Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        stack = [''] * len(s)
        head = 0

        for c in s:
            if c == '(':
                stack[head] = ')'
                head += 1
            elif c == '{':
                stack[head] = '}'
                head += 1
            elif c == '[':
                stack[head] = ']'
                head += 1
            else:
                if head == 0:
                    return False

                head -= 1

                if stack[head] != c:
                    return False

        return head == 0 Previous🎯 Beginner Friendly | Step-by-Step Visualization 🔍 | Stack (Java/C++/Python/C/JS) ✅Next🚀 Brute Force → Optimal Approach | One-liner solution | Easy Solution | 0ms | Beats 100% ✅🔥Comments (0)Sort by:BestCommentNo comments yet.50Python3Auto16171819202122232425262728            elif c == '[':                stack[head] = ']'                head += 1            else:                if head == 0:                    return False                head -= 1                if stack[head] != c:                    return False        return head == 0SavedLn 28, Col 25AcceptedRuntime: 0 msCase 1Case 2Case 3Case 4Case 5Inputs ="()"OutputtrueExpectedtrueContribute a testcaseInput912345›"()""()[]{}""(]""([])""([)]"Output912345›truetruefalsetruefalseExpected912345›truetruefalsetruefalse All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 01, 2026 08:57AnalysisSolutionCodePython31class Solution:
2    def isValid(self, s):
3        if len(s) % 2 != 0:
4            return False
5
6        stack = [''] * len(s)
7        head = 0
8
9        for c in s:
10            if c == '(':
11                stack[head] = ')'
12                head += 1
13            elif c == '{':
14                stack[head] = '}'
15                head += 1
16            elif c == '[':
17                stack[head] = ']'
18                head += 1
19            else:
20                if head == 0:
21                    return False
22
23                head -= 1
24
25                if stack[head] != c:
26                    return False
27
28        return head == 0View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
