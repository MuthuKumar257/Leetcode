# 835. Image Overlap

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Image Overlap](https://leetcode.com/problems/image-overlap/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit10100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result835. Image OverlapMediumTopicsCompaniesYou are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 
Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).



Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1


Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0


 
Constraints:


	n == img1.length == img1[i].length
	n == img2.length == img2[i].length
	1 <= n <= 30
	img1[i][j] is either 0 or 1.
	img2[i][j] is either 0 or 1.

 Seen this question in a real interview before?1/6YesNoAccepted119,824/182.9KAcceptance Rate65.5%TopicsSenior StaffArrayMatrixWeekly Contest 84CompaniesDiscussion (47)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:Besttechsc0utOct 29, 2022pathetic description of the question ! Read more722timofeev_evgAug 23, 2023what's the purpose of examples #2 & #3? 😁 Read more3610-daedalusOct 27, 2022How is THIS ranked medium?? Read moreFeedback464Varoon KodithalaAug 11, 2024Here are some hints that helped me when I was stuck.
Hint I. Let's consider (r1, c1) in img1 and (r2, c2) in img2, where img1[r1][c1] == 1 and img2[r2][c2] == 1. The translation required for them to overlap would be (r2 - r1), (c2 - c1). The goal of this problem is to find other pairs of nodes for which the same translation would lead to an overlap (more specifically, to get the maximum number of those kinds of pairs). How can we do that?
Hint II. Consider each possible pair of cells from img1 and img2 that has a value of 1. Let's store the translations required to make each of these cells overlap. Think about how you can determine the translation that would produce the highest no. of overlapping cells. Read moreTip303Avishek5 hours ago*Me after a broken streak from yesterday's POTD: Read moreRead more331KamranBadirovJul 28, 2024Who are designing these questions? What kind of description is this "We translate one image however we choose by sliding..." Like, seriously? Spending more time on deciphering the English not algorithms.. smh.. Read more20Apple WatchMay 13, 2018 Read moreRead more152hustle3veryday4everApr 18, 2026My solution is retarded but it worked. That is what counts. Read more9Juvy3 hours agoIts more hard to understand the description than solving it...
even O(n^6) passed. Read more8erjoalgoMay 13, 2018Please also fix the empty matrix test case, which is invalid according to the description. Read moreRead more912345Copyright © 2026 LeetCode. All rights reserved.1.5K474022 Online
@property --beam-angle-_r_2a_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_2a_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_2a_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_2a_"][data-active] {
  animation:
    beam-spin-_r_2a_ 1.96s linear infinite,
    beam-fade-in-_r_2a_ 0.6s ease forwards;
}

[data-beam="_r_2a_"][data-fading] {
  animation:
    beam-spin-_r_2a_ 1.96s linear infinite,
    beam-fade-out-_r_2a_ 0.5s ease forwards;
}

[data-beam="_r_2a_"][data-active]::after,
[data-beam="_r_2a_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2a_),
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
      from var(--beam-angle-_r_2a_),
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
      from var(--beam-angle-_r_2a_),
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
  opacity: calc(var(--beam-opacity-_r_2a_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_2a_"][data-active]::before,
[data-beam="_r_2a_"][data-fading]::before {
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
    from var(--beam-angle-_r_2a_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_2a_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_2a_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_2a_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2a_),
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

[data-beam="_r_2a_"][data-active] [data-beam-bloom],
[data-beam="_r_2a_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_2a_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_2a_ {
  to { --beam-angle-_r_2a_: 360deg; }
}

@keyframes beam-fade-in-_r_2a_ {
  to { --beam-opacity-_r_2a_: 1; }
}

@keyframes beam-fade-out-_r_2a_ {
  from { --beam-opacity-_r_2a_: 1; }
  to { --beam-opacity-_r_2a_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoRustRubyC#SwiftKotlinTypeScriptElixirPHPScalaPython MLRacketDartErlangMatrixArrayBit ManipulationHash TableBitmaskDynamic ProgrammingGeometrySimulationDepth-First SearchTwo PointersCountingIteratorRecursionBacktrackingSortingCombinatoricsPrefix SumOrdered SetMathMemoizationSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Aug 05, 2020Image OverlapEditorial7892.7K81Md Aarzoo Islam・ Open・3 hours ago4ms | Beats 98.65% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayMatrixC++Java4+352.7K2LeetClub・ Open・3 hours agoStandard Approach Explanations || Shift and Count || Linear Transformation|| Imagine ConvolutionArrayMatrixPythonJava2+242.1K0Aura Farming・ Open・3 hours agoᯓ★ No Simulation Needed, Just Count the Shifts ⚡︎ • Easy Explanation with Images!✈︎Hash TableMatrixC++Java1+265302Dhanush Rajulapati・ Open・5 hours agoHashMap + Coordinate Difference Solution [Java, Python, C++, JavaScript]ArrayMatrixPythonC++2+121K2An-Wen Deng・ Open・4 hours agoBitset is good! vs Hashmap|0ms Beats 100%Hash TableBit ManipulationMatrixC++1+92861Aryan Kumar Shaw Halwai・ Open・3 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Frequency CountingArrayMatrixJava51550EdgeCaseOffByOne・ Open・4 hours agoThe Trick Behind Image Overlap Do Like and Subscribe our ChannelArrayHash TableMatrixC++3960Sonam Narula・ Open・2 hours ago0ms Beats 100% | Geometric Shift Tracking | 100% Intuitive Explanation ArrayHash TableGeometryMatrix1+2201RISHABH BABU・ Open・4 hours agoMax Overlap? Just Track the Shift! 🔥 O(n²+m²) HashMap Solution (C++/Java/JS/Python)ArrayMatrixPythonC++1+21441Alok・ Open・10 minutes ago60ms || Clean C++ SolutionArrayMatrixC++240sknayaz・ Open・an hour agoTry Every OffsetC++290Azhar_Beg・ Open・an hour agoImage Overlap — Coordinate Shift FrequencyMatrixC++2180chaharharsh67・ Open・3 hours agoJava | Simple Brute Force | Explained with Dry RunMatrixJava2510Luca・ Open・4 hours ago😼 Optimised Brute Forcing Beating 90%ArrayHash TableMatrixPython5+2930All Solutions4ms | Beats 98.65% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Md Aarzoo Islam2.8K3 hours agoArrayMatrixC++Java4+

Approach
I first walk through both images and collect the coordinates of every cell that holds a 1. Call the lists A for img1 and B for img2.
Then I consider every pair (a from A, b from B). The shift that would move a exactly onto b is simply
dx = b.row - a.row
dy = b.col - a.col
I keep a counter of how many pairs produce each (dx, dy). The highest count I ever see is the answer, because that many 1s will land on top of each other under that exact shift. Bits that slide outside the matrix simply never appear in any pair, so they are automatically ignored.
Here is the small example from the problem worked out by hand:
img1 1s: (0,0) (0,1) (1,1) (2,1)
img2 1s: (1,1) (1,2) (2,2)
Pairs and the shifts they need:
(0,0) -> (1,1) : dx=1, dy=1
(0,0) -> (1,2) : dx=1, dy=2
(0,0) -> (2,2) : dx=2, dy=2
(0,1) -> (1,1) : dx=1, dy=0
(0,1) -> (1,2) : dx=1, dy=1
(0,1) -> (2,2) : dx=2, dy=1
(1,1) -> (1,1) : dx=0, dy=0
(1,1) -> (1,2) : dx=0, dy=1
(1,1) -> (2,2) : dx=1, dy=1
(2,1) -> (1,1) : dx=-1, dy=0
(2,1) -> (1,2) : dx=-1, dy=1
(2,1) -> (2,2) : dx=0, dy=1
Counting the shifts:
(1,1) appears three times
everything else appears once
So the largest overlap is 3, which matches the official answer. The same shift (1,1) lines up three different pairs of 1s at once.

Code
C++JavaJavaScriptTypeScriptPython3goclass Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        cnt = [[0] * (2 * n) for _ in range(2 * n)]
        best = 0
        for ax, ay in A:
            for bx, by in B:
                dx = bx - ax + n
                dy = by - ay + n
                cnt[dx][dy] += 1
                best = max(best, cnt[dx][dy])
        return best

 PreviousImage OverlapNextStandard Approach Explanations || Shift and Count || Linear Transformation|| Imagine ConvolutionComments (2)Sort by:BestCommentMd Aarzoo Islam3 hours agoComplexity
Time Complexity: O(n^{2} + k1·k2) where n is the side length of the matrices and k1, k2 are the number of 1s in each image. Collecting the positions costs O(n^{2}). The double loop over positions is O(k1·k2). In the worst case both k1 and k2 equal n^{2}, so the bound is O(n^{4}), which is fine for n ≤ 30.
Space Complexity: O(n^{2}) in the worst case. The two lists of positions and the map (or 2-D count array) of shifts each hold at most O(n^{2}) entries. Read more12AHHSLAPan hour agoyou're good Read more01362Python3Auto1234567891011121314class Solution:    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:        n = len(img1)        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]        cnt = [[0] * (2 * n) for _ in range(2 * n)]        best = 0        for ax, ay in A:            for bx, by in B:                dx = bx - ax + n                dy = by - ay + n                cnt[dx][dy] += 1                best = max(best, cnt[dx][dy])        return bestSavedLn 11, Col 9AcceptedRuntime: 0 msCase 1Case 2Case 3Inputimg1 =[[1,1,0],[0,1,0],[0,1,0]]img2 =[[0,0,0],[0,1,1],[0,0,1]]Output3Expected3Contribute a testcaseInput9123456›[[1,1,0],[0,1,0],[0,1,0]][[0,0,0],[0,1,1],[0,0,1]][[1]][[1]][[0]][[0]]Output9123›310Expected9123›310 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 13, 2026 10:45AnalysisSolutionCodePython31class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
5        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
6        cnt = [[0] * (2 * n) for _ in range(2 * n)]
7        best = 0
8        for ax, ay in A:
9            for bx, by in B:
10                dx = bx - ax + n
11                dy = by - ay + n
12                cnt[dx][dy] += 1
13                best = max(best, cnt[dx][dy])
14        return bestView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
