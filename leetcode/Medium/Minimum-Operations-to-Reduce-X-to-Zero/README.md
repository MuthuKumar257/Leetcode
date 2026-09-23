# 1658. Minimum Operations to Reduce X to Zero

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1658. Minimum Operations to Reduce X to ZeroMediumTopicsCompaniesHintYou are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 
Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.


Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1


Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


 
Constraints:


	1 <= nums.length <= 105
	1 <= nums[i] <= 104
	1 <= x <= 109

 Seen this question in a real interview before?1/6YesNoAccepted287,037/670.2KAcceptance Rate42.8%TopicsStaffArrayHash TableBinary SearchSliding WindowPrefix SumWeekly Contest 215CompaniesHint 1Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.Hint 2Finding the maximum subarray is standard and can be done greedily.Similar QuestionsMinimum Size Subarray SumMediumSubarray Sum Equals KMediumMinimum Operations to Convert NumberMediumRemoving Minimum Number of Magic BeansMediumMinimum Operations to Make the Integer ZeroMediumDiscussion (174)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestShriom Singh BhatiSep 20, 2023I solve most of the problems using brute force and I fear that what if my interviewer ask for an optimized version
 Read more1843Siam AhmedFeb 03, 2023This the best problem I've ever seen in my entire life! Read more585Raghvendra Singh RathoreMar 09, 2023dfs with memo doesnt work in this Read more463Dhruv SinghJul 06, 2023I solved it with dp(got TLE) but I don't think I could have ever come up with subarray solution even if try my entire life. Read more434Atharva YawalkarJan 18, 2026me who though this can be solved using two pointer approach Read more423mstuebsSep 20, 2023Don't submit without testing the edge cases. Try these testcases:
[3914]
3913
[2431]
2432
[8576]
8576
[10,1,10,10,10]
40
https://github.com/mquintus/l33tcode-testcase-generator/blob/main/README.md Read more30jihec2843811 hours agoSee the images if you want to see the premium editorial (no codes) 🙂

 Read moreRead more412Shiva SaiSep 20, 2023hint:
maximum length  of subarray whose sum is sum(nums)-x Read more254sarbajit acharjeeSep 20, 2023Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
Finding the maximum subarray is standard and can be done greedily.
if helpful upvote Read more563123418Copyright © 2026 LeetCode. All rights reserved.6K1743211 Online
@property --beam-angle-_r_7m_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7m_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7m_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7m_"][data-active] {
  animation:
    beam-spin-_r_7m_ 1.96s linear infinite,
    beam-fade-in-_r_7m_ 0.6s ease forwards;
}

[data-beam="_r_7m_"][data-fading] {
  animation:
    beam-spin-_r_7m_ 1.96s linear infinite,
    beam-fade-out-_r_7m_ 0.5s ease forwards;
}

[data-beam="_r_7m_"][data-active]::after,
[data-beam="_r_7m_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7m_),
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
      from var(--beam-angle-_r_7m_),
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
      from var(--beam-angle-_r_7m_),
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
  opacity: calc(var(--beam-opacity-_r_7m_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7m_"][data-active]::before,
[data-beam="_r_7m_"][data-fading]::before {
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
    from var(--beam-angle-_r_7m_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7m_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7m_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7m_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7m_),
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

[data-beam="_r_7m_"][data-active] [data-beam-bloom],
[data-beam="_r_7m_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7m_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7m_ {
  to { --beam-angle-_r_7m_: 360deg; }
}

@keyframes beam-fade-in-_r_7m_ {
  to { --beam-opacity-_r_7m_: 1; }
}

@keyframes beam-fade-out-_r_7m_ {
  from { --beam-opacity-_r_7m_: 1; }
  to { --beam-opacity-_r_7m_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoTypeScriptRustC#KotlinSwiftRubyScalaDartElixirPHPRacketSliding WindowPrefix SumArrayTwo PointersHash TableBinary SearchGreedyBinary TreeDynamic ProgrammingRecursionMemoizationSuffix ArrayOrdered MapIteratorDepth-First SearchBacktrackingMathBreadth-First SearchHeap (Priority Queue)QueueSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Nov 14, 2020Minimum Operations to Reduce X to ZeroEditorial6250.3K27eunice・ Open・13 hours agoMaximum Size Subarray | Two - Pointers | Sliding Window | Beats 100%ArrayTwo PointersSliding WindowPython4+10712.7K3Aura Farming・ Open・12 hours agoᯓ★ 100% Beats ⚡︎ • Master Sliding Window ★ Less Theory • Pookie POTD! ✈︎Two PointersSliding WindowC++Java1+434.3K4An-Wen Deng・ Open・12 hours agoRunning sum + 2 pointers|0msTwo PointersPrefix SumC++141.9K2Md Aarzoo Islam・ Open・11 hours ago0ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayHash TableBinary SearchSliding Window6+121.3K2Aryan Kumar Shaw Halwai・ Open・11 hours agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Sliding WindowArrayHash TableBinary SearchSliding Window5+94140Shakti Pravesh・ Open・10 hours agoTwo Pointers: Enumerating Prefix and Suffix Combinations | O(n) Time | O(1) SpaceArrayHash TableBinary SearchC6+53680Praveen Kumar・ Open・11 hours agoSIMPLE INTUITION | VISUAL EXAMPLE | JAVASliding WindowJava52490Debesh P・ Open・16 hours ago0 ms | beats 100.00% | interview friendly - optimal | sliding window | you won't regret babygirl!ArrayHash TableBinary SearchC6+54181Ajay Choudhary・ Open・13 hours agopython3Python335930Anatoly・ Open・7 hours ago(21ms) pref and post ARRAYKotlin2211lokdalesh・ Open・11 hours ago21% Beats but better approchArraySliding WindowPythonC++2+21751Ujjawal・ Open・4 hours agoSolution that Beats 100%ArrayHash TableBinary SearchSliding Window2+2180Long Nguyen・ Open・5 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+2470Abhishek singh・ Open・6 hours agoVery Easy Solution ✅🔥 || Standard Sliding Window ✅ || One of the best Q || Pure Problem Solving 🔥ArraySliding WindowC++2560All SolutionsMaximum Size Subarray | Two - Pointers | Sliding Window | Beats 100%eunice12.7K13 hours agoArrayTwo PointersSliding WindowPython4+
Intuition
Removing elements from both ends is equivalent to choosing a prefix and a suffix whose combined sum is x.

Let S be the total sum of the input array, the remaining subarray must have sum:
k=S−x​
Inverted Operation
Since minimizing the removed elements is equivalent to maximizing the size of the remaining subarray:

We can instead find the  Maximum Size Subarray Sum Equals k.


Approach
Conceptually, we enumerate the prefix sums starting from each index i.



As shown in virtual 2D grid, the  prefix entries equal to k correspond to the subarrays with sum k, and we want the valid candidate with the maximum size.


However, since all values are positive, we can easily find a candidate by virtually moving the to the right or down.



Or simply by using a sliding window with two pointers in 1D.

Sliding Window
The current sum determines which pointer to move:
sum⎩⎨⎧​<k>k=k​→move right→move left→update max size​​

For the current subarray from left i to right j, its size is:

size=j−i+1​

We keep the larger size as the best candidate for the max size,


Given n is the size of the array, then n−best elements are removed.

Since each removal is one operation, therefore we return:
op=n−best​​

Time Complexity: O(n)
Space Complexity: O(1)

If you found the solution helpful, please UPVOTE, FOLLOW, and ADD TO ⭐.
 PreviousMinimum Operations to Reduce X to ZeroNextᯓ★ 100% Beats ⚡︎ • Master Sliding Window ★ Less Theory • Pookie POTD! ✈︎Comments (3)Sort by:BestCommentPriyadarshi10 hours agowonderful Read more11stasf252 hours agoCOOL!!!
Here is TWO-liner for this task Read more1Saurav Bhandari5 hours agocheat krne se kuch nhi hoga mujhe nhi dekhna solution or hint kyu ki aahii jaayega mujhe bas khud se krna h tabhi me pattern smjh paaunga kyu ki aisa question to nhi milega na mujhe waha Read more0111073Python3Auto6789101112131415161718                s = i = 0                for j, num in enumerate(A):            s += num            while s > k:                s -= A[i]                i += 1              if s == k:                best = max(best, j - i + 1)        return -1 if best < 0 else len(A) - bestSavedLn 18, Col 1AcceptedRuntime: 0 msCase 1Case 2Case 3Inputnums =[1,1,4,2,3]x =5Output2Expected2Contribute a testcaseInput9123456›[1,1,4,2,3]5[5,6,7,8,9]4[3,2,20,1,1,3]10Output9123›2-15Expected9123›2-15 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 23, 2026 18:18AnalysisSolutionCodePython31class Solution:
2    def minOperations(self, A: List[int], x: int) -> int:
3        k = sum(A) - x
4        if k < 0: return -1 
5        best = -1
6        
7        s = i = 0
8        
9        for j, num in enumerate(A):
10            s += num
11            while s > k:
12                s -= A[i]
13                i += 1  
14            if s == k:
15                best = max(best, j - i + 1)
16
17        return -1 if best < 0 else len(A) - best
18View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
