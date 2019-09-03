
from collections import deque

class Solution:
    def get_prerequisites(self, numCourse, prerequisites):
        prerequisites_to_courses = {course: [] for course in range(numCourse)}
        prerequisites_count = {course: 0 for course in range(numCourse)}
        
        for courses in prerequisites:
            prerequisites_to_courses[courses[1]].append(courses[0])
            prerequisites_count[courses[0]] += 1
        
        return prerequisites_to_courses, prerequisites_count
    
    def findOrder(self, numCourses, prerequisites):
        prerequisites_to_courses, prerequisites_count = self.get_prerequisites(numCourses, prerequisites)
        
        queue = deque([course for course in range(numCourses) if prerequisites_count[course] == 0])
        course_list = []
        
        while len(queue) > 0:
            prerequisite = queue.popleft()
            course_list.append(prerequisite)
            for course in prerequisites_to_courses[prerequisite]:
                prerequisites_count[course] -= 1
                if prerequisites_count[course] == 0:
                    queue.append(course)
        
        if len(course_list) == numCourses:
            return course_list
        
        return []