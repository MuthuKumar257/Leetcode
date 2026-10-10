# 2333. Minimum Sum of Squared Difference

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit500:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsPending...Pending...SubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result2333. Minimum Sum of Squared DifferenceAttemptedMediumTopicsCompaniesHintYou are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 
Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.


Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

 
Constraints:


	n == nums1.length == nums2.length
	1 <= n <= 105
	0 <= nums1[i], nums2[i] <= 105
	0 <= k1, k2 <= 109

 Seen this question in a real interview before?1/6YesNoAccepted62,393/161.6KAcceptance Rate38.6%TopicsStaffArrayBinary SearchGreedySortingHeap (Priority Queue)Biweekly Contest 82CompaniesHint 1There is no difference between the purpose of k1 and k2. Adding +1 to one element in nums1 is same as performing -1 to one element in nums2, and vice versa.Hint 2Reduce the sum of squared difference greedily. One operation of k should use the index that has the current maximum difference.Hint 3Binary search the maximum difference for the final result.Similar QuestionsMinimum Absolute Sum DifferenceMediumPartition Array Into Two Arrays to Minimize Sum DifferenceHardDiscussion (154)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestKeming He15 hours agoIt's finally over. No more parenthesis! 😂 Read more3845MCAOct 25, 2025Priority queue my ass. Its a counting problem; the pq solution gave me TLE. Read more10912hiteshh11 hours agoParentheses were better !! Read more74JEYSAN_Va day agoFinally we get rid of parentheses problems Read more705user13513968136132683Jul 09, 2022This is actually a joke. Why do people cheat on leetcode contests as if it is going to help them in the interviews?? Read moreRead more1076cruzerblade8213 hours agoAcceptance Rate giving the vibe of getting jobs these days Read more34Dany RendonOct 01, 2026[18,4,8,19,13,8]
[18,11,8,2,13,15]
16
8
[20,19,3,18,16,20,0]
[39,5,3,1,30,1,14]
6
14
[1,2,3,4]
[2,4,5,7]
0
1
[32,17,74,75,84,56,52,29,67,71,6,1,92,51,9,100,49,95,24,42,34,36,19,53,65,13,98,86,70,29,89,32,46,89,17,21,56,68,98,75,44,31,56,6,74,23,48,10,40,55,4,99,35,42,15,42,97,10,72,75,14,49,1,61,6,37,41,31,23,66,15,91,30,96,44,23,31,28,24,75,68,52,7,21,7,54,88,7,52,98,25,15,58,31,33,0,55,89,45,5]
[21,91,81,85,20,41,90,71,64,31,56,22,16,22,15,30,13,78,30,12,44,0,56,32,10,44,47,84,57,43,30,86,75,77,47,86,57,45,33,62,73,17,92,12,7,88,63,6,67,91,37,49,60,57,89,89,21,15,4,83,7,1,89,30,25,27,12,63,60,31,96,33,28,97,53,75,19,100,78,52,96,91,92,91,90,38,7,88,19,86,27,38,37,27,61,71,52,23,4,41]
138
3351
[100,100,100,100,100,100,0,0,100,100,100,100,100,0,100,0,0,100,100,0,0,100,0,0,100,0,0,100,100,0,100,0,100,100,0,100,0,0,0,0,0,100,0,0,100,0,0,0,0,100,100,0,100,100,0,0,100,100,0,100,100,100,100,100,0,0,100,0,0,100,0,0,0,100,0,0,100,0,100,0,0,100,100,0,0,0,0,0,100,0,0,100,0,100,100,100,100,0,100,100]
[0,0,0,0,0,0,100,100,0,0,0,0,0,100,0,100,100,0,0,100,100,0,100,100,0,100,100,0,0,100,0,100,0,0,100,0,100,100,100,100,100,0,100,100,0,100,100,100,100,0,0,100,0,0,100,100,0,0,100,0,0,0,0,0,100,100,0,100,100,0,100,100,100,0,100,100,0,100,0,100,100,0,0,100,100,100,100,100,0,100,100,0,100,0,0,0,0,100,0,0]
0
0
[95,88,29,22,91,15,91,48,90,16,4,22,14,81,43,34,90,14,51,80,41,4,1,35,5,22,44,26,23,42,59,95,4,58,51,38,33,19,52,21,13,17,83,68,13,77,100,75,71,63,39,14,82,52,11,61,24,86,60,72,74,99,45,46,10,17,27,72,66,65,59,63,54,29,85,77,25,58,2,16,92,77,89,8,100,80,12,22,81,27,60,96,90,41,83,24,37,22,88,67]
[95,88,29,22,91,15,91,48,90,16,4,22,14,81,43,34,90,14,51,80,41,4,1,35,5,22,44,26,23,42,59,95,4,58,51,38,33,19,52,21,13,17,83,68,13,77,100,75,71,63,39,14,82,52,11,61,24,86,60,72,74,99,45,46,10,17,27,72,66,65,59,63,54,29,85,77,25,58,2,16,92,77,89,8,100,80,12,22,81,27,60,96,90,41,83,24,37,22,88,67]
45
7
[61,19,9,47,42,51,57,42,66,92,68,28,51,85,54,52,16,33,92,86,62,1,32,73,11,23,66,49,55,57,99,99,63,19,98,36,51,48,27,11,75,24,43,34,93,95,73,55,31,31,14,6,12,26,79,54,96,23,87,9,2,8,58,60,20,41,53,55,53,33,99,79,95,2,79,86,74,30,92,90,12,98,5,83,84,17,65,33,99,50,91,25,50,69,56,20,55,76,86,44]
[62,18,8,48,41,50,56,43,65,91,69,29,52,84,55,53,17,34,93,85,63,0,33,74,10,22,67,48,56,58,98,100,64,18,99,37,50,47,28,10,74,25,42,35,92,94,74,54,32,30,13,7,13,27,78,53,95,22,88,10,1,9,57,61,19,40,52,56,54,32,100,80,94,1,78,85,73,31,93,89,13,99,6,82,85,18,66,34,100,49,90,26,49,68,55,21,54,75,87,43]
85
37
[73,90,17,30,22,70,6,4,25,89,23,70,33,38,30,85,16,68,17,65,22,62,26,31,70,61,34,100,35,75,78,96,37,32,33,87,25,14,4,6,80,16,4,25,97,12,100,73,73,16,73,32,93,31,81,99,92,64,20,98,61,36,63,96,26,7,21,72,5,74,80,93,64,82,75,23,16,32,87,73,78,89,86,22,74,93,16,88,97,21,82,12,36,37,67,61,70,68,64,100]
[12,29,78,91,83,9,67,65,86,28,84,9,94,99,91,24,77,7,78,4,83,1,87,92,9,0,95,39,96,14,17,35,98,93,94,26,86,75,65,67,19,77,65,86,36,73,39,12,12,77,12,93,32,92,20,38,31,3,81,37,0,97,2,35,87,68,82,11,66,13,19,32,3,21,14,84,77,93,26,12,17,28,25,83,13,32,77,27,36,82,21,73,97,98,6,0,9,7,3,39]
4710
162 Read more31Varun DharAug 13, 2024Bit confusing description,
Are we allowed to modify elements in total of k1/k2 times, or every single element can be modified k1 times? Read moreAsk Question244SanjayJun 08, 2025Very good problem:
You will find similar approach in many problems, it help you to use map and priority queue at once.
Hint 1:
Goal is to minimize sum of abs(nums1[i]-nums2[j])^2 now will k1 and k2 make a difference if we are minimizing each sum then we can either do operation on nums1 using k1 or on nums2 using k2 so we are minimizing each abs(nums[1]-nums[2]) so k1 and k2 does not matter.
Hint 2:
Now if you have a sorted difference array 2 3 4 5 and K as 5 then what would you reduce minimum like 2 or maximum which is 5?
If you reduce from start you get 0*0 + 0*0 + 4*4 + 5*5 = 41, now if you reduce from last then you get 2*2 + 3*3 + 4*4 = 29, so it is proven that we will remove elements from the maximum.
Hint 3:
Now in a sorted difference array like 1 1 2 2 4 4 4 5 5 5 5 you will reduce each element from last by 1 K times and to selecting maximum element you will use priority queue, but there is a problem what is the time complexity?
K*(NlogN) - reason is that we are finding maximum using priority queue and reducing only 1 element k` times.
With this much information you can solve it by thinking how to effectively perform such operation.
Hint 4:
Now let assume we have array as 4 4 4 4 4 and k as 5 now how to do reduce each element by 1 k times effectively?
Store in map. Then mp[4]=5 if k>=5 we can reduce each element in O(1) by making it 3 3 3 3 3 and directly updating it in map and store it in priority queue again.
And to make it consistent for each element of priority queue check the map.
Code for checking element is same in map and priority queue:
            int el=pq.top().first,fr=pq.top().second;             pq.pop();             if(mp[el]!=fr || el==0){                 continue;             } Read moreTip233Ronit RoushanAug 25, 2023Testcase 27 spoils your mood. Read more182123416Copyright © 2026 LeetCode. All rights reserved.8961542779 Online
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

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptRustGoTypeScriptSwiftC#KotlinScalaRacketRubyPHPGreedyHeap (Priority Queue)ArraySortingBinary SearchMathBinary TreeBucket SortHash TableCounting SortCountingTreeOrdered MapOrdered SetIteratorRecursionDynamic ProgrammingSimulationSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・12 hours agoMinimum Sum of Squared DifferenceEditorial615.4K8Ashok Varma・ Open・14 hours agoShave the Tallest Differences | Bucket Count, No Sorting | Easy IntuitionArrayBinary SearchGreedySorting6+1188K9Vaibhav Raj Singh・ Open・3 hours agoEasy Greedy SolutionGreedyC++233.8K1Md Aarzoo Islam・ Open・13 hours ago16ms | Beats 59.22% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayBinary SearchGreedySorting6+194K3Bijoy Sing・ Open・15 hours ago✅ Most Optimal Solution → ⏳ O(n + M) | Bucket + Greedy | C++, Python, Java, JavaScript, GoC++2610.1K3Vaibhav Raj Singh・ Open・13 hours agoEasy Greedy SolutionMathGreedyC++356.7K2Aryan Kumar Shaw Halwai・ Open・13 hours agoGreedy + Frequency Counting🔥| No BS + Easiest Solution with Step by Step Breakdown💯ArrayBinary SearchGreedySorting5+115661Baraa・ Open・15 hours agoGreedy + Binary Search | O(n log M) | Python, C++, Java, JavaScript & Go | ExplainedArrayBinary SearchGreedySorting6+102.3K1chaharharsh67・ Open・13 hours agoBinary Search & Greedy | Easy to Understand 🚀Java77691Long Nguyen・ Open・10 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+64721Boringpizza・ Open・4 hours agoGreedy (Sorting and Leveling Differences)| N logn Approach(Independent of k)MathGreedySortingC++5541Heyyy・ Open・6 hours agoMinimum Sum of Squared Difference | Greedy + Frequency ArrayGreedyHeap (Priority Queue)C++5890An-Wen Deng・ Open・3 hours agoGreedy Counting sort|0msGreedyCounting SortC++3262DailyDoseOfLeetCode・ Open・10 hours ago[YouTube Video] Java | Python | ✅ Simple problem and approach explanationArrayGreedyCountingJava1+32081YUVRAJ GULERIA・ Open・13 hours ago🔥 2 Approaches || 🚀 Priority Queue (Greedy) vs Optimal Bucket Sort || O(N) MasterpieceGreedySwiftSortingPython6+34251EdgeCaseOffByOne・ Open・44 minutes agoMinimum Sum of Squared Difference | Binary Search + Greedy | C++ SolutionArrayBinary SearchGreedySorting1+380DHRUVIK・ Open・5 hours agoEasy Greedy Approach + Frequency Array C++3590Vedansh Rathod・ Open・9 hours ago⚡ Flatten the Peaks | 🔥 Greedy Leveling | O(n log n) Squared-Difference OptimizationArrayMathGreedySorting1+2341grimreaper1212・ Open・11 hours agoGreedy Counting O(N+M)Python323351MikPosp・ Open・2 hours ago✅ Four Simple Lines of CodeArrayBinary SearchPythonPython32660Abhinav Rai・ Open・12 hours agoSimple Binary Search Approach | JavaArrayBinary SearchGreedySorting1+2880Aamod Dwivedi・ Open・14 hours agoMinimum Sum Of Squared Difference || Easy to understandArrayBinary SearchGreedySorting2+22700venkadasesan・ Open・15 hours agoBeats 100% | Ultimate O(N) Time / O(1) Space Greedy Solution / python3 , C , C++ ,JavaCC++JavaPython325770iLaliso・ Open・5 hours agoGreedy + Sorting + Binary Search (lower_bound) + Difference Array | O(n log n)C++1121Alexey Minkin・ Open・7 hours agoKotlin | O(n + C) (6ms) | O(C)ArrayGreedySortingCounting Sort1+1171Varun Bhutada・ Open・7 hours ago2333. Minimum Sum of Squared Difference | Binary Search + Greedy Leveling | JavaArrayBinary SearchGreedyJava1171MBBN・ Open・7 hours agoJava - Clean Solution | Greedy + Frequency ArrayJava1261Prabhas Sharma・ Open・11 hours ago2333. Minimum Sum of Squared DifferencePython311501Sadman Hafiz Shuvo・ Open・40 minutes agoGreedily Reduce Largest Gaps Between Arrays 📉ArrayBinary SearchGreedySorting2+120Aizen・ Open・42 minutes agoBruteForce to Optimized Easy Explained | Java | cpp | pythonArrayGreedySortingHeap (Priority Queue)4+130All SolutionsGreedy Counting O(N+M)grimreaper121234711 hours agoPython3Intuition
Greedy/Counting
Complexity


Time complexity:
O(N+M)


Space complexity:
O(N)


Code
Python3class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        k = k1 + k2

        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))

        counter = Counter(diff)

        maxDiff = max(counter.keys())

        for val in range(maxDiff, 0, -1):

            if k <= 0:
                break

            sub = min(k, counter[val])
            counter[val] -= sub
            counter[val-1] += sub
            k -= sub

        res = 0

        for d, v in counter.items():
            res += (d**2) * v
        return res


            
                

                





 NextMinimum Sum of Squared DifferenceComments (1)Sort by:BestCommentLogicalLuminary9 hours agoOh , its nice to realise that if we do binary search maxdiff , we miss the no of elements with diff >= maxdiff , so we need On more to check , but if we decrease maxdiff by 1 , we can maintain that in O1 .
I somehow assumed that elements in nums1 go uptp 1e9 , otherwise i would have thought of your approach.
Thank You Read more1121Python3Auto26272829303132333435363738            res += (d**2) * v        return res                                            SavedLn 38, Col 1AcceptedRuntime: 0 msCase 1Case 2Inputnums1 =[1,2,3,4]nums2 =[2,10,20,19]k1 =0k2 =0Output579Expected579Contribute a testcaseInput912345678›[1,2,3,4][2,10,20,19]00[1,4,10,12][5,8,6,9]11Output912›57943Expected912›57943 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Oct 10, 2026 20:26AnalysisSolutionCodePython31class Solution:
2    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
3        diff = []
4        k = k1 + k2
5
6        for i in range(len(nums1)):
7            diff.append(abs(nums1[i] - nums2[i]))
8
9        counter = Counter(diff)
10
11        maxDiff = max(counter.keys())
12
13        for val in range(maxDiff, 0, -1):
14
15            if k <= 0:
16                break
17
18            sub = min(k, counter[val])
19            counter[val] -= sub
20            counter[val-1] += sub
21            k -= sub
22
23        res = 0
24
25        for d, v in counter.items():
26            res += (d**2) * v
27        return res
28
29
30            
31                
32
33                
34
35
36
37
38View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
