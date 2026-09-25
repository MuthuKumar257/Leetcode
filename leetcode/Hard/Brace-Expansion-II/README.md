# 1096. Brace Expansion II

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit200:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1096. Brace Expansion IIHardTopicsCompaniesHintUnder the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:


	Single letters represent a singleton set containing that word.
	
		R("a") = {"a"}
		R("w") = {"w"}
	
	
	When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
	
		R("{a,b,c}") = {"a","b","c"}
		R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
	
	
	When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	
		R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
		R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
	
	


Formally, the three rules for our grammar:


	For every lowercase letter x, we have R(x) = {x}.
	For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
	For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.


Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 
Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]


Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.


 
Constraints:


	1 <= expression.length <= 60
	expression[i] consists of '{', '}', ','or lowercase English letters.
	The given expression represents a set of words based on the grammar given in the description.

 Seen this question in a real interview before?1/6YesNoAccepted68,809/89.8KAcceptance Rate76.6%TopicsPrincipalHash TableStringBacktrackingStackBreadth-First SearchSortingWeekly Contest 142CompaniesHint 1You can write helper methods to parse the next "chunk" of the expression.  If you see eg. "a", the answer is just the set {a}.  If you see "{", you parse until you complete the "}" (the number of { and } seen are equal) and that becomes a chunk that you find where the appropriate commas are, and parse each individual expression between the commas.Similar QuestionsBrace ExpansionMediumDiscussion (83)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestAlhindiSep 04, 2019This is a problem that I am not able to solve even after looking at solution. Wierd thing is intuitively I know what needs to be done and what some of the solutions are doing but I can't express that in code myself. Anyone in same boat? I guess I am not a google materiral. Read more1233O_JApr 25, 2024Finally, I solved this question by myself after dedicating 7-8 hours 🎉.
Yes, it took a lot of time, but I decided to solve it because my friend challenged⚔️ me. Read moreTip452Siva Sai BommisettyJul 17, 2023I wonder why the acceptance rate is greater than 63% Read more403Mayank Bhatt16 hours agoI'm not doing it 😭😭😭😭 Read more361AlexSep 22, 2024is it for LISP compiler developers? Read more22MatvSep 11, 2019Have spent some time trying to understand what is the problem statement. Without checking the discussion tab - it is not clear what we need to achieve? It is me or you guys having similar expirience? Read more161Parth13 hours agotribute to today's compiler design mid sem exam!!! Read more142Jitendrayt9 hours agoRemember to throw the chair out of the window if someone asks you this in a 45 min interview. Read more9Abhiraj200212 hours agoFor those who are still figuring out the question:
Each "," is treated as a new component, and if there is a "{" that simply means we multiply/concatenate.
eg: {a,b}{c,d}
a*{c,d} and b*{c,d} == {ac,ad,bc,bd}
eg: "{{a,z},a{b,c},{ab,z}}"
The separate components are {a,z}, a{b,c}, {ab,z} as they have a "," in between.
{a,z} also has a "," so it represents individual choices: a,z.
Now we will take all the possible results from each component. a{b,c} needs to be multiplied, which will result in ab,ac.
Now combining all the components:
a,z, ab,ac, ab,z
Notice that in the question we need to take each result at most once and return them in sorted order.
So the final answer is:
{a, ab, ac, z} Read moreTip8Stephen SunDec 29, 2025Similar to LC. 224 Basic Calculator, these type of parsing algorithms are just painful and unproductive Read more8112349Copyright © 2026 LeetCode. All rights reserved.627832956 Online
@property --beam-angle-_r_7n_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7n_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7n_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7n_"][data-active] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-in-_r_7n_ 0.6s ease forwards;
}

[data-beam="_r_7n_"][data-fading] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-out-_r_7n_ 0.5s ease forwards;
}

[data-beam="_r_7n_"][data-active]::after,
[data-beam="_r_7n_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"][data-active]::before,
[data-beam="_r_7n_"][data-fading]::before {
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
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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

[data-beam="_r_7n_"][data-active] [data-beam-bloom],
[data-beam="_r_7n_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7n_ {
  to { --beam-angle-_r_7n_: 360deg; }
}

@keyframes beam-fade-in-_r_7n_ {
  to { --beam-opacity-_r_7n_: 1; }
}

@keyframes beam-fade-out-_r_7n_ {
  from { --beam-opacity-_r_7n_: 1; }
  to { --beam-opacity-_r_7n_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++PythonJavaScriptCKotlinRustGoC#TypeScriptSwiftScalaPHPRubyStringStackBacktrackingSortingHash TableRecursionBreadth-First SearchOrdered SetDepth-First SearchTreeGreedyTrieLinked ListDivide and ConquerMathSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 16, 2026Brace Expansion IIEditorial613.3K10An-Wen Deng・ Open・15 hours agoUse stacks for operators & operands|Beats 100.00%StackSortingC++8713.8K7Aura Farming・ Open・13 hours agoᯓ★ Trust me it's not Hard! • Master DFS with Diagram ⚡︎ • Easy Explanation!✈︎StringRecursionOrdered SetC++2+1115K15Md Aarzoo Islam・ Open・15 hours ago11ms | Beats 49.11% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Hash TableStringBacktrackingStack6+235.1K4Aryan Kumar Shaw Halwai・ Open・14 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 |Recursive ParsingHash TableStringBacktrackingStack6+141.4K2Muthu Vrn・ Open・13 hours agoGod is Great 474Python3131390Aleksandr・ Open・6 hours ago✅ Let Python Parse It | eval + Operator Overloading | 4 LinesPythonPython363743Sai Vishal Matcha・ Open・16 hours agoBrace Expansion IIPython337752Achuthanaathan S・ Open・11 hours agoBrace Expansion II  || Easy and Simple Solution || Easy ExplanationHash TableStringBacktrackingStack4+22192Long Nguyen・ Open・9 hours ago100% - [Hard Problem with Easy Approach] 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+26081Prakhar・ Open・9 hours agoEasy & Intuitive SolutionStringSortingJava21871TCZON・ Open・10 hours ago😱 Brace Expansion II Looks Impossible - Until You See These 2 Tricks | TCZON | 🔥Hash TableStringBacktrackingSorting6+21151MBBN・ Open・11 hours agoJava - Clean Possible Solution :: Recursive Descent Parsing with Set Union and Cartesian ProductJava11252Vedansh Rathod・ Open・12 hours ago⚡ Recursive Parsing + Set Algebra | 🏆 Beats 100% | A Clean Recursive Expansion StrategyStringBacktrackingDepth-First SearchRecursion2+2781Ankit Singh・ Open・15 hours ago🔥 Brace Expansion II — Master DFS + Recursion in Java | LeetCode 1096Java44791All Solutions11ms | Beats 49.11% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Md Aarzoo Islam5.1K15 hours agoHash TableStringBacktrackingStack6+

Approach
I keep a single integer index that points to the current character of the expression. A recursive function called parse does the real work.
Inside parse I maintain two sets. One set (called cur) holds the strings built so far for the current alternative. The other set (called res) collects finished alternatives.

When I see a letter I turn it into a one-element set and multiply it into cur (Cartesian product of strings).
When I see an opening brace I recursively parse everything inside the matching closing brace and multiply the resulting set into cur.
When I see a comma I dump the current alternative into res, reset cur to the empty string, and continue.

At the end of the current scope I add whatever is left in cur into res and return that set. After the outermost call finishes I simply convert the set into a sorted list and return it.
This strategy processes the expression from left to right, respects nesting, and never generates duplicate words.

Code
C++JavaJavaScriptTypeScriptPython3goclass Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        self.expr = expression
        res = self.parse()
        return sorted(res)
    def parse(self):
        res = set()
        cur = {""}
        while self.i < len(self.expr) and self.expr[self.i] != '}':
            if self.expr[self.i] == '{':
                self.i += 1
                nxt = self.parse()
                self.i += 1
                cur = self.product(cur, nxt)
            elif self.expr[self.i] == ',':
                res |= cur
                cur = {""}
                self.i += 1
            else:
                nxt = {self.expr[self.i]}
                self.i += 1
                cur = self.product(cur, nxt)
        res |= cur
        return res
    def product(self, a, b):
        return {x + y for x in a for y in b}

 Previousᯓ★ Trust me it's not Hard! • Master DFS with Diagram ⚡︎ • Easy Explanation!✈︎NextBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 |Recursive ParsingComments (4)Sort by:BestCommentpreethsingh7 hours agoAbhay Mahalle. He appears to be using multiple accounts to downvote people.
I’ve tagged his profile/photo here so that people can identify the account involved.
Cheap guy begging for upvotes, lol. 😂 Earlier, his profile had links to his LinkedIn and GitHub accounts, but after people found out about his fake activities, he removed them from his profile. This is the proof, lolllll. 😂  And once again, look at bro’s profile “Bro thinks it’s a bug… nahh, it’s a skill issue!” 😂
https://leetcode.com/u/Abhay_Mahalle/ Read moreRead more4Md Aarzoo Islam15 hours agoComplexity
Time Complexity: O(n * s) where n is the length of the expression and s is the size of the final set of words. Each character is examined a constant number of times while the Cartesian products and unions cost time proportional to the number of strings produced.
Space Complexity: O(s) for the sets that hold intermediate and final results; the recursion depth is O(n) in the worst case of nested braces, but that is still linear in the input size. Read more3Mariaan hour agoSeven lines of code for this task Read more1stasf255 hours ago14 lines for this task: recursive parsing with look ahead Read more11234Python3Auto15161718192021222324252627                cur = self.product(cur, nxt)            elif self.expr[self.i] == ',':                res |= cur                cur = {""}                self.i += 1            else:                nxt = {self.expr[self.i]}                self.i += 1                cur = self.product(cur, nxt)        res |= cur        return res    def product(self, a, b):        return {x + y for x in a for y in b}SavedLn 27, Col 45AcceptedRuntime: 0 msCase 1Case 2Inputexpression ="{a,b}{c,{d,e}}"Output["ac","ad","ae","bc","bd","be"]Expected["ac","ad","ae","bc","bd","be"]Contribute a testcaseInput912›"{a,b}{c,{d,e}}""{{a,z},a{b,c},{ab,z}}"Output912›["ac","ad","ae","bc","bd","be"]["a","ab","ac","z"]Expected912›["ac","ad","ae","bc","bd","be"]["a","ab","ac","z"] All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 25, 2026 21:57AnalysisSolutionCodePython31class Solution:
2    def braceExpansionII(self, expression: str) -> list[str]:
3        self.i = 0
4        self.expr = expression
5        res = self.parse()
6        return sorted(res)
7    def parse(self):
8        res = set()
9        cur = {""}
10        while self.i < len(self.expr) and self.expr[self.i] != '}':
11            if self.expr[self.i] == '{':
12                self.i += 1
13                nxt = self.parse()
14                self.i += 1
15                cur = self.product(cur, nxt)
16            elif self.expr[self.i] == ',':
17                res |= cur
18                cur = {""}
19                self.i += 1
20            else:
21                nxt = {self.expr[self.i]}
22                self.i += 1
23                cur = self.product(cur, nxt)
24        res |= cur
25        return res
26    def product(self, a, b):
27        return {x + y for x in a for y in b}View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
