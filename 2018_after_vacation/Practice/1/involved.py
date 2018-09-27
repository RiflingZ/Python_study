# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                 }
    }


def involvede(courses, person):
    output = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            for key in courses[hexamester][course]:
                if courses[hexamester][course][key] == person:
                    if hexamester in output:
                        output[hexamester].append(course)
                    else:
                        output[hexamester] = [course]
    return output


def involved(courses, person):
    res = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            for key in courses[hexamester][course]:
                if courses[hexamester][course][key] == person:
                    if hexamester in res:
                        res[hexamester].append(course)
                    else:
                        res[hexamester] = [course]
    return res


print(involved(courses, 'Dave'))
# >>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

# print(involved(courses, 'Peter C.'))
# >>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

# print(involved(courses, 'Dorina'))
# >>> {'jan2044': ['cs001']}

# print(involved(courses, 'Peter'))
# >>> {}

# print involved(courses, 'Robotic')
# >>> {}

# print involved(courses, '')
# >>> {}

