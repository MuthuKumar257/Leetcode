# 3736. Minimum Moves to Equal Array Elements III

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Minimum Moves to Equal Array Elements III](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function l(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit200:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3736. Minimum Moves to Equal Array Elements IIIEasyTopicsCompaniesHintYou are given an integer array nums.

In one move, you may increase the value of any single element nums[i] by 1.

Return the minimum total number of moves required so that all elements in nums become equal.

 
Example 1:


Input: nums = [2,1,3]

Output: 3

Explanation:

To make all elements equal:


	Increase nums[0] = 2 by 1 to make it 3.
	Increase nums[1] = 1 by 1 to make it 2.
	Increase nums[1] = 2 by 1 to make it 3.


Now, all elements of nums are equal to 3. The minimum total moves is 3.


Example 2:


Input: nums = [4,4,5]

Output: 2

Explanation:

To make all elements equal:


	Increase nums[0] = 4 by 1 to make it 5.
	Increase nums[1] = 4 by 1 to make it 5.


Now, all elements of nums are equal to 5. The minimum total moves is 2.


 
Constraints:


	1 <= nums.length <= 100
	1 <= nums[i] <= 100

 Seen this question in a real interview before?1/6YesNoAccepted110,404/125.5KAcceptance Rate88.0%TopicsMid LevelArrayMathBiweekly Contest 169CompaniesHint 1To make all numbers equal, they must all reach at least the maximum value in the array.Discussion (90)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestChinmaya NarmdeshwarNov 09, 2025I just do leetcode easy problems, atleast somewhere i find success :) Read moreFeedback90Soham Gawde13 hours agoThis should have been 'I' not 'III'.... Read more822shahed_khanJan 21, 2026questions I do to maintain the streak before time runs out Read more44Varun TyagiNov 08, 2025leetcode gives you wings 🗿 Read more241nusidom11 hours agoHere are some testcases for you guys ------------------->
[1]
[7,7,7,7,7]
[1,100]
[9,1,9,3,9,5]
[10,9,8,7,6,5,4,3,2,1]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
[100,1,99,2,98,3,97,4,96,5,95,6,94,7,93,8,92,9,91,10,90,11,89,12,88,13,87,14,86,15,85,16,84,17,83,18,82,19,81,20,80,21,79,22,78,23,77,24,76,25,75,26,74,27,73,28,72,29,71,30]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
Randomly generated test cases using the web extension LeetTest!
Also provides up to date company tags and elo rating for problems!
Downloadable on the Chrome webstore or Firefox addons and works for most leetcode problems Read more201Achyut MishraFeb 07, 2026These types of questions boost your confidence when you can't take down a good hard question 🤣 Read more19heilheilNov 08, 2025Cant believe I choked this on my first few attempts because I didnt read the qn properly. Thought you could either add or subtract each element by 1 bruuuhhhhh Read more185Khumoyun19 hours agoThe strange thing about learning is that the more familiar something becomes, the less impressive it feels Read more16Achyut Mishra10 hours agoWho else can't believe that the 3rd version of this question is actually easier than the 1st and 2nd. Read more12Akash Pawar20 hours agoI think it's easy to guess POTD of tomorrow
Sequence of this month :

Minimum Moves to Equal Array Elements
Minimum Moves to Equal Array Elements - 2
Minimum Moves to Equal Array Elements - 3 (Today's)

BTW , useful Testcases
[1,10,2,9]
[3,3,10,20,25,25]
feedback Read more612349Copyright © 2026 LeetCode. All rights reserved.179901383 Online
@property --beam-angle-_r_2b_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_2b_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_2b_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_2b_"][data-active] {
  animation:
    beam-spin-_r_2b_ 1.96s linear infinite,
    beam-fade-in-_r_2b_ 0.6s ease forwards;
}

[data-beam="_r_2b_"][data-fading] {
  animation:
    beam-spin-_r_2b_ 1.96s linear infinite,
    beam-fade-out-_r_2b_ 0.5s ease forwards;
}

[data-beam="_r_2b_"][data-active]::after,
[data-beam="_r_2b_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2b_),
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
      from var(--beam-angle-_r_2b_),
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
      from var(--beam-angle-_r_2b_),
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
  opacity: calc(var(--beam-opacity-_r_2b_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_2b_"][data-active]::before,
[data-beam="_r_2b_"][data-fading]::before {
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
    from var(--beam-angle-_r_2b_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_2b_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_2b_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_2b_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2b_),
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

[data-beam="_r_2b_"][data-active] [data-beam-bloom],
[data-beam="_r_2b_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_2b_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_2b_ {
  to { --beam-angle-_r_2b_: 360deg; }
}

@keyframes beam-fade-in-_r_2b_ {
  to { --beam-opacity-_r_2b_: 1; }
}

@keyframes beam-fade-out-_r_2b_ {
  from { --beam-opacity-_r_2b_: 1; }
  to { --beam-opacity-_r_2b_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptCTypeScriptC#RustGoSwiftKotlinRacketDartRubyPHPScalaArrayMathGreedySimulationSortingHash TableEnumerationTwo PointersHeap (Priority Queue)IteratorBinary Indexed TreePrefix SumBit ManipulationDivide and ConquerSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Oct 29, 2026Minimum Moves to Equal Array Elements IIIEditorial58.8K10Shubhashree Sahu・ Open・8 hours agoShubha's LogicArrayMathEnumerationC++181.9K4SANJAY M N・ Open・12 hours ago*NO AI SLOP* JUST ANOTHER EZ MATH PROBLEM (BONUS : FENWICK TREE OVERKILL)ArrayMathBinary Indexed TreeC++4+131.9K2Jayant Patel・ Open・13 hours ago🔥 Minimal Code with Derivation | O(n) & O(1)MathC++JavaPython392.2K2Aryan Kumar Shaw Halwai・ Open・11 hours ago✅ Beats 98% 🚀 | Greedy 🔥 | Java, C++, Python, JSArrayMathGreedyPython4+97250Dhanush Rajulapati・ Open・13 hours agoMath + Maximum Element Solution | [Java, C++, Python, JavaScript | O(n) Time | O(1) SpaceArrayMathPythonC++2+56341Sandip Giri・ Open・8 hours agoBUZZWORD BUZZWORD Oh oh oh ONE MORE BUZZWORD.ArrayMathPython35900Nilesh_Odedara・ Open・30 minutes agoMath | Greedy | Make All Array Elements EqualArrayMathJava2140Long Nguyen・ Open・5 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+21490Shivam Chaurasiya・ Open・7 hours agoArray Equalization | Greedy Approach | Maximum-Based Calculation | O(n) Time | O(1) SpaceArrayMathPythonC++1+2610Ujjawal・ Open・9 hours agoSolution that Beats 100%ArrayHash TableMathGreedy5+21030VAG0tRzLaK・ Open・3 hours agoBest Solution (C++)C++1131Alexey Minkin・ Open・5 hours agoKotlin | O(n) (2ms) | O(1)ArrayMathKotlin191Souvik Dey・ Open・7 hours ago🔥 0 ms | 100% Beats | Two Approaches: 1-Pass Math Trick vs. 2-Pass Greedy | VisualizedMathTwo PointersGreedyBit Manipulation2+1681MBBN・ Open・8 hours agoJava - Clean Solution | Two-PassJava11091All Solutions🔥 Minimal Code with Derivation | O(n) & O(1)Jayant Patel2.2K13 hours agoMathC++JavaPython3
-> Jump to Derived Formula
-> Jump to Code

Intuition

Each move can only increase an element, so nobody can ever go down. That means the final common value can’t be smaller than the current maximum.

If the target were below max, the max element could never reach it.
If the target were above max, every element, including the max one, would need extra moves, so the total only grows.

So the cheapest target is exactly max. Each element nums[i] then needs
max - nums[i] moves, and the answer is the sum of those gaps.

Example: nums = [2, 5, 3, 1, 4], max = 5
2 → 5 costs 3
5 → 5 costs 0
3 → 5 costs 2
1 → 5 costs 4
4 → 5 costs 1
Total = 10

Solution 1 (direct sum of gaps)
Find max, then loop and add max - x for each element.
res = Σ (max − nums[i])   for i = 0..n-1
C++JavaPython3JavaScriptclass Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        res = 0
        for x in nums:
            res += mx - x
        return res

Solution 2 (closed-form formula)
-> Start from Solution 1’s sum:
res = Σ (max − nums[i])
The sum of a difference is the difference of the sums, so split it:
res = Σ max − Σ nums[i]
max is a constant, and adding a constant n times gives n * max:
Σ max = max + max + ... + max   (n times) = n * max
And Σ nums[i] is just the array’s total, sum. Therefore:
res = n * max − sum

Code
C++Python3JavaScriptclass Solution {
public:
    long long minMoves(vector<int>& nums) {
        long long n = nums.size();
        long long mx = *max_element(nums.begin(), nums.end());
        long long sum = accumulate(nums.begin(), nums.end(), 0LL);
        return n * mx - sum;
    }
};

Complexity

Time complexity: O(n)



Space complexity: O(1)



 Previous*NO AI SLOP* JUST ANOTHER EZ MATH PROBLEM (BONUS : FENWICK TREE OVERKILL)Next✅ Beats 98% 🚀 | Greedy 🔥 | Java, C++, Python, JSComments (2)Sort by:BestCommentJayant Patel13 hours agoUpvote if you found this solution helpful. Have a nice day ! Read more4Maria2 hours agoOne line solution Read more1192Python3Auto1234567class Solution:    def minMoves(self, nums: List[int]) -> int:        mx = max(nums)        res = 0        for x in nums:            res += mx - x        return resIn the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 7, Col 19AcceptedRuntime: 0 msCase 1Case 2Inputnums =[2,1,3]Output3Expected3Contribute a testcaseInput912›[2,1,3][4,4,5]Output912›32Expected912›32 All SubmissionsAccepted1016 / 1016 testcases passedMUTHU KUMAR Msubmitted at Nov 03, 2026 18:33AnalysisSolutionCodePython31class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        mx = max(nums)
4        res = 0
5        for x in nums:
6            res += mx - x
7        return res 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
