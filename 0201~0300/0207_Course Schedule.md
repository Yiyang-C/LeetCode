# 207. Course Schedule
## Medium
### Depth-first Search/Breadth-first Search/Graph/Topological Sort
Relative: 210, 261, 310, 630
#

There are a total of ```numCourses``` courses you have to take, labeled from ```0``` to ```numCourses-1```.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: ```[0,1]```

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

Example1:
> Input: numCourses = 2, prerequisites = [[1,0]]
> 
> Output: true
>
> Explanation: There are a total of 2 courses to take. 
>
> To take course 1 you should have finished course 0. So it is possible.

Example2:
> Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
> 
> Output: false
>
> Explanation: There are a total of 2 courses to take. 
>
> To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Constraints:** 
* The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
* You may assume that there are no duplicate edges in the input prerequisites.
* ```1 <= numCourses <= 10^5```

<details><summary>Hint1</summary>
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
</details>

<details><summary>Hint2</summary>
[Topological Sort via DFS](https://www.coursera.org/specializations/algorithms) - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
</details>

<details><summary>Hint3</summary>
Topological sort could also be done via [BFS](https://en.wikipedia.org/wiki/Topological_sorting#Algorithms).
</details>

**My Note:**
* Construct the graph with directed edge pointed from prerequisites course to target course
* Record the #prerequisites of each course
* Do Topological sorting (using deque to store the parent nodes everytime)

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_graph = collections.defaultdict(list)
        degree_cnt = collections.defaultdict(int)
        
        for course, pre in prerequisites:
            pre_graph[pre].append(course)
            degree_cnt[course] += 1
        
        dq = collections.deque()
        topo_res = []
        
        for n in range(numCourses):
            if n not in degree_cnt:
                dq.append(n)
                
        if not dq:
            return False
        
        while dq:
            pre = dq.popleft()
            for course in pre_graph[pre]:
                degree_cnt[course] -= 1
                if degree_cnt[course] == 0:
                    dq.append(course)
            topo_res.append(pre)
            
        if len(topo_res) == numCourses:
            return True
        return False
```
