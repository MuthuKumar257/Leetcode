# 3414. Maximum Score of Non-overlapping Intervals

- **Difficulty:** Hard
- **Language:** Python
- **LeetCode Link:** [Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)

## Solution

See [`solution.py`](./solution.py).

## Performance

- **Runtime:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily Coding Challenge Completed!Completion Streak: 101DaysConsistency is key, see you tomorrow!Friends Check-in0 friends checked in todaySort byTimeStreakNo friends have checked in today yetDaily QuestionDaily QuestionDebugging...Submit10100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3414. Maximum Score of Non-overlapping IntervalsSolvedHardTopicsCompaniesHintYou are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 
Example 1:


Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.


Example 2:


Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.


 
Constraints:


	1 <= intevals.length <= 5 * 104
	intervals[i].length == 3
	intervals[i] = [li, ri, weighti]
	1 <= li <= ri <= 109
	1 <= weighti <= 109

 Seen this question in a real interview before?1/6YesNoAccepted9,365/21.2KAcceptance Rate44.2%TopicsSenior StaffArrayBinary SearchDynamic ProgrammingSortingWeekly Contest 431CompaniesHint 1Use Dynamic Programming.Hint 2Sort intervals by right boundary.Hint 3Let dp[r][i] denote the maximum score having picked r intervals from the prefix of intervals ending at index i.Hint 4dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j]) where j is the largest index such that intervals[j][1] < intervals[i][0].Hint 5Since intervals is sorted by right boundary, we can find index j using binary search.Similar QuestionsTwo Best Non-Overlapping EventsMediumDiscussion (47)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestdekailJan 05, 2025Very classic Binary Search + 0-1 knapsack problem, the followings are the similar questions.
leetcode 1235
leetcode 2054
leetcode 1751
leetcode 2830
leetcode 2008 Read more2910goutham3 hours agoNot a very good morning Read more151NoahJan 05, 2025I believe hint number 4 has a minor error when it says "intervals[i][2] + dp[r][j]" - shouldn't it be dp[r - 1][j]? Since r denotes the number of intervals we can still take - and we start on dp[r][i] - taking intervals[i] should leave us the state (r - 1, j) right? Not (r, j) Read moreFeedback121proxy sigilJun 29, 2025this is not a question, this is a journey. going from WA to TLE brought a tear in my eye. it taught me nothing new, no new techniques, but getting the lexicographically smallest answer was a pain which i will remember for ages Read more83etanilaJan 05, 2025I'd never been this close to solving all 4 problems in a contest. Maybe next time... Read more7tokoc284153 hours agotest cases:
[[17,17,42],[8,17,5],[25,25,25],[21,23,1]]
[[17,20,36],[8,19,21],[8,17,35],[1,23,12],[22,22,14],[4,10,19],[18,22,31],[18,19,37],[6,22,24]]
[[2,9,7],[3,5,12],[5,23,45],[2,3,47],[20,23,34],[21,23,16],[15,22,30],[2,10,21],[6,16,24],[10,20,4]]
[[9,11,49],[16,24,47],[24,25,42],[18,21,6],[21,22,13],[19,19,20],[22,24,21],[14,18,23],[4,10,39]]
[[18,23,38],[19,24,5],[15,15,40],[15,15,1],[1,16,10],[12,21,1],[16,20,44],[23,23,49],[19,22,48]]
[[16,17,24],[10,21,2],[15,25,31],[18,19,24],[2,9,40],[20,24,23],[1,13,35],[24,25,11],[11,18,7]]
[[6,21,39],[2,23,15],[2,21,29],[1,2,8],[13,20,17],[15,25,37],[12,13,50],[13,21,46],[17,24,16]]
[[142471497,196026711,295607346],[451335135,483708295,218807535],[575511108,838936304,990962821],[436678633,749197884,234069539],[431621801,476042736,327590759],[731064983,794388193,292097202],[456428806,878843776,872141557],[623738826,645519513,508930008],[72031959,884939800,289146675],[173735145,400929010,631263045],[721976890,977251292,628985628],[866112509,987838009,774700922],[763707685,912476782,390045499],[148109973,927162475,403755085],[129596979,208217751,288065367],[698395727,911596635,317341103],[72460015,261990317,460522513],[885097167,952345627,840012443],[96671770,743500544,59119810],[771574067,935093303,708932764],[208589557,863648416,23980345],[361436477,922937280,742925302],[28833294,823032965,548699916],[904338960,994898882,650561084],[575099199,641181779,991872700],[829723755,853125980,522919387],[920690481,929298922,618629497],[946388550,991915180,175325339],[500885623,565108019,172888654],[655921326,720179460,705090816],[853010936,928622850,98817276],[316005677,816587327,509193879],[269328011,899973755,903476431],[740539743,930861347,996869209],[810328650,989999011,902108162],[536534754,677427180,971435824],[510582583,708845055,690162778],[723701864,821082718,6685426],[529530236,674179715,772771939],[54213787,667517229,85905385],[138137281,907924951,562266577],[239643207,887837825,405699407],[294241103,641974626,265388593],[57315179,591064491,643911523],[657275437,802374275,966319295],[257998898,301212431,808325694],[608366092,680175628,945716932],[429184657,733387338,180575274],[7368144,142787470,605606282],[263527888,981375477,410751408],[608404596,816854816,324661430],[828651488,844905007,559788168],[415334642,839519741,26629963],[182313360,733642289,993942346],[954335362,969102383,181120024],[926148225,948471382,619501724],[712398629,719863221,941837059],[282264374,475024556,121847882],[312880965,901850319,506362337],[551298222,983444443,779857137],[690148600,976364290,719023330],[464490139,546839739,128239038],[445515706,897379621,152770092],[326283714,505874341,960093323],[389410096,732931555,128331331],[81617691,998645169,600835082],[632150567,713308519,51803441],[829993047,941535517,48658359],[694257607,874262837,650397906],[687821239,782857761,172989986],[859997836,982400746,197461441],[780932154,887017215,52508707],[622655926,727280592,217407780],[182035992,702124076,69136618],[771053778,971437486,734075530],[644370518,718890580,267657535],[968405042,972980322,803208363],[399593782,720682247,783027634],[792311409,892565664,661746016],[490710003,694805263,749424357],[640869824,837120230,206112667],[300487267,469888092,518504132],[885091144,926326441,805153845],[456493030,936080825,239335178],[825751176,993353144,827631539],[1215985,788288588,675606957],[244839821,682352403,677722303],[550872746,723776226,437944570],[6193403,216673106,503013215],[531097059,815227562,158007985],[672912728,674545916,903044859],[416320262,878967192,579193655],[749360203,973924060,228851914],[366334092,977562496,496197988],[332675122,715620770,209958573],[989175990,996321513,904312937],[441441687,973572004,163943976],[907911655,966034013,652384688],[585187239,673340379,728985482],[276522486,469672133,18436209],[263946264,617911574,567487346],[616201743,691619038,952174526],[915286909,951229766,395431782],[784206598,899344637,475484731],[949109752,971758227,340902058],[585562332,667236565,228398800],[268361063,456931188,162546495],[150453521,866148858,96666898],[914079933,963420000,548839975],[973982339,988634900,930524568],[665027431,984874633,992899248],[995862024,998684004,914077730],[639455985,890439236,115931403],[117764259,286589461,994113151],[814971071,917020918,97952207],[57335740,123894852,319668363],[965294176,976645402,972064305],[146938985,342877533,9920114],[766767545,893714843,740600369],[195023527,272607303,127916496],[832835889,918976340,933488935],[6222279,585358943,955883720],[130721572,861711385,611852422],[252479154,910589578,161859035],[898470177,983746859,346211012],[58924113,910336272,286024023],[634142589,741561538,890396770],[665077562,757520463,447112680],[939689953,978844674,878451843],[82215393,268257729,125888772],[915149253,922897864,109884753],[910043247,937256510,269493519],[958004161,983603697,293384289],[762618348,891546496,506914317],[978882345,995974718,648869067],[250404566,886383863,412754238],[844444574,899250757,570490734],[169864597,900693924,572403655],[519339788,751133349,903869839],[993636117,995462186,327101486],[16402883,746177977,841343851],[658591010,752150835,112890227],[179393120,688150005,909760218],[704596360,865864767,427816854],[695239546,794602059,151413991],[350070471,689332859,63319669],[661238916,888857573,580829608],[20433103,531509934,240375155],[232099149,477230468,999315951],[537388332,715794448,147066567],[434911912,986064227,438845665],[752668174,785087443,150387102],[926918396,934027372,676905888],[886052091,996084249,987697371],[35881966,741486819,496320290],[562711882,907409315,484530390],[798545289,911375246,373453410],[814504081,983838186,796928649],[917205514,968542078,678737464],[171127912,350098932,550972361],[142000558,625357626,169174443],[205333787,320041012,877781539],[119746598,614795030,913060669],[585471834,834211142,412450528],[88116609,777060692,147530342],[490533944,741309263,899727128],[437029403,506752256,291011413],[322456673,774213108,440956944],[116014682,632566557,782492448],[518061546,975356475,800436728],[776725721,976405523,773794056],[395046611,464341585,694472416],[25107065,426355641,473162836],[468982695,987773183,334863697],[843408376,982451746,280120706],[998185848,998444712,786836355],[923784823,996503563,763567741],[931335577,984664688,269329767],[478412852,881437552,752368134],[587576996,871184772,284836948],[552095838,606597632,728487575],[437535576,489697568,740316654],[616949988,892206406,545106709],[605634041,863465514,696208975],[150724099,795277372,90060209],[683173002,935893962,306632640],[962427337,995253781,533826136],[797260743,997597598,501275858],[293493849,426377586,24079941],[946951294,950491333,554823201],[116813792,635789454,463102618],[763667742,785668038,919480759],[488401862,541501525,769820002],[786556660,872979230,464371687],[68969846,459094782,868358490],[659405559,701127902,559066563],[274404671,990171132,680315225],[891673146,940596445,666768054],[300393234,843658884,99965422],[442751340,723389227,758991733],[615127679,986317457,478808325],[536211610,718519044,487092007],[220739848,919817327,927711181],[208174295,726695729,511743058],[502882136,793177663,261905267],[496356445,956878561,527975466],[522937837,741279605,683452527],[539682945,666007184,982503177],[30485837,621775010,583470978],[175450698,830810926,299433716],[660163899,745911406,163642373],[792410547,881449018,701799618],[442798392,693386729,10820462],[49455732,171278332,714998281],[877582464,961377203,944752948],[208740916,462143197,96179950],[571495690,783001988,439074249],[239479427,891950592,849782697],[74064391,299576356,352231514],[92961111,291560550,647555089],[387586057,649625768,499483968],[774804602,933362277,594383963],[313341325,489025413,105311381],[761381892,909185280,756408513],[827237071,883599222,186300244],[846051057,955629720,436561892],[233633277,493358404,649456278],[882828093,983068245,669039965],[950801907,992032438,76533411],[794696851,926079226,422966146],[419471322,469128982,911740137],[738846306,756450041,89325030],[75348573,920378764,787121229],[421909142,472820190,25586184],[685995844,693905026,294582505],[830363220,861943838,568033796],[201220401,635997425,715572460],[572268775,652300372,718427814],[204454397,661493102,600639272],[836337590,942932620,251865586],[5198319,325684501,631835885],[552870994,598863703,364010797],[891737199,932853447,863452787],[144567970,974565116,668544409],[161496288,979157174,793255921],[667341300,809342997,57236777],[425240677,731817443,191897217],[618691762,792853176,969212474],[337910139,660998466,939427074],[280451523,715939402,357880865],[438517488,893617368,200157432],[251564246,828491585,588588814],[248991780,572951706,569331293],[762483392,765171393,144468360],[938203870,959423313,252325103],[559319784,951531020,945614761],[343649387,487232802,459641314],[726250943,788435736,428334802],[493962624,997222619,666023604],[490245934,601134712,177172034],[730184873,942515846,55326729],[448685425,651080933,882448104],[36234308,220890420,643736893],[623536177,835720270,345667157],[952060139,969188989,809715765],[342196768,456848763,285140685],[368249233,874899903,540188969],[839129622,847113579,724080644],[324002112,562257589,871364646],[400424460,965134749,628052812],[891751560,958710140,378527750],[755944887,993711986,556551379],[702417479,900721109,895616133],[746241543,749887873,150036974],[979938648,997043601,571303303],[825600959,984280076,471964964],[410936473,952853241,998926723],[454672676,802121117,958111179],[686825449,772878335,868802240],[26401878,825624976,307301744],[316642496,394014973,697813042],[323695310,491556727,914460572],[69613429,127789779,197057882],[595598118,851927101,960358956],[102717221,917570105,220662263],[197681853,515767551,610873020],[248347311,328812315,769175879],[790416509,906079215,921102834],[145301775,650555946,852862611],[614360602,978432494,143413311],[106074404,490738950,282034933],[748082327,845744114,797757788],[597830210,838621265,213514370],[524743743,863868860,230129752],[295864548,865017173,524699671]] Read more6Nigaro safo3 hours agoAm i the only one who didn't even understood the question ?? Read more31Prashant Singh3 hours agoi woke up at 5:30 to solve POTD and i think i am ready to sleep again Read more32Dahiya11Apr 02, 2025Attempt this problem before attempting this: https://leetcode.com/problems/two-best-non-overlapping-events/description/ Read more3Tanishq Singh RathoreApr 03, 2025Easily the hardest dp question, I have ever tried, answer construction killed me ngl. Read more212345Copyright © 2026 LeetCode. All rights reserved.75472294 Online
@property --beam-angle-_r_2v_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_2v_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_2v_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_2v_"][data-active] {
  animation:
    beam-spin-_r_2v_ 1.96s linear infinite,
    beam-fade-in-_r_2v_ 0.6s ease forwards;
}

[data-beam="_r_2v_"][data-fading] {
  animation:
    beam-spin-_r_2v_ 1.96s linear infinite,
    beam-fade-out-_r_2v_ 0.5s ease forwards;
}

[data-beam="_r_2v_"][data-active]::after,
[data-beam="_r_2v_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2v_),
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
      from var(--beam-angle-_r_2v_),
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
      from var(--beam-angle-_r_2v_),
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
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_2v_"][data-active]::before,
[data-beam="_r_2v_"][data-fading]::before {
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
    from var(--beam-angle-_r_2v_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_2v_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_2v_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2v_),
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

[data-beam="_r_2v_"][data-active] [data-beam-bloom],
[data-beam="_r_2v_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_2v_ {
  to { --beam-angle-_r_2v_: 360deg; }
}

@keyframes beam-fade-in-_r_2v_ {
  to { --beam-opacity-_r_2v_: 1; }
}

@keyframes beam-fade-out-_r_2v_ {
  from { --beam-opacity-_r_2v_: 1; }
  to { --beam-opacity-_r_2v_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptTypeScriptRustKotlinGoC#CScalaRubyDartSwiftPHPRacketElixirErlangDynamic ProgrammingBinary SearchSortingArrayHash TableHeap (Priority Queue)MemoizationRecursionBinary Indexed TreeOrdered MapRadix SortYour last submission beat 32% of other submissions' runtime.Share my solutionLeetCode・ Open・Sep 08, 2026Maximum Score of Non-overlapping IntervalsEditorial42.7K2Snapdragon・ Open・2 hours agoDynamic Programming + Binary Search + python | c++Binary SearchDynamic ProgrammingSortingPython2+209030Aura Farming・ Open・an hour agoᯓ★ Trust me it's not Hard! • (Take/Skip) DP Rec+Memo → Tab ⚡︎ • Easy Explanation!✈︎Hash TableBinary SearchDynamic ProgrammingPython2+123911Md Aarzoo Islam・ Open・an hour ago656ms | Beats 79.35% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayBinary SearchDynamic ProgrammingSorting6+101781An-Wen Deng・ Open・2 hours agoDP+binary search+(Radix) sort|beats 100%Binary SearchDynamic ProgrammingSortingRadix Sort1+6602Aryan Kumar Shaw Halwai・ Open・an hour agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | DP (Rec +Memo)ArrayBinary SearchDynamic ProgrammingSorting1+4480Anirudh・ Open・3 hours agoDP + Binary Search | N log N | C++ Java Python ✅Binary SearchPythonC++Java57310EdgeCaseOffByOne・ Open・2 hours agoEasy Solution Explained with Intuition, Approach, Code and Time ComplexityArrayBinary SearchDynamic ProgrammingSorting1+3530RISHABH BABU・ Open・2 hours agoMax Weight of K Intervals (DP + Binary Search)ArrayBinary SearchDynamic ProgrammingSorting3+2340chaharharsh67・ Open・2 hours agoDP + Binary Search | Right-to-Left | O(N log N)Java2540Magudarena・ Open・3 hours agoDynamic Programming + Binary Search | All 19 Languages Included 🚀Dynamic ProgrammingCPythonC++6+21660Ayush Dalal・ Open・10 minutes ago🚀 Very Easy Java Solution | Maximum Score of Non-overlapping IntervalsArrayBinary SearchDynamic ProgrammingSorting1+120Prabhas Sharma・ Open・40 minutes ago3414. Maximum Score of Non-overlapping IntervalsPython31140Ankit Mohapatra・ Open・43 minutes agoEasy C++ Code || Simple For Beginners || Beats 100%ArrayBinary SearchDynamic ProgrammingSorting1+140Sagar Gupta・ Open・2 hours agoC++ | DP with Lex Tie-Break | O(n log n)ArrayBinary SearchDynamic ProgrammingSorting1+1200All SolutionsDynamic Programming + Binary Search + python | c++Snapdragon9042 hours agoBinary SearchDynamic ProgrammingSortingPython2+Intuition
The problem asks us to find up to 4 non-overlapping intervals that yield the maximum total weight. If there are multiple combinations with the same maximum weight, we must return the one whose indices are lexicographically smallest.
This problem is a variation of the classic "Weighted Job Scheduling" problem, which can be efficiently solved using Dynamic Programming (DP) and Binary Search. The core idea is to process intervals in increasing order of their end times and, for each interval, decide whether to include it or not.
Algorithm


Format and Sort the Intervals:
First, we append the original index to each interval so we don't lose track of it after sorting. We convert each interval to a structure containing (end, start, weight, originalIndex) and sort the array based on the end boundary in ascending order. Sorting by end time allows us to optimally find the latest interval that ends before the current one starts.


Define the DP State:
We use a 2D DP array dp of size (N + 1) x 5, where N is the total number of intervals.

dp[i][j] stores the optimal configuration considering the first i sorted intervals and selecting exactly j intervals (0≤j≤4).
To elegantly handle the conditions (maximize weight, then minimize lexicographical indices), we store the state as a tuple: (-totalWeight, sortedIndices). Finding the minimum (min()) of these tuples inherently prioritizes the largest total weight (because of the negative sign) and then tie-breaks using the lexicographically smallest list of indices.



DP Transitions:
We iterate through each interval at index i:

To find the optimal previous state if we decide to pick this interval, we need the latest interval that does not overlap. We can use binary search (bisect_left in Python, lower_bound in C++) to find the index k of the first interval whose end boundary is strictly greater than or equal to our start. Since intervals at index k and beyond overlap, the valid non-overlapping intervals are up to index k, which maps perfectly to dp[k].
For each count j from 1 to 4, we consider two choices:

Skip the current interval: The optimal result is identical to the result without this interval, dp[i][j].
Take the current interval: We add the current interval's weight to dp[k][j - 1]. We append the current originalIndex to the chosen indices and sort them.


We assign dp[i + 1][j] the optimal (minimum) choice between skipping and taking.



Result:
After checking all intervals, the overall optimal configuration for at most 4 intervals will be stored at dp[N][4]. We extract and return the list of indices from this state.



Implementation (Python)
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store as (end, start, weight, originalIndex) and sort by end boundary
        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        sortedIntervals.sort(key=lambda x: x[0])

        # dp[i][j] stores a tuple: (-max_weight, lexicographically_smallest_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]

        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):
            # Binary search to find the latest non-overlapping interval
            # bisect_left finds the first interval whose end >= current start
            k = bisect_left(sortedIntervals, (start,), hi=i)
            
            for j in range(1, 5):
                prevWeight, prevIndices = dp[k][j - 1]
                
                skip = dp[i][j]
                
                # min() naturally prioritizes the lowest (most negative) weight sum, 
                # then lexicographically smallest sorted indices
                takeWeight = prevWeight - weight
                takeIndices = sorted(prevIndices + [originalIndex])
                take = (takeWeight, takeIndices)
                
                dp[i + 1][j] = min(skip, take)

        return dp[-1][4][1]
Implementation (C++)
Because C++ compares std::pair and std::vector identically to Python (element by element), this exact trick ports over perfectly using pair<long long, vector<int>>.
class Solution {
    struct IntervalData {
        int end, start, weight, originalIndex;
        // Used for sorting and lower_bound comparisons
        bool operator<(const IntervalData& other) const {
            return end < other.end;
        }
    };

public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<IntervalData> sortedIntervals;
        
        for (int i = 0; i < n; ++i) {
            sortedIntervals.push_back({intervals[i][1], intervals[i][0], intervals[i][2], i});
        }
        sort(sortedIntervals.begin(), sortedIntervals.end());
        
        // dp[i][j] stores a pair: {-max_weight, lexicographically_smallest_indices}
        vector<vector<pair<long long, vector<int>>>> dp(n + 1, vector<pair<long long, vector<int>>>(5, {0LL, {}}));
        
        for (int i = 0; i < n; ++i) {
            int start = sortedIntervals[i].start;
            int weight = sortedIntervals[i].weight;
            int originalIndex = sortedIntervals[i].originalIndex;
            
            // lower_bound finds the first interval whose end >= current start
            IntervalData target = {start, 0, 0, 0}; 
            int k = lower_bound(sortedIntervals.begin(), sortedIntervals.begin() + i, target) - sortedIntervals.begin();
            
            for (int j = 1; j <= 4; ++j) {
                long long prevWeight = dp[k][j - 1].first;
                vector<int> prevIndices = dp[k][j - 1].second;
                
                pair<long long, vector<int>> skip = dp[i][j];
                
                vector<int> takeIndices = prevIndices;
                takeIndices.push_back(originalIndex);
                sort(takeIndices.begin(), takeIndices.end());
                
                pair<long long, vector<int>> take = {prevWeight - weight, takeIndices};
                
                // min() naturally prioritizes the lowest (most negative) weight sum, 
                // then lexicographically smallest sorted indices
                dp[i + 1][j] = min(skip, take);
            }
        }
        
        return dp[n][4].second;
    }
};

Complexity

Time Complexity: O(NlogN)

Formatting and sorting the intervals takes O(NlogN) time.
For each of the N intervals, we execute a binary search which takes O(logN) time.
The inner loop always runs 4 times. Inside it, sorting a list of maximum size 4 takes O(1) time. Thus, filling the DP array is O(NlogN).


Space Complexity: O(N)

The formatted array requires O(N) space.
The dp array has dimensions (N+1)×5, where each cell stores a numeric value and an array of at most 4 integers, consuming O(N) overall memory.


 PreviousMaximum Score of Non-overlapping IntervalsNextᯓ★ Trust me it's not Hard! • (Take/Skip) DP Rec+Memo → Tab ⚡︎ • Easy Explanation!✈︎Comments (0)Sort by:BestCommentNo comments yet.200Python3Auto111213109876543211415            for j in range(1, 5):                prevWeight, prevIndices = dp[k][j - 1]                                        k = bisect_left(sortedIntervals, (start,), hi=i)        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]        sortedIntervals.sort(key=lambda x: x[0])        (intervals)]        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:class Solution:                skip = dp[i][j]                takeWeight = prevWeight - weightSavedLn 2, Col 70AcceptedRuntime: 35 msCase 1Case 2Inputintervals =[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]Output[2,3]Expected[2,3]Contribute a testcaseInput912›[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]][[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]Output912›[2,3][1,3,5,6]Expected912›[2,3][1,3,5,6] All SubmissionsAccepted581 / 581 testcases passedMUTHU KUMAR Msubmitted at Sep 12, 2026 09:00AnalysisSolution👑 Unlock the Full LeetCode ExperienceCompany problems, Ask Leet, and expert editorials — all in one plan.Runtime1646msBeats32.20%Memory86.47MBBeats33.90%Created with Highcharts 11.1.01209ms1430ms1470ms1565ms1670ms2196ms0%2%4%
                  
                Created with Highcharts 11.1.01209ms1430ms1470ms1565ms1670ms2196msCodePython31class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
4        sortedIntervals.sort(key=lambda x: x[0])
5
6        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]
7
8        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):
9            k = bisect_left(sortedIntervals, (start,), hi=i)
10            
11            for j in range(1, 5):
12                prevWeight, prevIndices = dp[k][j - 1]
13                
14                skip = dp[i][j]
15                takeWeight = prevWeight - weight
16                takeIndices = sorted(prevIndices + [originalIndex])
17                take = (takeWeight, takeIndices)
18                
19                dp[i + 1][j] = min(skip, take)
20
21        return dp[-1][4][1]View more More challenges2054. Two Best Non-Overlapping Events0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize
- **Memory:** !function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()Daily Coding Challenge Completed!Completion Streak: 101DaysConsistency is key, see you tomorrow!Friends Check-in0 friends checked in todaySort byTimeStreakNo friends have checked in today yetDaily QuestionDaily QuestionDebugging...Submit10100:00:00MUTHU KUMAR MAccess all features with our Premium subscription!My ListsNotebookProgressPointsTry New FeaturesOrdersMy PlaygroundsSettingsAppearanceAppearanceSystem DefaultLightDarkSign OutSystem DefaultLightDarkPremiumDescriptionDescriptionEditorialEditorialSolutionsSolutionsAcceptedAcceptedSubmissionsSubmissionsCodeCodeTestcaseTestcaseTest ResultTest Result3414. Maximum Score of Non-overlapping IntervalsSolvedHardTopicsCompaniesHintYou are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 
Example 1:


Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.


Example 2:


Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.


 
Constraints:


	1 <= intevals.length <= 5 * 104
	intervals[i].length == 3
	intervals[i] = [li, ri, weighti]
	1 <= li <= ri <= 109
	1 <= weighti <= 109

 Seen this question in a real interview before?1/6YesNoAccepted9,365/21.2KAcceptance Rate44.2%TopicsSenior StaffArrayBinary SearchDynamic ProgrammingSortingWeekly Contest 431CompaniesHint 1Use Dynamic Programming.Hint 2Sort intervals by right boundary.Hint 3Let dp[r][i] denote the maximum score having picked r intervals from the prefix of intervals ending at index i.Hint 4dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j]) where j is the largest index such that intervals[j][1] < intervals[i][0].Hint 5Since intervals is sorted by right boundary, we can find index j using binary search.Similar QuestionsTwo Best Non-Overlapping EventsMediumDiscussion (47)Choose a typeComment💡 Discussion Rules1. Please don't post any solutions in this discussion.2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.Sort by:BestdekailJan 05, 2025Very classic Binary Search + 0-1 knapsack problem, the followings are the similar questions.
leetcode 1235
leetcode 2054
leetcode 1751
leetcode 2830
leetcode 2008 Read more2910goutham3 hours agoNot a very good morning Read more151NoahJan 05, 2025I believe hint number 4 has a minor error when it says "intervals[i][2] + dp[r][j]" - shouldn't it be dp[r - 1][j]? Since r denotes the number of intervals we can still take - and we start on dp[r][i] - taking intervals[i] should leave us the state (r - 1, j) right? Not (r, j) Read moreFeedback121proxy sigilJun 29, 2025this is not a question, this is a journey. going from WA to TLE brought a tear in my eye. it taught me nothing new, no new techniques, but getting the lexicographically smallest answer was a pain which i will remember for ages Read more83etanilaJan 05, 2025I'd never been this close to solving all 4 problems in a contest. Maybe next time... Read more7tokoc284153 hours agotest cases:
[[17,17,42],[8,17,5],[25,25,25],[21,23,1]]
[[17,20,36],[8,19,21],[8,17,35],[1,23,12],[22,22,14],[4,10,19],[18,22,31],[18,19,37],[6,22,24]]
[[2,9,7],[3,5,12],[5,23,45],[2,3,47],[20,23,34],[21,23,16],[15,22,30],[2,10,21],[6,16,24],[10,20,4]]
[[9,11,49],[16,24,47],[24,25,42],[18,21,6],[21,22,13],[19,19,20],[22,24,21],[14,18,23],[4,10,39]]
[[18,23,38],[19,24,5],[15,15,40],[15,15,1],[1,16,10],[12,21,1],[16,20,44],[23,23,49],[19,22,48]]
[[16,17,24],[10,21,2],[15,25,31],[18,19,24],[2,9,40],[20,24,23],[1,13,35],[24,25,11],[11,18,7]]
[[6,21,39],[2,23,15],[2,21,29],[1,2,8],[13,20,17],[15,25,37],[12,13,50],[13,21,46],[17,24,16]]
[[142471497,196026711,295607346],[451335135,483708295,218807535],[575511108,838936304,990962821],[436678633,749197884,234069539],[431621801,476042736,327590759],[731064983,794388193,292097202],[456428806,878843776,872141557],[623738826,645519513,508930008],[72031959,884939800,289146675],[173735145,400929010,631263045],[721976890,977251292,628985628],[866112509,987838009,774700922],[763707685,912476782,390045499],[148109973,927162475,403755085],[129596979,208217751,288065367],[698395727,911596635,317341103],[72460015,261990317,460522513],[885097167,952345627,840012443],[96671770,743500544,59119810],[771574067,935093303,708932764],[208589557,863648416,23980345],[361436477,922937280,742925302],[28833294,823032965,548699916],[904338960,994898882,650561084],[575099199,641181779,991872700],[829723755,853125980,522919387],[920690481,929298922,618629497],[946388550,991915180,175325339],[500885623,565108019,172888654],[655921326,720179460,705090816],[853010936,928622850,98817276],[316005677,816587327,509193879],[269328011,899973755,903476431],[740539743,930861347,996869209],[810328650,989999011,902108162],[536534754,677427180,971435824],[510582583,708845055,690162778],[723701864,821082718,6685426],[529530236,674179715,772771939],[54213787,667517229,85905385],[138137281,907924951,562266577],[239643207,887837825,405699407],[294241103,641974626,265388593],[57315179,591064491,643911523],[657275437,802374275,966319295],[257998898,301212431,808325694],[608366092,680175628,945716932],[429184657,733387338,180575274],[7368144,142787470,605606282],[263527888,981375477,410751408],[608404596,816854816,324661430],[828651488,844905007,559788168],[415334642,839519741,26629963],[182313360,733642289,993942346],[954335362,969102383,181120024],[926148225,948471382,619501724],[712398629,719863221,941837059],[282264374,475024556,121847882],[312880965,901850319,506362337],[551298222,983444443,779857137],[690148600,976364290,719023330],[464490139,546839739,128239038],[445515706,897379621,152770092],[326283714,505874341,960093323],[389410096,732931555,128331331],[81617691,998645169,600835082],[632150567,713308519,51803441],[829993047,941535517,48658359],[694257607,874262837,650397906],[687821239,782857761,172989986],[859997836,982400746,197461441],[780932154,887017215,52508707],[622655926,727280592,217407780],[182035992,702124076,69136618],[771053778,971437486,734075530],[644370518,718890580,267657535],[968405042,972980322,803208363],[399593782,720682247,783027634],[792311409,892565664,661746016],[490710003,694805263,749424357],[640869824,837120230,206112667],[300487267,469888092,518504132],[885091144,926326441,805153845],[456493030,936080825,239335178],[825751176,993353144,827631539],[1215985,788288588,675606957],[244839821,682352403,677722303],[550872746,723776226,437944570],[6193403,216673106,503013215],[531097059,815227562,158007985],[672912728,674545916,903044859],[416320262,878967192,579193655],[749360203,973924060,228851914],[366334092,977562496,496197988],[332675122,715620770,209958573],[989175990,996321513,904312937],[441441687,973572004,163943976],[907911655,966034013,652384688],[585187239,673340379,728985482],[276522486,469672133,18436209],[263946264,617911574,567487346],[616201743,691619038,952174526],[915286909,951229766,395431782],[784206598,899344637,475484731],[949109752,971758227,340902058],[585562332,667236565,228398800],[268361063,456931188,162546495],[150453521,866148858,96666898],[914079933,963420000,548839975],[973982339,988634900,930524568],[665027431,984874633,992899248],[995862024,998684004,914077730],[639455985,890439236,115931403],[117764259,286589461,994113151],[814971071,917020918,97952207],[57335740,123894852,319668363],[965294176,976645402,972064305],[146938985,342877533,9920114],[766767545,893714843,740600369],[195023527,272607303,127916496],[832835889,918976340,933488935],[6222279,585358943,955883720],[130721572,861711385,611852422],[252479154,910589578,161859035],[898470177,983746859,346211012],[58924113,910336272,286024023],[634142589,741561538,890396770],[665077562,757520463,447112680],[939689953,978844674,878451843],[82215393,268257729,125888772],[915149253,922897864,109884753],[910043247,937256510,269493519],[958004161,983603697,293384289],[762618348,891546496,506914317],[978882345,995974718,648869067],[250404566,886383863,412754238],[844444574,899250757,570490734],[169864597,900693924,572403655],[519339788,751133349,903869839],[993636117,995462186,327101486],[16402883,746177977,841343851],[658591010,752150835,112890227],[179393120,688150005,909760218],[704596360,865864767,427816854],[695239546,794602059,151413991],[350070471,689332859,63319669],[661238916,888857573,580829608],[20433103,531509934,240375155],[232099149,477230468,999315951],[537388332,715794448,147066567],[434911912,986064227,438845665],[752668174,785087443,150387102],[926918396,934027372,676905888],[886052091,996084249,987697371],[35881966,741486819,496320290],[562711882,907409315,484530390],[798545289,911375246,373453410],[814504081,983838186,796928649],[917205514,968542078,678737464],[171127912,350098932,550972361],[142000558,625357626,169174443],[205333787,320041012,877781539],[119746598,614795030,913060669],[585471834,834211142,412450528],[88116609,777060692,147530342],[490533944,741309263,899727128],[437029403,506752256,291011413],[322456673,774213108,440956944],[116014682,632566557,782492448],[518061546,975356475,800436728],[776725721,976405523,773794056],[395046611,464341585,694472416],[25107065,426355641,473162836],[468982695,987773183,334863697],[843408376,982451746,280120706],[998185848,998444712,786836355],[923784823,996503563,763567741],[931335577,984664688,269329767],[478412852,881437552,752368134],[587576996,871184772,284836948],[552095838,606597632,728487575],[437535576,489697568,740316654],[616949988,892206406,545106709],[605634041,863465514,696208975],[150724099,795277372,90060209],[683173002,935893962,306632640],[962427337,995253781,533826136],[797260743,997597598,501275858],[293493849,426377586,24079941],[946951294,950491333,554823201],[116813792,635789454,463102618],[763667742,785668038,919480759],[488401862,541501525,769820002],[786556660,872979230,464371687],[68969846,459094782,868358490],[659405559,701127902,559066563],[274404671,990171132,680315225],[891673146,940596445,666768054],[300393234,843658884,99965422],[442751340,723389227,758991733],[615127679,986317457,478808325],[536211610,718519044,487092007],[220739848,919817327,927711181],[208174295,726695729,511743058],[502882136,793177663,261905267],[496356445,956878561,527975466],[522937837,741279605,683452527],[539682945,666007184,982503177],[30485837,621775010,583470978],[175450698,830810926,299433716],[660163899,745911406,163642373],[792410547,881449018,701799618],[442798392,693386729,10820462],[49455732,171278332,714998281],[877582464,961377203,944752948],[208740916,462143197,96179950],[571495690,783001988,439074249],[239479427,891950592,849782697],[74064391,299576356,352231514],[92961111,291560550,647555089],[387586057,649625768,499483968],[774804602,933362277,594383963],[313341325,489025413,105311381],[761381892,909185280,756408513],[827237071,883599222,186300244],[846051057,955629720,436561892],[233633277,493358404,649456278],[882828093,983068245,669039965],[950801907,992032438,76533411],[794696851,926079226,422966146],[419471322,469128982,911740137],[738846306,756450041,89325030],[75348573,920378764,787121229],[421909142,472820190,25586184],[685995844,693905026,294582505],[830363220,861943838,568033796],[201220401,635997425,715572460],[572268775,652300372,718427814],[204454397,661493102,600639272],[836337590,942932620,251865586],[5198319,325684501,631835885],[552870994,598863703,364010797],[891737199,932853447,863452787],[144567970,974565116,668544409],[161496288,979157174,793255921],[667341300,809342997,57236777],[425240677,731817443,191897217],[618691762,792853176,969212474],[337910139,660998466,939427074],[280451523,715939402,357880865],[438517488,893617368,200157432],[251564246,828491585,588588814],[248991780,572951706,569331293],[762483392,765171393,144468360],[938203870,959423313,252325103],[559319784,951531020,945614761],[343649387,487232802,459641314],[726250943,788435736,428334802],[493962624,997222619,666023604],[490245934,601134712,177172034],[730184873,942515846,55326729],[448685425,651080933,882448104],[36234308,220890420,643736893],[623536177,835720270,345667157],[952060139,969188989,809715765],[342196768,456848763,285140685],[368249233,874899903,540188969],[839129622,847113579,724080644],[324002112,562257589,871364646],[400424460,965134749,628052812],[891751560,958710140,378527750],[755944887,993711986,556551379],[702417479,900721109,895616133],[746241543,749887873,150036974],[979938648,997043601,571303303],[825600959,984280076,471964964],[410936473,952853241,998926723],[454672676,802121117,958111179],[686825449,772878335,868802240],[26401878,825624976,307301744],[316642496,394014973,697813042],[323695310,491556727,914460572],[69613429,127789779,197057882],[595598118,851927101,960358956],[102717221,917570105,220662263],[197681853,515767551,610873020],[248347311,328812315,769175879],[790416509,906079215,921102834],[145301775,650555946,852862611],[614360602,978432494,143413311],[106074404,490738950,282034933],[748082327,845744114,797757788],[597830210,838621265,213514370],[524743743,863868860,230129752],[295864548,865017173,524699671]] Read more6Nigaro safo3 hours agoAm i the only one who didn't even understood the question ?? Read more31Prashant Singh3 hours agoi woke up at 5:30 to solve POTD and i think i am ready to sleep again Read more32Dahiya11Apr 02, 2025Attempt this problem before attempting this: https://leetcode.com/problems/two-best-non-overlapping-events/description/ Read more3Tanishq Singh RathoreApr 03, 2025Easily the hardest dp question, I have ever tried, answer construction killed me ngl. Read more212345Copyright © 2026 LeetCode. All rights reserved.75472294 Online
@property --beam-angle-_r_2v_ {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: true;
}

@property --beam-opacity-_r_2v_ {
  syntax: "<number>";
  initial-value: 0;
  inherits: true;
}

[data-beam="_r_2v_"] {
  position: relative;
  border-radius: 9999px;
  overflow: hidden;
}

[data-beam="_r_2v_"][data-active] {
  animation:
    beam-spin-_r_2v_ 1.96s linear infinite,
    beam-fade-in-_r_2v_ 0.6s ease forwards;
}

[data-beam="_r_2v_"][data-fading] {
  animation:
    beam-spin-_r_2v_ 1.96s linear infinite,
    beam-fade-out-_r_2v_ 0.5s ease forwards;
}

[data-beam="_r_2v_"][data-active]::after,
[data-beam="_r_2v_"][data-fading]::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  padding: 1px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2v_),
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
      from var(--beam-angle-_r_2v_),
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
      from var(--beam-angle-_r_2v_),
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
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.33 * var(--beam-strength, 1));
  
}

[data-beam="_r_2v_"][data-active]::before,
[data-beam="_r_2v_"][data-fading]::before {
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
    from var(--beam-angle-_r_2v_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  -webkit-mask-composite: source-over;
  mask-image: conic-gradient(
    from var(--beam-angle-_r_2v_),
    transparent 0%, transparent 22%,
    rgba(255, 255, 255, 0.12) 28%, rgba(255, 255, 255, 0.4) 36%,
    white 46%, white 82%,
    rgba(255, 255, 255, 0.4) 88%, rgba(255, 255, 255, 0.12) 94%,
    transparent 97%, transparent 100%
  );
  mask-composite: add;
  pointer-events: none;
  z-index: 1;
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.46 * var(--beam-strength, 1));
  
}

[data-beam="_r_2v_"] [data-beam-bloom] {
  display: none;
  position: absolute;
  inset: 0;
  border-radius: 9998px;
  clip-path: inset(0 round 9999px);
  background: conic-gradient(
        from var(--beam-angle-_r_2v_),
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

[data-beam="_r_2v_"][data-active] [data-beam-bloom],
[data-beam="_r_2v_"][data-fading] [data-beam-bloom] {
  display: block;
  opacity: calc(var(--beam-opacity-_r_2v_) * 0.54 * var(--beam-strength, 1));
}

@keyframes beam-spin-_r_2v_ {
  to { --beam-angle-_r_2v_: 360deg; }
}

@keyframes beam-fade-in-_r_2v_ {
  to { --beam-opacity-_r_2v_: 1; }
}

@keyframes beam-fade-out-_r_2v_ {
  from { --beam-opacity-_r_2v_: 1; }
  to { --beam-opacity-_r_2v_: 0; }
}

LeetSort byAllMy SolutionPython3C++JavaPythonJavaScriptTypeScriptRustKotlinGoC#CScalaRubyDartSwiftPHPRacketElixirErlangDynamic ProgrammingBinary SearchSortingArrayHash TableHeap (Priority Queue)MemoizationRecursionBinary Indexed TreeOrdered MapRadix SortYour last submission beat 32% of other submissions' runtime.Share my solutionLeetCode・ Open・Sep 08, 2026Maximum Score of Non-overlapping IntervalsEditorial42.7K2Snapdragon・ Open・2 hours agoDynamic Programming + Binary Search + python | c++Binary SearchDynamic ProgrammingSortingPython2+209030Aura Farming・ Open・an hour agoᯓ★ Trust me it's not Hard! • (Take/Skip) DP Rec+Memo → Tab ⚡︎ • Easy Explanation!✈︎Hash TableBinary SearchDynamic ProgrammingPython2+123911Md Aarzoo Islam・ Open・an hour ago656ms | Beats 79.35% 👏 || Easy Approach and Step-by-Step Breakdown 💯🔥ArrayBinary SearchDynamic ProgrammingSorting6+101781An-Wen Deng・ Open・2 hours agoDP+binary search+(Radix) sort|beats 100%Binary SearchDynamic ProgrammingSortingRadix Sort1+6602Aryan Kumar Shaw Halwai・ Open・an hour agoBeats 100 % ✅ | No BS + Easy explanation With Breakdown💯 | DP (Rec +Memo)ArrayBinary SearchDynamic ProgrammingSorting1+4480Anirudh・ Open・3 hours agoDP + Binary Search | N log N | C++ Java Python ✅Binary SearchPythonC++Java57310EdgeCaseOffByOne・ Open・2 hours agoEasy Solution Explained with Intuition, Approach, Code and Time ComplexityArrayBinary SearchDynamic ProgrammingSorting1+3530RISHABH BABU・ Open・2 hours agoMax Weight of K Intervals (DP + Binary Search)ArrayBinary SearchDynamic ProgrammingSorting3+2340chaharharsh67・ Open・2 hours agoDP + Binary Search | Right-to-Left | O(N log N)Java2540Magudarena・ Open・3 hours agoDynamic Programming + Binary Search | All 19 Languages Included 🚀Dynamic ProgrammingCPythonC++6+21660Ayush Dalal・ Open・10 minutes ago🚀 Very Easy Java Solution | Maximum Score of Non-overlapping IntervalsArrayBinary SearchDynamic ProgrammingSorting1+120Prabhas Sharma・ Open・40 minutes ago3414. Maximum Score of Non-overlapping IntervalsPython31140Ankit Mohapatra・ Open・43 minutes agoEasy C++ Code || Simple For Beginners || Beats 100%ArrayBinary SearchDynamic ProgrammingSorting1+140Sagar Gupta・ Open・2 hours agoC++ | DP with Lex Tie-Break | O(n log n)ArrayBinary SearchDynamic ProgrammingSorting1+1200All SolutionsDynamic Programming + Binary Search + python | c++Snapdragon9042 hours agoBinary SearchDynamic ProgrammingSortingPython2+Intuition
The problem asks us to find up to 4 non-overlapping intervals that yield the maximum total weight. If there are multiple combinations with the same maximum weight, we must return the one whose indices are lexicographically smallest.
This problem is a variation of the classic "Weighted Job Scheduling" problem, which can be efficiently solved using Dynamic Programming (DP) and Binary Search. The core idea is to process intervals in increasing order of their end times and, for each interval, decide whether to include it or not.
Algorithm


Format and Sort the Intervals:
First, we append the original index to each interval so we don't lose track of it after sorting. We convert each interval to a structure containing (end, start, weight, originalIndex) and sort the array based on the end boundary in ascending order. Sorting by end time allows us to optimally find the latest interval that ends before the current one starts.


Define the DP State:
We use a 2D DP array dp of size (N + 1) x 5, where N is the total number of intervals.

dp[i][j] stores the optimal configuration considering the first i sorted intervals and selecting exactly j intervals (0≤j≤4).
To elegantly handle the conditions (maximize weight, then minimize lexicographical indices), we store the state as a tuple: (-totalWeight, sortedIndices). Finding the minimum (min()) of these tuples inherently prioritizes the largest total weight (because of the negative sign) and then tie-breaks using the lexicographically smallest list of indices.



DP Transitions:
We iterate through each interval at index i:

To find the optimal previous state if we decide to pick this interval, we need the latest interval that does not overlap. We can use binary search (bisect_left in Python, lower_bound in C++) to find the index k of the first interval whose end boundary is strictly greater than or equal to our start. Since intervals at index k and beyond overlap, the valid non-overlapping intervals are up to index k, which maps perfectly to dp[k].
For each count j from 1 to 4, we consider two choices:

Skip the current interval: The optimal result is identical to the result without this interval, dp[i][j].
Take the current interval: We add the current interval's weight to dp[k][j - 1]. We append the current originalIndex to the chosen indices and sort them.


We assign dp[i + 1][j] the optimal (minimum) choice between skipping and taking.



Result:
After checking all intervals, the overall optimal configuration for at most 4 intervals will be stored at dp[N][4]. We extract and return the list of indices from this state.



Implementation (Python)
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store as (end, start, weight, originalIndex) and sort by end boundary
        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        sortedIntervals.sort(key=lambda x: x[0])

        # dp[i][j] stores a tuple: (-max_weight, lexicographically_smallest_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]

        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):
            # Binary search to find the latest non-overlapping interval
            # bisect_left finds the first interval whose end >= current start
            k = bisect_left(sortedIntervals, (start,), hi=i)
            
            for j in range(1, 5):
                prevWeight, prevIndices = dp[k][j - 1]
                
                skip = dp[i][j]
                
                # min() naturally prioritizes the lowest (most negative) weight sum, 
                # then lexicographically smallest sorted indices
                takeWeight = prevWeight - weight
                takeIndices = sorted(prevIndices + [originalIndex])
                take = (takeWeight, takeIndices)
                
                dp[i + 1][j] = min(skip, take)

        return dp[-1][4][1]
Implementation (C++)
Because C++ compares std::pair and std::vector identically to Python (element by element), this exact trick ports over perfectly using pair<long long, vector<int>>.
class Solution {
    struct IntervalData {
        int end, start, weight, originalIndex;
        // Used for sorting and lower_bound comparisons
        bool operator<(const IntervalData& other) const {
            return end < other.end;
        }
    };

public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<IntervalData> sortedIntervals;
        
        for (int i = 0; i < n; ++i) {
            sortedIntervals.push_back({intervals[i][1], intervals[i][0], intervals[i][2], i});
        }
        sort(sortedIntervals.begin(), sortedIntervals.end());
        
        // dp[i][j] stores a pair: {-max_weight, lexicographically_smallest_indices}
        vector<vector<pair<long long, vector<int>>>> dp(n + 1, vector<pair<long long, vector<int>>>(5, {0LL, {}}));
        
        for (int i = 0; i < n; ++i) {
            int start = sortedIntervals[i].start;
            int weight = sortedIntervals[i].weight;
            int originalIndex = sortedIntervals[i].originalIndex;
            
            // lower_bound finds the first interval whose end >= current start
            IntervalData target = {start, 0, 0, 0}; 
            int k = lower_bound(sortedIntervals.begin(), sortedIntervals.begin() + i, target) - sortedIntervals.begin();
            
            for (int j = 1; j <= 4; ++j) {
                long long prevWeight = dp[k][j - 1].first;
                vector<int> prevIndices = dp[k][j - 1].second;
                
                pair<long long, vector<int>> skip = dp[i][j];
                
                vector<int> takeIndices = prevIndices;
                takeIndices.push_back(originalIndex);
                sort(takeIndices.begin(), takeIndices.end());
                
                pair<long long, vector<int>> take = {prevWeight - weight, takeIndices};
                
                // min() naturally prioritizes the lowest (most negative) weight sum, 
                // then lexicographically smallest sorted indices
                dp[i + 1][j] = min(skip, take);
            }
        }
        
        return dp[n][4].second;
    }
};

Complexity

Time Complexity: O(NlogN)

Formatting and sorting the intervals takes O(NlogN) time.
For each of the N intervals, we execute a binary search which takes O(logN) time.
The inner loop always runs 4 times. Inside it, sorting a list of maximum size 4 takes O(1) time. Thus, filling the DP array is O(NlogN).


Space Complexity: O(N)

The formatted array requires O(N) space.
The dp array has dimensions (N+1)×5, where each cell stores a numeric value and an array of at most 4 integers, consuming O(N) overall memory.


 PreviousMaximum Score of Non-overlapping IntervalsNextᯓ★ Trust me it's not Hard! • (Take/Skip) DP Rec+Memo → Tab ⚡︎ • Easy Explanation!✈︎Comments (0)Sort by:BestCommentNo comments yet.200Python3Auto111213109876543211415            for j in range(1, 5):                prevWeight, prevIndices = dp[k][j - 1]                                        k = bisect_left(sortedIntervals, (start,), hi=i)        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]        sortedIntervals.sort(key=lambda x: x[0])        (intervals)]        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:class Solution:                skip = dp[i][j]                takeWeight = prevWeight - weightSavedLn 2, Col 70AcceptedRuntime: 35 msCase 1Case 2Inputintervals =[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]Output[2,3]Expected[2,3]Contribute a testcaseInput912›[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]][[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]Output912›[2,3][1,3,5,6]Expected912›[2,3][1,3,5,6] All SubmissionsAccepted581 / 581 testcases passedMUTHU KUMAR Msubmitted at Sep 12, 2026 09:00AnalysisSolution👑 Unlock the Full LeetCode ExperienceCompany problems, Ask Leet, and expert editorials — all in one plan.Runtime1646msBeats32.20%Memory86.47MBBeats33.90%Created with Highcharts 11.1.01209ms1430ms1470ms1565ms1670ms2196ms0%2%4%
                  
                Created with Highcharts 11.1.01209ms1430ms1470ms1565ms1670ms2196msCodePython31class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
4        sortedIntervals.sort(key=lambda x: x[0])
5
6        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]
7
8        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):
9            k = bisect_left(sortedIntervals, (start,), hi=i)
10            
11            for j in range(1, 5):
12                prevWeight, prevIndices = dp[k][j - 1]
13                
14                skip = dp[i][j]
15                takeWeight = prevWeight - weight
16                takeIndices = sorted(prevIndices + [originalIndex])
17                take = (takeWeight, takeIndices)
18                
19                dp[i + 1][j] = min(skip, take)
20
21        return dp[-1][4][1]View more More challenges2054. Two Best Non-Overlapping Events0/5FindHeaderBarSizeFindTabBarSizeFindBorderBarSize

## Complexity

- **Time Complexity:** O(n) (Estimated / Problem dependent)
- **Space Complexity:** O(1) / O(n) (Estimated / Problem dependent)

> *Note: Complexity estimates are generated based on typical solutions. Always verify with actual submission implementation.*
