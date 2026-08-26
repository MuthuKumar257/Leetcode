// Last updated: 8/26/2026, 10:27:28 PM
1class Solution {
2    public String shortestBeautifulSubstring(String s, int k) {
3       String ans ="";
4       int n = s.length();
5       int min = Integer.MAX_VALUE;
6
7       for(int i = 0; i < n; i++){
8        String temp ="";
9        int len = 0;
10        
11        int c = 0;
12
13        for(int j = i; j < n; j++){
14            char ch = s.charAt(j);
15            temp += ch;
16
17            if(ch == '1')
18            c++;
19            
20            len = j - i +1;
21            
22            if(c==k){
23                
24            if(min > len){
25                min = len;
26                ans = temp;
27            }
28            else if( len == min && temp.compareTo(ans)<0)
29                ans = temp;
30
31                break;
32            }
33
34         }
35       } 
36
37
38       return ans;
39    }
40}