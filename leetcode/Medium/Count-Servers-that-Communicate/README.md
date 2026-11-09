# 1267. Count Servers that Communicate

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1267. Count Servers that CommunicateMediumTopicsCompaniesHintYou are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 
Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.


Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


 
Constraints:


	m == grid.length
	n == grid[i].length
	1 <= m <= 250
	1 <= n <= 250
	grid[i][j] == 0 or 1

 Seen this question in a real interview before?1/6YesNoAccepted275,122/358.3KAcceptance Rate76.8%TopicsSeniorArrayDepth-First SearchBreadth-First SearchUnion-FindMatrixCountingWeekly Contest 164CompaniesHint 1Store number of computer in each row and column.Hint 2Count all servers that are not isolated.Discussion (204)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestNo comments yet.123421Copyright © 2026 LeetCode. All rights reserved.2.1K204398 Online
@property --beam-angle-_r_7n_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7n_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7n_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7n_"][data-active] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-in-_r_7n_ 0.6s ease forwards;
}

[data-beam="_r_7n_"][data-fading] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-out-_r_7n_ 0.5s ease forwards;
}

[data-beam="_r_7n_"][data-active]::after,
[data-beam="_r_7n_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"][data-active]::before,
[data-beam="_r_7n_"][data-fading]::before {
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
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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

[data-beam="_r_7n_"][data-active] [data-beam-bloom],
[data-beam="_r_7n_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7n_ {
  to { --beam-angle-_r_7n_: 360deg; }
}

@keyframes beam-fade-in-_r_7n_ {
  to { --beam-opacity-_r_7n_: 1; }
}

@keyframes beam-fade-out-_r_7n_ {
  from { --beam-opacity-_r_7n_: 1; }
  to { --beam-opacity-_r_7n_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptCGoC#RustSwiftTypeScriptKotlinPHPRubyDartScalaElixirRacketMySQLCountingMatrixArrayDepth-First SearchUnion-FindBreadth-First SearchHash TableGraph TheorySimulationOrdered MapGreedyDynamic ProgrammingIteratorMathPrefix SumRecursionOrdered SetBit ManipulationCounting SortInteractiveQueueStrongly Connected ComponentBrute-Force SearchStringInclusion-Exclusion PrincipleSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Jan 18, 2025Count Servers that CommunicateEditorial5460.5K61Aleksandr・ Open・Nov 08, 2026✅ Count Once, Then Look UpArrayMatrixCountingPython6+6510.4K3Muthu Vrn・ Open・Nov 08, 2026God is Great 518Python3311.6K0Md Aarzoo Islam・ Open・Nov 08, 20260ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayDepth-First SearchBreadth-First SearchUnion-Find6+273.6K1Aryan Kumar Shaw Halwai・ Open・Nov 08, 2026✅ Beats 100% 🚀 | Row & Column Counting, Skip Lone Servers 🔥 | Java, C++, Python, JSArrayUnion-FindGraph TheoryMatrix6+138890Bijoy Sing・ Open・Nov 08, 2026✅ Simple & Easy Solution → O(m × n) | Row + Column Counting ArrayGraph TheoryPythonC++3+71.1K0Stefan Pochmann・ Open・Nov 07, 2026Short and beats 98.62% + Big benchmarkPython352570Dhanush Rajulapati・ Open・Nov 08, 2026Matrix + Row and Column Counting Solution | Java, Python, C++, JS | O(n × m) Time | O(n + m) SpaceArrayMatrixCountingPython3+42911Nilesh_Odedara・ Open・Nov 08, 2026Count Servers – Row & Column Frequency CountingArrayDepth-First SearchBreadth-First SearchUnion-Find3+3830Long Nguyen・ Open・Nov 08, 2026100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+31280OM JAMALE・ Open・Nov 08, 2026count of servers those can communicate question Easy solution Cpp beats 72%MathMatrixCountingC++1151ahhz・ Open・2 hours agoSingle pass, no extra space (0ms)C++120Schrodingerrrr・ Open・7 hours agoUsing Breath-first search.C++180anikbiswas2712・ Open・16 hours agoNo server left behind... unless it's alone. 😭ArrayDepth-First SearchBreadth-First SearchUnion-Find3+180hussainbinfazal・ Open・19 hours agoBeats 100% Optimal Solution of  Count Servers that Communicate (Javscript & Typescript ) with TrickTypeScript150All SolutionsShort and beats 98.62% + Big benchmarkStefan Pochmann257Nov 07, 2026Python3First compute the column sums. Then sum the row sums that are larger than 1 or whose only 1 is in a column with more than one.
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cs = list(map(sum, zip(*grid)))
        return sum(
            rs
            for row in grid
            if (rs := sum(row))
            if rs > 1 or cs[row.index(1)] > 1
        )
I was curious about speeds, so I benchmarked this and a bunch of other solutions, running on LeetCode with LeetCode's test cases:
 5.55 ± 0.01 ms  Stefan 
 1.85 ± 0.04 ms  Stefan_optimized 
 3.97 ± 0.02 ms  sample_0ms 
 2.46 ± 0.03 ms  sample_0ms_optimized 
 3.72 ± 0.01 ms  sample_2ms 
 2.59 ± 0.04 ms  sample_2ms_optimized 
19.50 ± 0.15 ms  Editorial_1 
15.48 ± 0.12 ms  Editorial_2 
 8.10 ± 0.08 ms  Editorial_3 
 8.89 ± 0.15 ms  Editorial_4 
12.12 ± 0.04 ms  Aleksandr 
The two "sample_" solutions are from the runtime distribution graph, for the two fastest submission times 0 and 2 ms. Their "_optimized" versions are optimized by me. The fastest overall was mine where I turn the whole grid into a bytearray and then query that:
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        b = reduce(iadd, map(bytearray, grid))
        @cache
        def column(j):
            c = b[j::n]
            return c.find(1) < c.rfind(1)
        count = 0
        i = 0
        for I in range(n, m*n+1, n):
            if rs := b.count(1, i, I):
                if rs > 1 or column(b.index(1, i) - i):
                    count += rs
            i = I
        return count Previous✅ Simple & Easy Solution → O(m × n) | Row + Column Counting NextMatrix + Row and Column Counting Solution | Java, Python, C++, JS | O(n × m) Time | O(n + m) SpaceComments (0)Sort by:BestCommentNo comments yet.50Python3Auto123456789class Solution:    def countServers(self, grid: list[list[int]]) -> int:        cs = list(map(sum, zip(*grid)))        return sum(            rs            for row in grid            if (rs := sum(row))            if rs > 1 or cs[row.index(1)] > 1        )In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 9, Col 10AcceptedRuntime: 0 msCase 1Case 2Case 3Inputgrid =[[1,0],[0,1]]Output0Expected0Contribute a testcaseInput9123›[[1,0],[0,1]][[1,0],[1,1]][[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]Output9123›034Expected9123›034 All SubmissionsAccepted55 / 55 testcases passedMUTHU KUMAR Msubmitted at Nov 09, 2026 18:07AnalysisSolutionRuntime4msBeats98.59%Memory21.42MBBeats65.07%Created with Highcharts 11.1.011ms21ms31ms44ms64ms0%5%10%15%
                  
                Created with Highcharts 11.1.011ms21ms31ms44ms64msCodePython31class Solution:
2    def countServers(self, grid: list[list[int]]) -> int:
3        cs = list(map(sum, zip(*grid)))
4        return sum(
5            rs
6            for row in grid
7            if (rs := sum(row))
8            if rs > 1 or cs[row.index(1)] > 1
9        ) 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize
- **Memory:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1267. Count Servers that CommunicateMediumTopicsCompaniesHintYou are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 
Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.


Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


 
Constraints:


	m == grid.length
	n == grid[i].length
	1 <= m <= 250
	1 <= n <= 250
	grid[i][j] == 0 or 1

 Seen this question in a real interview before?1/6YesNoAccepted275,122/358.3KAcceptance Rate76.8%TopicsSeniorArrayDepth-First SearchBreadth-First SearchUnion-FindMatrixCountingWeekly Contest 164CompaniesHint 1Store number of computer in each row and column.Hint 2Count all servers that are not isolated.Discussion (204)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestNo comments yet.123421Copyright © 2026 LeetCode. All rights reserved.2.1K204398 Online
@property --beam-angle-_r_7n_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7n_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7n_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7n_"][data-active] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-in-_r_7n_ 0.6s ease forwards;
}

[data-beam="_r_7n_"][data-fading] {
  animation:
    beam-spin-_r_7n_ 1.96s linear infinite,
    beam-fade-out-_r_7n_ 0.5s ease forwards;
}

[data-beam="_r_7n_"][data-active]::after,
[data-beam="_r_7n_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
      from var(--beam-angle-_r_7n_),
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
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"][data-active]::before,
[data-beam="_r_7n_"][data-fading]::before {
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
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7n_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7n_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7n_),
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

[data-beam="_r_7n_"][data-active] [data-beam-bloom],
[data-beam="_r_7n_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7n_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7n_ {
  to { --beam-angle-_r_7n_: 360deg; }
}

@keyframes beam-fade-in-_r_7n_ {
  to { --beam-opacity-_r_7n_: 1; }
}

@keyframes beam-fade-out-_r_7n_ {
  from { --beam-opacity-_r_7n_: 1; }
  to { --beam-opacity-_r_7n_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptCGoC#RustSwiftTypeScriptKotlinPHPRubyDartScalaElixirRacketMySQLCountingMatrixArrayDepth-First SearchUnion-FindBreadth-First SearchHash TableGraph TheorySimulationOrdered MapGreedyDynamic ProgrammingIteratorMathPrefix SumRecursionOrdered SetBit ManipulationCounting SortInteractiveQueueStrongly Connected ComponentBrute-Force SearchStringInclusion-Exclusion PrincipleSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Jan 18, 2025Count Servers that CommunicateEditorial5460.5K61Aleksandr・ Open・Nov 08, 2026✅ Count Once, Then Look UpArrayMatrixCountingPython6+6510.4K3Muthu Vrn・ Open・Nov 08, 2026God is Great 518Python3311.6K0Md Aarzoo Islam・ Open・Nov 08, 20260ms | Beats 100.00% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayDepth-First SearchBreadth-First SearchUnion-Find6+273.6K1Aryan Kumar Shaw Halwai・ Open・Nov 08, 2026✅ Beats 100% 🚀 | Row & Column Counting, Skip Lone Servers 🔥 | Java, C++, Python, JSArrayUnion-FindGraph TheoryMatrix6+138890Bijoy Sing・ Open・Nov 08, 2026✅ Simple & Easy Solution → O(m × n) | Row + Column Counting ArrayGraph TheoryPythonC++3+71.1K0Stefan Pochmann・ Open・Nov 07, 2026Short and beats 98.62% + Big benchmarkPython352570Dhanush Rajulapati・ Open・Nov 08, 2026Matrix + Row and Column Counting Solution | Java, Python, C++, JS | O(n × m) Time | O(n + m) SpaceArrayMatrixCountingPython3+42911Nilesh_Odedara・ Open・Nov 08, 2026Count Servers – Row & Column Frequency CountingArrayDepth-First SearchBreadth-First SearchUnion-Find3+3830Long Nguyen・ Open・Nov 08, 2026100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+31280OM JAMALE・ Open・Nov 08, 2026count of servers those can communicate question Easy solution Cpp beats 72%MathMatrixCountingC++1151ahhz・ Open・2 hours agoSingle pass, no extra space (0ms)C++120Schrodingerrrr・ Open・7 hours agoUsing Breath-first search.C++180anikbiswas2712・ Open・16 hours agoNo server left behind... unless it's alone. 😭ArrayDepth-First SearchBreadth-First SearchUnion-Find3+180hussainbinfazal・ Open・19 hours agoBeats 100% Optimal Solution of  Count Servers that Communicate (Javscript & Typescript ) with TrickTypeScript150All SolutionsShort and beats 98.62% + Big benchmarkStefan Pochmann257Nov 07, 2026Python3First compute the column sums. Then sum the row sums that are larger than 1 or whose only 1 is in a column with more than one.
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cs = list(map(sum, zip(*grid)))
        return sum(
            rs
            for row in grid
            if (rs := sum(row))
            if rs > 1 or cs[row.index(1)] > 1
        )
I was curious about speeds, so I benchmarked this and a bunch of other solutions, running on LeetCode with LeetCode's test cases:
 5.55 ± 0.01 ms  Stefan 
 1.85 ± 0.04 ms  Stefan_optimized 
 3.97 ± 0.02 ms  sample_0ms 
 2.46 ± 0.03 ms  sample_0ms_optimized 
 3.72 ± 0.01 ms  sample_2ms 
 2.59 ± 0.04 ms  sample_2ms_optimized 
19.50 ± 0.15 ms  Editorial_1 
15.48 ± 0.12 ms  Editorial_2 
 8.10 ± 0.08 ms  Editorial_3 
 8.89 ± 0.15 ms  Editorial_4 
12.12 ± 0.04 ms  Aleksandr 
The two "sample_" solutions are from the runtime distribution graph, for the two fastest submission times 0 and 2 ms. Their "_optimized" versions are optimized by me. The fastest overall was mine where I turn the whole grid into a bytearray and then query that:
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        b = reduce(iadd, map(bytearray, grid))
        @cache
        def column(j):
            c = b[j::n]
            return c.find(1) < c.rfind(1)
        count = 0
        i = 0
        for I in range(n, m*n+1, n):
            if rs := b.count(1, i, I):
                if rs > 1 or column(b.index(1, i) - i):
                    count += rs
            i = I
        return count Previous✅ Simple & Easy Solution → O(m × n) | Row + Column Counting NextMatrix + Row and Column Counting Solution | Java, Python, C++, JS | O(n × m) Time | O(n + m) SpaceComments (0)Sort by:BestCommentNo comments yet.50Python3Auto123456789class Solution:    def countServers(self, grid: list[list[int]]) -> int:        cs = list(map(sum, zip(*grid)))        return sum(            rs            for row in grid            if (rs := sum(row))            if rs > 1 or cs[row.index(1)] > 1        )In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 9, Col 10AcceptedRuntime: 0 msCase 1Case 2Case 3Inputgrid =[[1,0],[0,1]]Output0Expected0Contribute a testcaseInput9123›[[1,0],[0,1]][[1,0],[1,1]][[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]Output9123›034Expected9123›034 All SubmissionsAccepted55 / 55 testcases passedMUTHU KUMAR Msubmitted at Nov 09, 2026 18:07AnalysisSolutionRuntime4msBeats98.59%Memory21.42MBBeats65.07%Created with Highcharts 11.1.011ms21ms31ms44ms64ms0%5%10%15%
                  
                Created with Highcharts 11.1.011ms21ms31ms44ms64msCodePython31class Solution:
2    def countServers(self, grid: list[list[int]]) -> int:
3        cs = list(map(sum, zip(*grid)))
4        return sum(
5            rs
6            for row in grid
7            if (rs := sum(row))
8            if rs > 1 or cs[row.index(1)] > 1
9        ) 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
