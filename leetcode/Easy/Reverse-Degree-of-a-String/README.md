# 3498. Reverse Degree of a String

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit300:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3498. Reverse Degree of a StringEasyTopicsCompaniesHintGiven a string s, calculate its reverse degree.

The reverse degree is calculated as follows:


	For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
	Sum these products for all characters in the string.


Return the reverse degree of s.

 
Example 1:


Input: s = "abc"

Output: 148

Explanation:

LetterIndex in Reversed AlphabetIndex in StringProduct'a'26126'b'25250'c'24372

The reversed degree is 26 + 50 + 72 = 148.


Example 2:


Input: s = "zaza"

Output: 160

Explanation:

LetterIndex in Reversed AlphabetIndex in StringProduct'z'111'a'26252'z'133'a'264104

The reverse degree is 1 + 52 + 3 + 104 = 160.


 
Constraints:


	1 <= s.length <= 1000
	s contains only lowercase English letters.

 Seen this question in a real interview before?1/6YesNoAccepted142,652/156.6KAcceptance Rate91.1%TopicsMid LevelStringSimulationBiweekly Contest 153CompaniesHint 1Simulate the operations as described.Discussion (128)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestIneedchezzborgerMar 31, 2025That zaza be hitting different Read more833qvenn8 hours ago"Just do it" type of problem.

💀💀💀💀 Read more47anoob3711 hours agowhen they want to hire you Read more622vidhaanApr 11, 2025With this I solved my 500th problem. Leetcode has been such a fun journey :) Read more495Oggy_457 hours agoFinally..its over for overlapping.. Read more26Nithyanandan MOct 14, 2025The hint doesn’t really help 😅 Read more23Varun TyagiMar 29, 2025This problem give me confidence 🎉. Thanks Leetcode 👋🏻 Read more16Yarlagadda Sarath ChaitanyaJun 24, 2025What exactly do we learn from these sort of questions? Read moreFeedback134Aura Farming8 hours agoFinally! After so many days, LeetCode stopped giving us overlapping Daily Problem!! Read more47Soham KhannaMar 31, 2025just a small trick and the work is done :) Read more5123413Copyright © 2026 LeetCode. All rights reserved.220128
@property --beam-angle-_r_7l_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7l_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7l_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7l_"][data-active] {
  animation:
    beam-spin-_r_7l_ 1.96s linear infinite,
    beam-fade-in-_r_7l_ 0.6s ease forwards;
}

[data-beam="_r_7l_"][data-fading] {
  animation:
    beam-spin-_r_7l_ 1.96s linear infinite,
    beam-fade-out-_r_7l_ 0.5s ease forwards;
}

[data-beam="_r_7l_"][data-active]::after,
[data-beam="_r_7l_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7l_),
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
      from var(--beam-angle-_r_7l_),
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
      from var(--beam-angle-_r_7l_),
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
  opacity: calc(var(--beam-opacity-_r_7l_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7l_"][data-active]::before,
[data-beam="_r_7l_"][data-fading]::before {
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
    from var(--beam-angle-_r_7l_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7l_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7l_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7l_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7l_),
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

[data-beam="_r_7l_"][data-active] [data-beam-bloom],
[data-beam="_r_7l_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7l_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7l_ {
  to { --beam-angle-_r_7l_: 360deg; }
}

@keyframes beam-fade-in-_r_7l_ {
  to { --beam-opacity-_r_7l_: 1; }
}

@keyframes beam-fade-out-_r_7l_ {
  from { --beam-opacity-_r_7l_: 1; }
  to { --beam-opacity-_r_7l_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++PythonJavaScriptCC#GoTypeScriptRustKotlinSwiftRubyPHPDartRacketScalaMS SQL ServerElixirErlangMySQLStringSimulationMathString MatchingArrayHash TableEnumerationCountingGreedyIteratorInteractiveRecursionBrainteaserTwo PointersSliding WindowDynamic ProgrammingSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 08, 2026Reverse Degree of a StringEditorial59.1K12An-Wen Deng・ Open・12 hours agoSingle loop vs 1-liner|0msSimulationC++Python3604.8K7Ashok Varma・ Open・11 hours ago100% ||✅ Beginner Friendly | Step-by-Step Visualization | Java/C++/Python/JSStringSimulationPythonC++3+193.5K2Coding_Ghost・ Open・6 hours agoEast Work || 100% beatsC++71435Aryan Kumar Shaw Halwai・ Open・10 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Traversal + MappingStringSimulationPythonC++2+78872Dhanush Rajulapati・ Open・12 hours agoString + Character Arithmetic Solution | Java, C++, Python, JavaScript | O(n) Time | O(1) SpaceMathStringPythonC++2+54962subhankar・ Open・10 hours ago100% | One-Pass Solution | Simple and EasyStringPythonC++Java1+54691Md Aarzoo Islam・ Open・10 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥StringSimulationC++Java4+65401Satyam Singh・ Open・8 hours agoSimulation | Character Mapping | Single Pass | Beats 100 % | 0msArrayHash TableMathString6+4400Shakti Pravesh・ Open・12 hours agoSingle Pass Solution | Interview friendly | Step by Step guideJava42160Rohitttt・ Open・8 hours agoSimple O(N) Iteration | Detailed Explanation | C++ & GolangStringSimulationC++Go3181EdgeCaseOffByOne・ Open・9 hours agoReverse Degree Made Easy — Just One Simple Formula! | Like & SubscribeStringSimulationC++3300SRC_9060・ Open・9 hours agoSimple O(n) Java Solution | Reverse Alphabet Trick | Beginner-FriendlyArrayMathStringString Matching3+2131anoob37・ Open・11 hours agoClean C++ 1-Pass Solution | Beats 100% StringSimulationC++2401Nikhil Karrolla・ Open・4 hours agoeasy cpp code//C++280All SolutionsSingle loop vs 1-liner|0msAn-Wen Deng4.8K12 hours agoSimulationC++Python3Intuition

This problem is very easy which is done by a single loop
Approach


Declare int sum=0, n=s.size()
Proceed the loop for(int i=0; i<n; i++) sum+=(i+1)*('z'-s[i]+1)
return sum
Python code is 1-line
Add a C++ "1-liner"

Complexity

Time complexity:


O(n)

Space complexity:


O(1)
Code C++ 0ms
C++class Solution {
public:
    int reverseDegree(string& s) {
        int sum=0, n=s.size();
        for(int i=0; i<n; i++) sum+=(i+1)*('z'-s[i]+1);
        return sum;
    }
};
Python 1-liner
Pythonclass Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))
C++ 1-liner
class Solution {
public:
    int reverseDegree(string& s) {
        return accumulate(s.begin(), s.end(), 0, [i=0](int sum, char c) mutable {
            return sum+=(i+++1)*('z'-c+1);
        });
    }
}; PreviousReverse Degree of a StringNext100% ||✅ Beginner Friendly | Step-by-Step Visualization | Java/C++/Python/JSComments (7)Sort by:BestCommentAn-Wen Deng12 hours ago1-line code is done.
Have a nice day! Read more11eunice9 hours agono need to multiply, you can do a row-wise accumulation.
int reverseDegree(string s) {
    int res = 0, acc = 0;

    for (int i = s.size() - 1; i >= 0; i--)
        res += acc += '{' - s[i];

    return res;
} Read more71Mariaan hour agoOne line solution for this task Read more2Aeona11 hours agoayo, we can also use a "1 liner" in C++ with the power of ranges:  return std::ranges::fold_left(             s | std::views::enumerate, 0, [](const auto acc, const auto& p) {                 const auto& [idx, ch]{ p };                 return acc + ('z' - ch + 1) * (idx + 1);             }         ); Read more21stasf254 hours agoSimplest ONE-liner for this task Read more1Long Nguyen11 hours agoHave a nice day sir!!! Read more1abduhakimovA3 hours agoint res = 0;
    int pos = 1;

    for (char c : s) {
        res += pos++ * ('z' - c + 1);


    }
    return res; Read more01607Python3Auto123class Solution:    def reverseDegree(self, s: str) -> int:         return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))SavedLn 3, Col 72AcceptedRuntime: 0 msCase 1Case 2Inputs ="abc"Output148Expected148Contribute a testcaseInput912›"abc""zaza"Output912›148160Expected912›148160 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 20, 2026 17:50AnalysisSolutionCodePython31class Solution:
2    def reverseDegree(self, s: str) -> int:
3         return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s)) 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
