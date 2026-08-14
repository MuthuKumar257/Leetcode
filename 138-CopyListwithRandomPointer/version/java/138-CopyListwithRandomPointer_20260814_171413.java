// Last updated: 8/14/2026, 5:14:13 PM
1/*
2// Definition for a Node.
3class Node {
4    int val;
5    Node next;
6    Node random;
7
8    public Node(int val) {
9        this.val = val;
10        this.next = null;
11        this.random = null;
12    }
13}
14*/
15
16class Solution {
17    public Node copyRandomList(Node head) {
18        // Map to keep track of the link between original nodes and cloned nodes 🗺️
19        Map<Node, Node> hashMap = new HashMap<>();
20        Node curr = head;
21
22        // Step 1: Create deep-copied shells of all nodes and catalog them 🖨️
23        while (curr != null) {
24            hashMap.put(curr, new Node(curr.val));
25            curr = curr.next; 
26        }
27
28        curr = head;
29        // Step 2: Loop back through to wire up next and random pointers securely 🪡
30        while (curr != null) {
31            Node cp = hashMap.get(curr);
32            
33            // Set pointers using mapped values
34            cp.next = hashMap.get(curr.next);
35            cp.random = hashMap.get(curr.random);
36            
37            curr = curr.next;
38        } 
39        
40        // Return the cloned head node
41        return hashMap.get(head);
42    }
43}