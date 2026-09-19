# 1401. Circle and Rectangle Overlapping

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit200:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1401. Circle and Rectangle OverlappingMediumTopicsCompaniesHintYou are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

 
Example 1:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).


Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false


Example 3:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true


 
Constraints:


	1 <= radius <= 2000
	-104 <= xCenter, yCenter <= 104
	-104 <= x1 < x2 <= 104
	-104 <= y1 < y2 <= 104

 Seen this question in a real interview before?1/6YesNoAccepted72,770/114.2KAcceptance Rate63.7%TopicsStaffMathGeometryBiweekly Contest 23CompaniesHint 1Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.Discussion (100)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestRohan15 hours agoSometimes I think of becoming a baker after graduating CS. Read more1455harsh355615 hours agonow my brain is overlapping 🧠 to much overlapping  in this month 😢 Read moreFeedback86Harish12 hours agoThis problem took us back to 12th-grade JEE preparation, where we had already solved problems like this. 😄 Read more732Ankush11 hours agoleetcode's obsession has grown from alice & bob to overlapping now... Read more311Max_5613 hours agoPretty enjoyable problem if you like math Read more28Anubhav MondalNov 15, 2024Test case to check:
radius = 1415
xCenter, yCenter = 807, -784
x1, y1 = -733, 623
x2, y2 = -533, 1005 Read more215Vansh Bhatnagar11 hours agosomeone overlap my life with a job pls Read more161ccampbell08May 19, 2025This feels like a Trigonometry question, I'm spending so much time trying to figure the solution before I can even start coding. How is this relevant for being a software engineer if I'm not like a videogame dev? Read more162Rakesh Bhandary13 hours agoLeetcode system get overlapped. Read more10Mayank SharmaJan 05, 2025why do these people provide solutions in description , it makes a begineer demotivated Read more161123410Copyright © 2026 LeetCode. All rights reserved.5671002759 Online
@property --beam-angle-_r_2l_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_2l_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_2l_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_2l_"][data-active] {
  animation:
    beam-spin-_r_2l_ 1.96s linear infinite,
    beam-fade-in-_r_2l_ 0.6s ease forwards;
}

[data-beam="_r_2l_"][data-fading] {
  animation:
    beam-spin-_r_2l_ 1.96s linear infinite,
    beam-fade-out-_r_2l_ 0.5s ease forwards;
}

[data-beam="_r_2l_"][data-active]::after,
[data-beam="_r_2l_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2l_),
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
      from var(--beam-angle-_r_2l_),
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
      from var(--beam-angle-_r_2l_),
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
  opacity: calc(var(--beam-opacity-_r_2l_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_2l_"][data-active]::before,
[data-beam="_r_2l_"][data-fading]::before {
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
    from var(--beam-angle-_r_2l_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_2l_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_2l_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_2l_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2l_),
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

[data-beam="_r_2l_"][data-active] [data-beam-bloom],
[data-beam="_r_2l_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_2l_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_2l_ {
  to { --beam-angle-_r_2l_: 360deg; }
}

@keyframes beam-fade-in-_r_2l_ {
  to { --beam-opacity-_r_2l_: 1; }
}

@keyframes beam-fade-out-_r_2l_ {
  from { --beam-opacity-_r_2l_: 1; }
  to { --beam-opacity-_r_2l_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptCGoKotlinRustC#SwiftTypeScriptDartRubyRacketPHPElixirErlangPandasMathGeometrySimulationDepth-First SearchBinary SearchBitmaskBrainteaserNumber TheoryRandomizedSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 16, 2026Circle and Rectangle OverlappingEditorial1113.8K7eunice・ Open・20 hours agoCircle and Rectangle Overlapping | Geometry | Math | Closed-Form | Beats 100%MathGeometryPythonC++5+14314.3K8Muthu Vrn・ Open・4 hours agoGod is Great 468Python3275861Aura Farming・ Open・10 hours agoᯓ★ 100% Beats ⚡︎ O(1) • Hate Geometry? Just Find the Closest Point with Diagram! ✈︎MathGeometryC++Java1+292.2K1An-Wen Deng・ Open・15 hours agoMove center to origin by translation|0msGeometryCBitmaskC++1+207432Ashok Varma・ Open・15 hours ago100% ||✅ Beginner Friendly | Step-by-Step Visualization | Clamp Trick in O(1) | Java/C++/Python/JSMathGeometryPythonC++3+233.6K1Md Aarzoo Islam・ Open・14 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥MathGeometryC++Java4+98211Aryan Kumar Shaw Halwai・ Open・15 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Distance Formula MathGeometryPythonC++2+85351Dhanush Rajulapati・ Open・15 hours agoGeometry + Closest Point Solution | Java, C++, Python, JavaScript | O(1) Time | O(1) SpaceMathGeometryPythonC++2+62871Coding_Ghost・ Open・4 hours agoUsing the locus of Centre of Circle || 100% time || 100% memoryC++5474Long Nguyen・ Open・12 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+31691Debesh P・ Open・21 hours ago0 ms | beats 100.00% | explained like a mentor | geometry | you won't regret babygirl!MathGeometryCPython6+31981EdgeCaseOffByOne・ Open・13 hours agoThe Distance Trick That Solves Circle vs Rectangle Overlap Have Video Solution Do Like and SubscribeMathGeometryC++3950hj-core・ Open・12 hours agoMy kotlin solution with time O(1) and space O(1)Kotlin2421Azad_96・ Open・8 hours agoSimple Solution using Circle EquationC++2800All SolutionsGod is Great 468Muthu Vrn5864 hours agoPython3Intuition

Approach

Complexity

Time complexity:



Space complexity:


Code
Python3class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearestX = max(x1, min(x2, xCenter))
        nearestY = max(y1, min(y2, yCenter))

        dist = (nearestX - xCenter) ** 2 + (nearestY - yCenter) ** 2
        return dist <= radius * radius PreviousCircle and Rectangle Overlapping | Geometry | Math | Closed-Form | Beats 100%Nextᯓ★ 100% Beats ⚡︎ O(1) • Hate Geometry? Just Find the Closest Point with Diagram! ✈︎Comments (1)Sort by:BestCommentTanay Pandeyan hour agoany texts related to god have solutions , but no explanations eh . Read more01271Python3Auto1234567class Solution:    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int,     y2: int) -> bool:        nearestX = max(x1, min(x2, xCenter))        nearestY = max(y1, min(y2, yCenter))        dist = (nearestX - xCenter) ** 2 + (nearestY - yCenter) ** 2        return dist <= radius * radiusSavedLn 7, Col 39Case 1Case 2Case 3radius =1xCenter =0yCenter =0x1 =1y1 =-1x2 =3y2 =199123456789101112131415161718192021›1001-1311111-32-1100-1001SourceAcceptedRuntime: 0 msCase 1Case 2Case 3Inputradius =1xCenter =0yCenter =0x1 =1y1 =-1x2 =3y2 =1OutputtrueExpectedtrueContribute a testcaseInput99123456789101112131415161718192021›1001-1311111-32-1100-1001Output9123›truefalsetrueExpected9123›truefalsetrue All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 19, 2026 21:01AnalysisSolutionCodePython31class Solution:
2    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
3        nearestX = max(x1, min(x2, xCenter))
4        nearestY = max(y1, min(y2, yCenter))
5
6        dist = (nearestX - xCenter) ** 2 + (nearestY - yCenter) ** 2
7        return dist <= radius * radius 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
