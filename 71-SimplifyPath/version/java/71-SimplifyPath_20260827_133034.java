// Last updated: 8/27/2026, 1:30:34 PM
1class Solution {
2    public int subarraysWithKDistinct(int[] nums, int k) {
3      
4        
5        return (total(nums,k)-total(nums,k-1));
6    }
7    private int total(int[]nums,int k){
8          int l=0;
9        int r=0;
10        int count=0;
11        HashMap<Integer,Integer>map = new HashMap<>();
12        while(r<nums.length){
13            map.put(nums[r],map.getOrDefault(nums[r],0)+1);
14            while(map.size() > k){
15                 map.put(nums[l], map.get(nums[l]) - 1);
16            if(map.get(nums[l]) == 0){
17                map.remove(nums[l]);
18                
19            }
20            l++;
21            }
22            count = count+(r-l+1);
23            r++;
24        }return count;
25    }
26}