import collections
c = 0
class Solution(object):
    def findOrder(self, numCourses, prerequisites,c):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            print(u,v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path,c):
                return []
        return path
    
    def dfs(self, graph, visited, i, path,c):
        print('c:%d'% c)
        c += 1
        print('i:%d' % i)
        print('path')
        print(path)
        
        print(visited)
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path,c):
                return False
        visited[i] = 2
        path.append(i)
        return True
numCourses = 4
prerequisites = [[2,3],[1,2],[0,1]]
s = Solution()
path = s.findOrder(numCourses, prerequisites,c)
print(path)