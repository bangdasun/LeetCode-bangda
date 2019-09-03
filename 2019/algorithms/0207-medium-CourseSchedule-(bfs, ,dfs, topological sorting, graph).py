
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
