# 3841. Palindromic Path Queries in a Tree

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Palindromic Path Queries in a Tree](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()(function l(a,b,c,d,e){let f=a=>!a.hasAttribute("data-qd-shell-splitter"),g=(a,h)=>{if(a.classList.contains(c))return d;let i=Array.from(a.children).filter(f).map(a=>g(a,h)),j=Array.from(a.children).find(a=>!f(a));return j&&j.classList.contains(b)===h?i.reduce((a,b)=>a+b,0)+(i.length-1)*e:i.reduce((a,b)=>Math.max(a,b),0)};document.addEventListener("pointerdown",c=>{let d=c.target,e=d.closest?d.closest("[data-qd-shell-splitter]"):null;if(!e||!e.parentElement||!c.isPrimary||0!==c.button)return;let h=e.classList.contains(b),i=Array.from(e.parentElement.children).filter(f),j=i.map(a=>a.getBoundingClientRect()[h?"width":"height"]),k=j.reduce((a,b)=>a+b,0);if(k<=0)return;let l=i.indexOf(e.previousElementSibling),m=g(i[l],h)-j[l],n=j[l+1]-g(i[l+1],h),o=h?c.clientX:c.clientY,p=e.dataset.qdShellSplitter;c.preventDefault(),e.setPointerCapture(c.pointerId);let q=b=>{if(!e.isConnected)return;let c=Math.min(Math.max((h?b.clientX:b.clientY)-o,m),n);i.forEach((b,d)=>{document.documentElement.style.setProperty(`${a}${p?`${p}-`:""}${d}`,String((j[d]+(d===l?c:d===l+1?-c:0))/k))})};e.addEventListener("pointermove",q),e.addEventListener("lostpointercapture",()=>e.removeEventListener("pointermove",q),{once:!0})})})("--qd-shell-pane-","flexlayout__splitter_vert","flexlayout__tabset",36,8)Daily QuestionDaily QuestionDebugging...Submit200:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsFavoritesNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3841. Palindromic Path Queries in a TreeHardTopicsCompaniesHintYou are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:


	"update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
	"query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.


Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

 
Example 1:


Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:


	"query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
	"update 1 b": Update node 1 to 'b', now s = "abc".
	"query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.


Thus, answer = [true, false].


Example 2:


Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:


	"query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
	"update 0 b": Update node 0 to 'b', now s = "bbca".
	"query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
	"update 3 a": Update node 3 to 'a', s = "bbca".
	"query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.


Thus, answer = [false, false, true].


 
Constraints:


	1 <= n == s.length <= 5 * 104
	edges.length == n - 1
	edges[i] = [ui, vi]
	0 <= ui, vi <= n - 1
	s consists of lowercase English letters.
	The input is generated such that edges represents a valid tree.
	1 <= queries.length <= 5 * 104​​​​​​​
	
		queries[i] = "update ui c" or
		queries[i] = "query ui vi"
		0 <= ui, vi <= n - 1
		c is a lowercase English letter.
	
	

 Seen this question in a real interview before?1/6YesNoAccepted27,580/41.5KAcceptance Rate66.5%TopicsPrincipalArrayStringDivide and ConquerBit ManipulationTreeDepth-First SearchBinary Indexed TreeSegment TreeBiweekly Contest 176CompaniesHint 1Use heavy light decomposition to break each path query into O(log n) segments.Hint 2Represent characters as a 26-bit mask and maintain segment data with XOR. A path can form a palindrome if the resulting mask has at most one bit set.Discussion (98)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestAniket AinapurFeb 14, 2026Peacefully writing brute force knowing it wont get accepted 🥸 Read more1315Tiantian16 hours agoclass Solution:
    def palindromePath(self, n, edges, s, queries):
        return "Stay happy every day, and eat well." Read more61Pratyush DebFeb 14, 2026I got a 3/4 today, one day I'll get 4/4 even if there are beast questions like this. Read more519jatin kumarFeb 14, 2026Knowing Everything about the problem
Build a se*y approach
Implement
-> Binary Lifting for LCA
-> Segment Tree for updating and getting frequency array
after 40 minutes of code
hit run -> accepted (finally the 200 lines of code working se*y)
hit submit -> got TLE 💔, 993/1040 passed Read moreRead more473Rahul ShrivastavaFeb 24, 2026Topics you should know before solving this question :

LCA with Binary Lifting
Fenwick / Segment Tree
Euler Tour to flatten the Tree
Basic XOR properties and Palindrome
 Read moreTip336Aaradhy SharmaFeb 14, 2026Another Valentines ending in a heartbreak cuz of this. Read more27Ravinder SinghFeb 14, 2026I must say it is an amazing question! (Couldnt solve it🥲) Read more15Nilesh Tiwari13 hours agoDil ka dariya beh hi gya Read moreRead more141Segment TreeFeb 14, 2026After writing lca + prefix sum code, I realized the problem has an update as well. And I watched the clock tick tick silently... Read more183Ched311 hours agoHere are some testcases for you guys ------------------->
5
[[0,1],[2,3],[0,2],[3,4]]
"omoon"
["update 2 a"]
6
[[3,4],[0,1],[0,5],[1,2],[0,3]]
"fijhjf"
["query 0 4","query 2 2","query 5 2"]
10
[[1,8],[0,3],[3,7],[0,2],[2,4],[6,9],[3,5],[0,1],[0,6]]
"tqprqtrtrq"
["update 7 a","query 0 0","update 1 b","query 4 0","query 9 0"]
12
[[0,10],[3,5],[6,8],[5,11],[2,3],[3,4],[4,6],[1,7],[0,9],[1,2],[0,1]]
"okmlnknnnmon"
["update 7 e","query 0 0","query 6 8","query 9 5","update 10 a"]
15
[[10,11],[0,2],[0,1],[2,5],[3,4],[3,10],[2,3],[5,6],[9,13],[13,14],[4,8],[2,7],[7,9],[9,12]]
"aebddadadbeebed"
["query 10 1","query 12 13","query 8 12","query 11 14","query 13 5","update 11 e","query 14 9"]
20
[[10,15],[5,18],[13,16],[2,10],[0,4],[4,8],[4,14],[3,6],[0,11],[2,3],[0,17],[11,12],[0,2],[12,19],[4,5],[10,13],[5,9],[4,7],[0,1]]
"jijiijfjgiiiifgigihg"
["query 1 12","update 19 d"]
40
[[0,1],[19,29],[8,16],[2,5],[13,38],[2,6],[14,18],[2,4],[10,25],[8,19],[7,28],[10,12],[1,3],[12,20],[10,11],[7,15],[22,31],[12,24],[11,32],[0,8],[27,34],[4,23],[8,22],[0,2],[27,36],[10,26],[17,35],[4,39],[4,9],[6,13],[1,7],[1,10],[17,21],[27,30],[4,17],[9,37],[15,33],[5,14],[25,27]]
"knklnmmonmmnnllkokmnokmkonlolonlonmllmko"
["update 3 e","update 6 e","query 4 31","query 39 27","update 17 d","query 23 32","query 7 22","query 13 21","query 37 21","query 33 21","update 37 d","query 33 21","query 11 9","update 37 e"]
507
[[167,249],[346,373],[94,223],[302,311],[77,225],[219,270],[135,162],[35,361],[22,139],[1,504],[358,461],[23,83],[7,8],[172,218],[87,193],[100,474],[35,76],[26,165],[35,94],[17,30],[106,228],[5,65],[3,81],[194,494],[224,441],[219,348],[50,110],[79,204],[154,450],[98,123],[30,413],[20,48],[211,367],[154,313],[67,69],[110,233],[91,103],[201,205],[12,131],[257,296],[85,330],[69,395],[238,281],[136,219],[11,63],[150,208],[12,55],[300,346],[131,184],[3,15],[45,79],[79,159],[127,287],[7,280],[27,156],[193,246],[130,195],[70,414],[40,255],[1,399],[3,86],[245,407],[233,370],[176,284],[85,101],[24,42],[19,52],[15,176],[278,500],[148,417],[99,222],[193,293],[19,24],[232,485],[94,138],[187,445],[206,460],[16,20],[40,145],[48,107],[236,357],[96,232],[55,377],[9,144],[75,121],[143,289],[74,291],[385,437],[330,379],[299,418],[60,312],[12,29],[15,21],[238,408],[81,436],[236,324],[109,297],[90,290],[60,337],[90,116],[419,429],[42,112],[267,271],[177,405],[49,120],[101,178],[318,368],[34,453],[176,189],[95,234],[80,168],[65,160],[293,321],[236,420],[25,481],[22,32],[38,198],[214,362],[20,117],[2,236],[52,130],[8,477],[219,447],[74,237],[45,134],[31,39],[87,155],[131,152],[4,6],[9,28],[153,186],[91,250],[29,31],[66,196],[343,451],[126,146],[122,135],[134,207],[19,128],[314,482],[9,44],[244,359],[301,424],[27,49],[32,169],[67,394],[206,421],[118,264],[242,459],[19,97],[168,216],[107,142],[37,201],[223,473],[63,149],[288,302],[186,304],[104,147],[76,369],[38,360],[338,440],[259,401],[125,191],[72,75],[43,153],[177,307],[12,286],[431,462],[62,172],[295,392],[288,351],[48,400],[218,239],[112,458],[51,496],[57,137],[3,26],[22,46],[178,404],[254,298],[169,364],[291,391],[130,259],[145,213],[0,23],[20,133],[13,25],[84,140],[165,173],[126,166],[252,388],[165,167],[16,161],[16,17],[226,254],[2,3],[245,422],[36,38],[158,188],[133,288],[130,352],[180,431],[431,492],[63,96],[133,278],[128,334],[34,67],[74,119],[150,478],[53,181],[53,350],[77,179],[8,33],[0,7],[288,339],[22,476],[17,74],[172,235],[190,434],[305,502],[92,175],[90,332],[49,333],[154,505],[186,310],[99,387],[66,497],[44,88],[75,126],[11,62],[138,261],[194,306],[172,344],[310,371],[104,248],[239,326],[111,322],[32,452],[279,327],[170,240],[84,432],[50,491],[165,220],[135,136],[247,268],[167,402],[376,403],[50,115],[8,51],[284,383],[121,244],[3,85],[187,435],[31,469],[39,353],[332,345],[316,472],[271,465],[298,380],[408,468],[207,292],[101,319],[42,241],[344,419],[9,36],[273,363],[66,71],[38,93],[143,341],[132,242],[44,56],[6,9],[7,54],[61,267],[263,342],[9,19],[135,190],[84,118],[63,308],[301,328],[283,295],[298,331],[244,323],[56,356],[152,406],[365,416],[144,238],[43,60],[75,199],[27,58],[56,122],[22,282],[25,53],[44,82],[277,349],[86,104],[102,185],[71,113],[6,41],[232,443],[89,347],[234,470],[337,397],[93,164],[113,124],[76,105],[74,141],[49,73],[78,212],[66,483],[0,1],[32,72],[259,467],[176,251],[97,427],[24,89],[174,411],[127,393],[17,84],[248,372],[219,245],[148,354],[37,148],[53,454],[66,197],[170,182],[48,231],[113,180],[399,466],[101,127],[228,423],[276,336],[181,202],[205,382],[172,177],[58,438],[50,456],[82,243],[71,95],[5,13],[107,209],[92,381],[136,154],[127,317],[82,132],[20,157],[163,486],[71,163],[242,275],[94,100],[307,444],[10,50],[27,70],[372,457],[52,320],[422,425],[57,229],[32,143],[18,87],[227,495],[263,266],[94,366],[75,215],[89,200],[71,125],[177,412],[341,455],[259,314],[197,260],[7,12],[0,449],[49,109],[118,489],[188,279],[61,183],[438,503],[67,171],[17,384],[78,253],[212,273],[22,34],[2,5],[11,37],[271,272],[176,252],[69,224],[425,475],[117,170],[63,214],[200,335],[275,276],[157,247],[195,386],[188,428],[5,91],[28,78],[74,258],[27,493],[22,501],[82,463],[219,410],[111,389],[18,442],[3,11],[24,194],[60,227],[290,303],[302,376],[176,365],[101,150],[91,187],[43,111],[13,256],[267,375],[74,479],[57,299],[0,4],[91,206],[263,301],[88,274],[135,211],[275,338],[312,480],[207,300],[64,265],[44,90],[8,57],[0,45],[74,498],[38,98],[30,158],[354,374],[47,448],[202,257],[8,16],[38,294],[5,343],[46,68],[324,446],[272,385],[186,488],[157,415],[45,203],[133,269],[41,129],[290,340],[97,108],[97,99],[57,92],[143,315],[113,114],[213,426],[27,40],[24,439],[184,378],[43,358],[6,80],[75,77],[134,230],[1,43],[278,490],[140,226],[84,484],[14,22],[127,430],[439,487],[29,59],[42,66],[251,316],[173,174],[142,329],[271,506],[142,151],[417,471],[64,283],[4,14],[1,2],[357,464],[128,285],[4,10],[241,277],[64,210],[132,390],[100,263],[246,325],[368,396],[142,221],[272,433],[10,217],[130,192],[127,409],[218,309],[269,499],[300,305],[24,61],[32,355],[33,64],[41,262],[88,102],[21,27],[7,35],[8,18],[244,318],[66,106],[7,47],[110,398]]
"zxywvzvvvvyyxvywzyvuwwwuwyvyvwzzxzwyvyxxywvwzzyuyxxxyyyyxzwuzvvywvxyxzxyzvxzwuyyyzuuuvxxwvzxxyxzvzxzzuwvuyvyvvvwuwxzzzuvuzyyywxvuyxxzvzuywwwzwxyxzzuzwxvwuxwwyyyxywxwwvyzxxwxzxyyzxyuxyuwwzuvyvzyyyxwxvyzwvyzyzuzuuwvzzuxzvuwwvywuxuuzxvwuzuzyzzxwyvxuwyzyxwzyvxzuuyxwzwuzzwyuyyuyxyuzyzuvxzuvuuvvzyvwyzzwwzxyvvwyyvwxuvzvzxxwvuwuxxvxyvuxywxwwzvzxzyzwzzuyzwuyywvvvuuuvuwyvxzuuuvvzvwzvyzzwxzuwxyxuyzwxyuxxyxxzuvxvwxxwwuzwvuyvxvywvvyvyxzvvyuxzwuvyuvvxyvyzwywvxxxuyzwuzwzzyzyyvzwyuuxwvzuuzwyxyyzywwyuxxxuxzwzwuzxxwyxzw"
["update 445 d","query 170 348","query 198 214","update 379 d","update 77 e","query 133 64","query 479 89","query 291 436","query 321 276","update 116 d","query 269 494","query 141 504","query 24 35","query 33 96","query 91 313","query 172 268","query 197 3","query 454 500","query 138 290","query 153 231","query 293 47","query 345 133","update 446 b","query 401 27","query 73 156","update 312 a","update 212 b","query 92 257","query 319 79","update 117 b","update 347 e","query 325 191","query 439 406","query 391 292","query 264 129","query 101 105","query 332 64","query 66 305","update 489 d","query 480 340","query 313 449","query 164 478","update 356 c","query 119 395","query 454 300","update 488 c","query 315 480","update 374 a","query 149 400","query 362 225","query 169 53","update 393 c","query 270 10","update 285 a","query 60 239","query 68 222","query 320 223","update 73 a","query 203 86","update 305 d","update 86 c","update 479 c","update 227 a","query 277 489","query 360 458","query 78 394","update 172 a","query 69 506","query 468 375","update 369 b","query 394 199","query 97 59","query 55 407","query 125 271","query 330 109","update 261 c","query 319 225","update 481 c","query 43 498","update 28 c","query 412 190","query 15 249","query 440 182","query 198 426","update 152 a","query 203 51","update 367 c","query 490 479","query 307 460","query 109 376","query 223 48","update 446 b","query 274 301","update 363 e","query 450 87","query 460 477","query 236 506","query 358 264","update 212 a","query 227 500","update 439 e","query 302 104","update 71 d","query 73 257","update 184 a","query 74 297","update 277 d","query 84 129","update 379 b","query 278 213","query 84 89","query 17 154","update 359 d","query 241 114","query 473 218","query 125 193","query 165 349","update 178 e","query 438 45","query 108 375"]
Randomly generated test cases using the web extension LeetTest!
Also provides up to date company tags and elo rating for problems!
Downloadable on the Chrome webstore or Firefox addons and works for most leetcode problems Read more8123410Copyright © 2026 LeetCode. All rights reserved.16098
@property --beam-angle-_r_27_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_27_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_27_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_27_"][data-active] {
  animation:
    beam-spin-_r_27_ 1.96s linear infinite,
    beam-fade-in-_r_27_ 0.6s ease forwards;
}

[data-beam="_r_27_"][data-fading] {
  animation:
    beam-spin-_r_27_ 1.96s linear infinite,
    beam-fade-out-_r_27_ 0.5s ease forwards;
}

[data-beam="_r_27_"][data-active]::after,
[data-beam="_r_27_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_27_),
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
      from var(--beam-angle-_r_27_),
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
      from var(--beam-angle-_r_27_),
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
  opacity: calc(var(--beam-opacity-_r_27_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_27_"][data-active]::before,
[data-beam="_r_27_"][data-fading]::before {
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
    from var(--beam-angle-_r_27_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_27_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_27_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_27_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_27_),
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

[data-beam="_r_27_"][data-active] [data-beam-bloom],
[data-beam="_r_27_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_27_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_27_ {
  to { --beam-angle-_r_27_: 360deg; }
}

@keyframes beam-fade-in-_r_27_ {
  to { --beam-opacity-_r_27_: 1; }
}

@keyframes beam-fade-out-_r_27_ {
  from { --beam-opacity-_r_27_: 1; }
  to { --beam-opacity-_r_27_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaJavaScriptPythonTypeScriptGoCC#KotlinRustSwiftPHPBit ManipulationTreeDepth-First SearchArrayStringDivide and ConquerBinary Indexed TreeSegment TreeLowest Common AncestorBinary LiftingHeavy-Light DecompositionEulerian PathBitmaskOrdered MapPalindromic TreeSparse TablePrefix SumBinary SearchSubmit at least 1 AC to publish a solution.Share my solutionLeetCode・ Open・Oct 16, 2026Palindromic Path Queries in a TreeEditorial710.4K9Aleksandr・ Open・16 hours ago✅ The Answer Is One Bit, the Code Isn’t | Euler Tour + Fenwick + O(1) LCABit ManipulationTreeDepth-First SearchBinary Indexed Tree6+887.3K4Vaibhav Raj Singh・ Open・11 hours agoHeavy-Light Decomposition + Bitmask XORBit ManipulationBitmaskC++Heavy-Light Decomposition562.1K2Shubhashree Sahu・ Open・8 hours agoShubha's LogicArray525460Muthu Vrn・ Open・10 hours agoGod is Great 508Python3299161Md Aarzoo Islam・ Open・12 hours ago899ms | Beats 23.86% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayStringDivide and ConquerBit Manipulation6+221.3K2Aryan Kumar Shaw Halwai・ Open・11 hours ago✅ Beats 100% 🚀 | Euler Tour + Fenwick Tree (XOR) + Binary Lifting LCA 🔥 | Java, C++, Python, JSBit ManipulationTreeDepth-First SearchBinary Indexed Tree5+97811Samarth Agrawal・ Open・9 hours ago✅ The Answer Is One Bit, the Code Isn’t | Euler Tour + Fenwick + O(1) LCAArrayStringCPython5+44316Bijoy Sing・ Open・13 hours ago✅ Efficient Solution → ⏳ O((n + q) log n) | Euler Tour + LCA + Fenwick Tree + | C++, Python, JavaStringBit ManipulationTreePython4+66431Subhashree Sahu・ Open・10 hours ago2 Approach | Step by Step | Square Root Decomposition without Fenwick Tree | with Fenwick tree 🔥ArrayDivide and ConquerBit ManipulationTree6+42181Ujjawal・ Open・9 hours agoSolution that Beats 100%ArrayStringDivide and ConquerBit Manipulation5+21561Long Nguyen・ Open・5 hours ago100% - [Hard Problem with Easy Approach] 6 Languages | C++ | C | Python3 | Java | JS | TS CC++JavaTypeScript2+21410Joseph Jackson・ Open・12 hours agosimplest solution for beginners, introducing HLD (easier than Euler Tour)C++Python322580Hasan Al Mamun・ Open・13 hours agoKotlin - Palindromic path queries in a treeKotlin2500Aryan Yadav・ Open・13 hours agoBeat 90%Python321700All SolutionsGod is Great 508Muthu Vrn91810 hours agoPython3Intuition

Approach

Complexity

Time complexity:



Space complexity:


Code
Python3class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # LCA preprocessing
        LOG = 17  # sufficient for n ≤ ~1e5
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(node: int, par: int):
            nonlocal timer
            tin[node] = timer
            timer += 1
            parent[0][node] = par

            for nei in graph[node]:
                if nei == par:
                    continue
                depth[nei] = depth[node] + 1
                dfs(nei, node)

            tout[node] = timer - 1

        dfs(0, -1)

        # Binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                p = parent[k - 1][i]
                if p != -1:
                    parent[k][i] = parent[k - 1][p]

        def lca(u: int, v: int) -> int:
            """Lowest common ancestor via binary lifting."""
            if depth[u] < depth[v]:
                u, v = v, u

            # Lift u to same depth
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in reversed(range(LOG)):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Fenwick tree (XOR)
        size = n
        fenwick = [0] * (n + 1)

        def fenwick_add(i: int, val: int):
            i += 1
            while i <= size:
                fenwick[i] ^= val
                i += i & -i

        def fenwick_prefix(i: int) -> int:
            res = 0
            i += 1
            while i > 0:
                res ^= fenwick[i]
                i -= i & -i
            return res

        # Character mask
        def char_mask(c: str) -> int:
            return 1 << (ord(c) - ord('a'))

        labels = list(s)

        # Initialize Fenwick tree with subtree toggling
        for u, c in enumerate(labels):
            m = char_mask(c)
            fenwick_add(tin[u], m)
            fenwick_add(tout[u] + 1, m)

        # Process queries
        answers = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = char_mask(labels[u]) ^ char_mask(new_char)
                labels[u] = new_char

                fenwick_add(tin[u], delta)
                fenwick_add(tout[u] + 1, delta)

            else:  # path query
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                path_mask = (
                    fenwick_prefix(tin[u])
                    ^ fenwick_prefix(tin[v])
                    ^ char_mask(labels[w])
                )

                # palindrome condition: ≤ 1 bit set
                answers.append(
                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
                )

        return answers PreviousShubha's LogicNext899ms | Beats 23.86% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥Comments (1)Sort by:BestCommentcodeDominar9 hours ago Read more11291Python3Auto110111112113114115116117118119120121122                path_mask = (                    fenwick_prefix(tin[u])                    ^ fenwick_prefix(tin[v])                    ^ char_mask(labels[w])                )                # palindrome condition: ≤ 1 bit set                answers.append(                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0                )        return answersIn the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.SavedLn 122, Col 23AcceptedRuntime: 0 msCase 1Case 2Inputn =3edges =[[0,1],[1,2]]s ="aac"queries =["query 0 2","update 1 b","query 0 2"]Output[true,false]Expected[true,false]Contribute a testcaseInput912345678›3[[0,1],[1,2]]"aac"["query 0 2","update 1 b","query 0 2"]4[[0,1],[0,2],[0,3]]"abca"["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]Output912›[true,false][false,false,true]Expected912›[true,false][false,false,true] All SubmissionsAccepted1040 / 1040 testcases passedMUTHU KUMAR Msubmitted at Oct 29, 2026 18:51AnalysisSolutionCodePython31class Solution:
2    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
3
4        graph = [[] for _ in range(n)]
5        for u, v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8
9        # LCA preprocessing
10        LOG = 17  # sufficient for n ≤ ~1e5
11        parent = [[-1] * n for _ in range(LOG)]
12        depth = [0] * n
13        tin = [0] * n
14        tout = [0] * n
15        timer = 0
16
17        def dfs(node: int, par: int):
18            nonlocal timer
19            tin[node] = timer
20            timer += 1
21            parent[0][node] = par
22
23            for nei in graph[node]:
24                if nei == par:
25                    continue
26                depth[nei] = depth[node] + 1
27                dfs(nei, node)
28
29            tout[node] = timer - 1
30
31        dfs(0, -1)
32
33        # Binary lifting table
34        for k in range(1, LOG):
35            for i in range(n):
36                p = parent[k - 1][i]
37                if p != -1:
38                    parent[k][i] = parent[k - 1][p]
39
40        def lca(u: int, v: int) -> int:
41            """Lowest common ancestor via binary lifting."""
42            if depth[u] < depth[v]:
43                u, v = v, u
44
45            # Lift u to same depth
46            diff = depth[u] - depth[v]
47            for k in range(LOG):
48                if diff & (1 << k):
49                    u = parent[k][u]
50
51            if u == v:
52                return u
53
54            for k in reversed(range(LOG)):
55                if parent[k][u] != parent[k][v]:
56                    u = parent[k][u]
57                    v = parent[k][v]
58
59            return parent[0][u]
60
61        # Fenwick tree (XOR)
62        size = n
63        fenwick = [0] * (n + 1)
64
65        def fenwick_add(i: int, val: int):
66            i += 1
67            while i <= size:
68                fenwick[i] ^= val
69                i += i & -i
70
71        def fenwick_prefix(i: int) -> int:
72            res = 0
73            i += 1
74            while i > 0:
75                res ^= fenwick[i]
76                i -= i & -i
77            return res
78
79        # Character mask
80        def char_mask(c: str) -> int:
81            return 1 << (ord(c) - ord('a'))
82
83        labels = list(s)
84
85        # Initialize Fenwick tree with subtree toggling
86        for u, c in enumerate(labels):
87            m = char_mask(c)
88            fenwick_add(tin[u], m)
89            fenwick_add(tout[u] + 1, m)
90
91        # Process queries
92        answers = []
93
94        for q in queries:
95            parts = q.split()
96
97            if parts[0] == "update":
98                u = int(parts[1])
99                new_char = parts[2]
100
101                delta = char_mask(labels[u]) ^ char_mask(new_char)
102                labels[u] = new_char
103
104                fenwick_add(tin[u], delta)
105                fenwick_add(tout[u] + 1, delta)
106
107            else:  # path query
108                u, v = int(parts[1]), int(parts[2])
109                w = lca(u, v)
110
111                path_mask = (
112                    fenwick_prefix(tin[u])
113                    ^ fenwick_prefix(tin[v])
114                    ^ char_mask(labels[w])
115                )
116
117                # palindrome condition: ≤ 1 bit set
118                answers.append(
119                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
120                )
121
122        return answersView more 0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
