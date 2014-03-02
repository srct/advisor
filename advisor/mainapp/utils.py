from mainapp.models import Course # import more

### common functionality

def programCourses(program):

    programCourses = []
    requirements = program.requirements
    for requirement in requirements:
        for coursegroup in requirement.coursegroup:
            for course in coursegroup.courses:
                programCourses.append(course)

    return programCourses

### creating a trajectory

#def maxProgramsAllowed():
#    """ the maximum programs allowed, e.g. 2 majors and 3 minors tops """
#   return True

### automatically building a trajectory

def assignedWeights(weightedCourse, programCourses):
    """ assign weights to all courses in a program for automation """
    assignedWeights = {}

    for weightedCourse in programCourses:
        weightedCourseCounter = 0
        reqs = set()
        for prereq in weightedCourse.preq:
            reqs.add(prereq)
        for coreq in weightedCourse.coreq:
            reqs.add(coreq)
        for req in reqs:
            for course in programCourses:
                childReqList = []
                if req is course:
                    weightedCourseCounter += 1
                    childReqList.append(course)
                    assignedWeights(course, childReqList)
                
        assignedWeights[weighedCourse] = coursecounter
        
    return assignWeights

def customAssignedWeights(assignedWeights, selectedCourses):
    """ remove courses that a student has not selected from the weighted
        courses """
    customAssignedWeights = assignedWeights

    for course in selectedCourses:
        del customAssignedWeights[course]

    return customAssignedWeights

def shortestPath(assignedWeights):
    return True

### editing a trajectory

def requirementsFulfilled(alreadyTaken, program):
    """ for *A* program, return a list of all requirements fulfilled """

    requirementsFulfilled = []
    alreadyTaken = set(alreadyTaken)
    requirements = program.requirements

    for requirement in requirements:
        for coursegroup in requirement.coursegroup:
            courseRequirements = set(coursegroup.courses)
            requirementCoursesTaken = intersection(courseRequirements, alreadyTaken)
        
            if len(requirementCoursesTaken) is requirement.coursegroup.numneeded:
                requirementsFulfilled.append(requirement)

    return requirementsFulfilled

#def alreadyTaken():
#    """ return all of the courses that a student has already taken so far
#        in the trajectory """
#    return True

def remainingReqCourses(alreadyTaken, program):
    """ returns the remaining required courses for a program given
    the already taken courses """

    alreadyTaken = set(alreadyTaken)
    programCourses = set( programCourses(program) )

    remainingReqCourses = intersection(alreadyTaken, programCourses)

    return remainingReqCourses

def nextCourses(remainingReqCourses, alreadyTaken):
    """ which courses you can take next based on prereqs and coreqs, given
        already taken courses and remaining required courses """
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

def allTrajectories(topSemester):
    """ returns all paths to each end node of a trajectories tree
        for the user page, do this over all trees """
    # traverse the tree

    # find the end leafs

    # find the shortest path to each leaf

    # add the list of that semesters to the allTrajectories list
    
    # return said list of lists

    #endLeafs = []
    #for
    allTrajectories  = []
    #for
    #    singleTrajectory = []
    #    singleTrajectory.append(semester)
    #    allTrajectories.append(singleTrajectory)

    return allTrajectories
