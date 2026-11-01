# 453. Minimum Moves to Equal Array Elements

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function l(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result453. Minimum Moves to Equal Array ElementsMediumTopicsCompaniesGiven an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 
Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


Example 2:

Input: nums = [1,1,1]
Output: 0


 
Constraints:


	n == nums.length
	1 <= nums.length <= 105
	-109 <= nums[i] <= 109
	The answer is guaranteed to fit in a 32-bit integer.

 Seen this question in a real interview before?1/6YesNoAccepted280,631/453.9KAcceptance Rate61.8%TopicsJuniorArrayMathCompaniesSimilar QuestionsMinimum Moves to Equal Array Elements IIMediumMaximum Running Time of N ComputersHardPour Water Between Buckets to Make Water Levels EqualMediumDivide Players Into Teams of Equal SkillMediumFind Minimum Operations to Make All Elements Divisible by ThreeEasyDiscussion (136)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestGuilherme LatrovaJan 17, 2021I'm willing to show my reasoning because it took me a long time to really understand it.
So, first things first, let's consider the same example: an array with [1, 2, 3]. Cool.
The problem description tells you that you should count how much moves (or sums) to make all values equal, always excluding one. So, we can think reversely by saying we could count how much moves (or subtracts) to make all values equal, only considering one.
So, instead of:
[1,2,3] -> [2,3,3] -> [3,3,4] -> [4,4,4] = 3 moves
We do:
[1,2,3] -> [1,2,2] -> [1,1,2] -> [1,1,1] = 3 moves
The logic is the same:

Decrease 1 over Sum every but one.

Nice, with that being clear it gets easier. We need to find out how much subtracts should happen, and it always will be related to the minimum number. So, in our case, if it's 1 (one), then we need to find out how much different to subtract. So:

3 - 1 = 2
2 - 1 = 1
1 - 1 = 0

Now we sum the difference: 2 + 1 + 0 = 3, so we got here! 3 moves!! Read more38236Ayush AnandJun 16, 2023Increasing n-1 numbers essentially means reducing that ith number relatively. Just this fact! Read moreTip1095motorbreathingMar 24, 2022Let's get one thing out of the way first - let's just bloody sort the damn array before worrying about anything else :)
Now, the idea is to reach a state where all elements are equal - simple, fair enough.
In the process, the element which will change the most is the first element - the leftmost one - while, conversely, the element which will change the least is the last one, the rightmost one i.e. The sodding array is sorted, after all.
So for nothing but the heck of it, let's look at the whole thing from the perspective of the first element.
Let's imagine the first element setting an initial task for itself - I have to catch up with my neighbor (i.e. second) element. So what does it do - increments itself and all other elements, except the second one of course, by the exact difference between itself and the second element.
If the array was "1, 5, 6, 7" then the array change to "5 5 10 11".
Next, the first element expands it's horizons a bit and looks at the element just beyond the second one  - the third element. It must catch up with the third element. So: every element, except the third element is upgraded by the difference between the first element and the third one. As a result, the array now is - "10 10 10 16".
Finally, only one element left that's towering above everyone else - the last element. In the final step, the array is modified to "16 16 16 16". Read more1539Vlad-Antoniu GhenghiuApr 21, 2024One move increments n - 1 elements. Saying "can" is misleading. Read moreFeedback1283DAOYUAN YAOJan 22, 2021There are n elements, after reordering, the minimum element is a(1), the maximum element is a(n), we have a(1) <= a(2) <= a(3) <= ... <= a(n).
We set the solution is m, after m moves, all the elements will be the same value, that is a(1) + m, so the other (n-1) element will add a(1) + m - a(i) times, we know that m moves will introduce m * (n - 1) to the array's total sums. we can have the equation:
m * (n - 1) = m + a(1) + m - a(2) + a(1) + m - a(3) +... + a(1) + m - a(n)
=> m * n - m = m * n + (n - 1) * a(1) - a(2) - a(3) -... - a(n)
=> m = a(2) + a(3) + ... + a(n) - (n - 1) * a(1)
=> m = Sum - n * Min
Done! Read more632UI-ShashankJul 20, 2025i'm dumb af Read more341Yummy ChenNov 23, 2018every move means select #n-1 numbers plus 1, which equals to select #1 number minus 1.
hence, just every number reduce to the minimum number. Read more251Guy AlsterNov 08, 2016This problem is at least a medium. Read more234viraj7403Feb 04, 2022here , by iterating array and find min steps : that will be more complex.
we have to solve this question via some equation.
suppose at initial stage , sum of all array elements is "s" ,minimum element is "mi" , and "n" is number of elements and we have to find "m" ( number of moves) , and  "p"  will gonna be equal element at last.
after m moves ,
sum + m*(n-1) = p*n   ....(1)
as we know , in each step we have to add 1 in minimum element ,
so we can write p( equal element at last) as
p = mi + m .....(2)
from eqn(1) and (2)
sum + mn - m =(mi+m)n
sum+ mn - m = mi n + mn
now we make m as a subject of eqn ,
m = sum - mi*n
**(sum= sum of elements of array without any move , mi = minimum element at initial , n=number of elements , m=number of moves that we have to find ) * Read more133123414Copyright © 2026 LeetCode. All rights reserved.3.1K136
@property --beam-angle-_r_7i_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7i_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7i_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7i_"][data-active] {
  animation:
    beam-spin-_r_7i_ 1.96s linear infinite,
    beam-fade-in-_r_7i_ 0.6s ease forwards;
}

[data-beam="_r_7i_"][data-fading] {
  animation:
    beam-spin-_r_7i_ 1.96s linear infinite,
    beam-fade-out-_r_7i_ 0.5s ease forwards;
}

[data-beam="_r_7i_"][data-active]::after,
[data-beam="_r_7i_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7i_),
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
      from var(--beam-angle-_r_7i_),
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
      from var(--beam-angle-_r_7i_),
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
  opacity: calc(var(--beam-opacity-_r_7i_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7i_"][data-active]::before,
[data-beam="_r_7i_"][data-fading]::before {
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
    from var(--beam-angle-_r_7i_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7i_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7i_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7i_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7i_),
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

[data-beam="_r_7i_"][data-active] [data-beam-bloom],
[data-beam="_r_7i_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7i_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7i_ {
  to { --beam-angle-_r_7i_: 360deg; }
}

@keyframes beam-fade-in-_r_7i_ {
  to { --beam-opacity-_r_7i_: 1; }
}

@keyframes beam-fade-out-_r_7i_ {
  from { --beam-opacity-_r_7i_: 1; }
  to { --beam-opacity-_r_7i_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptC#TypeScriptRustGoKotlinSwiftPHPDartScalaRacketMySQLRubyMathArraySortingGreedyBrainteaserSimulationStackHeap (Priority Queue)Two PointersDivide and ConquerBinary Indexed TreeInteractiveIteratorBinary TreeQueueCountingSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Jan 05, 2017Minimum Moves to Equal Array ElementsEditorial5968.7K63Vaibhav Raj Singh・ Open・10 hours agoEasy Visual Solution + One Line SolutionC++824.9K1Aleksandr・ Open・16 hours ago✅ Don’t Simulate, Solve min · n = sum | Closed Form | Beats 100%ArrayMathBrainteaserPython6+7012.3K9SANJAY M N・ Open・12 hours ago*NO AI SLOP* EZ IF THE MATH CLICKS! (BONUS : FENWICK TREE OVERKILL)ArrayMathBinary Indexed TreeC6+211.2K4Md Aarzoo Islam・ Open・12 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayMathC++Java4+203.6K2Samarth Agrawal・ Open・11 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayMathCPython5+77775Aryan Kumar Shaw Halwai・ Open・13 hours ago✅ Beats 95% 🚀 | Simple Logic No Brainer 🔥 | Java, C++, Python, JSArrayMathGreedyPython4+95231Dhanush Rajulapati・ Open・14 hours agoMath + Minimum Element Solution | Java, Python, C++, JavaScript | O(n) Time | O(1) SpaceArrayMathGreedyPython3+55192Unnamed・ Open・12 hours ago🔥 The Mathematical Trick Simplifying Everything | Intuition Building💡ArrayMathJava41362aatifa_mugheer・ Open・10 hours agoC++  Easy SolutionArrayMathC++41851Kostiantyn Lazukin・ Open・14 hours agoSingle pass, branchlessC++31852Joseph Jackson・ Open・14 hours agoSimple 1-liner for beginnersPython333361VipulRaj・ Open・8 hours ago🔥 EASIEST |⚡MULTIPLE APPROACH | 🚀 O(N) Time & O(1) SpaceArrayMathC++Java31160Ujjawal・ Open・3 hours agoSolution that Beats 100%ArrayMathDivide and ConquerStack6+2211Long Nguyen・ Open・6 hours ago100% - [Easy Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+2600All Solutions✅ Don’t Simulate, Solve min · n = sum | Closed Form | Beats 100%Aleksandr12.3K16 hours agoArrayMathBrainteaserPython6+Python3C++JavaGoJavaScriptTypeScriptclass Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
Leave out the max. Every move raises n - 1 of the n elements. To make them equal we have to close the gap between max and min, and raising the max never shrinks it. So each move raises everything except the max, and the min goes up by 1 every time.
Equal means min * n == sum. In any array sum >= min * n, and the two are equal only when every element equals the min. So we stop at the first move where min * n == sum.
Track min and sum. Let M = min(nums) and S = sum(nums). Each move adds 1 to the min and n - 1 to the sum:
move |  min  |  sum
-----+-------+-----------------
  0  |   M   |  S
  1  | M + 1 |  S + (n - 1)
 ... |  ...  |  ...
  k  | M + k |  S + k * (n - 1)
After k moves all elements same and we can solve min * n == sum for k:
(M + k) * n   = S + k * (n - 1)
M * n + k * n = S + k * n - k
            k = S - M * n = sum(nums) - min(nums) * len(nums)
Example 1: k = 6 - 1 * 3 = 3.
Approach: add up the gaps
S can reach 10^5 * 10^9 = 10^14, far beyond a 32-bit int. But S - M * n is just the sum of the gaps x - M >= 0, so the running total never exceeds the answer, which is guaranteed to fit in 32 bits. Python's integers never overflow.
Complexity

Time: O(n)
Space: O(1)
 PreviousEasy Visual Solution + One Line SolutionNext*NO AI SLOP* EZ IF THE MATH CLICKS! (BONUS : FENWICK TREE OVERKILL)Comments (9)Sort by:BestCommentPeter10 hours agoHere's a huge simplification:  raising n-1 integers by 1 is the same as lowering 1 integer by 1 with respect to making everything equal.  THink of it this way and the problem becomes trivial. Read more132Kostiantyn Lazukin14 hours agoSingle pass option Read more3devhindo12 hours agoreally Read more2Debargha Sikdar2 hours agogreat explanation ! Read more1Akmal Mahardika N P9 hours agogreat explanation, thanks! I was a little confused earlier when sum(nums) - min(nums)*len(nums) became a loop. but I figured it out.
moves = (nums[0] - min_value)
        + (nums[1] - min_value)
        + ...
        + (nums[n-1] - min_value)

Distribute the summation:

moves = sum(nums) - (min_value + min_value + ... + min_value)

Since min_value appears n times:

moves = sum(nums) - n * min_value Read more11Mr Aman12 hours agobut what is the garenty that it's return minimum operation as there is not equality sign there Read more11Maria14 hours agoOne line solution Read more1BT19CIV052 BHUSHAN KOLPE11 hours agofor best explaination
 Read more0Mr Aman12 hours ago🫡🫡🫡 Read more01709Python3Auto1234class Solution:    def minMoves(self, nums: list[int]) -> int:                return sum(nums) - len(nums) * min(nums)In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 4, Col 1AcceptedRuntime: 0 msCase 1Case 2Inputnums =[1,2,3]Output3Expected3Contribute a testcaseInput912›[1,2,3][1,1,1]Output912›30Expected912›30 All SubmissionsAccepted84 / 84 testcases passedMUTHU KUMAR Msubmitted at Nov 01, 2026 19:23AnalysisSolutionCodePython31class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3                return sum(nums) - len(nums) * min(nums)
4 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
