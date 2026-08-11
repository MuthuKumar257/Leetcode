// Last updated: 8/11/2026, 6:51:24 PM
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