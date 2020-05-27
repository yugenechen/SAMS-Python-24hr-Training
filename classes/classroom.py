# -*- coding: utf-8 -*-
"""
SAMS Python 2.7, Chapter 17, p 189

Created on Sat May 09 09:26:26 2020

@author: Lifygen
"""


class Classroom(object):
    '''
    Classroom ojbect that holds students and their assigned room#.
    INPUTS:
        \t   room_numbers= text string object, name of the classroom.
        \n\t students = list of students.  If one student is entered
        /n/t            as a str then the student is added to the list.
    OUTPUTS:
        \t   none.
    METHODS:
        \t   get_JSON_dict - produce and returns a dictionary containing
        \n\t                 a dictionary for each student that contains
        \n\t                 the student.
        \t\n ShowMe()      - prints each classroom with its lists of
        \t\n            students.
    '''
    def __init__(self,
                 room_number="",
                 students=[],
                 ):
        self.room_number = room_number
        self.students = students
        #self.d = {}

    def get_JSON_dict(self):
        d = vars(self)
        myList = self.students
        stuList = []
        for person in myList:
            stuList.append(vars(person))
        d['students'] = stuList
        #self.d = d
        return d


# Example from the SAMS Python Ch 17 putting two classes in one file.
class Student(object):
    '''
    Student ojbects hold names and grades students and their assigned room#.
    INPUTS:
        \t   name  = text string, student name.
        \n\t grade = the grade year of the student (k-12; not letter grade).
        /n/t            as a str then the student is added to the list.
    OUTPUTS:
        \t   none.
    METHODS:
        \t   ShowMe() - prints each classroom with its lists of
        \t              students.
    '''
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

