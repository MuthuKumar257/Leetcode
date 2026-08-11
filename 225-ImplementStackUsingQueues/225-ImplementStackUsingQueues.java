// Last updated: 8/11/2026, 6:46:25 PM
class MyStack {

    Queue<Integer> queue;

    public MyStack() {
        this.queue = new ArrayDeque<>();
    }
    
    public void push(int x) {

        queue.add(x);

        for (int i = 0; i < queue.size() - 1; i++) {
            queue.add(queue.poll());
        }
    }
    
    public int pop() {
        return queue.poll();
    }
    
    public int top() {
        return queue.peek();
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}
