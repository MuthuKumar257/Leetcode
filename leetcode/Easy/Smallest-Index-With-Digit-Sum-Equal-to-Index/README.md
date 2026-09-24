# 3550. Smallest Index With Digit Sum Equal to Index

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Smallest Index With Digit Sum Equal to Index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionPending...Pending...EditorialEditorialSolutionsSolutionsSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3550. Smallest Index With Digit Sum Equal to IndexEasyTopicsCompaniesHintYou are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 
Example 1:


Input: nums = [1,3,2]

Output: 2

Explanation:


	For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.



Example 2:


Input: nums = [1,10,11]

Output: 1

Explanation:


	For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
	For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
	Since index 1 is the smallest, the output is 1.



Example 3:


Input: nums = [1,2,3]

Output: -1

Explanation:


	Since no index satisfies the condition, the output is -1.



 
Constraints:


	1 <= nums.length <= 100
	0 <= nums[i] <= 1000

 Seen this question in a real interview before?1/6YesNoAccepted80,033/98.2KAcceptance Rate81.5%TopicsMid LevelArrayMathWeekly Contest 450CompaniesHint 1Simulate as describedDiscussion (45)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestAriandne4 hours ago
 Read more29Khumoyun10 hours agoFunny how problems that used to feel difficult finally become just a warmup... but Hards are still Hards 😆 Read more171LwltJun 03, 2025We need new difficulty level -- Baby. Read moreFeedback261SoloPlayer2 hours agoAfter long time I can able to solve Daily!! Ghee Khatam...🥀 Read more141Mudit kalraSep 22, 2026What a fine morning that will be, when this problem become POTD Read more134anoob373 hours agoWhen they want to  hire you Read more101Varun TyagiMay 18, 2025Easy Question for beginners to Good Start Read more8ayeshairsha19773 hours agoToday we got an easy one… tomorrow the crocodiles might be waiting for us. 🐊😂 Read more7FFTFFTFFTFFTFFTFFTFFTFFTFFTFFTMay 18, 2025my first contest problem : D Read more4Som 072 hours agoSolved it under 3 mins I wish I get this in an interview Read moreRead more3312345Copyright © 2026 LeetCode. All rights reserved.111452082 Online
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

LeetSort byAllMy SolutionPython3JavaC++PythonJavaScriptCGoC#RustSwiftDartTypeScriptRacketKotlinRubyPHPScalaArrayMathSimulationStringGreedyRecursionDynamic ProgrammingSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 18, 2026Smallest Index With Digit Sum Equal to IndexEditorial23.6K4An-Wen Deng・ Open・4 hours agoNested loop for digit sums|0msArrayC++Python3202.5K3Aura Farming・ Open・3 hours agoᯓ★ 100% Beats ⚡︎ • Easy Approach ★ Less Theory • Pookie POTD! ✈︎ArrayMathC++Java1+229652Ashok Varma・ Open・8 hours agoTwo Ways to Add Digits | Step-by-Step Visualization | O(n) | Java/C++/Python/JSArrayMathStringPython4+51681Md Aarzoo Islam・ Open・an hour ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayMathC++Java4+71521Aryan Kumar Shaw Halwai・ Open・3 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Iteration OnlyArrayMathPythonC++2+63030Dhanush Rajulapati・ Open・4 hours agoDigit Sum + Linear Search Solution | Java, C++, Python, JavaScript | O(n · d) Time | O(1) SpaceArrayMathPythonC++2+31061EdgeCaseOffByOne・ Open・an hour agoEasy Explanation in C++ with Video Solution | Do Like and Subscribe EdgeCaseOffByOne ChannelArrayMathC++3100hj-core・ Open・2 hours agoMy kotlin solution with precomputed digit sumKotlin251anoob37・ Open・3 hours ago[C++] Easy Digit Sum Check with Modulo | Step-by-StepC++2172meet_pipaliya__・ Open・17 minutes agoDigit Sum Matching Index | O(n) | JavaJava240Ujjawal・ Open・an hour agoSolution that Beats 100%ArrayMathDynamic ProgrammingGreedy1+2100chaharharsh67・ Open・3 hours agoVery Easy Solution | Beats 100%Java2320Shakti Pravesh・ Open・4 hours agoBrute Force Digit Sum Check | O(n × d) Time | O(1) SpaceArrayMathCPython3+4890Jayant Patel・ Open・3 hours agoEasiest Solution | TC: O(n) | SC: O(1) ArrayMathC++Java2+72391All SolutionsNested loop for digit sums|0msAn-Wen Deng2.5K4 hours agoArrayC++Python3Intuition

Compute digit sum for every nums[i] in a nested loop until digit sum==i.
Approach


Let n=|nums|
Proceed the loop as follows:

for(int i=0; i<n; i++){
    int x=nums[i], digitSum=0;
    for(; x>0; x/=10){
        digitSum+=x%10;
    }
    if (digitSum==i) return i;
}

when the loop is through, there is no such i, return -1
Python code is implemented in a similar way by using while loop with divmod for inner loop.

Complexity

Time complexity:


O(nlog10​max(x))

Space complexity:


O(1)
Code |C++ 0ms
C++class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        const int n=nums.size();
        for(int i=0; i<n; i++){
            int x=nums[i], digitSum=0;
            for(; x>0; x/=10){
                digitSum+=x%10;
            }
            if (digitSum==i) return i;
        }
        return -1;
    }
};
Python |0ms
Pythonclass Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            digitSum=0
            while x>0:
                x, r=divmod(x, 10)
                digitSum+=r
            if digitSum==i: return i
        return -1      PreviousSmallest Index With Digit Sum Equal to IndexNextᯓ★ 100% Beats ⚡︎ • Easy Approach ★ Less Theory • Pookie POTD! ✈︎Comments (3)Sort by:BestCommentAn-Wen Deng4 hours agoEasy task.
Have a nice day! Read more7eunice2 hours agoint smallestIndex(auto& A) {
    for (int i = 0; i < A.size() && i < 28; i++)
        if (A[i] - 9 * (A[i] / 10 * 11 / 10 + A[i] / 1000) == i)
            return i;

    return -1;
} Read more3Jordinario4 hours agoThis problem actually got a sublinear solution. Have a nice day! Read more211203Python3Auto1234567891011class Solution:    def smallestIndex(self, nums: List[int]) -> int:        for i in range(len(nums)):            a=nums[i]            t=0            while a>0:                t+=a%10                a//=10            if i==t:                return i        return -1SavedLn 11, Col 18AcceptedRuntime: 0 msCase 1Case 2Case 3Inputnums =[1,2,3]Output-1Expected-1Contribute a testcaseInput9123›[1,3,2][1,10,11][1,2,3]Output9123›21-1Expected9123›21-1 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 24, 2026 09:56AnalysisSolutionCodePython31class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            a=nums[i]
5            t=0
6            while a>0:
7                t+=a%10
8                a//=10
9            if i==t:
10                return i
11        return -1View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
