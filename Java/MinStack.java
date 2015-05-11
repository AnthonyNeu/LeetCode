/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
*/

//O(n) time, O(n) space
class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();
    
    public void push(int x) {
        stack.push(x);
        if(minStack.isEmpty()|| minStack.peek() >= x)
            minStack.push(x);
    }

    public void pop() {
        if((stack.pop()).equals(minStack.peek())) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}

//O(n) time, O(1) space
class MinStack {
    private Stack<Long> stack = new Stack<>();
    private long min = 0;
    
    public void push(int x) {
        if(stack.isEmpty()){
            min = x;
            stack.push((long)0);
        }
        else{
            if(x < min){
                stack.push((long)(x-min));
                min = x;
            }
            else
                stack.push((long)(x-min));
        }
    }

    public void pop() {
        if(stack.peek() < 0){
            min = min  - stack.pop();
        }
        else
            stack.pop();
    }

    public int top() {
        if(stack.peek() < 0){
            return (int)min;
        }
        else
            return (int)(min + stack.peek());
    }

    public int getMin() {
        return (int)min;
    }
}