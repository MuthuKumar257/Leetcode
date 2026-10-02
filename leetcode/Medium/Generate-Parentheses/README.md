# 22. Generate Parentheses

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit300:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result22. Generate ParenthesesMediumTopicsCompaniesGiven n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:


	1 <= n <= 8

 Seen this question in a real interview before?1/6YesNoAccepted3,138,881/4MAcceptance Rate79.3%TopicsStringDynamic ProgrammingBacktrackingBracket SequencesCompaniesSimilar QuestionsLetter Combinations of a Phone NumberMediumValid ParenthesesEasyCheck if a Parentheses String Can Be ValidMediumDiscussion (306)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:Besttejavenkat lankaSep 04, 2020click for view
[https://embed.creately.com/cclS6u7Upy3?type=svg]
left path represent possible one parentheses and right represent possible of right parentheses.
leaf node contains answer.
hope it will help. Read moreRead more97129Bonson ZhengAug 25, 2018Using different implmentation,the elements will be in different orders. e.g. n = 3.
It can be
["((()))","(())()","()(())","(()())","()()()"]
while the expected answer is
["((()))","(()())","(())()","()(())","()()()"]
Both are correct answers. However, the difference of ordering is reckoned as "wrong answer". Read more42416Chirag RajputJul 22, 2023Draw the recursive tree and think about the conditions when an opening/closing bracket can be appended
     (
    / \
   ((  ()
  / \   |
((( (() ()(
 .   .   .
 .   .   .
... and so on Read moreTip2007khanuja05Apr 14, 2017My solution generates the same set of outputs but the ordering is different. The question should be edited and they should mention that the order matters. Read more2088Anton RomanenkoAug 30, 2023To solve this problem, you can use a recursive approach. Here's how you can approach the task and put your mind in the right direction:


Base Case: Start by identifying the base case. When n is 0, there's only one possible combination: an empty string.


Recursive Case: For each pair of parentheses, you have two options: open a new parenthesis or close an existing open parenthesis. So, you'll recursively generate combinations by trying both options for each parenthesis.


Recursion with Backtracking: Use recursion to explore all possibilities. When adding an open parenthesis, decrement n by 1 to indicate that one opening parenthesis has been used. When adding a closing parenthesis, make sure there's a matching open parenthesis available (meaning n hasn't reached 0 yet).


Build and Return the Combinations: As you explore the possibilities, build and store the combinations in a list. Once you've exhausted all possibilities for a given state, return the list of combinations.


Edge Cases: Handle edge cases like if n is negative or zero, and set up the initial call to the recursive function.


In terms of algorithm, the key idea is to generate all possible combinations while ensuring that they're well-formed parentheses. The recursive approach allows you to explore these combinations in a structured manner. Remember to think about the base case, the recursive cases, and how to build and return the combinations as you traverse the recursion tree.
In terms of implementation, you can create a recursive function that takes parameters such as the current combination being built, the remaining open and close parentheses, and the list to store combinations. Each recursive call will decide whether to add an open or close parenthesis, and the parameters will be updated accordingly.
Remember that recursive problems often involve thinking about how to break down the problem into smaller, more manageable subproblems, and how to combine the results of those subproblems to get the final solution. Read more1027AbdullahiSep 11, 2023I feel so happy that i was able to solve this problem. This is the first backtracking I solved by myself. I feel more motivated to tackle others now Read more861Changjin LeeSep 23, 2020I solved this problem with 60m/s by generating permutations with duplicates and for each permutation result I used stack to check if it's valid parenthesis and now I came here and ppl post simple/mind-blowing solutions that I never expected and A LOT OF people be like "yeahnice solutioni thought kinda the same way~". WTH!!!!!
I started algorithm roughly 3 months ago and I've been studying 12-14 hrs a day til now and solved probably 200 questions so far. I'm kinda confident in BFS DFS DP and some general algorithm but totally new to combinatorics. What should I focus more on? I haven't studied Greedy yet. Can you guys recommend me how I study Greedy? cuz its so vague I've looked up so much
Bless to y'all

Non-smart Asian sophomore kid-
 Read more907panwu5588Apr 10, 2018BAD test cases. The order should not matter.
For example, the following should be the same:
["(())","()()"]
["()()","(())"] Read more1033andy_r_sJul 27, 2018For n = 4 is following one of the valid combinations?
(())(())
My code has this but the leetcode says it's not valid. I don't understand why is it invalid? Read more604kistch6 hours ago
 Read more31123431Copyright © 2026 LeetCode. All rights reserved.23.7K306
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

LeetSort byAllMy SolutionPython3C++JavaPythonCJavaScriptGoC#TypeScriptSwiftRustKotlinRubyScalaPHPDartElixirRacketMySQLErlangBacktrackingRecursionStringDynamic ProgrammingDepth-First SearchStackIteratorBreadth-First SearchArrayBracket SequencesCombinatoricsMemoizationQueueTreeMathBit ManipulationBitmaskOrdered SetString MatchingGreedyHash TableDivide and ConquerTwo PointersBinary TreeBrainteaserSortingSimulationBinary SearchDesignBinary Search TreeGraph TheoryProbability and StatisticsCountingSuffix ArrayMinimum Spanning TreeLinked ListEnumerationTrieRandomizedMatrixSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Aug 19, 2023Generate ParenthesesEditorial80287.3K68eunice・ Open・5 hours agoBacktracking || Bitmasking + ASCII Tricks || No Precomputation ||  Beats 100%StringDynamic ProgrammingBacktrackingDepth-First Search5+281.3K0Md Aarzoo Islam・ Open・2 hours ago2ms | Beats 79.44% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringDynamic ProgrammingBacktrackingC++6+125521Vaibhav Raj Singh・ Open・3 hours agoEasy Backtrack SolutionBacktrackingC++128150TCZON・ Open・3 hours ago🚀 Optimal Approach | ✅ 0ms | Beats 100% | Easy solution | Beginner Friendly | 💯 One-line solutionStringDynamic ProgrammingBacktrackingC++6+74781An-Wen Deng・ Open・3 hours agoDFS+Backtracking with Notes on Catalan Numbers||beats 100%BacktrackingDepth-First SearchCombinatoricsC++1+6892Dhanush Rajulapati・ Open・4 hours agoBacktracking Solution [Java, Python, C++, JavaScript]StringBacktrackingPythonC++2+54431NEXUS・ Open・an hour ago⚡ 0ms | 100% Beats 🚀 — Generate Parentheses  | Clean Backtracking Solution 🧩StringPythonC++Java2+5520Aryan Kumar Shaw Halwai・ Open・2 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 |BacktrackingStringDynamic ProgrammingBacktrackingPython4+4420Shakti Pravesh・ Open・2 hours agoDynamic Programming using Catalan RecurrenceStringDynamic ProgrammingBacktrackingC5+4510Kostiantyn Lazukin・ Open・3 hours agoC++ PrecomputeC++3443Jordinario・ Open・3 hours agoO(4^n / sqrt(n)), optimal iterative solutionStringCombinatoricsGo2343rc_dominator・ Open・4 hours ago0 ms | | Backtracking | | C++ | | StringStringBacktrackingC++Bracket Sequences2700Yuvaraj・ Open・Sep 07, 2022Python, Java w/ Explanation | Faster than 96% w/ Proof | Easy to UnderstandBacktrackingDepth-First SearchRecursionPython2+2.3K274.3K81Prabhas Sharma・ Open・an hour ago22. Generate ParenthesesPython31251All SolutionsBacktracking Solution [Java, Python, C++, JavaScript]Dhanush Rajulapati4434 hours agoStringBacktrackingPythonC++2+Intuition
Generate parentheses step by step while maintaining two counts:

open → number of ( used
close → number of ) used

We can add ( as long as open < n.
We can add ) only when close < open, ensuring that no prefix becomes invalid.
Approach
1️⃣ Start with an Empty String
Call the recursive function with open = 0 and close = 0.
2️⃣ Add Opening Parenthesis
If open < n, add ( and increase open.
3️⃣ Add Closing Parenthesis
If close < open, add ) and increase close.
4️⃣ Store Valid String
When the string length becomes 2 * n, add it to the result.
Complexity


Time complexity:

O(4n/√n) --> proportional to the number of valid combinations (Catalan numbers).



Space complexity:

O(n) --> recursion depth, excluding the output.



Code
JavaJavaScriptPythonC++class Solution {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<>();

        getParanthesis(0,0,"",n,res);
        return res;
    }
    static void getParanthesis(int open,int close,String s,int n,ArrayList<String> res)
    {
        if(s.length() == 2*n)
        {
            res.add(s);
        }
        if(open < n)
        {
            getParanthesis(open+1,close,s+"(",n,res);
        }
        if(close < open)
        {
            getParanthesis(open,close+1,s+")",n,res);
        }
    }
}
 PreviousDFS+Backtracking with Notes on Catalan Numbers||beats 100%Next⚡ 0ms | 100% Beats 🚀 — Generate Parentheses  | Clean Backtracking Solution 🧩Comments (1)Sort by:BestCommentDhanush Rajulapati4 hours agoPlease leave any suggestions or improvements in the comments below
Have a nice day Read more4151Python3Auto78910111213141516171819        res = []        self.getParenthesis(0, 0, "", n, res)        return res    def getParenthesis(self, open, close, s, n, res):        if len(s) == 2 * n:            res.append(s)        if open < n:            self.getParenthesis(open + 1, close, s + "(", n, res)        if close < open:            self.getParenthesis(open, close + 1, s + ")", n, res)SavedLn 19, Col 66AcceptedRuntime: 0 msCase 1Case 2Inputn =3Output["((()))","(()())","(())()","()(())","()()()"]Expected["((()))","(()())","(())()","()(())","()()()"]Contribute a testcaseInput912›31Output912›["((()))","(()())","(())()","()(())","()()()"]["()"]Expected912›["((()))","(()())","(())()","()(())","()()()"]["()"] All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 02, 2026 09:26AnalysisSolutionCodePython31class Solution(object):
2    def generateParenthesis(self, n):
3        """
4        :type n: int
5        :rtype: List[str]
6        """
7        res = []
8        self.getParenthesis(0, 0, "", n, res)
9        return res
10
11    def getParenthesis(self, open, close, s, n, res):
12        if len(s) == 2 * n:
13            res.append(s)
14
15        if open < n:
16            self.getParenthesis(open + 1, close, s + "(", n, res)
17
18        if close < open:
19            self.getParenthesis(open, close + 1, s + ")", n, res)View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
