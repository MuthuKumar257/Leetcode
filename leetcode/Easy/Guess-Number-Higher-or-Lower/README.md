# 374. Guess Number Higher or Lower

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

## Solution

See [`solution_v2.py`](./solution_v2.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Problem ListProblem ListDebugging...Submit10100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionAcceptedAcceptedEditorialEditorialSolutionsSolutionsSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result374. Guess Number Higher or LowerSolvedEasyTopicsCompaniesWe are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:


	-1: Your guess is higher than the number I picked (i.e. num > pick).
	1: Your guess is lower than the number I picked (i.e. num < pick).
	0: your guess is equal to the number I picked (i.e. num == pick).


Return the number that I picked.

 
Example 1:

Input: n = 10, pick = 6
Output: 6


Example 2:

Input: n = 1, pick = 1
Output: 1


Example 3:

Input: n = 2, pick = 1
Output: 1


 
Constraints:


	1 <= n <= 231 - 1
	1 <= pick <= n

 Seen this question in a real interview before?1/6YesNoAccepted1,091,842/1.9MAcceptance Rate58.3%TopicsBinary SearchInteractiveCompaniesSimilar QuestionsFirst Bad VersionEasyGuess Number Higher or Lower IIMediumFind K Closest ElementsMediumDiscussion (310)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestSakhawat Hossain MridulNov 16, 2022i did not understand the question properly,can any one help to understand this question? Read moreAsk Question31511sophearyJul 19, 2023This question is difficult to understand than solving. 😂 Read more2508AbdullahNov 16, 2022I believer the phrasing of the problem description could be better. It feels exactly the opposite of what the problem intends actually. Read moreFeedback1592Ashutosh RattanNov 16, 2022In case its confusing, as it was for me intially :-
You are given a function guessNumber() that you are to complete. Given  a upper bound n this function should guess the correct number picked between 1 and n.
To help you with the guessing you are provided with an API guess(). You pass in the value that you have guessed and this function will return 3 values depending upon whether the guess is right or wrong :
-1 if the number guessed is higher than the picked number
1 if the number guessed is lower than the picked number
otherwise return 0 when the number guessed  is equal to picked number.
Based upon this you're to formulate  a strategy so that you can zero in on the picked number.
Happy leetcoding :)
.
.
.
.
.
.
.
.
.
Hint :- try binary search maybe? Read moreTip1186RuntimeTerrorApr 01, 2023what the hell is this question... Read more751NakanuJul 13, 2016-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!
Here "My" means the number which is given for you to guess not the number you put into      guess(int num). Read more3151Aavash KuikelJun 19, 2023Misleading problem statement. Needs to be fixed asap! Read moreFeedback51Heng Harry ZhouJan 20, 2021Any body feel the guess() function logic is reversed? Read more361It's a secretJul 22, 2016It must be said , there is a trap in the question. A description used is difficult to understand. It said: 'return -1 if my number is lower, 1 if my number is higher, otherwise return 0'
At frist ,I thought it means if the target num is 10 ,guess(3) would return -1 ，but it got wrong result ,then I found it return 1 actually.So the description is said by the dealer ,we are players.It almost  wasted half of this night.I hope I can help somebody to save a little time Read more324Vivek Kumar AgrawalNov 16, 2022I was calling guessNumber intead of guess function so please do not repeate same mistake again Read more271123431Copyright © 2026 LeetCode. All rights reserved.4.3K31010 Online
@property --beam-angle-_r_36_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_36_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_36_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_36_"][data-active] {
  animation:
    beam-spin-_r_36_ 1.96s linear infinite,
    beam-fade-in-_r_36_ 0.6s ease forwards;
}

[data-beam="_r_36_"][data-fading] {
  animation:
    beam-spin-_r_36_ 1.96s linear infinite,
    beam-fade-out-_r_36_ 0.5s ease forwards;
}

[data-beam="_r_36_"][data-active]::after,
[data-beam="_r_36_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_36_),
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
      from var(--beam-angle-_r_36_),
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
      from var(--beam-angle-_r_36_),
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
  opacity: calc(var(--beam-opacity-_r_36_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_36_"][data-active]::before,
[data-beam="_r_36_"][data-fading]::before {
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
    from var(--beam-angle-_r_36_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_36_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_36_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_36_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_36_),
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

[data-beam="_r_36_"][data-active] [data-beam-bloom],
[data-beam="_r_36_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_36_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_36_ {
  to { --beam-angle-_r_36_: 360deg; }
}

@keyframes beam-fade-in-_r_36_ {
  to { --beam-opacity-_r_36_: 1; }
}

@keyframes beam-fade-out-_r_36_ {
  from { --beam-opacity-_r_36_: 1; }
  to { --beam-opacity-_r_36_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++CPythonJavaScriptGoC#TypeScriptSwiftKotlinRustRubyPHPScalaDartBashMySQLPostgreSQLBinary SearchBinary TreeInteractiveRecursionArrayMathTwo PointersBinary Search TreeIteratorDivide and ConquerSortingRandomizedBrainteaserDynamic ProgrammingBit ManipulationMerge SortGreedyTreeYour last submission beat 86% of other submissions' runtime.Share my solutionLeetCode・ Open・Dec 13, 2022Guess Number Higher or LowerEditorial130325.9K88Abhishek Kumar Ranjan・ Open・a day agoBinary Search | Easy Java1350Average Guy・ Open・Aug 26, 2026✅✅✅Easy C++ Code | Beats 100% ms | 95% mb🔥🔥✅✅Binary SearchInteractiveC++84830Discover moreLearn Coding OnlineLoginov Kirill・ Open・Apr 11, 2025🧠 Master Binary Search to Outsmart Any Guessing GameBinary SearchInteractivePythonJavaScript13416.5K5polymath_arnav・ Open・Sep 04, 2026Not that easy I run the code 10+ times to get the final resultJava21620Suraj Kumar・ Open・Mar 29, 2026Beats 100%✅| Binary Search | JAVA/C++/Python/JS| log (n) Time & O(1) Time|Easy & Beginner's FriendlyArrayBinary SearchPythonC++2+195.1K1Praveen S・ Open・Aug 30, 2026Binary Search | Optimal Sol | 100.00% Beats ✅✅✅C++11100amazingDeveloper976・ Open・Aug 08, 2026👉Understand  Binary Search | 🔥Beats 1000% | 🚀Simple solution Binary SearchInteractiveC++25441STANISLAV IABLOKOV・ Open・Nov 16, 2022✅ [Python/C++/Java/Rust] binary search to halve your ignorance + BONUS O(0) ONE-LINER (explained)8211.8K15Serhii・ Open・Aug 23, 2026Easy | Beats 100% | JavaJava13331Abhinash Singh・ Open・Feb 21, 2023C++ || Binary Search || Easiest Beginner Friendly SolBinary SearchC++JavaPython37314.8K5akrb8999・ Open・Aug 25, 2026Guess Number Higher or Lower — Binary SearchPython31750Mukund Rakholiya・ Open・Nov 27, 2024✅ EASY || 💯 BEATS-PROOF || 🌟 JAVA || 🙂 BEGINNER FRENDLY || 📒 DETAILED EXPLANATONBinary SearchJava308.7K12Anya Porwal・ Open・Aug 15, 2026Solution in JavaMathBinary SearchInteractiveJava12460Yatin Singla・ Open・Jan 04, 2021Python: Beats 99% solutions O(log(n)) (w/ comments and using Walrus Operator)Binary SearchBinary TreePythonPython36513.8K7All Solutions🧠 Master Binary Search to Outsmart Any Guessing GameLoginov Kirill16.5KApr 11, 2025Binary SearchInteractivePythonJavaScriptIntuition
The goal is to find a hidden number between 1 and n using feedback from a guess() API. The problem screams binary search, as the API tells you if your guess is too high or too low.
Approach


Start with left = 1 and right = n.
Use binary search to narrow the range based on the response from guess(mid).
If the response is 0, you've found the number.
Adjust the search boundaries until you converge.

Classic divide-and-conquer at its finest — fast, efficient, and interview gold.
Complexity
Time Complexity:
( O(log n) ) — binary search over the range [1, n].
Space Complexity:
( O(1) ) — constant space.
Code
PythonJavaScriptclass Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Writing clean code is just the start.
I'm building startups solo — and sharing the whole ride.
Follow the journey:
🐦 Twitter: solotounicorn
🔗 LinkedIn: loginov-kirill
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Discover moreComputer Programming BooksPrevious✅✅✅Easy C++ Code | Beats 100% ms | 95% mb🔥🔥✅✅NextNot that easy I run the code 10+ times to get the final resultComments (5)Sort by:BestCommentioanaAug 20, 2025almost, however this solution gives TLE. mid should be left + (right - left) / 2; Read more4Loginov KirillApr 11, 2025Don't forget to connect with me on Twitter.
Thank You! Read more4Piyush SharmaAug 20, 2025If you implement it in C++, make sure to use int mid = left + ((right - left) / 2); to not run into signed integer overflow issues. Read more2RohanDec 17, 2025Not useful getting TLE Read more1AlphaSep 05, 2025buddy great work Read more011345Python3Auto678910111213141516171819# def guess(num: int) -> int:class Solution:    def guessNumber(self, n: int) -> int:        left, right = 1, n        while left <= right:            mid = (left + right) // 2            result = guess(mid)            if result == 0:                return mid            elif result == -1:                right = mid - 1            else:                left = mid + 1SavedLn 19, Col 31AcceptedRuntime: 42 msCase 1Case 2Case 3Inputn =10pick =6Output6Expected6Contribute a testcaseInput9123456›1061121Output9123›611Expected9123›611 All SubmissionsAccepted25 / 25 testcases passedMUTHU KUMAR Msubmitted at Sep 12, 2026 09:38AnalysisSolution👑 Unlock the Full LeetCode ExperienceCompany problems, Ask Leet, and expert editorials — all in one plan.Runtime39msBeats86.41%Memory19.30MBBeats7.42%Created with Highcharts 11.1.022ms28ms33ms38ms43ms48ms0%5%10%
                  
                Created with Highcharts 11.1.022ms28ms33ms38ms43ms48msCodePython31# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        left, right = 1, n
11        while left <= right:
12            mid = (left + right) // 2
13            result = guess(mid)
14            if result == 0:
15                return mid
16            elif result == -1:
17                right = mid - 1
18            else:
19                left = mid + 1View more More challenges375. Guess Number Higher or Lower II658. Find K Closest Elements0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize
- **Memory:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Problem ListProblem ListDebugging...Submit10100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionAcceptedAcceptedEditorialEditorialSolutionsSolutionsSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result374. Guess Number Higher or LowerSolvedEasyTopicsCompaniesWe are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:


	-1: Your guess is higher than the number I picked (i.e. num > pick).
	1: Your guess is lower than the number I picked (i.e. num < pick).
	0: your guess is equal to the number I picked (i.e. num == pick).


Return the number that I picked.

 
Example 1:

Input: n = 10, pick = 6
Output: 6


Example 2:

Input: n = 1, pick = 1
Output: 1


Example 3:

Input: n = 2, pick = 1
Output: 1


 
Constraints:


	1 <= n <= 231 - 1
	1 <= pick <= n

 Seen this question in a real interview before?1/6YesNoAccepted1,091,842/1.9MAcceptance Rate58.3%TopicsBinary SearchInteractiveCompaniesSimilar QuestionsFirst Bad VersionEasyGuess Number Higher or Lower IIMediumFind K Closest ElementsMediumDiscussion (310)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestSakhawat Hossain MridulNov 16, 2022i did not understand the question properly,can any one help to understand this question? Read moreAsk Question31511sophearyJul 19, 2023This question is difficult to understand than solving. 😂 Read more2508AbdullahNov 16, 2022I believer the phrasing of the problem description could be better. It feels exactly the opposite of what the problem intends actually. Read moreFeedback1592Ashutosh RattanNov 16, 2022In case its confusing, as it was for me intially :-
You are given a function guessNumber() that you are to complete. Given  a upper bound n this function should guess the correct number picked between 1 and n.
To help you with the guessing you are provided with an API guess(). You pass in the value that you have guessed and this function will return 3 values depending upon whether the guess is right or wrong :
-1 if the number guessed is higher than the picked number
1 if the number guessed is lower than the picked number
otherwise return 0 when the number guessed  is equal to picked number.
Based upon this you're to formulate  a strategy so that you can zero in on the picked number.
Happy leetcoding :)
.
.
.
.
.
.
.
.
.
Hint :- try binary search maybe? Read moreTip1186RuntimeTerrorApr 01, 2023what the hell is this question... Read more751NakanuJul 13, 2016-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!
Here "My" means the number which is given for you to guess not the number you put into      guess(int num). Read more3151Aavash KuikelJun 19, 2023Misleading problem statement. Needs to be fixed asap! Read moreFeedback51Heng Harry ZhouJan 20, 2021Any body feel the guess() function logic is reversed? Read more361It's a secretJul 22, 2016It must be said , there is a trap in the question. A description used is difficult to understand. It said: 'return -1 if my number is lower, 1 if my number is higher, otherwise return 0'
At frist ,I thought it means if the target num is 10 ,guess(3) would return -1 ，but it got wrong result ,then I found it return 1 actually.So the description is said by the dealer ,we are players.It almost  wasted half of this night.I hope I can help somebody to save a little time Read more324Vivek Kumar AgrawalNov 16, 2022I was calling guessNumber intead of guess function so please do not repeate same mistake again Read more271123431Copyright © 2026 LeetCode. All rights reserved.4.3K31010 Online
@property --beam-angle-_r_36_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_36_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_36_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_36_"][data-active] {
  animation:
    beam-spin-_r_36_ 1.96s linear infinite,
    beam-fade-in-_r_36_ 0.6s ease forwards;
}

[data-beam="_r_36_"][data-fading] {
  animation:
    beam-spin-_r_36_ 1.96s linear infinite,
    beam-fade-out-_r_36_ 0.5s ease forwards;
}

[data-beam="_r_36_"][data-active]::after,
[data-beam="_r_36_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_36_),
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
      from var(--beam-angle-_r_36_),
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
      from var(--beam-angle-_r_36_),
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
  opacity: calc(var(--beam-opacity-_r_36_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_36_"][data-active]::before,
[data-beam="_r_36_"][data-fading]::before {
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
    from var(--beam-angle-_r_36_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_36_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_36_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_36_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_36_),
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

[data-beam="_r_36_"][data-active] [data-beam-bloom],
[data-beam="_r_36_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_36_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_36_ {
  to { --beam-angle-_r_36_: 360deg; }
}

@keyframes beam-fade-in-_r_36_ {
  to { --beam-opacity-_r_36_: 1; }
}

@keyframes beam-fade-out-_r_36_ {
  from { --beam-opacity-_r_36_: 1; }
  to { --beam-opacity-_r_36_: 0; }
}

LeetSort byAllMy SolutionPython3JavaC++CPythonJavaScriptGoC#TypeScriptSwiftKotlinRustRubyPHPScalaDartBashMySQLPostgreSQLBinary SearchBinary TreeInteractiveRecursionArrayMathTwo PointersBinary Search TreeIteratorDivide and ConquerSortingRandomizedBrainteaserDynamic ProgrammingBit ManipulationMerge SortGreedyTreeYour last submission beat 86% of other submissions' runtime.Share my solutionLeetCode・ Open・Dec 13, 2022Guess Number Higher or LowerEditorial130325.9K88Abhishek Kumar Ranjan・ Open・a day agoBinary Search | Easy Java1350Average Guy・ Open・Aug 26, 2026✅✅✅Easy C++ Code | Beats 100% ms | 95% mb🔥🔥✅✅Binary SearchInteractiveC++84830Discover moreLearn Coding OnlineLoginov Kirill・ Open・Apr 11, 2025🧠 Master Binary Search to Outsmart Any Guessing GameBinary SearchInteractivePythonJavaScript13416.5K5polymath_arnav・ Open・Sep 04, 2026Not that easy I run the code 10+ times to get the final resultJava21620Suraj Kumar・ Open・Mar 29, 2026Beats 100%✅| Binary Search | JAVA/C++/Python/JS| log (n) Time & O(1) Time|Easy & Beginner's FriendlyArrayBinary SearchPythonC++2+195.1K1Praveen S・ Open・Aug 30, 2026Binary Search | Optimal Sol | 100.00% Beats ✅✅✅C++11100amazingDeveloper976・ Open・Aug 08, 2026👉Understand  Binary Search | 🔥Beats 1000% | 🚀Simple solution Binary SearchInteractiveC++25441STANISLAV IABLOKOV・ Open・Nov 16, 2022✅ [Python/C++/Java/Rust] binary search to halve your ignorance + BONUS O(0) ONE-LINER (explained)8211.8K15Serhii・ Open・Aug 23, 2026Easy | Beats 100% | JavaJava13331Abhinash Singh・ Open・Feb 21, 2023C++ || Binary Search || Easiest Beginner Friendly SolBinary SearchC++JavaPython37314.8K5akrb8999・ Open・Aug 25, 2026Guess Number Higher or Lower — Binary SearchPython31750Mukund Rakholiya・ Open・Nov 27, 2024✅ EASY || 💯 BEATS-PROOF || 🌟 JAVA || 🙂 BEGINNER FRENDLY || 📒 DETAILED EXPLANATONBinary SearchJava308.7K12Anya Porwal・ Open・Aug 15, 2026Solution in JavaMathBinary SearchInteractiveJava12460Yatin Singla・ Open・Jan 04, 2021Python: Beats 99% solutions O(log(n)) (w/ comments and using Walrus Operator)Binary SearchBinary TreePythonPython36513.8K7All Solutions🧠 Master Binary Search to Outsmart Any Guessing GameLoginov Kirill16.5KApr 11, 2025Binary SearchInteractivePythonJavaScriptIntuition
The goal is to find a hidden number between 1 and n using feedback from a guess() API. The problem screams binary search, as the API tells you if your guess is too high or too low.
Approach


Start with left = 1 and right = n.
Use binary search to narrow the range based on the response from guess(mid).
If the response is 0, you've found the number.
Adjust the search boundaries until you converge.

Classic divide-and-conquer at its finest — fast, efficient, and interview gold.
Complexity
Time Complexity:
( O(log n) ) — binary search over the range [1, n].
Space Complexity:
( O(1) ) — constant space.
Code
PythonJavaScriptclass Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Writing clean code is just the start.
I'm building startups solo — and sharing the whole ride.
Follow the journey:
🐦 Twitter: solotounicorn
🔗 LinkedIn: loginov-kirill
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Discover moreComputer Programming BooksPrevious✅✅✅Easy C++ Code | Beats 100% ms | 95% mb🔥🔥✅✅NextNot that easy I run the code 10+ times to get the final resultComments (5)Sort by:BestCommentioanaAug 20, 2025almost, however this solution gives TLE. mid should be left + (right - left) / 2; Read more4Loginov KirillApr 11, 2025Don't forget to connect with me on Twitter.
Thank You! Read more4Piyush SharmaAug 20, 2025If you implement it in C++, make sure to use int mid = left + ((right - left) / 2); to not run into signed integer overflow issues. Read more2RohanDec 17, 2025Not useful getting TLE Read more1AlphaSep 05, 2025buddy great work Read more011345Python3Auto678910111213141516171819# def guess(num: int) -> int:class Solution:    def guessNumber(self, n: int) -> int:        left, right = 1, n        while left <= right:            mid = (left + right) // 2            result = guess(mid)            if result == 0:                return mid            elif result == -1:                right = mid - 1            else:                left = mid + 1SavedLn 19, Col 31AcceptedRuntime: 42 msCase 1Case 2Case 3Inputn =10pick =6Output6Expected6Contribute a testcaseInput9123456›1061121Output9123›611Expected9123›611 All SubmissionsAccepted25 / 25 testcases passedMUTHU KUMAR Msubmitted at Sep 12, 2026 09:38AnalysisSolution👑 Unlock the Full LeetCode ExperienceCompany problems, Ask Leet, and expert editorials — all in one plan.Runtime39msBeats86.41%Memory19.30MBBeats7.42%Created with Highcharts 11.1.022ms28ms33ms38ms43ms48ms0%5%10%
                  
                Created with Highcharts 11.1.022ms28ms33ms38ms43ms48msCodePython31# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        left, right = 1, n
11        while left <= right:
12            mid = (left + right) // 2
13            result = guess(mid)
14            if result == 0:
15                return mid
16            elif result == -1:
17                right = mid - 1
18            else:
19                left = mid + 1View more More challenges375. Guess Number Higher or Lower II658. Find K Closest Elements0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
