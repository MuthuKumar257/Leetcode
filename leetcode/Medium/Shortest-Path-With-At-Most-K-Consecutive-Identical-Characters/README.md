# 3970. Shortest Path With At Most K Consecutive Identical Characters

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Shortest Path With At Most K Consecutive Identical Characters](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

## Solution

See [`solution_v2.py`](./solution_v2.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function l(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit300:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3970. Shortest Path With At Most K Consecutive Identical CharactersSolvedMediumTopicsCompaniesHintYou are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

 
Example 1:


Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:


	Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.

The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

Example 2:


Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

Output: 2

Explanation:

The optimal valid path from node 0 to node 2 is as follows:


	Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
	Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.

The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.

Example 3:


Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

Output: -1

Explanation:

There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.


 
Constraints:


	1 <= n == labels.length <= 5 * 104
	0 <= edges.length <= 5 * 104
	edges[i] == [ui, vi, wi]
	0 <= ui, vi <= n - 1
	ui != vi
	1 <= wi <= 104
	labels consists of lowercase English letters
	1 <= k <= 50

 Seen this question in a real interview before?1/6YesNoAccepted54,727/92.1KAcceptance Rate59.4%TopicsStaffStringGraph TheoryHeap (Priority Queue)Shortest PathWeekly Contest 507CompaniesHint 1The validity of a path depends not only on the current node, but also on how many consecutive times the current node’s label has appeared at the end of the path.Hint 2Use Dijkstra on states (node, count), where count is the current consecutive run length of labels[node].Hint 3When moving from node u to node v, the next count becomes count + 1 if labels[u] == labels[v], otherwise it becomes 1. Ignore transitions where the next count exceeds k.Hint 4The answer is the minimum distance among all states ending at node n - 1.Discussion (105)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestRitik SainiJun 21, 2026who all tried DFS and failed 🥀 Read more647Shashank SinhaJun 21, 2026998/999 gang 🥀🥀 Read more391rajganatra11Jun 21, 2026998/999 wrong ans Read more391Som 07Jun 21, 2026 Read moreRead more353r1suJun 21, 2026If you have solved 787. Cheapest Flights Within K Stops
or similar problems, this wasn't too hard. Read more266SS88Jun 21, 2026I dont know how 7.5 k could solve so easily :( Read more181Ched314 hours agoHere are some testcases for you guys ------------------->
4
[[1,2,1746],[0,1,3],[1,2,9],[2,3,2]]
"abab"
1
4
[[3,2,9451],[2,0,1125],[2,3,3227],[2,0,2859],[0,1,8],[1,2,8],[2,3,8]]
"abab"
1
5
[[2,0,3632],[2,0,6106],[4,2,9001],[2,1,6743],[0,1,6],[1,2,4],[2,3,1],[3,4,3]]
"ababa"
2
7
[[6,0,7605],[6,4,8817],[0,1,6],[1,2,8],[2,3,8],[3,4,3],[4,5,3],[5,6,3]]
"abababa"
2
7
[[3,1,4380],[4,5,2824],[2,3,2955],[1,6,7805],[2,1,5476],[0,1,1],[1,2,7],[2,3,5],[3,4,9],[4,5,7],[5,6,2]]
"abababa"
2
8
[[7,6,3632],[5,7,5795],[0,3,9644],[3,7,7723],[2,0,3361],[1,4,2754],[1,7,8012],[0,1,5],[1,2,4],[2,3,9],[3,4,10],[4,5,6],[5,6,10],[6,7,7]]
"abababab"
3
18
[[11,0,4511],[9,8,8467],[17,6,8643],[14,11,8513],[9,12,3534],[1,12,7359],[7,4,850],[2,6,7945],[14,0,9242],[5,6,5188],[4,10,2552],[17,11,8428],[0,6,3076],[2,5,1505],[12,5,3681],[9,13,4756],[0,1,10],[1,2,2],[2,3,4],[3,4,3],[4,5,7],[5,6,6],[6,7,10],[7,8,9],[8,9,2],[9,10,4],[10,11,3],[11,12,5],[12,13,2],[13,14,7],[14,15,8],[15,16,9],[16,17,4]]
"ababababababababab"
6
368
[[122,263,1449],[337,290,3312],[17,32,2730],[138,328,6705],[3,215,540],[20,292,8425],[176,16,6051],[222,57,9879],[74,109,3272],[34,302,7036],[362,348,5718],[192,72,3042],[145,58,8590],[98,268,8038],[189,191,9241],[21,306,2502],[185,26,3976],[330,141,5256],[317,167,9062],[45,123,1715],[320,278,7986],[363,184,1778],[301,67,376],[355,161,1920],[339,44,7905],[367,339,8135],[168,235,8292],[329,245,8873],[269,253,6307],[319,117,3943],[218,331,2772],[349,39,7884],[344,57,1998],[320,108,1112],[42,144,2065],[129,179,8430],[95,338,3908],[257,260,4416],[183,239,5977],[12,344,1122],[113,250,909],[108,229,2196],[308,347,4774],[175,276,7459],[187,191,6962],[162,335,7925],[305,159,133],[231,184,1833],[18,117,9110],[227,268,5230],[359,90,6224],[93,217,7033],[270,48,3406],[312,58,402],[336,177,3058],[240,124,4156],[310,328,9509],[303,135,8346],[6,348,6663],[4,57,3275],[230,86,7817],[102,42,911],[246,340,867],[323,295,4495],[0,1,2],[1,2,6],[2,3,2],[3,4,3],[4,5,7],[5,6,4],[6,7,5],[7,8,8],[8,9,3],[9,10,6],[10,11,4],[11,12,3],[12,13,7],[13,14,9],[14,15,6],[15,16,9],[16,17,7],[17,18,10],[18,19,3],[19,20,5],[20,21,7],[21,22,6],[22,23,1],[23,24,5],[24,25,3],[25,26,7],[26,27,8],[27,28,9],[28,29,6],[29,30,10],[30,31,4],[31,32,1],[32,33,1],[33,34,8],[34,35,5],[35,36,10],[36,37,8],[37,38,7],[38,39,9],[39,40,3],[40,41,9],[41,42,4],[42,43,3],[43,44,2],[44,45,2],[45,46,8],[46,47,2],[47,48,7],[48,49,5],[49,50,1],[50,51,1],[51,52,4],[52,53,6],[53,54,8],[54,55,2],[55,56,6],[56,57,5],[57,58,4],[58,59,10],[59,60,5],[60,61,8],[61,62,3],[62,63,8],[63,64,1],[64,65,6],[65,66,2],[66,67,4],[67,68,4],[68,69,5],[69,70,4],[70,71,2],[71,72,4],[72,73,10],[73,74,7],[74,75,8],[75,76,4],[76,77,5],[77,78,1],[78,79,5],[79,80,8],[80,81,8],[81,82,6],[82,83,1],[83,84,2],[84,85,9],[85,86,2],[86,87,4],[87,88,2],[88,89,5],[89,90,5],[90,91,2],[91,92,6],[92,93,4],[93,94,1],[94,95,8],[95,96,2],[96,97,7],[97,98,6],[98,99,1],[99,100,2],[100,101,10],[101,102,9],[102,103,6],[103,104,6],[104,105,7],[105,106,9],[106,107,7],[107,108,2],[108,109,10],[109,110,2],[110,111,9],[111,112,1],[112,113,9],[113,114,10],[114,115,4],[115,116,8],[116,117,9],[117,118,6],[118,119,8],[119,120,8],[120,121,3],[121,122,1],[122,123,8],[123,124,3],[124,125,1],[125,126,2],[126,127,8],[127,128,5],[128,129,8],[129,130,8],[130,131,6],[131,132,1],[132,133,2],[133,134,5],[134,135,2],[135,136,8],[136,137,1],[137,138,2],[138,139,7],[139,140,6],[140,141,5],[141,142,2],[142,143,6],[143,144,9],[144,145,7],[145,146,4],[146,147,4],[147,148,1],[148,149,9],[149,150,10],[150,151,3],[151,152,3],[152,153,9],[153,154,9],[154,155,8],[155,156,3],[156,157,9],[157,158,4],[158,159,1],[159,160,3],[160,161,6],[161,162,1],[162,163,8],[163,164,1],[164,165,6],[165,166,1],[166,167,10],[167,168,8],[168,169,8],[169,170,8],[170,171,8],[171,172,8],[172,173,3],[173,174,7],[174,175,6],[175,176,4],[176,177,7],[177,178,7],[178,179,3],[179,180,4],[180,181,5],[181,182,9],[182,183,3],[183,184,6],[184,185,8],[185,186,10],[186,187,8],[187,188,10],[188,189,8],[189,190,8],[190,191,10],[191,192,2],[192,193,8],[193,194,10],[194,195,9],[195,196,4],[196,197,3],[197,198,5],[198,199,6],[199,200,2],[200,201,8],[201,202,6],[202,203,2],[203,204,2],[204,205,6],[205,206,4],[206,207,9],[207,208,6],[208,209,8],[209,210,5],[210,211,2],[211,212,2],[212,213,6],[213,214,1],[214,215,6],[215,216,4],[216,217,10],[217,218,1],[218,219,8],[219,220,6],[220,221,7],[221,222,9],[222,223,10],[223,224,1],[224,225,5],[225,226,4],[226,227,4],[227,228,3],[228,229,7],[229,230,9],[230,231,4],[231,232,3],[232,233,2],[233,234,10],[234,235,5],[235,236,5],[236,237,3],[237,238,5],[238,239,3],[239,240,7],[240,241,6],[241,242,9],[242,243,2],[243,244,2],[244,245,8],[245,246,3],[246,247,3],[247,248,2],[248,249,4],[249,250,3],[250,251,5],[251,252,4],[252,253,1],[253,254,4],[254,255,9],[255,256,10],[256,257,8],[257,258,6],[258,259,3],[259,260,3],[260,261,8],[261,262,3],[262,263,3],[263,264,3],[264,265,6],[265,266,6],[266,267,7],[267,268,5],[268,269,7],[269,270,9],[270,271,6],[271,272,6],[272,273,6],[273,274,2],[274,275,5],[275,276,4],[276,277,6],[277,278,8],[278,279,3],[279,280,5],[280,281,2],[281,282,9],[282,283,1],[283,284,7],[284,285,8],[285,286,4],[286,287,10],[287,288,1],[288,289,3],[289,290,5],[290,291,8],[291,292,9],[292,293,4],[293,294,4],[294,295,4],[295,296,9],[296,297,2],[297,298,5],[298,299,3],[299,300,1],[300,301,10],[301,302,5],[302,303,9],[303,304,9],[304,305,8],[305,306,6],[306,307,6],[307,308,1],[308,309,7],[309,310,7],[310,311,2],[311,312,4],[312,313,3],[313,314,3],[314,315,6],[315,316,2],[316,317,7],[317,318,6],[318,319,8],[319,320,9],[320,321,9],[321,322,1],[322,323,8],[323,324,2],[324,325,6],[325,326,10],[326,327,5],[327,328,5],[328,329,3],[329,330,10],[330,331,4],[331,332,7],[332,333,3],[333,334,10],[334,335,9],[335,336,4],[336,337,6],[337,338,4],[338,339,3],[339,340,4],[340,341,3],[341,342,4],[342,343,8],[343,344,6],[344,345,4],[345,346,10],[346,347,3],[347,348,4],[348,349,2],[349,350,2],[350,351,10],[351,352,2],[352,353,7],[353,354,1],[354,355,8],[355,356,10],[356,357,1],[357,358,9],[358,359,6],[359,360,3],[360,361,9],[361,362,7],[362,363,2],[363,364,3],[364,365,5],[365,366,10],[366,367,2]]
"abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
28
Randomly generated test cases using the web extension LeetTest!
Also provides up to date company tags and elo rating for problems!
Downloadable on the Chrome webstore or Firefox addons and works for most leetcode problems Read more16Sushant4599Jun 21, 2026This was actually a pretty standard dp on graphs problem!
If one has seen state modelling problems on dijakstra algo. Read more114TusharJun 21, 2026I did my part lowering the acceptance rate—6 wrong submissions this contest! 🤡 Honestly, sleeping would have been a much better choice. 😴💤 Read more223Cajun Mar16 hours agoSplit into layers according to the consecutive characters at the end of the path, and then just run Dijkstra.
 Read more91123411Copyright © 2026 LeetCode. All rights reserved.2181052531 Online
@property --beam-angle-_r_7p_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_7p_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_7p_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_7p_"][data-active] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-in-_r_7p_ 0.6s ease forwards;
}

[data-beam="_r_7p_"][data-fading] {
  animation:
    beam-spin-_r_7p_ 1.96s linear infinite,
    beam-fade-out-_r_7p_ 0.5s ease forwards;
}

[data-beam="_r_7p_"][data-active]::after,
[data-beam="_r_7p_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
      from var(--beam-angle-_r_7p_),
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
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"][data-active]::before,
[data-beam="_r_7p_"][data-fading]::before {
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
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_7p_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_7p_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_7p_),
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

[data-beam="_r_7p_"][data-active] [data-beam-bloom],
[data-beam="_r_7p_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_7p_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_7p_ {
  to { --beam-angle-_r_7p_: 360deg; }
}

@keyframes beam-fade-in-_r_7p_ {
  to { --beam-opacity-_r_7p_: 1; }
}

@keyframes beam-fade-out-_r_7p_ {
  from { --beam-opacity-_r_7p_: 1; }
  to { --beam-opacity-_r_7p_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaJavaScriptPythonGoTypeScriptRustCC#KotlinSwiftPHPGraph TheoryHeap (Priority Queue)Shortest PathDijkstra's AlgorithmStringDynamic ProgrammingDirected Acyclic GraphBreadth-First SearchGreedyMathArrayBit ManipulationLinked ListQueueHash TableYour last submission beat 38% of other submissions' runtime.Share my solutionLeetCode・ Open・Oct 16, 2026Shortest Path With At Most K Consecutive Identical CharactersEditorial510.8K3Aleksandr・ Open・18 hours ago✅ Dijkstra with a Twist | Beats 99%Graph TheoryShortest PathPythonC++6+709.9K5Vaibhav Raj Singh・ Open・12 hours agoModified Dijkstra SolutionGraph TheoryHeap (Priority Queue)Shortest PathC++1+551.6K2Md Aarzoo Islam・ Open・14 hours ago201ms | Beats 74.42% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Graph TheoryHeap (Priority Queue)Shortest PathC++5+344.3K4Muthu Vrn・ Open・13 hours agoGod is Great 509C++307491Aryan Kumar Shaw Halwai・ Open・13 hours ago✅ Beats 54% 🚀 |  Dijkstra’s algorithm 🔥 | Java, C++, Python, JSStringGraph TheoryHeap (Priority Queue)Shortest Path5+125811Debesh P・ Open・15 hours agobeats 99% | 30 ms | dijkstra's algorithm | dynamic programming | you won't regret babygirl!Dynamic ProgrammingGraph TheoryHeap (Priority Queue)Shortest Path6+54702Kostiantyn Lazukin・ Open・15 hours agoC++ 7msC++31542Abhinav Pardhu・ Open・11 hours agoDijkstra’s Algorithm | Shortest Path with Consecutive Label Constraint (State Expansion)Java33170Ujjawal・ Open・10 hours agoSolution that Beats 100%StringDynamic ProgrammingGreedyBreadth-First Search5+21631SATYAM・ Open・2 hours agoEasy-to-Understand Java Solution | Stateful Dijkstra StrategyJava2350Long Nguyen・ Open・6 hours ago100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+21330SouLAditya・ Open・8 hours agoO((V + E) · k log(V · k)) Time | O(V · k + E) Space | 2D Dijkstra on State-Expanded GraphStringGraph TheoryHeap (Priority Queue)Shortest Path2+2270Anushka Tripathi・ Open・3 hours agoDijkstra's Algorithm + State Expansion + Min Heap | Python 3 | Graph + HeapGraph TheoryHeap (Priority Queue)Shortest PathPython31+1181MBBN・ Open・7 hours agoJava - Clean Solution | Modified Dijkstra's AlgorithmJava1631DANDAPAT_sUBHAM・ Open・8 hours agoRuntime 0 ms ,, Beats 100.00%,,,,,,,,,,,,,,,,Accepted 1001 / 1001 testcases passed..............Python311151Prabhas Sharma・ Open・12 hours ago3970. Shortest Path With At Most K Consecutive Identical CharactersPython312201Sagar Gupta・ Open・14 hours agoDijkstra Over (Node, Run Length) | C++ Java Python JSStringGraph TheoryHeap (Priority Queue)Shortest Path4+11381Chidipothu Jaswin・ Open・14 hours agoC++ | Beats 95% | DijkstrasDynamic ProgrammingGreedyGraph TheoryHeap (Priority Queue)2+11101Den Raskovalov・ Open・15 hours agoFast Java Solution of 3970. Shortest Path With At Most K Consecutive Identical CharactersJava12071Ankit Mohapatra・ Open・an hour agoEasy C++ Code || Simple For Beginners || Beats 100%StringGraph TheoryHeap (Priority Queue)Shortest Path1+160UseridTaken・ Open・3 hours agoDijkstra's Algorithm with Consecutive Character Constraints ✌️✌️C++1100LeetCodeBee・ Open・3 hours ago✅ C++ | | Clear and Efficient Solution | | Beats 99.22% 💯StringGraph TheoryHeap (Priority Queue)Shortest Path1+170CodingVoid・ Open・3 hours ago350msJavaScript140ShivekGupta0003・ Open・5 hours ago⚡ [0ms / Beats 100%] State-Space Expansion Dijkstra | O((E*K) log(V*K)) | Java / C++ / Python3 🚀StringGraph TheoryHeap (Priority Queue)Shortest Path3+1130Vaidehi Kharde・ Open・5 hours agoDijkstra's Catch: Why Distance Alone Isn't Enough! 😎StringGraph TheoryHeap (Priority Queue)Shortest Path1+160Kr_Suryansh・ Open・6 hours agoConstrained Shortest PathDynamic ProgrammingGraph TheoryCHeap (Priority Queue)1+1100kunal kathore・ Open・6 hours ago3970. Shortest Path With At Most K Consecutive Identical CharactersPython31160Abhay Mishra・ Open・6 hours agoSimple Approach | | Dijkstra's AlgorithmPython1290myNiceCloud・ Open・7 hours agoJS Easy – Dijkstra + State Expansion + MinPQ, T(O): O((n + m) · k log(nk)), S(O): O(nk + m)JavaScript160All Solutions✅ Dijkstra with a Twist | Beats 99%Aleksandr9.9K18 hours agoGraph TheoryShortest PathPythonC++6+Python3C++JavaGoJavaScriptTypeScriptclass Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        best = [k + 1] * n  # best[x]: the shortest run x was settled with, k + 1 until then
        heap = [(0, 1, 0)]  # (distance, run, node): the walk ends with run nodes labeled labels[node]
        while heap:
            d, run, x = heappop(heap)
            if run >= best[x]:  # x was settled before, no farther away and with a run no longer
                continue
            if x == n - 1:
                return d
            best[x] = run
            for y, w in graph[x]:
                r = run + 1 if labels[y] == labels[x] else 1
                if r < best[y]:
                    heappush(heap, (d + w, r, y))
        return -1
Intuition
We need the cheapest way from node 0 to node n - 1 along directed edges with positive weights: sounds like Dijkstra.
Why Plain Dijkstra Will Fail
The label rule adds a twist: reading the labels along the way, no letter may appear more than k times in a row. Because of that, the best walk can visit a node twice. With labels = "aaba", k = 2 and every weight 1:
0a → 1a → 3a
     ↑↓
     2b

Dijkstra:  0 → 1, and 1 → 3   ->  "aaa": stuck at 1  ->  ans = -1  ❌
Shortest:  0 → 1 → 2 → 1 → 3  ->  "aabaa"            ->  ans = 4   ✅
Plain Dijkstra finishes node 1 on its first visit, after "aa", and from there 3 is out of reach. The detour through 2 comes back to 1 reading "aaba", with a single a at the end, and only that second visit can step to 3.
Dijkstra with the Label Rule
The Rule doesn't change weights, only which steps are allowed.
And that depends on how the walk ends, not just on where it is. With k = 2:
"…baa" + a  →  "…baaa"   ❌ three a's in a row
"…aba" + a  →  "…abaa"   ✅
So each Dijkstra state also keeps the run: how many nodes at the end of the walk share the last node's label. A state is (node, run), and a step from x to y updates the run like this:
# same label: the run grows; otherwise it restarts
r = run + 1 if labels[y] == labels[x] else 1
The step is allowed only while r <= k.
The rest is plain Dijkstra, just over states instead of nodes.
Many states can be skipped.
Dijkstra settles states in order of distance, so any state settled at x before is no farther away. If its run is no longer either, it can take every step a new state at x can, and the new one has nothing to add.
So one number per node is enough, best[x]: the shortest run x was settled with. A popped state is expanded only if its run beats it:
if run >= best[x]:  # x was settled before, no farther away and with a run no longer
    continue
states at x, as Dijkstra pops them: (distance, run)
(5, 2)  settled → best[x] = 2
(6, 2)  skipped: farther, with the same run
(7, 1)  settled → best[x] = 1: farther, but a shorter run allows more same-label steps
(9, 1)  skipped: farther, with the same run
The best run at a node only goes down, so each node is settled at most k times.
Approach: Dijkstra over (node, run)
Graph. graph[u] lists (v, w) for every edge u → v of weight w.
graph = [[] for _ in range(n)]
for u, v, w in edges:
    graph[u].append((v, w))
Heap. Holds states nearest first, starting with node 0 at distance 0. Each state also carries its run: (distance, run, node) instead of (distance, node), and node 0 alone is a run of 1, so the heap starts as [(0, 1, 0)].
heap = [(0, 1, 0)]
Best. best[x] is the shortest run x was settled with. It takes the place of plain Dijkstra's "visited": a node can be settled again, but only with a shorter run. It starts at k + 1, which also caps every run at k.
best = [k + 1] * n
Loop. Pop the nearest state (d, run, x), then:

skip it if run >= best[x]
return d if x is n - 1
set best[x] = run
relax every edge x → y, with the new run r
push (d + w, r, y) only if r < best[y]: any other would be skipped when popped

while heap:
    d, run, x = heappop(heap)
    if run >= best[x]:  # skip
        continue
    if x == n - 1:  # return
        return d
    best[x] = run  # set
    for y, w in graph[x]:  # relax
        r = run + 1 if labels[y] == labels[x] else 1
        if r < best[y]:  # push
            heappush(heap, (d + w, r, y))
Return -1 if the heap runs dry: n - 1 can't be reached.
Complexity

Time: O(n+k⋅mlog(k⋅m)): each node is settled at most k times, each settlement scans node out-edges, and each push/pop is a heap operation.
Space: O(n+k⋅m): graph,best and up to k·m + 1 states in the heap.
 PreviousShortest Path With At Most K Consecutive Identical CharactersNextModified Dijkstra SolutionComments (5)Sort by:BestCommentKostiantyn Lazukin15 hours agoI think you can make further optimisations but choose not to 🤔 Read more21Ishanbagra10 hours agohttps://leetcode.com/discuss/post/8594253/leetcode-keeps-logging-me-out-every-day-l7buq/comments/3592520/ Read more0Jaysurya90911 hours agoyou are not even using the best array u can just use k+1 for comparison dont even need  a array Read more01DrawToCode13 hours ago💡 Can't visualize this problem? Contribute!
🎯 Visualize:  Shortest Path With At Most K Consecutive Identical Characters
🎯 Contribute just one frame! Others can continue from where you left off, and together we can build a complete visualization.
💡 Can't find the visualization you need? Request it and let the community know!
🚀 One frame from you, another from someone else. Let's visualize together!
🎥 Watch how to contribute


✨ If you use DrawToCode, you'll want to use it every time. If you don't, it's your loss.
 Read moreRead more0codeDominar13 hours ago Read more01705Python3Auto91011121314151617181920        labels[node]        while heap:            d, run, x = heappop(heap)            if run >= best[x]:  # x was settled before, no farther away and with a run no             longer                continue            if x == n - 1:                return d            best[x] = run            for y, w in graph[x]:                r = run + 1 if labels[y] == labels[x] else 1                if r < best[y]:                    heappush(heap, (d + w, r, y))        return -1In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 20, Col 18AcceptedRuntime: 0 msCase 1Case 2Case 3Inputn =3edges =[[0,1,1],[1,2,1],[0,2,3]]labels ="aab"k =1Output3Expected3Contribute a testcaseInput99123456789101112›3[[0,1,1],[1,2,1],[0,2,3]]"aab"13[[0,1,1],[1,2,1],[0,2,3]]"aab"23[[0,1,1],[1,2,1]]"aaa"2Output9123›32-1Expected9123›32-1 All SubmissionsAccepted1001 / 1001 testcases passedMUTHU KUMAR Msubmitted at Oct 30, 2026 20:32AnalysisSolutionCodePython31class Solution:
2    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
3        graph = [[] for _ in range(n)]
4        for u, v, w in edges:
5            graph[u].append((v, w))
6
7        best = [k + 1] * n  # best[x]: the shortest run x was settled with, k + 1 until then
8        heap = [(0, 1, 0)]  # (distance, run, node): the walk ends with run nodes labeled labels[node]
9        while heap:
10            d, run, x = heappop(heap)
11            if run >= best[x]:  # x was settled before, no farther away and with a run no longer
12                continue
13            if x == n - 1:
14                return d
15            best[x] = run
16            for y, w in graph[x]:
17                r = run + 1 if labels[y] == labels[x] else 1
18                if r < best[y]:
19                    heappush(heap, (d + w, r, y))
20        return -1View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
