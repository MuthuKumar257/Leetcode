/*
 * LeetCode: Valid Parentheses
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/valid-parentheses/
 */

class Solution {
    public boolean isValid(String s) {
        Stack<Character> par=new Stack<>();
        for(int i=0;i<s.length();i++){
            if (s.charAt(i)=='('|| s.charAt(i)=='['||s.charAt(i)=='{'){
                par.push(s.charAt(i));
            }
            if (s.charAt(i)==')'|| s.charAt(i)==']'||s.charAt(i)=='}'){
                if(par.isEmpty()) return false;

                    Character temp=par.pop();
                    if(s.charAt(i)==')' && temp!='('){
                        return false;
                    }
                    if(s.charAt(i)==']' && temp!='['){
                        return false;
                    }
                    if(s.charAt(i)=='}' && temp!='{'){
                        return false;
                    }
                
            }
            
        }
        return par.isEmpty();
    }
}
