from mainapp.models import Course # import more

### creating a trajectory

#def maxProgramsAllowed():
#    """ the maximum programs allowed, e.g. 2 majors and 3 minors tops """
#   return True

### automatically building a trajectory

#def someautomaticfunction():

### editing a trajectory

def requirementFulfilled():
    """ is this handled in the models? if a requirement if fulfilled, then don't look at thoses classes again """
    return True

# add to a list of requirements filled

def remainingReqCourses():
    """ returns the remaining required courses given previous courses taken """

    return True

def previousCourses():
    """ return all of the courses that a student has already taken so far
        in the trajectory """
    # it would unfortunately be really hard for this to be saved somewhere
    return True

def nextCourses(remainingReqCourses, previousCourses):
    """ which courses you can take next based on prereqs and coreqs, given
        previous courses and remaining required courses """
    nextCourses = []
    for course in remainingReqCourses:
        reqs = set()
        course.prereq.append(reqs)
        course.coreq.append(reqs)
        for req in reqs:
            if req in previousCourses:
                nextCourses.append(course)

    return nextCourses

# IMPLEMENT THIS IN JS!
#def maxCreditsAllowed():
#    """ the maximum credits allowed for a semester-- returns different values
#        to warn or disallow if maximum credits are touched or exceeded """

def findDependancies(deletedCourse, semester):
    """ if a student removes a course while editing, find all courses
        that have require the removed courses """
    foundDependancies = []
    for suspectCourse in semester.nextSemester.courses:
        reqs = set()
        suspectCourse.prereq.append(reqs)
        suspectCourse.coreq.append(reqs)
            for req in reqs:
                if req is deletedCourse:
                    req.append(foundDependancies)

    findDependancies(deletedCourse, semester.nextSemester)

    return foundDependancies

def enoughCredits(previousCourses, numRequired):
    """ checks if enough credits have been taken to graduate """
    enoughCredits = False
    numTaken = 0
    for course in previousCourses:
        numTaken += course.credits
    
    if numTaken >= numRequired:
        enoughCredits = True

    return enoughCredits

### student page

def trajectoryEnds():
    """ returns all paths to each end node of the trajectories tree """
    return True
