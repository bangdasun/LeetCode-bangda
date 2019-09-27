
from collections import deque

class Solution:
    def get_prerequisites(self, numCourses, prerequisites):
        prerequisites_to_course = {course : [] for course in range(numCourses)}
        prerequisites_count = {course: 0 for course in range(numCourses)}
        
        # course = [course, prerequisite]
        for courses in prerequisites:
            prerequisites_to_course[courses[1]].append(courses[0])
            prerequisites_count[courses[0]] += 1
        
        return prerequisites_to_course, prerequisites_count

    def canFinish(self, numCourses, prerequisites):
        prerequisites_to_course, prerequisites_count = self.get_prerequisites(numCourses, prerequisites)
        
        queue = deque([course for course in range(numCourses) if prerequisites_count[course] == 0])
        course_count = 0
        
        while len(queue) > 0:
            prerequisite = queue.popleft()
            course_count += 1
            for course in prerequisites_to_course[prerequisite]:
                prerequisites_count[course] -= 1
                if prerequisites_count[course] == 0:
                    queue.append(course)
                
        return course_count == numCourses

# better commented / neat solution
class Solution:
    def get_prerequisite(self, numCourses, prerequisites):
		# this function constructs the graph
		# prerequisites_to_course is a graph with
		# prerequisite -> [next courses list]
        prerequisites_to_course = {course: [] for course in range(numCourses)}
        prerequisites_count = {course: 0 for course in range(numCourses)}
        
        for curr, prev in prerequisites:
            prerequisites_to_course[prev].append(curr)
            prerequisites_count[curr] += 1
            
        return prerequisites_to_course, prerequisites_count
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_to_course, prerequisites_count = self.get_prerequisite(numCourses, prerequisites)
        queue = deque([course for course in prerequisites_count if prerequisites_count[course] == 0])
        course_count = 0
        
        while len(queue) > 0:
            course = queue.popleft()
            course_count += 1
            for next_course in prerequisites_to_course[course]:
                prerequisites_count[next_course] -= 1
                if prerequisites_count[next_course] == 0:
                    queue.append(next_course)
        
        return course_count == numCourses