# 2747. Count Zero Request Servers

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Count Zero Request Servers](https://leetcode.com/problems/count-zero-request-servers/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit500:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result2747. Count Zero Request ServersMediumTopicsCompaniesHintYou are given an integer n denoting the total number of servers and a 2D 0-indexed integer array logs, where logs[i] = [server_id, time] denotes that the server with id server_id received a request at time time.

You are also given an integer x and a 0-indexed integer array queries.

Return a 0-indexed integer array arr of length queries.length where arr[i] represents the number of servers that did not receive any requests during the time interval [queries[i] - x, queries[i]].

Note that the time intervals are inclusive.

 
Example 1:

Input: n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
Output: [1,2]
Explanation: 
For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.



Example 2:

Input: n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]
Output: [0,1]
Explanation: 
For queries[0]: All servers get at least one request in the duration of [1, 3].
For queries[1]: Only server with id 3 gets no request in the duration [2,4].



 
Constraints:


	1 <= n <= 105
	1 <= logs.length <= 105
	1 <= queries.length <= 105
	logs[i].length == 2
	1 <= logs[i][0] <= n
	1 <= logs[i][1] <= 106
	1 <= x <= 105
	x < queries[i] <= 106

 Seen this question in a real interview before?1/6YesNoAccepted55,176/100.1KAcceptance Rate55.1%TopicsStaffArrayHash TableSliding WindowSortingBiweekly Contest 107CompaniesHint 1Can we use sorting and two-pointer approach here?Hint 2Sort the queries array and logs array based on time in increasing order.Hint 3For every window of size x, use sliding window and two-pointer approach to find the answer to the queries.Discussion (124)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestDaniel KallaJun 25, 2023I feel this problem should be ranked hard, unless there's some medium-level solution for it I'm missing. Read more681Aman BhardwajJul 02, 2023Where is id 3 ??
Input: n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
Output: [1,2]
Explanation:
For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period. Read more607Dmitry SapelnikovNov 09, 2024Medium problems around 2750 have been apparently written by the same author: they all have awful descriptions, poor examples, high difficulty and acceptance rates ~30%. Read more501AAADMay 20, 2025how can one question description be so confusing ? Read more411DrMonotoneJul 15, 2024Understanding the question itself could probably quantify as a hard problem, not to mention solving it 💀 Read more36Harshit Kushwah9 hours agoHappy Dhanteras To Everyone Read more28SarveshJun 24, 2023Servers were crash world-wide and only Chinese servers were running properly. That's why they ranked top in this contest. Read more391Shourya Vaidhya Jain15 hours ago2400+ rated medium Read moreRead more305SidJun 25, 2023This is NOT a medium problem as far as my solution is considered, even finding it difficult to explain my solution. Read more16meow12 hours agoSuch a bad description. Read more15123413Copyright © 2026 LeetCode. All rights reserved.6111243509 Online
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

LeetSort byAllMy SolutionPython3C++JavaJavaScriptPythonGoCRustC#TypeScriptKotlinScalaSwiftRubyDartSliding WindowSortingHash TableArrayTwo PointersOrdered MapCountingBinary TreeSweep LineOrdered SetBinary SearchHash FunctionBit ManipulationHeap (Priority Queue)Submit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Oct 29, 2026Count Zero Request ServersEditorial913.5K6Aleksandr・ Open・19 hours ago✅ Sort and SlideHash TableSliding WindowSortingPython6+5512.2K5Muthu Vrn・ Open・14 hours agoGod is Great 516Python3311.5K0Bijoy Sing・ Open・16 hours ago✅ Optimal Solution → O(m log m + k log k) | Sliding Window Sliding WindowSortingPythonC++3+133.9K1Aryan Kumar Shaw Halwai・ Open・15 hours ago✅ Beats 100% 🚀 | Sort Queries, Slide the Window, Count Active Servers  🔥 | Java, C++, Python, JSArrayHash TableTwo PointersSliding Window6+101.1K0Md Aarzoo Islam・ Open・16 hours ago96ms | Beats 47.62% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayHash TableSliding WindowSorting6+81.4K1MBBN・ Open・11 hours agoJava - Clean Solution | Sorting + Sliding WindowJava54001Manjeet Dhayal・ Open・12 hours agoSort and use Sliding window as time is monotonic | Intutive | ExplainedArrayHash TableSliding WindowSorting1+53350Stefan Pochmann・ Open・8 hours agoThree types of eventPython34650Vaidehi Kharde・ Open・5 hours ago🤯 When Linear Isn't Faster: How Sparse Timestamps Make O(L log L) Beat O(T)! ⚡ArrayHash TableSliding WindowSorting1+2491Prabhas Sharma・ Open・13 hours ago2747. Count Zero Request ServersPython321571Aman sahu・ Open・34 minutes agoC++ | TC : O(Nlog(N) + Mlog(M)) C++2210calligraphyguruji・ Open・7 hours agoEasiest Approach Ever | 0 ms | Sorting + Sliding Window C++2820Long Nguyen・ Open・8 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+22280Saadan_Naqvi・ Open・13 hours agoDifference Array + Prefix Sum | O(1) per Query | No Sliding Window | Least Optimal SolutionC++22480All SolutionsGod is Great 516Muthu Vrn1.5K14 hours agoPython3Intuition


Approach

Complexity

Time complexity:



Space complexity:


Code
Python3class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        dico={i:0 for i in range (1,n+1)}
        logs=sorted(logs,key=lambda x:x[1])
        queries=sorted([query,i] for i,query in enumerate(queries))
        p=len(logs)
        right,left=0,-1
        countNull=n
        res=[0]*len(queries)
        for query,i in queries:
            while right <p and logs[right][1]<=query:
                serv=logs[right][0]
                if dico[serv]==0:
                    countNull-=1
                dico[serv]+=1
                right+=1
            while left+1<p and logs[left+1][1]<query-x:
                left+=1
                serv=logs[left][0]
                dico[serv]-=1
                if dico[serv]==0:
                    countNull+=1
            res[i]=countNull
        return res
             Previous✅ Sort and SlideNext✅ Optimal Solution → O(m log m + k log k) | Sliding Window Comments (0)Sort by:BestCommentNo comments yet.310Python3Auto13141516171819202122232425                if dico[serv]==0:                    countNull-=1                dico[serv]+=1                right+=1            while left+1<p and logs[left+1][1]<query-x:                left+=1                serv=logs[left][0]                dico[serv]-=1                if dico[serv]==0:                    countNull+=1            res[i]=countNull        return res            In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 25, Col 13AcceptedRuntime: 0 msCase 1Case 2Inputn =3logs =[[1,3],[2,6],[1,5]]x =5queries =[10,11]Output[1,2]Expected[1,2]Contribute a testcaseInput912345678›3[[1,3],[2,6],[1,5]]5[10,11]3[[2,4],[2,1],[1,2],[3,1]]2[3,4]Output912›[1,2][0,1]Expected912›[1,2][0,1] All SubmissionsAccepted3129 / 3129 testcases passedMUTHU KUMAR Msubmitted at Nov 06, 2026 22:08AnalysisSolutionCodePython31class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        dico={i:0 for i in range (1,n+1)}
4        logs=sorted(logs,key=lambda x:x[1])
5        queries=sorted([query,i] for i,query in enumerate(queries))
6        p=len(logs)
7        right,left=0,-1
8        countNull=n
9        res=[0]*len(queries)
10        for query,i in queries:
11            while right <p and logs[right][1]<=query:
12                serv=logs[right][0]
13                if dico[serv]==0:
14                    countNull-=1
15                dico[serv]+=1
16                right+=1
17            while left+1<p and logs[left+1][1]<query-x:
18                left+=1
19                serv=logs[left][0]
20                dico[serv]-=1
21                if dico[serv]==0:
22                    countNull+=1
23            res[i]=countNull
24        return res
25            View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
