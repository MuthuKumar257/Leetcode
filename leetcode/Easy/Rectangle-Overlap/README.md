# 836. Rectangle Overlap

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result836. Rectangle OverlapEasyTopicsCompaniesAn axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 
Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

 
Constraints:


	rec1.length == 4
	rec2.length == 4
	-109 <= rec1[i], rec2[i] <= 109
	rec1 and rec2 represent a valid rectangle with a non-zero area.

 Seen this question in a real interview before?1/6YesNoAccepted295,279/556.8KAcceptance Rate53.0%TopicsMid LevelMathGeometryWeekly Contest 85CompaniesSimilar QuestionsRectangle AreaMediumDiscussion (177)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestChidipothu JaswinSep 14, 2026Happy Vinayak Chaturthi ! May he give you everything you want. : ) Read more33610Himanshu BhartiJul 06, 2023Damn, one of the toughest easy on this goddamn platform Read more1663Movsar MakhmutovApr 16, 2023Think about cases when there will never be overlap. For example look at the picture bellow. We can be 100% sure that
if (x1 >= x4 || y1 >= y4 || ...) {}
will never be overlap. There are two more cases to think about. Hope this will help. Good luck Read moreRead moreTip959ChrisSep 14, 2026Easier to prove when they don't overlap. Read more412Gaurav KabraAug 14, 2024⚠️ This is an honest opinion on the problem ⚠️
I see in Discussion section that this question is being asked in companies.
In my opionion this question does not fit interview criteria (unless interviewer already has mood to disqualify you). I will tell why. If we observe by drawing various cases and come to a conclusion, interviewer can still ask for a formal proof of its working in every scenario. Now either draw all cases or give a mathematical proof - both of which are too tedious, leaving little to no space for next question.
But we are engineers, we solve most complex problems. In that regard, I find this question interesting. This fun problem tests your thinking of all scenarios + observation power of what is common in all scenarios.
Also this problem is NOT easy. It should be marked medium. Easy problems are generally too straight forward. I think LeetCode is not consistent in difficulty marking of its questions. Read more405Punyaslok NathSep 18, 2025guys don't think too much , just think when two rectangles are not overlap with each other . Read more261Mayanka day agoTest Cases :
[-4,-9,-2,3]
[1,-5,9,-1]
[-9,6,-3,10]
[-8,-10,-5,-4]
[5,15,8,18]
[0,3,7,9]
[512320138,339316137,683242142,909216020]
[553822491,613363800,681801037,899732269]
[491512649,-528380151,977509156,620803381]
[977509191,-528380114,1000000000,-343176072]
[768722049,-237759592,884113285,-99681789]
[768721982,-99681704,1000000000,273514698]
[-786818791,567559749,-346347634,699723081]
[-346347607,699723128,247165384,1000000000]
[-552260740,909854970,-263634921,942191543]
[-374923864,915642060,-314801007,930370357] Read moreTip20BlackStallion456Jan 20, 2025Definitely should be a medium problem. Read more306mayur vaswaniMay 12, 2025Think of rectangles drawing its shadow on x axis and y axis. This way the problem becomes 1D based intersection problem. Read moreTip17pangpangdeiMay 24, 2023This was one of the questions I met during the interview back in 2018... Read more233123418Copyright © 2026 LeetCode. All rights reserved.2.4K1771063 Online
@property --beam-angle-_r_7r_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7r_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7r_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7r_"][data-active] {
  animation:
    beam-spin-_r_7r_ 1.96s linear infinite,
    beam-fade-in-_r_7r_ 0.6s ease forwards;
}

[data-beam="_r_7r_"][data-fading] {
  animation:
    beam-spin-_r_7r_ 1.96s linear infinite,
    beam-fade-out-_r_7r_ 0.5s ease forwards;
}

[data-beam="_r_7r_"][data-active]::after,
[data-beam="_r_7r_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7r_),
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
      from var(--beam-angle-_r_7r_),
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
      from var(--beam-angle-_r_7r_),
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
  opacity: calc(var(--beam-opacity-_r_7r_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7r_"][data-active]::before,
[data-beam="_r_7r_"][data-fading]::before {
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
    from var(--beam-angle-_r_7r_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7r_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7r_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7r_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7r_),
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

[data-beam="_r_7r_"][data-active] [data-beam-bloom],
[data-beam="_r_7r_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7r_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7r_ {
  to { --beam-angle-_r_7r_: 360deg; }
}

@keyframes beam-fade-in-_r_7r_ {
  to { --beam-opacity-_r_7r_: 1; }
}

@keyframes beam-fade-out-_r_7r_ {
  from { --beam-opacity-_r_7r_: 1; }
  to { --beam-opacity-_r_7r_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonCJavaScriptC#GoTypeScriptRustKotlinSwiftRubyScalaRacketElixirPHPBashDartErlangMathGeometryArrayMatrixGreedyBrainteaserSortingSimulationRecursionSweep LineDynamic ProgrammingSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・May 19, 2018Rectangle OverlapEditorial80165.9K67eunice・ Open・Sep 14, 2026Rectangle Overlap | Geometry | SAT | Simple Explanation | Beats 100%MathGeometryPythonC++3+22226.5K7Aura Farming・ Open・Sep 14, 2026ᯓ★ 100% Beats ⚡︎ O(1) • 2 Easiest Approach with Diagram (Image's) ★ ✈︎MathGeometryC++Java1+366.1K4Md Aarzoo Islam・ Open・Sep 14, 20260ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥MathGeometryC++Java4+295.4K2Muthu Vrn・ Open・Sep 14, 2026God is Great 463Python3266500An-Wen Deng・ Open・Sep 14, 20261-liner|0msGeometryC++218062Amit Prasad Lal・ Open・a day agoNo Area Calculation Needed !! | Rectangle Overlap | O(1) SolutionMathGeometryCPython5+53580Aryan Kumar Shaw Halwai・ Open・Sep 14, 2026Beats 100 % ✅ |1 Liner +  No BS ✅ | Easiest explanation With Step to Step Breakdown💯MathGeometryJava54720Suraj_06・ Open・19 hours agoRectangle Overlap | Simple Geometry Approach | O(1) Time & O(1) Space | 100% Acceptance RateJava41011Dhanush Rajulapati・ Open・Sep 14, 2026Geometry Solution | Java, Python, C++, JavaScript | O(1) Time | O(1) SpaceMathGeometryPythonC++2+61K1chaharharsh67・ Open・Sep 14, 2026Very Easy Approach | Beats 100 %Java32430Kaushal Kumar・ Open・10 hours agoRectangle Overlap | Easy way | SAT | Beats 100%MathGeometryJava2142qyGf0uXBke・ Open・a day agoSimple 1D Interval Approach | Rectangle Overlap | your all doubt solved here ....C++2731hj-core・ Open・Sep 14, 2026My kotlin solution with time O(1) and space O(1)Kotlin2321Vinay kumar・ Open・Sep 14, 2026🏆⚡ 100% Beats! • 2 Approaches • One-Line Optimal 🚀💯MathGeometryPythonC++1+43151All SolutionsNo Area Calculation Needed !! | Rectangle Overlap | O(1) SolutionAmit Prasad Lal358a day agoMathGeometryCPython5+Intuition
Instead of calculating the overlapping area, we can check the situations where the two rectangles cannot overlap.
Two rectangles do not overlap if one rectangle is completely:

To the right of the other
To the left of the other
Above the other
Below the other

If none of these situations occurs, the rectangles must overlap.
Approach
Let rec1 = [x1, y1, x2, y2], where:

x1, y1 → bottom-left corner
x2, y2 → top-right corner

Now consider rec2.
1. rec2[0] >= rec1[2] → rec2 is completely to the right
For example:
rec1 = [1, 1, 4, 4]
rec2 = [4, 2, 6, 5]
Here, the left edge of rec2 is 4, while the right edge of rec1 is also 4.
So:
rec2[0] >= rec1[2]
4 >= 4 → true
Therefore, the rectangles don't overlap.
2. rec2[1] >= rec1[3] → rec2 is completely above
For example:
rec1 = [1, 1, 4, 4]
rec2 = [2, 4, 5, 6]
The bottom edge of rec2 is 4, while the top edge of rec1 is 4.
So:
rec2[1] >= rec1[3]
4 >= 4 → true
Therefore, there is no overlap.
3. rec2[2] <= rec1[0] → rec2 is completely to the left
For example:
rec1 = [1, 1, 4, 4]
rec2 = [-2, 2, 1, 3]
The right edge of rec2 is 1, while the left edge of rec1 is 1.
So:
rec2[2] <= rec1[0]
1 <= 1 → true
Therefore, there is no overlap.
4. rec2[3] <= rec1[1] → rec2 is completely below
For example:
rec1 = [1, 1, 4, 4]
rec2 = [2, -2, 5, 1]
The top edge of rec2 is 1, while the bottom edge of rec1 is 1.
So:
rec2[3] <= rec1[1]
1 <= 1 → true
Therefore, there is no overlap.
If none of these 4 conditions is true, rec2 must have some positive-width and positive-height intersection with rec1, so we return true.
Complexity


Time complexity: (O(1))


Space complexity: (O(1))


# Code
JavaC++PythonJavaScriptTypeScriptC
class Solution:

    def isRectangleOverlap(self, rec1, rec2):

        if rec2[0] >= rec1[2]:
            return False

        if rec2[1] >= rec1[3]:
            return False

        if rec2[2] <= rec1[0]:
            return False

        if rec2[3] <= rec1[1]:
            return False

        return True
 Previous1-liner|0msNextBeats 100 % ✅ |1 Liner +  No BS ✅ | Easiest explanation With Step to Step Breakdown💯Comments (0)Sort by:BestCommentNo comments yet.50Python3Auto56789101112131415161718        if rec2[0] >= rec1[2]:            return False        if rec2[1] >= rec1[3]:            return False        if rec2[2] <= rec1[0]:            return False        if rec2[3] <= rec1[1]:            return False        return TrueSavedLn 18, Col 20AcceptedRuntime: 0 msCase 1Case 2Case 3Inputrec1 =[0,0,2,2]rec2 =[1,1,3,3]OutputtrueExpectedtrueContribute a testcaseInput9123456›[0,0,2,2][1,1,3,3][0,0,1,1][1,0,2,1][0,0,1,1][2,2,3,3]Output9123›truefalsefalseExpected9123›truefalsefalse All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 15, 2026 10:10AnalysisSolutionCodePython31
2class Solution:
3
4    def isRectangleOverlap(self, rec1, rec2):
5
6        if rec2[0] >= rec1[2]:
7            return False
8
9        if rec2[1] >= rec1[3]:
10            return False
11
12        if rec2[2] <= rec1[0]:
13            return False
14
15        if rec2[3] <= rec1[1]:
16            return False
17
18        return TrueView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
