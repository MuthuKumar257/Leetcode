# 1385. Find the Distance Value Between Two Arrays

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit400:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1385. Find the Distance Value Between Two ArraysAttemptedEasyTopicsCompaniesHintGiven two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 
Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2


Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2


Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1


 
Constraints:


	1 <= arr1.length, arr2.length <= 500
	-1000 <= arr1[i], arr2[j] <= 1000
	0 <= d <= 100

 Seen this question in a real interview before?1/6YesNoAccepted226,348/295.2KAcceptance Rate76.7%TopicsMid LevelArrayTwo PointersBinary SearchSortingBiweekly Contest 22CompaniesHint 1Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]', it gives a time complexity of O(nlogn).Discussion (216)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestArthur KimFeb 17, 2023It seems like english test. Read more3513Eti-ini Effiong-RobertApr 08, 2022I spent a lot of time testing different implementations and trying to deal with errors, before I realized that the question itself isn't properly phrased. The example too is opaque unless you already know the answer.
You're supposed to count the elements in arr1 that do NOT yield a value <= d when any element from arr2 is subtracted from it. To explain the example;
arr1[0] = 4 doesn't violate the condition. Hence, we count it.
arr1[1] = 5 also doesn't violate the condition. We also count it, bringing our count to two.
arr1[8] = 8 violates the condition, so it isn't counted.
Since that's the end of arr1, the total number of GOOD numbers we have is 2. That's why the output is 2 Read more31014DonutloopMar 25, 2020This description is pretty bad and example, language are very misleading. Read more6803Suman KumarMay 27, 2022If anyone understand this question then please explain me. Read more1084AurèleApr 07, 2023Rephrased:
You are given two integer arrays arr1 and arr2, and an integer d. The problem asks you to find the number of elements in arr1 that are at a distance of more than d from all the elements in arr2. Here, the distance between two integers a and b is defined as |a - b|.
For example, if arr1 = [4, 5, 8], arr2 = [10, 9, 1, 8], and d = 2, then the answer would be 2 because there are only two elements in arr1 (i.e., 4 and 5) that are at a distance of more than 2 from all the elements in arr2. Read more873ansumanbOct 20, 2022Example 1:
arr1 = [4,5,8] arr2 = [10,9,1,8] d = 2
----arr1[0]---
|4-(10)|=6 6 <= 2 is False
|4-(9)|=5 5 <= 2 is False
|4-(1)|=3 3 <= 2 is False
|4-(8)|=4 4 <= 2 is False
Since for this i=0 we have all false, consider this row
----arr1[1]---
|5-(10)|=5 5 <= 2 is False
|5-(9)|=4 4 <= 2 is False
|5-(1)|=4 4 <= 2 is False
|5-(8)|=3 3 <= 2 is False
Since for this i=1 we have all false, consider this row
----arr1[2]---
|8-(10)|=2 2 <= 2 is True
|8-(9)|=1 1 <= 2 is True
|8-(1)|=7 7 <= 2 is False
|8-(8)|=0 0 <= 2 is True

Answer is total number of rows we have considered 2
Example 2:
arr1 = [1,4,2,3] arr2 = [-4,-3,6,10,20,30] d = 3
----arr1[0]---
|1-(-4)|=5 5 <= 3 is False
|1-(-3)|=4 4 <= 3 is False
|1-(6)|=5 5 <= 3 is False
|1-(10)|=9 9 <= 3 is False
|1-(20)|=19 19 <= 3 is False
|1-(30)|=29 29 <= 3 is False
Since for this i=0 we have all false, consider this row
----arr1[1]---
|4-(-4)|=8 8 <= 3 is False
|4-(-3)|=7 7 <= 3 is False
|4-(6)|=2 2 <= 3 is True
|4-(10)|=6 6 <= 3 is False
|4-(20)|=16 16 <= 3 is False
|4-(30)|=26 26 <= 3 is False
----arr1[2]---
|2-(-4)|=6 6 <= 3 is False
|2-(-3)|=5 5 <= 3 is False
|2-(6)|=4 4 <= 3 is False
|2-(10)|=8 8 <= 3 is False
|2-(20)|=18 18 <= 3 is False
|2-(30)|=28 28 <= 3 is False
Since for this i=2 we have all false, consider this row
----arr1[3]---
|3-(-4)|=7 7 <= 3 is False
|3-(-3)|=6 6 <= 3 is False
|3-(6)|=3 3 <= 3 is True
|3-(10)|=7 7 <= 3 is False
|3-(20)|=17 17 <= 3 is False
|3-(30)|=27 27 <= 3 is False

Answer is total number of rows we have considered 2
Example 3:
arr1 = [2,1,100,3] arr2 = [-5,-2,10,-3,7] d = 6
----arr1[0]---
|2-(-5)|=7 7 <= 6 is False
|2-(-2)|=4 4 <= 6 is True
|2-(10)|=8 8 <= 6 is False
|2-(-3)|=5 5 <= 6 is True
|2-(7)|=5 5 <= 6 is True
----arr1[1]---
|1-(-5)|=6 6 <= 6 is True
|1-(-2)|=3 3 <= 6 is True
|1-(10)|=9 9 <= 6 is False
|1-(-3)|=4 4 <= 6 is True
|1-(7)|=6 6 <= 6 is True
----arr1[2]---
|100-(-5)|=105 105 <= 6 is False
|100-(-2)|=102 102 <= 6 is False
|100-(10)|=90 90 <= 6 is False
|100-(-3)|=103 103 <= 6 is False
|100-(7)|=93 93 <= 6 is False
Since for this i=2 we have all false, consider this row
----arr1[3]---
|3-(-5)|=8 8 <= 6 is False
|3-(-2)|=5 5 <= 6 is True
|3-(10)|=7 7 <= 6 is False
|3-(-3)|=6 6 <= 6 is True
|3-(7)|=4 4 <= 6 is True

Answer is total number of rows we have considered 1 Read more906Jahon BozarovJan 15, 2023Very bad example given. I did not understand until read this discussion part. Thanks all Read more421Shubham IngoleDec 14, 2022I think question setter also doesn't understand what he have written here. lol Read moreFeedback271Nitish KumarJun 25, 2021This code  has very Bad description it doesn't  match with example given Read more26MahmOud_GaDJan 24, 2023This description is pretty bad and test cases are very misleading. Read more15123422Copyright © 2026 LeetCode. All rights reserved.1.2K2162584 Online
@property --beam-angle-_r_7j_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7j_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7j_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7j_"][data-active] {
  animation:
    beam-spin-_r_7j_ 1.96s linear infinite,
    beam-fade-in-_r_7j_ 0.6s ease forwards;
}

[data-beam="_r_7j_"][data-fading] {
  animation:
    beam-spin-_r_7j_ 1.96s linear infinite,
    beam-fade-out-_r_7j_ 0.5s ease forwards;
}

[data-beam="_r_7j_"][data-active]::after,
[data-beam="_r_7j_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7j_),
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
      from var(--beam-angle-_r_7j_),
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
      from var(--beam-angle-_r_7j_),
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
  opacity: calc(var(--beam-opacity-_r_7j_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7j_"][data-active]::before,
[data-beam="_r_7j_"][data-fading]::before {
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
    from var(--beam-angle-_r_7j_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7j_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7j_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7j_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7j_),
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

[data-beam="_r_7j_"][data-active] [data-beam-bloom],
[data-beam="_r_7j_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7j_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7j_ {
  to { --beam-angle-_r_7j_: 360deg; }
}

@keyframes beam-fade-in-_r_7j_ {
  to { --beam-opacity-_r_7j_: 1; }
}

@keyframes beam-fade-out-_r_7j_ {
  from { --beam-opacity-_r_7j_: 1; }
  to { --beam-opacity-_r_7j_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++CPythonJavaScriptC#GoTypeScriptSwiftKotlinRustDartRubyPHPScalaElixirRacketBinary SearchArrayBinary TreeSortingTwo PointersMathBrute-Force SearchIteratorOrdered SetDynamic ProgrammingRecursionHash TableTreeDepth-First SearchGreedySweep LineCountingBinary Search TreeBucket SortSliding WindowCounting SortBinary Indexed TreePrefix SumMerge SortCombinatoricsDesignSegment TreeSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Nov 02, 2026Find the Distance Value Between Two ArraysEditorial1111.9K10Aleksandr・ Open・18 hours ago✅ Keep Your Distance | O(n·m) → O(n + m) Explained | Beats 100%Two PointersBinary SearchSortingPython6+849.2K4Aryan Kumar Shaw Halwai・ Open・13 hours ago✅ Beats 99% 🚀 | Check Every Pair, Stop at the First Close Value 🔥 | Java, C++, Python, JSArrayTwo PointersBinary SearchSorting6+171.6K1Shubhashree Sahu・ Open・9 hours agoShubha's LogicC++161.1K4VipeenKumar・ Open・14 hours agoBrute Force & Binary Search | Question in simple wordsArrayTwo PointersBinary SearchSorting3+66620Bijoy Sing・ Open・15 hours ago✅Optimal Solution→ ⏳ O(n log n + m log m) || Sorting + Two Pointers || C++, Python, JS, GoArrayTwo PointersSortingPython3+61.2K0Ujjawal・ Open・10 hours agoSolution that Beats 100%ArrayTwo PointersBinary SearchDynamic Programming5+41620amitK300・ Open・2 hours ago2 loop Solution ↗️Java3831MBBN・ Open・15 hours agoJava - Clean Solution | Sorting + Two PointersJava36001Nilesh_Odedara・ Open・3 hours agoBrute Force | Nested Loops | Absolute DifferenceArrayTwo PointersBinary SearchSorting1+3400MikPosp・ Open・6 hours ago✅ One Line SolutionArrayBinary SearchSortingPython1+31820hj-core・ Open・10 hours agoMy kotlin solution with time O(N1+N2+M) and space O(M)Kotlin2271Anatoly・ Open・11 hours ago(11ms) Something like this...Kotlin2171Anatoly・ Open・8 hours ago(3ms) array of invalidKotlin2191Suraj Kumar・ Open・7 hours ago2 Approaches ✅| Sorting + Binary Search & Brute-Force🚀| JAVA/C++/Python/JS | O(m * n) Time & O(1) ArrayBinary SearchSortingPython3+21050All Solutions✅ One Line SolutionMikPosp1826 hours agoArrayBinary SearchSortingPython1+Code #1
Time complexity: O(n⋅m). Space complexity: O(1).
class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(d<min(abs(v-u) for u in b) for v in a)
Code #2
Time complexity: O(m+n⋅d). Space complexity: O(m).
class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(map({*b}.isdisjoint,(range(v-d,v+d+1) for v in a)))
Code #3
Time complexity: O((n+m)⋅log(m)). Space complexity: O(m).
class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        b.sort()
        return sum(bisect_left(b,v-d)==bisect_right(b,v+d) for v in a)
Code #4
Time complexity: O((n+m)⋅log(m)). Space complexity: O(m).
class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        b = sorted(b+[-inf,inf])
        return sum(b[i:=bisect_left(b,v)]-v>d<v-b[i-1] for v in a) NextFind the Distance Value Between Two ArraysComments (0)Sort by:BestCommentNo comments yet.30Python3Auto123class Solution:    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:        return sum(d<min(abs(v-u) for u in b) for v in a)In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 3, Col 58AcceptedRuntime: 0 msCase 1Case 2Case 3Inputarr1 =[4,5,8]arr2 =[10,9,1,8]d =2Output2Expected2Contribute a testcaseInput9123456789›[4,5,8][10,9,1,8]2[1,4,2,3][-4,-3,6,10,20,30]3[2,1,100,3][-5,-2,10,-3,7]6Output9123›221Expected9123›221 All SubmissionsAccepted103 / 103 testcases passedMUTHU KUMAR Msubmitted at Nov 05, 2026 20:43AnalysisSolutionCodePython31class Solution:
2    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
3        return sum(d<min(abs(v-u) for u in b) for v in a) 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
