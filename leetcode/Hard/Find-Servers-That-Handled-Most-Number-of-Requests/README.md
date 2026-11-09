# 1606. Find Servers That Handled Most Number of Requests

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function j(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit000:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result1606. Find Servers That Handled Most Number of RequestsHardTopicsCompaniesHintYou have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:


	The ith (0-indexed) request arrives.
	If all servers are busy, the request is dropped (not handled at all).
	If the (i % k)th server is available, assign the request to that server.
	Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.


You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 
Example 1:

Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation: 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.


Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation: 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.


Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all considered the busiest.


 
Constraints:


	1 <= k <= 105
	1 <= arrival.length, load.length <= 105
	arrival.length == load.length
	1 <= arrival[i], load[i] <= 109
	arrival is strictly increasing.

 Seen this question in a real interview before?1/6YesNoAccepted46,428/87.3KAcceptance Rate53.2%TopicsPrincipalArrayHeap (Priority Queue)SimulationOrdered SetBiweekly Contest 36CompaniesHint 1To speed up the next available server search, keep track of the available servers in a sorted structure such as an ordered set.Hint 2To determine if a server is available, keep track of the end times for each task in a heap and add the server to the available set once the soonest task ending time is less than or equal to the next task to add.Similar QuestionsMeeting Rooms IIIHardDiscussion (39)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestKhumoyun14 hours agoSometimes the only thing holding you back is the thought that you can't do it. Crack it! Read more191potpieOct 19, 2021Input: k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
Output: [1]
Why not output is [0, 1]?
Servers that will handle each request are as follows:
0 1 2 1 0 1 0 Read more173Cash21Jul 19, 2024Typical booking keeping problem. Know your heaps and sets and its a piece of cake. Read more121Takijic636 hours agoIt's just a straightforward application of DSA.
Unlike those other hard problems that is hard to figure out.
 Read more81nusidom6 hours agoHere are some testcases for you guys ------------------->
1
[1]
[1]
1
[1,2,3,4,5,10]
[3,1,1,1,5,1]
6
[2,5,9]
[100,100,100]
3
[1,2,3,4,5,6,7,8]
[1,10,10,1,1,1,1,1]
4
[1,2,3,4,5,6,7,8,9,10,11,12]
[7,6,5,4,100,100,100,4,1,1,1,1]
5
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
[20,1,7,2,10,1,15,3,1,8,2,2,12,1,6,30,1,4,9,2,1,18,3,3,1,7,2,10,1,5]
7
[1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,25,26,27,28,29,100,101,102,103,104,105,106,107,108,109,200,201,202,203,204,205,206,207,208,209,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009]
[100,2,50,4,20,6,1,30,1,8,1,1,1,40,2,2,60,3,3,3,7,6,5,4,3,2,1,100,100,100,200,1,2,3,4,5,6,7,8,9,1,1000,1,1000,1,1000,1,2,2,2]
10
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,999999981,999999982,999999983,999999984,999999985,999999986,999999987,999999988,999999989,999999990,999999991,999999992,999999993,999999994,999999995,999999996,999999997,999999998,999999999,1000000000]
[1000000000,1,2,3,4,5,6,7,8,9,1,30,1,30,1,30,1,30,1,30,10,9,8,7,6,5,4,3,2,1,50,1,1,50,1,1,50,1,1,50,2,4,6,8,10,12,14,16,18,20,1,1,1,1,1,1,1,1,1,1,1000000000,1,1000000000,1,1000000000,1,1000000000,1,1000000000,1,1,1,1,1,1,1,1,1,1,1000000000]
Randomly generated test cases using the web extension LeetTest!
Also provides up to date company tags and elo rating for problems!
Downloadable on the Chrome webstore or Firefox addons and works for most leetcode problems Read more6Ezio AuditoreJun 16, 2023A bit simpler version of  2402. Meeting Rooms III

Take care of Integer Overflow!
Think about how you can optimize the process of finding the next available server! ;)
 Read moreTip6CyberPunkOct 03, 2020Recently, I feel it's easy to get TLE using C++ for any problem with the solution NlogN( n is around 10^5).
You have to pay attention to the implementatoin.
For example, this question:
using
priority_queue<pair<int, int64_t>, vector<pair<int, int64_t>>, Comparator> Q is certainly faster than
priority_queue<vector<int64_t>,   vector<int64_t>, Comparator> Q;
But it  shouldn't be the key to solve this question.
Maybe leetcode should change data range to 2 * 10^4 for this kind of problem?
I don't have the similar problem on other platforms. Some other platforms offer 2 seconds for 10^5 for C++.
I am talking about several questions in last 6 months.
Anyone feels the same?
Sure, if the solution is expect to be the segment tree, that would be another story. Read more41divyamagarwal1947Oct 05, 2025asked in sqaurepoint OA 2 days ago Read more7Aman Agrahari2 hours agothe calm side of HARD questions 😄 Read more3Pravinkumar SNov 09, 2022Why  lower_bound(available.begin(), available.end()) gives TLE but  available.lower_bound(i%k) got Accepted ?
lower_bound(available.begin(), available.end())  => TLE
class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int N = arrival.size();

        priority_queue<pair<int, int> , vector<pair<int, int>>, greater<>> pq;
        set<int> available;
        
        for(int i=0; i<k; i++){
            available.insert(i);
        }

        vector<int> count(k);
        
        for(int i=0; i<N; i++){
            int start = arrival[i], end = load[i];
            
            while(!pq.empty() && pq.top().first <= start){
                available.insert(pq.top().second);
                pq.pop();
            }

            if(available.size()==0)
                continue;

            auto it = lower_bound(available.begin(), available.end());
            int ind = 0;
            if(it==available.end())
                ind = *available.begin();
            else 
                ind = *it;

            available.erase(ind);
            pq.emplace(start+end, ind);
            count[ind]++;
        }

        vector<int> ans;
        int mx = *max_element(count.begin(), count.end());
        for(int i=0; i<k; i++){
            if(count[i]==mx){
                ans.push_back(i);
            }
        }
        return ans;
    }
};
available.lower_bound(i%k) => Accepted
class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int N = arrival.size();

        priority_queue<pair<int, int> , vector<pair<int, int>>, greater<>> pq;
        set<int> available;
        
        for(int i=0; i<k; i++){
            available.insert(i);
        }

        vector<int> count(k);
        
        for(int i=0; i<N; i++){
            int start = arrival[i], end = load[i];
            
            while(!pq.empty() && pq.top().first <= start){
                available.insert(pq.top().second);
                pq.pop();
            }

            if(available.size()==0)
                continue;

            auto it = available.lower_bound(i%k);
            int ind = 0;
            if(it==available.end())
                ind = *available.begin();
            else 
                ind = *it;

            available.erase(ind);
            pq.emplace(start+end, ind);
            count[ind]++;
        }

        vector<int> ans;
        int mx = *max_element(count.begin(), count.end());
        for(int i=0; i<k; i++){
            if(count[i]==mx){
                ans.push_back(i);
            }
        }
        return ans;
    }
};
Can any one explain me why this happens ? Read moreAsk Question331234Copyright © 2026 LeetCode. All rights reserved.75239
@property --beam-angle-_r_73_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_73_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_73_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_73_"][data-active] {
  animation:
    beam-spin-_r_73_ 1.96s linear infinite,
    beam-fade-in-_r_73_ 0.6s ease forwards;
}

[data-beam="_r_73_"][data-fading] {
  animation:
    beam-spin-_r_73_ 1.96s linear infinite,
    beam-fade-out-_r_73_ 0.5s ease forwards;
}

[data-beam="_r_73_"][data-active]::after,
[data-beam="_r_73_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_73_),
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
      from var(--beam-angle-_r_73_),
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
      from var(--beam-angle-_r_73_),
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
  opacity: calc(var(--beam-opacity-_r_73_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_73_"][data-active]::before,
[data-beam="_r_73_"][data-fading]::before {
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
    from var(--beam-angle-_r_73_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_73_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_73_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_73_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_73_),
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

[data-beam="_r_73_"][data-active] [data-beam-bloom],
[data-beam="_r_73_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_73_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_73_ {
  to { --beam-angle-_r_73_: 360deg; }
}

@keyframes beam-fade-in-_r_73_ {
  to { --beam-opacity-_r_73_: 1; }
}

@keyframes beam-fade-out-_r_73_ {
  from { --beam-opacity-_r_73_: 1; }
  to { --beam-opacity-_r_73_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonCJavaScriptGoC#TypeScriptRustKotlinScalaPHPRubySwiftHeap (Priority Queue)Ordered SetSimulationArrayGreedyBinary SearchTreeBinary TreeSegment TreeHash TableSweep LineOrdered MapBinary Search TreeBinary Indexed TreeQueueSortingMathProbability and StatisticsSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Oct 21, 2022Find Servers That Handled Most Number of RequestsEditorial2619.4K10Aleksandr・ Open・10 hours ago✅ Two Heaps Around a Circle | Next-Turn Keys | Beats 100%Heap (Priority Queue)SimulationPythonC++5+354.8K4Muthu Vrn・ Open・5 hours agoGod is Great 519Python3331.1K0Discover moreProgramming practice questionsDeveloper toolsTake Tech CoursesGet Career AdviceLearning resourcesprogrammingOnline coding contestsTry Cloud ToolsEnroll in ClassesFind Study Aidsthis_is_naruto・ Open・6 hours ago🧩 Heap Frees, Set Chooses Next SlotArrayBinary SearchHeap (Priority Queue)Simulation2+175300Md Aarzoo Islam・ Open・6 hours ago151ms | Beats 49.06% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayHeap (Priority Queue)SimulationOrdered Set6+156041this_is_derek・ Open・7 hours ago🌀 Free-First Ring: Heap Wakes, Set WrapsArrayBinary SearchHeap (Priority Queue)Simulation2+162270Manjeet Dhayal・ Open・2 hours agoSimulate | Observation - Optimal data structure to find next available server & when server is free?ArrayTreeHeap (Priority Queue)Simulation2+6680Aryan Kumar Shaw Halwai・ Open・5 hours ago✅ Beats 95% 🚀 | Two Heaps +  Virtual Index Trick for Circular Free Server🔥| Java, C++, Python, JSArrayGreedyHeap (Priority Queue)Simulation6+52570shivaa_11・ Open・6 hours agoBEATS 100% ✅ | BEGINNER FRIENDLY CODE | Two Heaps Around a CircleHeap (Priority Queue)Ordered SetC++Java34331Kostiantyn Lazukin・ Open・7 hours ago8 msC++3981Praveen Kumar・ Open・2 hours agoSIMPLE INTUITION | VISUAL EXAMPLE | {JAVA,C++}Heap (Priority Queue)SimulationOrdered SetC++1+2330Ujjawal・ Open・3 hours agoSolution that Beats 100%ArrayGreedyBinary Indexed TreeOrdered Map6+2340Prabhas Sharma・ Open・3 hours ago1606. Find Servers That Handled Most Number of RequestsPython31191MBBN・ Open・3 hours agoJava - Clean Solution | TreeSet + Min Heap (Priority Queue)Java1491kunal_vish・ Open・7 hours ago✅ Two Heaps Around a Circle | Next-Turn Keys | Beats 100%C++1521All SolutionsGod is Great 519Muthu Vrn1.1K5 hours agoPython3Intuition


Approach

Complexity

Time complexity:



Space complexity:


Code
Python3class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [] # min-heap
        free = list(range(k)) # min-heap 
        freq = [0]*k
        
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                heappush(free, i + (ii - i) % k) # circularly relocate it
            if free: 
                ii = heappop(free) % k 
                freq[ii] += 1
                heappush(busy, (ta+tl, ii))
        
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx] Previous✅ Two Heaps Around a Circle | Next-Turn Keys | Beats 100%Next🧩 Heap Frees, Set Chooses Next SlotComments (0)Sort by:BestCommentNo comments yet.330Python3Auto567891011121314151617        freq = [0]*k                for i, (ta, tl) in enumerate(zip(arrival, load)):             while busy and busy[0][0] <= ta:                 _, ii = heappop(busy)                heappush(free, i + (ii - i) % k) # circularly relocate it            if free:                 ii = heappop(free) % k                 freq[ii] += 1                heappush(busy, (ta+tl, ii))                mx = max(freq)        return [i for i, x in enumerate(freq) if x == mx]In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 17, Col 58AcceptedRuntime: 0 msCase 1Case 2Case 3Inputk =3arrival =[1,2,3,4,5]load =[5,2,3,3,3]Output[1]Expected[1]Contribute a testcaseInput9123456789›3[1,2,3,4,5][5,2,3,3,3]3[1,2,3,4][1,2,1,2]3[1,2,3][10,12,11]Output9123›[1][0][0,1,2]Expected9123›[1][0][0,1,2] All SubmissionsAccepted108 / 108 testcases passedMUTHU KUMAR Msubmitted at Nov 09, 2026 12:54AnalysisSolutionCodePython31class Solution:
2    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
3        busy = [] # min-heap
4        free = list(range(k)) # min-heap 
5        freq = [0]*k
6        
7        for i, (ta, tl) in enumerate(zip(arrival, load)): 
8            while busy and busy[0][0] <= ta: 
9                _, ii = heappop(busy)
10                heappush(free, i + (ii - i) % k) # circularly relocate it
11            if free: 
12                ii = heappop(free) % k 
13                freq[ii] += 1
14                heappush(busy, (ta+tl, ii))
15        
16        mx = max(freq)
17        return [i for i, x in enumerate(freq) if x == mx]View more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
