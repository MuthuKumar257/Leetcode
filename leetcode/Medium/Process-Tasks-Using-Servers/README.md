# 1882. Process Tasks Using Servers

- **Difficulty:** Medium
- **Language:** Python
- **LeetCode Link:** [Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1882. Process Tasks Using ServersMediumTopicsCompaniesHintYou are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.

 
Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

Example 2:

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.


 
Constraints:


	servers.length == n
	tasks.length == m
	1 <= n, m <= 2 * 105
	1 <= servers[i], tasks[j] <= 2 * 105

 Seen this question in a real interview before?1/6YesNoAccepted111,669/211.1KAcceptance Rate52.9%TopicsStaffArrayHeap (Priority Queue)Weekly Contest 243CompaniesHint 1You can maintain a Heap of available Servers and a Heap of unavailable serversHint 2Note that the tasks will be processed in the input order so you just need to find the x-th server that will be available according to the rulesSimilar QuestionsParallel Courses IIIHardDiscussion (123)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestPratham mehtaFeb 14, 2024i anyone who like me not understand the problem ? Read more641user1115GoAug 30, 2025For some reason, the problems involving scheduling of tasks fascinate me. Seem to be closer to real world implementations.
Anybody else who feels the same ? 😶 Read more782SidAug 22, 2023found it to be a lower hard than medium Read more51SerhiiJun 23, 2023servers
[338,890,301,532,284,930,426,616,919,267,571,140,716,859,980,469,628,490,195,664,925,652,503,301,917,563,82,947,910,451,366,190,253,516,503,721,889,964,506,914,986,718,520,328,341,765,922,139,911,578,86,435,824,321,942,215,147,985,619,865]
tasks
[773,537,46,317,233,34,712,625,336,221,145,227,194,693,981,861,317,308,400,2,391,12,626,265,710,792,620,416,267,611,875,361,494,128,133,157,638,632,2,158,428,284,847,431,94,782,888,44,117,489,222,932,494,948,405,44,185,587,738,164,356,783,276,547,605,609,930,847,39,579,768,59,976,790,612,196,865,149,975,28,653,417,539,131,220,325,252,160,761,226,629,317,185,42,713,142,130,695,944,40,700,122,992,33,30,136,773,124,203,384,910,214,536,767,859,478,96,172,398,146,713,80,235,176,876,983,363,646,166,928,232,699,504,612,918,406,42,931,647,795,139,933,746,51,63,359,303,752,799,836,50,854,161,87,346,507,468,651,32,717,279,139,851,178,934,233,876,797,701,505,878,731,468,884,87,921,782,788,803,994,67,905,309,2,85,200,368,672,995,128,734,157,157,814,327,31,556,394,47,53,755,721,159,843]
This test case probably incorrect!
Expected output:
[26,50,47,11,56,31,18,55,32,9,4,2,23,53,43,0,44,30,6,51,29,51,15,17,22,34,38,33,42,3,25,10,49,51,7,58,16,21,19,31,19,12,41,35,45,52,13,59,47,36,1,28,48,39,24,8,46,20,5,54,27,37,14,57,40,59,8,45,4,51,47,7,58,4,31,23,54,7,9,56,2,46,56,1,17,42,11,30,12,44,14,32,7,10,23,1,29,27,6,10,33,24,19,10,35,30,35,10,17,49,50,36,29,1,48,44,7,11,24,57,42,30,10,55,3,20,38,15,7,46,32,21,40,16,59,30,53,17,18,22,51,11,53,36,57,26,5,
36,56, 55,31,34,57,7,52,37,31,10,0,51,41,2,32,25,0,7,49,47,13,14,24,57,28,4,45,43,39,38,8,2,44,45,29,25,25,12,54,5,44,30,27,23,26,7,33,58,41,25,52,40,58,9,52,40]
I marked the wrong place. server#56 has to start doing task before server#36 because both of them free at that moment and do not have any current task. However, 56 server has weigh (147) lower than server#36(889).
Have anybody also got this problem?
Or can anyone answer. When I get few free servers at the same time. What server I have to pick next? With lower index or weigh?? Read more4914DevNov 07, 2026i aint reading allat Read more351AlbanoNov 07, 2026Whoever writes these awful descriptions please just look for another job.... I'm tired of reading your bad explanations Read moreFeedback19nk713Jan 30, 2024Should be a hard imo because of the edge case and based on other hard PriorityQueue questions Read more16NITESHNov 07, 2026TASK SCHEDULER IN DISGUISE :)
UPVOTE IF U GOT IT Read more19mojajes851Nov 07, 2026attempting n^n^n solution to crash leetcode servers.
 Read more123ScottMay 02, 2025Anyone stuck at this testcase
Servers
[988,390,311,409,205,885,209,92,94,859,533,295,455,320,615,52,291,879,638,757,810,714,946,527,128,487,551,28,204,673,742,817,93,30,758,169,432,53,89,510,377,722,525,556,1000,108,696,583,527,537,781,248,201,201,218,151,586,29,853,340,833,883,293,981,728,928,848,916,873,105,721,146,498,870,186,105,291,341,348,511,466,889,967,796,315,20,296,525,240,104,171,558,672,124,827,868,993,121,72,545,851,932,302,249,520,763,364,97,410,414,31,992,576,403,165,89,7,709,530,701,886,570,640,444,790,371,47,49,328,792,398,159,863,912,594,804,635,462,489,607,230,522,705,636,14,508,213,827,313,952,839,866,319,30,427,475,24,654,212,468,768,718,910,795,322,399,76,788,641,416,926,670,947,242,273,668,194,536,907,747,177,590,841,118,219,438,527,115,561,945,454,589,600,813,666,810,11,447,749,765,40,37,590,431,959,353,64,843,791,258,124,587,330,51,804,379,781,626,808,902,846,905,27,938,169,149,130,896,870,41,682,27,188,201,313,260,119,20,270,572,176,287,530,899,155,70,944,53,519,179,963,693,429,989,956,708,466,764,160,730,641,831,376,555,801,340,219,789,895,242,881,189,360,597,90,271,295,645,247,795,41,290,233,468,201,138,22,666,463,820,285,382,207,688,607,204,131,738,605,266,908,213,621,246,132,168,633,499,913,273,885,317,438,876,960,35,388,878,858,38,217,112,820,767,95,180,851,808,628,84,384,424,468,344,499,428,754,849,1000,210,779,392,232,17,813,693,668,221,713,982,840,516,614,132,119,212,229,854,3,962,742,318,562,778,894,625,779,605,849,935,704,977,262,554,398,926,628,379,250,310,839,450,995,103,801,504,814,935,142,617,820,255,655,363,122,616,789,786,908,836,907,161,283,65,100,985,761,521,954,691,484,899,374,463,441,795,152,952,283,236,179,659,558,646,805,798,97,239,404,160,615,277,418,691,42,920,803,269,24,565,302,588,780,947,103,934,587,510,733,794,553,902,815,425,621,247,593,651,728,135,622,790,814,714,480,380,216,25,24,138,845,799,691,328,342,777,197,33,321,473,673,202,533,396,383,38,634,36,553,754,547,423,174,332,325,251,353,670,987,608,73,129,929,619,405,803,974,174,39,664,47,251,441,750,795,180,588,241,216,579,86,499,687,987,91,520,492,839,150,842,363,542,399,690,604,570,220,15,262,348,412,224,645,193,948,376,357,782,303,971,930,764,83,305,873,506,519,631,446,702,123,703,555,464,264,321,630,560,52,759,50,881,431,321,4,428,518,299,657,387,816,61,828,384,677,415,944,981,517,203,406,444,452,633,838,255,812,351,53,632,561,70,938]
Tasks
[120,632,959,811,918,888,326,541,420,199,57,497,309,495,28,614,308,11,876,132,928,101,880,846,117,718,712,678,921,752,862,141,730,620,419,377,561,645,889,902,89,548,220,986,451,169,191,207,401,1000,11,715,879,197,663,744,319,45,146,14,229,833,377,347,570,391,13,805,615,307,765,644,708,583,724,44,297,385,259,26,248,829,50,929,604,734,518,439,905,540,609,236,468,184,837,951,926,185,401,515,81,682,697,268,201,368,708,120,229,658,539,288,109,139,944,166,852,848,149,373,129,879,984,449,737,519,231,228,264,681,820,32,792,795,418,902,850,150,105,154,90,923,237,433,225,535,168,232,132,973,823,143,392,668,771,646,551,761,473,916,983,469,820,165,145,337,713,631,342,226,389,216,136,757,762,702,651,644,194,666,277,955,76,13,266,578,370,669,119,239,70,246,839,129,58,773,334,83,90,226,411,349,826,119,164,329,652,580,5,284,53,313,954,292,824,383,368,108,811,295,876,511,846,152,106,305,319,365,70,363,5,869,629,452,810,459,80,287,801,90,467,509,939,989,75,798,179,685,90,542,259,394,826,138,275,964,958,820,541,651,934,285,773,290,800,530,9,192,780,191,764,601,610,394,328,759,563,902,175,66,792,290,8,289,53,832,367,949,10,430,490,769,15,217,3,641,607,912,802,522,728,994,10,431,414,183,791,714,648,633,250,467,421,678,346,436,873,358,966,383,273,342,744,270,349,885,551,566,997,17,462,623,284,200,566,721,219,142,434,485,212,509,960,340,349,820,819,527,610,784,288,678,419,75,12,520]
The answer on leetcode may not be correct. The answer provided is
[358,574,116,196,144,537,343,85,237,286,156,438,468,467,222,231,27,57,33,153,110,477,315,487,201,319,485,508,57,200,229,280,434,126,510,127,570,213,15,568,37,247,222,598,581,206,403,245,601,98,500,166,552,329,520,38,115,274,524,7,32,500,8,324,107,426,404,156,383,444,89,69,75,7,45,321,187,183,236,404,354,97,394,560,93,210,24,501,226,296,304,353,459,285,469,388,71,225,528,55,416,244,274,131,258,404,429,401,114,305,35,224,90,492,507,240,180,249,420,321,358,325,477,515,74,232,271,543,176,37,476,52,394,53,233,284,481,589,28,295,4,201,292,6,339,158,355,146,301,466,518,153,320,54,184,266,536,347,541,356,140,342,282,52,419,427,88,517,173,269,303,278,280,455,51,103,378,495,511,391,595,416,209,235,372,538,564,299,437,238,275,174,309,431,402,418,235,290,241,281,16,76,62,11,524,276,86,577,286,102,440,548,553,286,206,379,2,148,234,84,311,90,361,152,13,478,565,401,573,164,4,494,128,473,212,4,493,403,59,265,77,474,333,28,78,539,597,205,496,358,329,546,492,402,245,272,393,530,209,106,275,125,222,440,412,262,545,420,40,215,377,465,291,484,330,545,583,285,579,316,301,240,225,290,1,341,483,589,241,32,225,130,374,295,153,165,532,153,241,573,113,428,504,590,3,258,108,437,280,419,374,540,504,109,355,585,493,169,432,78,491,468,431,11,27,148,331,353,354,52,13,265,343,453,154,335,575,236,114,496,1,252,203,572,36,316,52,185,312,414,512,123,591,558,197,543]
the correct answer should be [358,574,116,196,144,537,343,85,237,286,156,438,468,467,222,231,27,57,33,153,110,477,315,487,201,319,485,508,57,200,229,280,434,126,510,127,570,213,15,568,37,247,222,598,581,206,403,245,601,98,500,166,552,329,520,38,115,274,524,7,32,500,8,324,107,426,404,156,383,444,89,69,75,7,45,321,187,183,236,404,354,97,394,560,93,210,24,501,226,296,304,353,459,285,469,388,71,225,528,55,416,244,274,131,258,404,429,401,114,305,35,224,90,492,507,240,180,249,420,321,358,325,477,515,74,232,271,543,176,37,476,52,394,53,233,284,481,589,28,295,4,201,292,6,339,158,355,146,301,466,518,153,320,54,184,266,536,347,541,356,140,342,282,52,419,427,88,517,173,269,303,278,280,455,51,103,378,495,511,391,595,416,209,235,372,538,564,299,437,238,275,174,309,431,402,418,235,290,241,281,16,76,62,11,524,276,86,577,286,102,440,548,553,286,206,379,2,148,234,84,311,90,361,152,13,478,565,401,573,164,4,494,128,473,212,4,493,403,59,265,77,474,333,28,78,539,597,205,496,358,329,546,492,402,245,272,393,530,209,106,275,125,222,440,412,262,545,420,40,215,377,465,291,484,330,545,583,285,579,316,301,290,240,225,1,341,483,589,241,32,240,130,374,295,153,165,532,153,241,573,113,428,504,590,3,258,108,437,374,280,419,540,504,109,355,585,493,169,432,78,491,468,431,11,27,148,331,353,354,52,265,13,343,453,154,335,575,236,114,1,496,252,203,572,36,316,52,185,312,414,512,123,591,558,197,543]
The incorrect answer swap the order of server 1 and 496. Server 1 task is finished on second 337 and server 496 task is finished on second 338. Clearly server 1 should handle next task, but answer let 496 be. Read more71123413Copyright © 2026 LeetCode. All rights reserved.1.3K123292 Online
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

LeetSort byAllMy SolutionPython3C++JavaCPythonJavaScriptGoSwiftRustKotlinTypeScriptC#RubyPHPHeap (Priority Queue)ArraySimulationQueueGreedySortingOrdered SetMathBit ManipulationTreeOrdered MapSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Nov 03, 2026Process Tasks Using ServersEditorial1717.5K9Aleksandr・ Open・Nov 07, 2026✅ Two Heaps of Servers | Beats 100%ArrayHeap (Priority Queue)SimulationPython6+6813.7K4Muthu Vrn・ Open・Nov 07, 2026God is Great 517Python3352K1Md Aarzoo Islam・ Open・Nov 07, 2026213ms | Beats 24.54% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayHeap (Priority Queue)C++Java4+244.4K1Aryan Kumar Shaw Halwai・ Open・Nov 07, 2026✅ Beats 78% 🚀 | Two Min-Heaps, Idle vs Busy Servers, Jump the Clock 🔥 | Java, C++, Python, JSArrayGreedyHeap (Priority Queue)Simulation5+111.5K1Vishal Tiwari・ Open・Nov 07, 2026[C++ / Python] Two Heaps Approach (Available & Busy) | Detailed Explanation 🚀ArrayHeap (Priority Queue)PythonC++1+54980Manjeet Dhayal・ Open・Nov 07, 2026Two PriorityQueue's for Busy server and Empty server pool | Simulate time | Intutive ArrayHeap (Priority Queue)Java57340Sanskar Singh・ Open・Nov 07, 2026C++ | Multiset | Easy to understandC++47530MBBN・ Open・Nov 07, 2026Java - Clean Solution | 2 Priority Queues (Min Heaps) + GreedyJava33261Prabz・ Open・Nov 07, 20263 Queues solutionArrayHeap (Priority Queue)C++1350Shivam Chaurasiya・ Open・Nov 07, 2026Smart Server Scheduler | Dual Min-Heaps | Greedy Task Assignment | Priority-Based SchedulingArrayHeap (Priority Queue)PythonC++1+2790SouLAditya・ Open・Nov 07, 2026O((M + N) log M) Time O(M) Space | Two Min-Heaps & Virtual Clock SimulationC++2400CodingVoid・ Open・Nov 07, 2026666msJavaScript2120chris_grif・ Open・Nov 07, 2026⏱️ Release-Time Race: Free and Busy HeapsArrayHeap (Priority Queue)C++2820Long Nguyen・ Open・Nov 07, 2026100% - [Medium Problem with Easy Approach ] with 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+33060All SolutionsGod is Great 517Muthu Vrn2KNov 07, 2026Python3Intuition


Approach

Complexity

Time complexity:



Space complexity:


Code
Python3class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        n, ans, busy_servers = len(servers), [], []
        free_servers = list(zip(servers, range(n)))
        heapify(free_servers)

        for time, task in enumerate(tasks):
            
            while busy_servers:
                sec, wgt, idx = busy_servers[0]
                if sec != time: break

                heappush(free_servers, (wgt, idx))
                heappop(busy_servers)

            if free_servers == []:
                sec, wgt, idx = heappop(busy_servers)
                heappush(busy_servers, (sec + task, wgt, idx))

            else:
                wgt, idx = heappop(free_servers)
                heappush(busy_servers, (time + task, wgt, idx))
                
            ans.append(idx)

        return ans Previous✅ Two Heaps of Servers | Beats 100%Next213ms | Beats 24.54% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Comments (1)Sort by:BestCommentMitproNov 07, 2026Please stop creating your Trash, Garbage, Horrible, Atrocious Abysmal, Disgusting solution Read more121351Python3Auto15161718192021222324252627                heappop(busy_servers)            if free_servers == []:                sec, wgt, idx = heappop(busy_servers)                heappush(busy_servers, (sec + task, wgt, idx))            else:                wgt, idx = heappop(free_servers)                heappush(busy_servers, (time + task, wgt, idx))                            ans.append(idx)        return ansIn the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 27, Col 19AcceptedRuntime: 0 msCase 1Case 2Inputservers =[3,3,2]tasks =[1,2,3,2,1,2]Output[2,2,0,2,1,2]Expected[2,2,0,2,1,2]Contribute a testcaseInput91234›[3,3,2][1,2,3,2,1,2][5,1,4,3,2][2,1,2,4,5,2,1]Output912›[2,2,0,2,1,2][1,4,1,4,1,3,2]Expected912›[2,2,0,2,1,2][1,4,1,4,1,3,2] All SubmissionsAccepted37 / 37 testcases passedMUTHU KUMAR Msubmitted at Nov 09, 2026 18:06AnalysisSolutionCodePython31class Solution:
2    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
3
4        n, ans, busy_servers = len(servers), [], []
5        free_servers = list(zip(servers, range(n)))
6        heapify(free_servers)
7
8        for time, task in enumerate(tasks):
9            
10            while busy_servers:
11                sec, wgt, idx = busy_servers[0]
12                if sec != time: break
13
14                heappush(free_servers, (wgt, idx))
15                heappop(busy_servers)
16
17            if free_servers == []:
18                sec, wgt, idx = heappop(busy_servers)
19                heappush(busy_servers, (sec + task, wgt, idx))
20
21            else:
22                wgt, idx = heappop(free_servers)
23                heappush(busy_servers, (time + task, wgt, idx))
24                
25            ans.append(idx)
26
27        return ansView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
