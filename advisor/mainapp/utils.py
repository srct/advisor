from mainapp.models import Course, Semester, Trajectory # import more

### common functionality

def programCourses(program):

    courses = []
    requirements = program.requirements
    for requirement in requirements:
        for coursegroup in requirement.coursegroup:
            for course in coursegroup.courses:
                courses.append(course)

    return courses

def genDepTree(course):
    toscan = []
    courseset = set(course)
    for prerequisite in course.prerequisites:
        toscan.add(course)
    for corequisite in course.corequisites:
        toscan.add(course)

    for elem in toscan:
        recursiveDepTree(elem, courseset)

def recursiveDepTree(course, courseset):
    toscan = []
    courseset.add(course)
    for prerequisite in course.prerequisites:
        toscan.append(course)
    for corequisite in course.corequisites:
        toscan.append(course)

    if len(toscan) == 0:
        return
    for elem in toscan:
        if elem not in courseset:
            recursiveDepTree(elem, courseset)

### creating a trajectory

#def maxProgramsAllowed():
#    """ the maximum programs allowed, e.g. 2 majors and 3 minors tops """
#   return True

### automatically building a trajectory

def assignedWeights(weightedCourse, programCourses):
    """ assign weights to all courses in a program for automation """

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

        weights[weightedCourse] = weightedCourseCounter

    return weights

def courseWeighting(programCourses):
    """ a helper function for properly recursing """

    weights = {}

    weightedCourse = programCourses[0]

    assignedWeights(weightedCourse, programCourses)

    return weights    

def customAssignedWeights(weights, selectedCourses):
    """ remove courses that a student has not selected from the weighted
        courses """
    customweights = weights

    for course in selectedCourses:
        del customweights[course]

    return customweights

### editing a trajectory

def requirementsFulfilled(taken, program):
    """ for *A* program, return a list of all requirements fulfilled """

    fulfilled = []
    taken = set(taken)
    requirements = program.requirements

    for requirement in requirements:
        for coursegroup in requirement.coursegroup:
            courseRequirements = set(coursegroup.courses)
            requirementCoursesTaken = courseRequirements.intersection(alreadyTaken)

            if len(requirementCoursesTaken) is requirement.coursegroup.numneeded:
                fulfilled.append(requirement)
    
    # this should return true or false
    return fulfilled


#def alreadyTaken():
#    """ return all of the courses that a student has already taken so far
#        in the trajectory """
#    return True

def remainingReqCourses(taken, programCourses):
    """ returns the remaining required courses for a program given
    the already taken courses """

    taken = set(taken)
    programCourses = set(programCourses)

    remainingReqCourses = programCourses.difference(taken)

    return remainingReqCourses

def nextCourses(remainingReqCourses, taken):
    """ which courses you can take next based on prereqs and coreqs, given
        already taken courses and remaining required courses """
    nextcourses = []
    for course in remainingReqCourses:
        reqs = set()
        for prereq in course.preq:
            reqs.add(prereq)
        #for coreq in course.coreq:
        #    reqs.add(coreq)
        for req in reqs:
            if req in taken:
                nextcourses.append(course)


    return nextCourses

# IMPLEMENT THIS IN JS!
#def maxCreditsAllowed():
#    """ the maximum credits allowed for a semester-- returns different values
#        to warn or disallow if maximum credits are touched or exceeded """

def findDependencies(deletedCourse, semester):
    """ if a student removes a course while editing, find all courses
        that have require the removed courses """
    foundDependencies = []
    for suspectCourse in semester.nextSemester.courses:
        reqs = set()
        for prereq in suspectCourse.preq:
            if prereq is deletedCourse:
                reqs.append(foundDependencies)
        for coreq in suspectCourse.coreq:
            if coreq is deletedCourse:
                reqs.append(foundDependencies)

    findDependencies(deletedCourse, semester.nextSemester)

    return foundDependencies

def enoughCredits(previousCourses, numRequired):
    """ checks if enough credits have been taken to graduate """
    enoughcredits = False
    numTaken = 0
    for course in previousCourses:
        numTaken += course.credits
    
    if numTaken >= numRequired:
        enoughcredits = True

    return enoughcredits


def genTrajectories(taken, programs, user):
    tj = Trajectory(user=user, semesters=[])
    taken = set(taken)
    sem = Semester(number=0, user=user, courses=taken,
        programs=programs)
    tj.semesters.append(sem)
    programCourses = []
    for program in programs:
        programcourses+=programCourses(program)
    remainingCourses=remainingReqCourses(taken, programCourses)
    while True:
        availableCourses=nextCourses(remainingCourses, taken)
        semclasses=[]
        for i in xrange(5):
            doneclass = availableCourses.pop()
            semclasses.append(doneclass)
            taken.add(doneclass)
        newsem = Semester(number=sem.number+1, user=user, courses=semclasses,
            programs=programs)
        tj.semesters.append(sem)
        sem = newsem
        
        failed=False
        for program in programs:
            if requirementsFulfilled(program, taken) != program.requirements:
                failed=True
        if not failed:
             break
    return tj
            
    


'''def generatedTrajectory(taken, programs, user):
    
    tj = Trajectory(user=user, semesters=[])
    programCourses = []
    # get the course's programs
    for program in programs:
        programCourses.append(programCourses( program ))

    # find the weights of all of the programs
    courseWeighting( programCourses )

    while len(remainingReqCourses) > 0:
        courseWeighting(programCourses)

        # get the courses you have to take next
        remainingReqCourses( taken, programCourses )
        requirementsFulfilled( taken, program )
        nextCourses( remainingReqCourses, taken )
        # TODO: pick five highest-weighted
        #
        nextsem = Semester(number=len(tj.semesters)+1, user=user,
            courses=semcourses, programs=program, 


    # of those, pick five of the heaviest
    ### IMPLEMENT THIS

    # associate courseWeights with nextCourses
    courseWeighting(nextCourses()
    # add a list of courses with the five highest weights from nextCourses to
    # generated Trajectory
    # add these new courses to taken

    # retrieve the next courses you need to take, and so forth
    remainingReqCourses()
    requirementsFulfilled()
    nextCourses()

    # if there are no remainingReqCourses or requirementsFulfilled is True

    # do you have enough credits?
    enoughCredits()

    # hooray!
    return generatedTrajectory
'''
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
