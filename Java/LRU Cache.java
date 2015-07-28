/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
*/



public class LRUCache {
    private class Node{
        int key;
        int value;
        Node prev;
        Node next;
        
        public Node(int key, int value){
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }
    
    private int capacity;
    private Map<Integer,Node> map = new HashMap<>();
    private Node head = new Node(-1,-1);
    private Node tail = new Node(-1,-1);
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    private void move_to_tail(Node cur){
        cur.prev = tail.prev;
        tail.prev = cur;
        cur.prev.next = cur;
        cur.next = tail;
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){
            return -1;
        }
        
        Node cur = map.get(key);
        cur.prev.next = cur.next;
        cur.next.prev = cur.prev;
        
        //move to tail
        move_to_tail(cur);
        
        return cur.value;
    }
    
    public void set(int key, int value) {
        if(get(key) != -1){
            map.get(key).value = value;
            return;
        }
        
        if(map.size() == capacity){
            map.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }
        
        Node insert = new Node(key, value);
        map.put(key, insert);
        move_to_tail(insert);
    }
}