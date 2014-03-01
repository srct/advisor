from mainapp.models import Course # import more

# creating a trajectory

def maxProgramsAllowed():
    """ the maximum programs allowed, e.g. 2 majors and 3 minors tops """
    return True

# automatically building a trajectory

# editing a trajectory

def requirementFulfilled():
    """ yikes! I don't know how to do this, but I need to set whether
        requirements are already fulfilled... this is a HUGE issue """
    return True

def remainingReqCourses():
    """ returns the remaining required courses given previous courses taken """
    return True

def previousCourses():
    """ return all of the courses that a student has already taken so far
        in the trajectory """
    # it would unfortunately be really hard for this to be saved somewhere
    return True

def nextCourses():
    """ which courses you can take next based on prereqs and coreqs, given
        previous courses and remaining required courses """
    return True

def maxCreditsAllowed():
    """ the maximum credits allowed for a semester-- returns different values
        to warn or disallow if maximum credits are touched or exceeded """

def findDependancies():
    """ if a student removes a course while editing, find all courses
        that have require the removed courses """
    return True

def enoughCredits():
    """ checks if enough credits have been taken to graduate """
    return True

# student page

def trajectoryEnds():
    """ returns all paths to each end node of the trajectories tree """
    return True
    
