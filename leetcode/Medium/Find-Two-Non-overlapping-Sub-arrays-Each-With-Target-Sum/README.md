# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

- **Difficulty:** Medium
- **Language:** Java
- **LeetCode Link:** [Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## Solution

See [`solution.java`](./solution.java).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionPending...Pending...EditorialEditorialSolutionsSolutionsSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1477. Find Two Non-overlapping Sub-arrays Each With Target SumAttemptedMediumTopicsCompaniesHintYou are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 
Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.


Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.


Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.


 
Constraints:


	1 <= arr.length <= 105
	1 <= arr[i] <= 1000
	1 <= target <= 108

 Seen this question in a real interview before?1/6YesNoAccepted63,622/163.6KAcceptance Rate38.9%TopicsStaffArrayHash TableBinary SearchDynamic ProgrammingSliding WindowBiweekly Contest 28CompaniesHint 1Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.Hint 2The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where n == arr.length.Hint 3If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.Similar QuestionsFind Subarrays With Equal SumEasyDiscussion (46)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestitsokayAug 09, 2020Shouldn't this one be a hard one ? Read more936srikanth248Feb 01, 2021The question says 2 non-overlapping sub arrays.
How can the answer for [1,6,1] target 7 be 4? [1,6] and [6,1] are overlapping sub arrays. Read more143Limon020Oct 11, 2023tricky, mixing a couple different topics together. Really good question Read more123Biligo3 hours agoMore overlapping/non-overlapping problems omg Read more10Kushal NagwanshiJan 11, 2023Real great question imo !! Read more7sairammmmmmmmmmmmAug 23, 2025prefix sum + binary_search + suffix_min + binary_search on pairs
fantastic question to revise all of the concepts !!! Read more51KiraAug 22, 2024Sliding Window + Dp is Love Read moreFeedback52LC123Sep 10, 2020[1,1,1,2,2,2,4,4]
6
This should return len =6 (index 1 thorugh 4) + (index 5 through 6) but test case expects -1 Read more4Alex JiNov 09, 2023Test case is wrong on the definition of overlapping
test: arr =[2,1,3,3,2,3,1] target =6
Expected output is 5, it is only true if you consider [2,1,3] and [3,3]
but it should be 6, which is  [2,1,3] and [2,3,1] Read more32Shivam Rajput2 hours agoYesterday: K non-overlapping line segments.
Today: Two non-overlapping subarrays.
LeetCode is taking social distancing way too seriously. 💀😂
At this point, the only things overlapping are my confusion and yesterday's DP trauma. 🫠 Read more2112345Copyright © 2026 LeetCode. All rights reserved.1.8K462746 Online
@property --beam-angle-_r_8m_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_8m_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_8m_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_8m_"][data-active] {
  animation:
    beam-spin-_r_8m_ 1.96s linear infinite,
    beam-fade-in-_r_8m_ 0.6s ease forwards;
}

[data-beam="_r_8m_"][data-fading] {
  animation:
    beam-spin-_r_8m_ 1.96s linear infinite,
    beam-fade-out-_r_8m_ 0.5s ease forwards;
}

[data-beam="_r_8m_"][data-active]::after,
[data-beam="_r_8m_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_8m_),
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
      from var(--beam-angle-_r_8m_),
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
      from var(--beam-angle-_r_8m_),
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
  opacity: calc(var(--beam-opacity-_r_8m_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_8m_"][data-active]::before,
[data-beam="_r_8m_"][data-fading]::before {
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
    from var(--beam-angle-_r_8m_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_8m_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_8m_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_8m_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_8m_),
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

[data-beam="_r_8m_"][data-active] [data-beam-bloom],
[data-beam="_r_8m_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_8m_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_8m_ {
  to { --beam-angle-_r_8m_: 360deg; }
}

@keyframes beam-fade-in-_r_8m_ {
  to { --beam-opacity-_r_8m_: 1; }
}

@keyframes beam-fade-out-_r_8m_ {
  from { --beam-opacity-_r_8m_: 1; }
  to { --beam-opacity-_r_8m_: 0; }
}

LeetSort byAllMy SolutionJavaC++Python3PythonCJavaScriptC#GoSwiftScalaRustKotlinDartPHPRubyRacketElixirErlangTypeScriptSliding WindowDynamic ProgrammingPrefix SumArrayHash TableBinary SearchTwo PointersSuffix ArrayGreedyBinary TreeMathMemoizationDivide and ConquerQueueSortingHeap (Priority Queue)Sweep LineSegment TreeSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Sep 09, 2026Find Two Non-overlapping Sub-arrays Each With Target SumEditorial33.4K5eunice・ Open・4 hours agoSliding Window + Prefix DP | 2D Visualization | Easy Explanation | Beats 100%Two PointersDynamic ProgrammingSliding WindowPrefix Sum5+202.6K3An-Wen Deng・ Open・3 hours agoSliding window+ DP|beats 100%Dynamic ProgrammingSliding WindowC++112372Md Aarzoo Islam・ Open・an hour ago3ms | Beats 94.59% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayHash TableBinary SearchDynamic Programming6+113011Aryan Kumar Shaw Halwai・ Open・an hour agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | Sliding Window + 1D DPArrayHash TableBinary SearchDynamic Programming5+71410Ritik Saini・ Open・3 hours agoSimple way to solve 2 ways || Sliding window + prefix/suffix map || DPArrayDynamic ProgrammingSliding WindowC++83450Debesh P・ Open・10 hours ago0 ms | beats 100.00% | dynamic programming | sliding window | you won't regret babygirl!ArrayHash TableBinary SearchDynamic Programming6+42191EdgeCaseOffByOne・ Open・an hour agoSliding Window + DP: The Trick Behind LeetCode 1477 With Video ExplanationArrayDynamic ProgrammingSliding WindowC++3200Aryan Yadav・ Open・3 hours agoBeat 100 % Simple Python331030Utkarsh Tiwari・ Open・14 minutes ago⭕🔺Clean & Short Solution || Sliding WindowArrayDynamic ProgrammingCSliding Window6+270Deku・ Open・2 hours agoSegment Tree + Binary Search + Prefix Sum 🔥|| Simple Explanation⚡|| cpp | python | JavaArrayHash TableBinary SearchDynamic Programming6+2400Seither・ Open・2 hours agoSliding Window + Best Previous Subarray | O(n) Time | Beats 100%ArrayDynamic ProgrammingSliding WindowPython32430Deepak_Vikin・ Open・19 minutes agoSliding Window + DP: Find the Two Shortest Non-Overlapping SubarraysDynamic ProgrammingSliding WindowPrefix SumPython3130Vedansh Rathod・ Open・an hour ago🪟 Two Windows Beat Brute Force | 🚀 Target-Sum Pairing in O(n) | 🧠 Easy Python SolutionArrayTwo PointersDynamic ProgrammingSliding Window3+160Shuvom Dhar・ Open・2 hours agoOptimized solutionArrayHash TableBinary SearchDynamic Programming2+1230All Solutions0 ms | beats 100.00% | dynamic programming | sliding window | you won't regret babygirl!Debesh P21910 hours agoArrayHash TableBinary SearchDynamic Programming6+

This one looks like a normal subarray-sum problem.
And the first thing that probably comes to mind is:

"Okay, find all subarrays whose sum is target, then somehow pick two that don't overlap."

That thought is correct.
But there is a problem.
There can be many such subarrays.
so now we need to efficiently find the best pair.
The beautiful part of this solution is that we don't need to store all valid subarrays. We only need to remember the shortest valid subarray we've seen so far.
And once that clicks, the whole solution becomes surprisingly clean.

1. First Understand the Problem
We are given:
arr
and:
target
We need to find two non-overlapping subarrays whose sums are both equal to target.
Among all possible pairs, we want the minimum:
length(subarray1) + length(subarray2)
If no such pair exists:
return -1
For example:
arr = [3, 2, 2, 4, 3]
target = 3
We have:
[3]
and:
[3]
at the end.
They don't overlap.
So:
1 + 1 = 2
and the answer is:
2

2. Why Brute Force Is Bad
The most obvious approach is:
Take every possible subarray and check whether its sum is target.
Then try every pair of valid subarrays and check whether they overlap.
That can get expensive very quickly.
Even just finding all subarrays is already:
O(n²)
And comparing pairs can make things even worse.
We need something much closer to:
O(n)
And fortunately, the array contains positive integers.
That detail is extremely important.

3. Positive Numbers Give Us a Sliding Window
Because every element is positive:
arr[i] > 0
when we increase the right pointer:
sum increases
And when we move the left pointer:
sum decreases
There is no weird behavior where the sum can suddenly go up after removing an element.
That makes the classic sliding window perfect.
We'll maintain:
l = left boundary
r = right boundary
sum = sum of arr[l...r]
For every r:
sum += arr[r];
If the sum gets too large:
while (sum > target) {
    sum -= arr[l++];
}
After that, there are only two possibilities.
Either:
sum < target
or:
sum == target
If:
sum == target
we have found a valid subarray.

4. Finding One Valid Subarray Is Not Enough
Suppose we find:
[l ... r]
whose sum is target.
Its length is:
r - l + 1
Let's call it:
currLen
Now we need another valid subarray that doesn't overlap with this one.
Since the current subarray starts at:
l
any previous subarray ending before:
l
will automatically be non-overlapping.
So we need to answer:

Among all valid subarrays that end before l, what is the shortest one?

And this is the key observation.

5. The minLen Array
This is why we maintain:
int[] minLen = new int[n];
For every index i:
minLen[i]
means:

The minimum length of any valid subarray whose right endpoint is at or before i.

That sentence is the most important part of the entire solution.
For example, suppose we have already found:
[0...2] → length 3
[4...4] → length 1
Then:
minLen[0] = INF
minLen[1] = INF
minLen[2] = 3

minLen[3] = 3
minLen[4] = 1
Notice something interesting.
Once we know a valid subarray of length 1 exists by index 4, every later position also remembers that 1.
So:
minLen[i]
is effectively a prefix minimum.

6. Why Do We Need Prefix Minimum?
Suppose our current valid subarray is:
[l ... r]
We want an earlier valid subarray that ends before l.
We don't care exactly where it ended.
We only care about:
the shortest one among all valid subarrays ending before l
And that is exactly what:
minLen[l - 1]
stores.
So if:
minLen[l - 1] != Integer.MAX_VALUE
then a compatible previous subarray exists.
And we can try:
currLen + minLen[l - 1]
This gives a candidate answer.

7. This Is The Main Formula
Suppose the current valid subarray is:
[l ... r]
with length:
currLen = r - l + 1
Then the best previous non-overlapping subarray is already stored in:
minLen[l - 1]
Therefore:
candidate answer
=
currLen + minLen[l - 1]
So:
if (l > 0 && minLen[l - 1] != Integer.MAX_VALUE) {
    ans = Math.min(ans, currLen + minLen[l - 1]);
}
That's the core of the solution.
Everything else is just maintaining those values correctly.

8. Let's See Why l - 1 Is So Important
Suppose the current subarray is:
[3 ... 5]
Its left boundary is:
l = 3
Then the previous subarray must end at:
0, 1, or 2
It cannot end at 3, because that would overlap.
So we need all valid subarrays whose end index is at most:
l - 1
which is:
2
That's exactly why we query:
minLen[l - 1]
Not:
minLen[l]
and definitely not:
minLen[r]
This little index is the reason the non-overlap condition is handled so neatly.

9. What Exactly Is best?
There are actually two different things being maintained.
We have:
int ans = Integer.MAX_VALUE;
int best = Integer.MAX_VALUE;
Let's understand both.
best
best is:

the shortest valid subarray found so far.

Whenever we discover:
sum == target
we do:
best = Math.min(best, currLen);
Then:
minLen[r] = best;
So minLen[r] becomes the shortest valid subarray ending anywhere up to r.

ans
ans is different.
It is the best total length we've found for two compatible subarrays.
So:
best
→ shortest one valid subarray

ans
→ shortest pair of non-overlapping valid subarrays
Keeping these two concepts separate makes the code much easier to understand.

10. Let's Walk Through a Real Example
Consider:
arr = [3, 2, 2, 4, 3]
target = 3
We start with:
best = INF
ans = INF

r = 0
We add:
3
So:
sum = 3
We found:
[0...0]
with length:
1
There is no previous subarray.
So:
best = 1
and:
minLen[0] = 1

r = 1
Add:
2
Now:
sum = 5
Too large.
Move l:
sum -= arr[l]
Remove the 3.
Now:
sum = 2
l = 1
Not a valid subarray.
So:
minLen[1] = best = 1
The previous information is preserved.

r = 2
Add:
2
Now:
sum = 4
Still too large.
Remove:
arr[1] = 2
Now:
sum = 2
l = 2
Again, not valid.
So:
minLen[2] = 1

r = 3
Add:
4
Now:
sum = 6
Shrink:
remove 2
remove 2
Now:
sum = 4
Remove:
4
Now:
sum = 0
l = 4
No valid subarray ending at r = 3.
So:
minLen[3] = 1

r = 4
Add:
3
Now:
sum = 3
We found:
[4...4]
length:
1
Now look at:
minLen[l - 1]
Here:
l = 4
so we check:
minLen[3]
which is:
1
That means we already have a previous valid subarray of length 1 ending before index 4.
So:
candidate = 1 + 1
          = 2
Therefore:
ans = 2
Done.

11. The Beautiful Part
Notice what we didn't do.
We didn't store:
all valid subarrays
We didn't store:
their starting positions
We didn't compare every pair.
We simply remembered:
the shortest valid subarray seen so far
That is enough.
Because when a new valid subarray appears, we know exactly which previous subarrays are compatible:
those ending before l
And minLen[l - 1] already gives us the best one among them.

12. Why Do We Assign minLen[r] = best Outside The if?
This line is easy to overlook:
minLen[r] = best;
It executes whether or not we found a valid subarray ending at r.
Why?
Because minLen[r] isn't asking:

"Is there a valid subarray ending exactly at r?"

Instead, it asks:

"What is the shortest valid subarray we've seen anywhere from index 0 through r?"

Suppose:
minLen[4] = 2
and index 5 doesn't produce a valid subarray.
We still want:
minLen[5] = 2
because that earlier length-2 subarray is still useful for future subarrays.
So:
minLen[r] = best;
is what turns the array into a prefix minimum.

13. Another Way To Think About minLen
Imagine every index is asking:

"If another valid subarray starts somewhere after me, what is the shortest valid subarray I can give it from the left?"

Then:
minLen[i]
is basically our answer to that question.
For example:
index:     0   1   2   3   4   5
minLen:   INF INF  5   5   2   2
This means:

by index 2, the best valid subarray has length 5
by index 4, we've discovered something better: length 2
after that, 2 remains the best

So when a future subarray needs a partner, we can immediately retrieve the shortest possible one.

14. Why The Sliding Window Is Linear
Every element enters the window once:
sum += arr[r]
And every element leaves the window at most once:
sum -= arr[l++]
So even though we have a:
while (sum > target)
inside the loop, the overall work is still linear.
This is the classic sliding-window amortized argument:
each element is added once
each element is removed once
Therefore:
O(n)

15. Why This Works Only Because The Array Is Positive
This is an important detail.
The whole sliding-window logic relies on:
arr[i] > 0
When:
sum > target
we can safely remove elements from the left because removing a positive number will decrease the sum.
With negative numbers, that logic breaks.
For example:
[5, -2]
Removing or adding elements can move the sum in either direction.
So this particular two-pointer technique would no longer be reliable.
That's why the positivity constraint is doing a lot of work for us.

16. Why We Don't Need To Check Whether Two Subarrays Overlap Explicitly
This is another nice trick.
Normally, after finding two subarrays:
[l1 ... r1]
[l2 ... r2]
we might check:
r1 < l2
But here we don't need to.
When the current subarray begins at:
l
we only look at:
minLen[l - 1]
By definition, that value represents a subarray ending no later than:
l - 1
Therefore:
previous right <= l - 1
which automatically means:
previous right < current left
So the two subarrays are guaranteed to be non-overlapping.
The condition is built directly into the lookup.

17. The Complete Flow
For every r:
add arr[r]
     ↓
if sum > target
     ↓
move l until sum <= target
     ↓
if sum == target
     ↓
current valid subarray found
     ↓
check minLen[l - 1]
     ↓
combine with shortest compatible previous subarray
     ↓
update best
     ↓
store minLen[r]
That's the whole algorithm.

18. The Code Becomes Much Easier Now
class Solution {
    public int minSumOfLengths(int[] arr, int target) {

        int n = arr.length;

        // minLen[i] = shortest valid subarray
        // ending at or before index i
        int[] minLen = new int[n];

        int l = 0;
        int sum = 0;

        int ans = Integer.MAX_VALUE;
        int best = Integer.MAX_VALUE;

        for (int r = 0; r < n; r++) {

            sum += arr[r];

            // Shrink window if sum becomes too large
            while (sum > target) {
                sum -= arr[l++];
            }

            // Found a subarray with sum = target
            if (sum == target) {

                int currLen = r - l + 1;

                // Find the best non-overlapping subarray
                // completely to the left of l
                if (l > 0 &&
                    minLen[l - 1] != Integer.MAX_VALUE) {

                    ans = Math.min(
                        ans,
                        currLen + minLen[l - 1]
                    );
                }

                // Keep the shortest valid subarray seen so far
                best = Math.min(best, currLen);
            }

            // Carry the best value forward
            minLen[r] = best;
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}

19. The Two Variables You Absolutely Must Understand
If you remember nothing else from this solution, remember these two:
best
and:
minLen[i]
best means:
shortest valid subarray found so far
minLen[i] means:
shortest valid subarray
whose right endpoint is <= i
So when the current subarray starts at l:
minLen[l - 1]
is exactly the best possible partner.
That's the entire trick.

20. Why We Store Only The Minimum Length
Suppose before the current subarray we have three valid subarrays:
length 7
length 4
length 2
and all of them are non-overlapping with the current one.
Which one should we use?
Obviously:
length 2
because our objective is:
length1 + length2
We don't care about the longer ones anymore.
So keeping anything except the shortest valid length would be wasted information.
This is a very common DP-style idea:

When the future only cares about the best previous state, throw away everything else.


21. A Small Mental Model
Think of the algorithm as two people walking through the array.
The first person, the sliding window, is constantly finding:
"a subarray ending here whose sum is target."
The second person, minLen, is remembering:
"What's the shortest valid subarray I've seen on the left?"
Whenever the first person finds a valid subarray:
current subarray
       +
best compatible previous subarray
       =
candidate answer
Then we continue.
So we're effectively doing:
       current
          ↓
      [ l ... r ]
          ↓
  look just before l
          ↓
   minLen[l - 1]
          ↓
     combine them
That is why the whole problem can be solved in one pass.

22. Complexity
Let:
n = arr.length
The right pointer moves from:
0 → n - 1
and the left pointer also moves forward at most n times.
Therefore the total sliding-window work is:
O(n)
Updating minLen and ans is constant time.
So:
Time  → O(n)
Space → O(n)
The O(n) space is for the minLen array.

Final Mental Model
This problem initially looks like:
"Find two subarrays."
But that's not really what we're doing.
We're doing:
Find one valid subarray
        ↓
Ask:
"What is the shortest valid subarray
 completely before this one?"
        ↓
minLen[l - 1]
        ↓
combine
        ↓
update answer
And the sliding window is responsible for finding the current valid subarray in O(n).
So the final idea is:
Sliding Window
      +
Prefix Minimum
      =
O(n) solution
The real trick is not the sliding window itself.
The real trick is realizing that for every valid subarray, we don't need all previous subarrays. we only need the shortest valid one that ends before its starting point.
once that observation is made, the problem becomes beautifully simple.
that's all for today!
have a nice dayy babygirl :) PreviousSimple way to solve 2 ways || Sliding window + prefix/suffix map || DPNextSliding Window + DP: The Trick Behind LeetCode 1477 With Video ExplanationComments (1)Sort by:BestCommentDebesh P10 hours agodo upvote if it was helpful babygirl 🫶 Read more1141JavaAuto141510111213789345612            }            sum += arr[r];            while (sum > target) {                sum -= arr[l++];        int best = Integer.MAX_VALUE;        for (int r = 0; r < n; r++) {        int n = arr.length;        int[] minLen = new int[n];        int l = 0, sum = 0;        int ans = Integer.MAX_VALUE;class Solution {    public int minSumOfLengths(int[] arr, int target) {SavedLn 31, Col 2AcceptedRuntime: 0 msCase 1Case 2Case 3Inputarr =[3,2,2,4,3]target =3Output2Expected2Contribute a testcaseInput9123456›[3,2,2,4,3]3[7,3,4,7]7[4,3,2,6,2,3,4]6Output9123›22-1Expected9123›22-1 All SubmissionsAcceptedMUTHU KUMAR Msubmitted at Sep 17, 2026 09:07AnalysisSolutionCodeJava1class Solution {
2    public int minSumOfLengths(int[] arr, int target) {
3        int n = arr.length;
4        int[] minLen = new int[n];
5        int l = 0, sum = 0;
6        int ans = Integer.MAX_VALUE;
7        int best = Integer.MAX_VALUE;
8
9        for (int r = 0; r < n; r++) {
10            sum += arr[r];
11
12            while (sum > target) {
13                sum -= arr[l++];
14            }
15
16            if (sum == target) {
17                int currLen = r - l + 1;
18
19                if (l > 0 && minLen[l - 1] != Integer.MAX_VALUE) {
20                    ans = Math.min(ans, currLen + minLen[l - 1]);
21                }
22
23                best = Math.min(best, currLen);
24            }
25
26            minLen[r] = best;
27        }
28
29        return ans == Integer.MAX_VALUE ? -1 : ans;
30    }
31}View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
