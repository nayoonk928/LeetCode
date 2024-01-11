class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(list)
        prerequisite_cnt = [0] * num_courses
    
        for p in prerequisites:
            course, prerequisite_course = p[0], p[1]
            course_graph[prerequisite_course].append(course)
            prerequisite_cnt[course] += 1
    
        # 선행과목 수가 0인 노드를 큐에 추가
        queue = deque(course for course in range(num_courses) if prerequisite_cnt[course] == 0)

        while queue:
            current_course = queue.popleft()
            num_courses -= 1
    
            # 현재 코스를 들어면 수강할 수 있는 과목 확인
            for adj in course_graph[current_course]:
                prerequisite_cnt[adj] -= 1
                if prerequisite_cnt[adj] == 0:
                    queue.append(adj)
    
        return num_courses == 0