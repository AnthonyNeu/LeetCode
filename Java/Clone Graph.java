/*
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
*/


/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */

//DFS
public class Solution {
    private HashMap<Integer,UndirectedGraphNode> map= new HashMap<>();
    
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node == null) return node;
        return DFS(node);
    }
    
    private UndirectedGraphNode DFS(UndirectedGraphNode node){
        if(map.containsKey(node.label)) return map.get(node.label);
        UndirectedGraphNode copy = new UndirectedGraphNode(node.label);
        map.put(node.label,copy);
        for(UndirectedGraphNode neighbor:node.neighbors){
            copy.neighbors.add(DFS(neighbor));
        }
        return copy;
    }
}


//BFS
public class Solution {
    private HashMap<Integer,UndirectedGraphNode> map= new HashMap<>();
    
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node == null) return node;
        return BFS(node);
    }
    
    private UndirectedGraphNode BFS(UndirectedGraphNode node){
        if(map.containsKey(node.label)) return map.get(node.label);
        UndirectedGraphNode copy = new UndirectedGraphNode(node.label);
        map.put(node.label,copy);
        Queue<UndirectedGraphNode> q = new LinkedList<>();
        q.add(node);
        while(!q.isEmpty()){
            UndirectedGraphNode p = q.poll();
            for(UndirectedGraphNode neighbor:p.neighbors){
                if(map.containsKey(neighbor.label))
                    map.get(p.label).neighbors.add(map.get(neighbor.label));
                else{
                    q.add(neighbor);
                    UndirectedGraphNode neighborcopy = new UndirectedGraphNode(neighbor.label);
                    map.put(neighbor.label,neighborcopy);
                    map.get(p.label).neighbors.add(neighborcopy);
                }
            }
        }
        return copy;
    }
}