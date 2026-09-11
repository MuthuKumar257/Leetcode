// Last updated: 9/11/2026, 9:47:24 AM
class Solution {
    public String simplifyPath(String path) {
        String[] components = path.split("/");
        Stack<String> st = new Stack<>();

        for (String comp : components) {
            if (comp.equals("") || comp.equals(".")) {
                continue;
            }

            if (comp.equals("..")) {
                if (!st.isEmpty()) {
                    st.pop();
                }
            } else {
                st.push(comp);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!st.isEmpty()) {
            sb.insert(0, "/" + st.pop());
        }

        return sb.length() == 0 ? "/" : sb.toString();        
    }
}