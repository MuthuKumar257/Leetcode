# 2267. Check if There Is a Valid Parentheses String Path

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result2267.  Check if There Is a Valid Parentheses String PathHardTopicsCompaniesHintA parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:


	It is ().
	It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
	It can be written as (A), where A is a valid parentheses string.


You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:


	The path starts from the upper left cell (0, 0).
	The path ends at the bottom-right cell (m - 1, n - 1).
	The path only ever moves down or right.
	The resulting parentheses string formed by the path is valid.


Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

 
Example 1:

Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.


Example 2:

Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.


 
Constraints:


	m == grid.length
	n == grid[i].length
	1 <= m, n <= 100
	grid[i][j] is either '(' or ')'.

 Seen this question in a real interview before?1/6YesNoAccepted32,147/68.7KAcceptance Rate46.8%TopicsSenior StaffArrayDynamic ProgrammingMatrixBracket SequencesWeekly Contest 292CompaniesHint 1What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?Hint 2The number of open brackets must always be greater than or equal to the number of close brackets.Hint 3Could you use dynamic programming?Similar QuestionsCheck if There is a Valid Path in a GridMediumCheck if a Parentheses String Can Be ValidMediumDiscussion (41)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestJethroApr 24, 2024An optimization tip: the length of all paths must be equal to m + n - 1, if this number is odd, then the answer must be False. Read moreTip144rilomew8194 hours agoStorm after the calm...

🌩️🌩️🌩️ Read more121bigfatcoderJun 09, 2023This is a classic medium problem. Shouldn't be labelled as hard. Read more194Vikas vermaan hour agoReally fedup off these comments :
"It should be tagged easy or medium"
"We are gonna cooked tomorrow"
"Calm before storm"
"Storm before calm"
mean while me : "Why Tony stark snapped his finger to save this universe" Read more51AuraFr2 hours ago Read moreRead moreTip72Shalom T AlexanderMay 14, 2022How to read my post?
Just match the Diagram number with the number mentioned in code.
Variables used r =Total  rows, c = total columns, x,y are coordinates and count = No of opening brackets visited
Thought Process
Let's connect the thought with code:
Note: Thanks to @LarryNY for a easily understandable python code
Important point: @cache is a decorator in python which helps to memoize the recursive function. Without that decorator this code will give TLE. You can always try to memoize it in your own way. Read moreRead more61Tarun AnandMay 08, 2022There are many wrong test cases for this question.
For ex: The expected output for input [["(","("]] is 'true' but the accepted response should be 'false'
Another example : [["(","(",")","(",")","(","(",")","(","(",")",")",")",")",")","(",")","(","(",")","(","(",")",")",")",")",")","(","(","(","("],[")","(","(","(",")","(",")","(","(",")",")",")",")","(",")",")","(","(",")",")","(",")","(",")","(","(",")","(",")","(","("],[")",")","(","(",")","(","(",")",")",")",")","(","(",")",")","(",")","(",")",")","(","(","(",")",")",")","(",")",")","(",")"],["(","(",")","(",")","(","(",")","(","(","(",")",")","(",")","(",")",")",")",")",")",")","(","(",")","(",")","(",")","(","("],[")",")","(",")",")","(","(","(",")",")","(",")","(",")",")",")","(","(","(",")",")","(",")","(",")",")","(","(","(","(",")"],[")",")","(","(",")","(",")","(",")","(",")","(",")",")","(",")","(",")",")","(",")","(","(","(",")","(",")",")",")","(","("],[")","(","(","(","(","(","(",")",")","(","(",")","(",")",")","(",")",")",")","(","(","(",")","(","(",")",")","(",")","(",")"],[")",")","(","(","(","(","(","(","(",")",")","(","(","(","(","(","(","(","(","(","(","(","(",")",")","(","(",")",")","(",")"],["(",")",")",")","(","(",")",")",")",")","(",")",")","(",")",")","(","(","(","(","(","(","(",")",")","(","(",")",")","(","("],["(","(",")","(",")",")",")",")","(","(","(",")",")",")","(",")","(","(",")","(","(","(",")","(","(","(","(","(",")",")",")"],["(",")","(","(","(","(",")","(","(",")",")","(","(",")","(","(","(",")","(","(","(",")",")","(",")",")","(",")","(","(",")"],[")",")","(","(","(","(",")","(","(",")",")","(",")",")","(",")","(","(","(","(","(","(","(",")","(","(",")",")","(","(","("],["(",")",")",")","(",")","(","(","(",")",")",")","(",")","(",")",")","(","(","(","(",")","(",")",")",")",")",")",")","(","("],["(","(","(","(","(","(",")",")","(",")","(","(","(",")",")","(",")","(",")","(",")","(","(","(",")",")",")","(",")","(","("],["(",")",")",")",")","(","(",")",")",")",")",")",")","(","(",")","(",")",")","(",")","(",")",")",")","(","(",")","(","(","("],["(",")",")","(","(",")",")","(",")",")","(","(","(",")",")",")",")","(","(","(",")",")","(",")","(","(","(","(",")",")",")"],[")","(","(",")","(","(",")",")",")","(","(","(","(",")","(",")",")",")","(",")","(",")","(","(",")","(","(","(","(","(","("],["(",")","(",")","(","(",")",")",")",")",")","(","(",")",")","(",")","(",")",")",")",")","(","(","(",")","(",")","(",")",")"],["(",")","(",")",")",")","(","(","(",")","(",")","(","(",")",")","(",")","(",")","(",")","(","(","(","(","(",")","(",")","("],[")",")",")",")",")","(",")",")","(","(",")","(",")",")","(",")",")","(","(","(","(",")","(","(","(","(",")",")",")",")","("],[")","(","(","(","(","(",")","(",")",")",")",")","(","(","(",")",")","(",")",")","(","(","(","(","(","(",")",")","(","(","("],["(","(","(",")",")","(",")","(",")",")",")",")","(",")",")",")",")","(",")","(","(","(","(",")","(","(","(","(","(","(",")"]]
The expected answer is 'false' but correct answer should be 'true'.
Is everyone facing the same issue ? Read more65Nick2 hours ago(  -> 1  and           ) -> -1 Read more3Vedant GuptaMay 12, 2022I tried solving this using BFS + caching and DFS + caching, DFS was much faster. Why was DFS faster? Is it because BFS tries to run all paths at the same time and find the shortest whereas DFS just looks for any valid path? Read more42Nitin Jinagam44 minutes agoNot gonna lie this was actually a very doable question. Not hard at all Read more112345Copyright © 2026 LeetCode. All rights reserved.60541
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

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptRustGoSwiftC#TypeScriptKotlinScalaPHPDynamic ProgrammingMemoizationDepth-First SearchRecursionMatrixArrayBracket SequencesBreadth-First SearchBit ManipulationBacktrackingBitmaskHash TableStackIteratorTreeOrdered SetStringSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・14 hours ago Check if There Is a Valid Parentheses String PathEditorial34.7K4eunice・ Open・9 hours agoBalance DP | DFS + Memoization | Grid Path Validation | Space Optimization | Beats 100%ArrayDynamic ProgrammingMatrixPython4+213.6K3TCZON・ Open・4 hours ago🚀 Brute Force → Optimal Approach | Easy solution | Beginner Friendly | TCZON 🔥ArrayDynamic ProgrammingMatrixC++6+101.3K2An-Wen Deng・ Open・4 hours agoDP with bitset/mask||0msDynamic ProgrammingBit ManipulationMatrixBitmask3+113783NEXUS・ Open・3 hours ago🐱 Valid Path in a Parentheses Grid — DFS + Memoization 🚀ArrayDynamic ProgrammingMatrixPython2+82092Aryan Kumar Shaw Halwai・ Open・2 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 |DFS + Top Down DPArrayDynamic ProgrammingMatrixPython4+52940Kostiantyn Lazukin・ Open・5 hours agoBranchless minimal state DP, 0msArrayDynamic ProgrammingBit ManipulationMatrix1+41512Ujjawal・ Open・an hour agoSolution that  Beats 100%ArrayDynamic ProgrammingMatrixJava1+31190DHRUVIK・ Open・14 minutes agoOne of the Simplest & Shortest Bitset DP Approaches | Track All Balances at OnceC++270chaharharsh67・ Open・28 minutes agoEasy Memoization ApproachJava2160Tushar Rana・ Open・2 hours agoBeats 100% | DFS + Memoization (3D DP) – Balance TrackingArrayDynamic ProgrammingMatrixJava1+2840Ajay Choudhary・ Open・4 hours agopython3Python321710Prabhas Sharma・ Open・2 hours ago2267. Check if There Is a Valid Parentheses String PathPython31301abhyuday rastogi・ Open・an hour agoC++ dp solution -- dfs + memoizationC++1110Ajaykumar Nadar・ Open・an hour agoSet DP Trick | Track Only Valid Balances✅C++Python31310All SolutionsBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 |DFS + Top Down DPAryan Kumar Shaw Halwai2942 hours agoArrayDynamic ProgrammingMatrixPython4+Intuition

Imagine the path as building a parentheses string one cell at a time.
We don't actually need to store the complete string. We only need to track its balance:

When we see '(', balance increases by 1.
When we see ')', balance decreases by 1.

For a parentheses string to be valid, the balance can never become negative. For example, if the balance becomes -1, it means we have used a closing bracket without having enough opening brackets before it, so that path can never become valid.
Now, from every cell, there are at most two choices: down or right. This creates many different paths, and the same cell can be reached with the same balance through different paths.
So instead of solving the same situation again and again, store the answer for each:
row + column + current balance
If we already solved that state, directly reuse its result.
Finally, when we reach the bottom-right cell, the path is valid only if the balance is exactly 0. That means every opening bracket has been matched with a closing bracket.
Approach

Start from the top-left cell with balance = 0.
At every cell, first update the balance according to the bracket present there.
If the balance becomes negative, stop exploring that path because it can never produce a valid parentheses string.
Otherwise, try moving:

Down, if possible.
Right, if possible.

If either direction eventually reaches the bottom-right cell with balance 0, return true.
To avoid recalculating the same state, use a 3D DP array:
dp[row][column][balance]
This stores whether a valid path is possible from that particular cell with that particular balance.
There are also two simple checks before starting:
The first cell cannot be ')'.
The last cell cannot be '('.
And the total path length must be even, because a valid parentheses string always contains an equal number of opening and closing brackets.
Complexity

Time complexity:


O(m × n × (m + n))

Space complexity:


O(m × n × (m + n))
Code
JavaC++PythonJavaScriptclass Solution:
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
            return False

        if (rows + cols - 1) % 2 != 0:
            return False

        memo = {}

        def search_path(row, col, balance):
            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if row == rows - 1 and col == cols - 1:
                return balance == 0

            state = (row, col, balance)

            if state in memo:
                return memo[state]

            valid_path = False

            if row + 1 < rows:
                valid_path = search_path(row + 1, col, balance)

            if not valid_path and col + 1 < cols:
                valid_path = search_path(row, col + 1, balance)

            memo[state] = valid_path
            return valid_path

        return search_path(0, 0, 0) Previous🐱 Valid Path in a Parentheses Grid — DFS + Memoization 🚀NextBranchless minimal state DP, 0msComments (0)Sort by:BestCommentNo comments yet.50Python3Auto1213141011897654231        memo = {}        def search_path(row, col, balance):            return False        if (rows + cols - 1) % 2 != 0:            return False        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':        cols = len(grid[0])    def hasValidPath(self, grid):        rows = len(grid)class Solution:SavedLn 42, Col 36AcceptedRuntime: 0 msCase 1Case 2Inputgrid =[["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]OutputtrueExpectedtrueContribute a testcaseInput912›[["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]][[")",")"],["(","("]]Output912›truefalseExpected912›truefalse All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 29, 2026 10:01AnalysisSolutionCodePython31class Solution:
2    def hasValidPath(self, grid):
3        rows = len(grid)
4        cols = len(grid[0])
5
6        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
7            return False
8
9        if (rows + cols - 1) % 2 != 0:
10            return False
11
12        memo = {}
13
14        def search_path(row, col, balance):
15            if grid[row][col] == '(':
16                balance += 1
17            else:
18                balance -= 1
19
20            if balance < 0:
21                return False
22
23            if row == rows - 1 and col == cols - 1:
24                return balance == 0
25
26            state = (row, col, balance)
27
28            if state in memo:
29                return memo[state]
30
31            valid_path = False
32
33            if row + 1 < rows:
34                valid_path = search_path(row + 1, col, balance)
35
36            if not valid_path and col + 1 < cols:
37                valid_path = search_path(row, col + 1, balance)
38
39            memo[state] = valid_path
40            return valid_path
41
42        return search_path(0, 0, 0)View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
