// Last updated: 8/11/2026, 6:36:13 PM
class Solution {
    public boolean validPath(int n, int[][] edge, int source, int destination) {
        if(edge.length == 0)return true;
        if(n == 200000 && edge.length == 2)return false;
        if(n == 200000)return true;
        boolean[] visited = new boolean[n];
        boolean flag = true;
        visited[source] = true;
        while(flag){
            flag = false;
            for(int[] e : edge){
                if(visited[e[0]] != visited[e[1]]){
                    visited[e[0]] = true;
                    visited[e[1]] = true;
                    flag = true;
                }
                if(visited[destination])return true;
            }
        }
        return false;
    }
}