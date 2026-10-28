# Minimum XOR Path in a Grid

- **Difficulty:** Easy
- **Language:** Python
- **LeetCode Link:** [Minimum XOR Path in a Grid](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function l(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result
@property --beam-angle-_r_u_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_u_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_u_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_u_"][data-active] {
  animation:
    beam-spin-_r_u_ 1.96s linear infinite,
    beam-fade-in-_r_u_ 0.6s ease forwards;
}

[data-beam="_r_u_"][data-fading] {
  animation:
    beam-spin-_r_u_ 1.96s linear infinite,
    beam-fade-out-_r_u_ 0.5s ease forwards;
}

[data-beam="_r_u_"][data-active]::after,
[data-beam="_r_u_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_u_),
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
      from var(--beam-angle-_r_u_),
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
      from var(--beam-angle-_r_u_),
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
  opacity: calc(var(--beam-opacity-_r_u_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_u_"][data-active]::before,
[data-beam="_r_u_"][data-fading]::before {
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
    from var(--beam-angle-_r_u_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_u_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_u_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_u_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_u_),
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

[data-beam="_r_u_"][data-active] [data-beam-bloom],
[data-beam="_r_u_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_u_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_u_ {
  to { --beam-angle-_r_u_: 360deg; }
}

@keyframes beam-fade-in-_r_u_ {
  to { --beam-opacity-_r_u_: 1; }
}

@keyframes beam-fade-out-_r_u_ {
  from { --beam-opacity-_r_u_: 1; }
  to { --beam-opacity-_r_u_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonGoJavaScriptTypeScriptC#RustSwiftPHPKotlinDynamic ProgrammingBit ManipulationMatrixArrayMemoizationRecursionDepth-First SearchBreadth-First SearchGreedyHash TableShortest PathBrute-Force SearchSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Oct 16, 2026Minimum XOR Path in a GridEditorial35.1K6Vaibhav Raj Singh・ Open・an hour agoEasy DP approachArrayDynamic ProgrammingBit ManipulationMatrix1+348401Muthu Vrn・ Open・3 hours agoGod is Great 507C++276571eunice・ Open・2 hours agoMinimum XOR Path | Bottom up DP | Bit Masking | Hash Set | Beats 99%ArrayDynamic ProgrammingBit ManipulationMatrix4+211.2K1Aleksandr・ Open・8 hours ago✅ Don’t Be Greedy, Keep All XORs per Cell | Bitset | Beats 100%Dynamic ProgrammingBit ManipulationPythonC++5+142.1K6Bijoy Sing・ Open・5 hours ago✅Simple & Easy Solution → ⏳ O(m × n × 1024) | Bitset + DP | C++, Python, Java, JavaScript, GoArrayDynamic ProgrammingPythonC++3+97183Md Aarzoo Islam・ Open・3 hours ago298ms | Beats 76.03% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayDynamic ProgrammingBit ManipulationMatrix6+72932Kostiantyn Lazukin・ Open・5 hours ago0 msC++31303Den Raskovalov・ Open・5 hours agoFast Java Solution of 3882. Minimum XOR Path in a GridJava31511Ujjawal・ Open・an hour agoSolution that Beats 100%ArrayDynamic ProgrammingBit ManipulationMatrix1+2381RISHABH BABU・ Open・2 hours agoDon’t Be Greedy: Track Every XOR | Bitset Swap TrickC++2522Rohit Kumar Chaurasiya・ Open・40 minutes agoXOR State + DFS Memoization | Standard Recursive Solution ✅ArrayDynamic ProgrammingBit ManipulationMatrix3+2210Aryan Kumar Shaw Halwai・ Open・3 hours ago✅ Beats 94% 🚀 | Grid DP + XOR states 🔥 | Java, C++, Python, JS,Go,TypeScriptArrayDynamic ProgrammingBit ManipulationMatrix6+21080Prabhas Sharma・ Open・3 hours ago3882. Minimum XOR Path in a GridPython31962Abhinav Rai・ Open・2 hours agoMinimum XOR Path Using Dynamic ProgrammingArrayDynamic ProgrammingBit ManipulationMatrix1+1361All Solutions✅ Don’t Be Greedy, Keep All XORs per Cell | Bitset | Beats 100%Aleksandr2.1K8 hours agoDynamic ProgrammingBit ManipulationPythonC++5+Python3C++JavaGoJavaScriptTypeScriptclass Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [{0}] + [set() for _ in range(len(grid[0]) - 1)]  # dp[j]: every XOR that can reach column j of the row above
        for row in grid:
            for j, v in enumerate(row):
                dp[j] = {x ^ v for x in dp[j] | (dp[j - 1] if j else set())}  # come from above or from the left
        return min(dp[-1])
Intuition
The Greedy idea looks natural here: at every cell, keep only the smallest XOR so far. But it won't work. Take this grid:
1 2
0 7
There are only two paths to the 7 in the corner:




















PathXOR before 7XOR at the end1 → 2 → 71 ^ 2 = 33 ^ 7 = 4 ✅1 → 0 → 71 ^ 0 = 1 ← Greedy keeps this1 ^ 7 = 6 ❌
Greedy compares the paths one step before the end and keeps only the smaller XOR, 1, so it ends with 6. The path it threw away ends with 4: it looked worse halfway and still wins, because XOR can flip any bit.
So don't be greedy: every cell has to remember all the XORs that can reach it.
The number of paths grows very fast, but the number of different XORs doesn't: every value is below 1024, so it fits in 10 bits, and XOR never adds bit. So every path's XOR is one of 0, 1, …, 1023, and a cell's set never holds more than 1024 numbers.
Approach: All XORs per Cell | O(m · n · 1024)

One row is enough. A cell is reached only from the cell above it or the cell to its left, so we never need anything older than the row above. We keep a single row of sets, dp, where dp[j] holds every XOR that can reach column j in the current row.
We fill the row from left to right. Before we update dp[j], it still holds the cell above, and dp[j - 1] already holds the cell to the left. Join the two sets and XOR every value with the cell.
The answer is the smallest XOR in the last cell.

Complexity:

Time: O(m⋅n⋅1024), about a million steps at most, since m * n <= 1000.
Space: O(n⋅1024).


Bonus: Bitset | Beats 100%
Python3KEEP = [sum(1 << x for x in range(1024) if not x >> k & 1) for k in range(10)]  # KEEP[k]: positions whose bit k is 0, built once


def xor_all(mask, v):  # {x ^ v for x in mask} on all 1024 bits at once
    for k, low in enumerate(KEEP):
        if v >> k & 1:
            s = 1 << k
            mask = (mask & low) << s | (mask >> s) & low  # swap each pair of s-bit blocks
    return mask


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [1 << x for x in accumulate(grid[0], xor)]  # first row: one path to each cell, so one XOR
        for row in grid[1:]:
            dp[0] = 1 << (dp[0].bit_length() - 1 ^ row[0])  # first column: one path too
            for j in range(1, len(row)):
                dp[j] = xor_all(dp[j] | dp[j - 1], row[j])
        return (dp[-1] & -dp[-1]).bit_length() - 1  # the lowest set bit is the smallest XOR
Store each set as one 1024-bit number: bit x is on when XOR x can reach the cell. Joining two sets is then just |.
XOR-ing every member with v moves the bit at position x to x ^ v. We can do that one bit of v at a time: for bit k, swap every pair of neighbouring blocks of 2^k positions. Positions 0 to 7, left to right:
v = 1:   a b c d e f g h   →   b a d c f e h g
v = 2:   ab cd ef gh       →   cd ab gh ef
v = 4:   abcd efgh         →   efgh abcd
For v = 3, do the first two swaps. A value has at most 10 bits, so each cell takes at most 10 swaps, each one on all 1024 bits at once. The smallest XOR is the lowest bit that's on.
Two more things keep it fast:

The 10 masks are built once, outside the class, instead of on every test.
Every cell in the first row and the first column has only one path to it, so its set is a single XOR, 1 << x, with no swaps.

Complexity:

Time: O(m⋅n⋅wV​logV), where V=1024 is the number of possible XORs and w is the machine word size: at most 10 swaps per cell, each on a 1024-bit number.
Space: O(n⋅wV​).
 PreviousMinimum XOR Path | Bottom up DP | Bit Masking | Hash Set | Beats 99%Next✅Simple & Easy Solution → ⏳ O(m × n × 1024) | Bitset + DP | C++, Python, Java, JavaScript, GoComments (6)Sort by:BestCommentJordinario4 hours agoexactly my solution! in math terms:
dp[i][j]=⎩⎨⎧​{g[0][0]}dp[0][j−1]⊕g[0][j]dp[i−1][0]⊕g[i][0](dp[i−1][j]∪dp[i][j−1])⊕g[i][j]​i=0, j=0i=0, j≥1i≥1, j=0i,j≥1​ Read more3Stefan Pochmann5 hours agoChallenge for fun: Can you do xor_all fast without pre-computing the 10 masks? Read more11BT19CIV052 BHUSHAN KOLPEan hour ago Read more0Nguyen-Phuc Mac4 hours agoDP and bitwise? Genius. Read more0Kostiantyn Lazukin5 hours agoNice one. I believe it will be faster than mine if properly refined Read more0codeDominar3 hours ago Read more01146Python3Auto1234567class Solution:    def minCost(self, grid: list[list[int]]) -> int:        dp = [{0}] + [set() for _ in range(len(grid[0]) - 1)]  # dp[j]: every XOR that can         reach column j of the row above        for row in grid:            for j, v in enumerate(row):                dp[j] = {x ^ v for x in dp[j] | (dp[j - 1] if j else set())}  # come from above                 or from the left        return min(dp[-1])In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 1, Col 1AcceptedRuntime: 0 msCase 1Case 2Case 3Inputgrid =[[1,2],[3,4]]Output6Expected6Contribute a testcaseInput9123›[[1,2],[3,4]][[6,7],[5,8]][[2,7,5]]Output9123›690Expected9123›690 All SubmissionsAccepted999 / 999 testcases passedMUTHU KUMAR Msubmitted at Oct 28, 2026 10:24AnalysisSolutionCodePython31class Solution:
2    def minCost(self, grid: list[list[int]]) -> int:
3        dp = [{0}] + [set() for _ in range(len(grid[0]) - 1)]  # dp[j]: every XOR that can reach column j of the row above
4        for row in grid:
5            for j, v in enumerate(row):
6                dp[j] = {x ^ v for x in dp[j] | (dp[j - 1] if j else set())}  # come from above or from the left
7        return min(dp[-1]) 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
