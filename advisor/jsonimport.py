# Make sure to run export DJANGO_SETTINGS_MODULE="advisor.settings"
import json
import unicodedata
from mainapp.models import Course

json_data=open('all_course_data.json')
data = json.load(json_data)
year=20132014
#for course in data:
#    dept = course['subject']
#    courseid = course['course']
#    title = course['title']
#    desc = course['description']
#    credits = course['credits']
#    uniqname = '%s%s%s' % (dept, courseid, year)
#    print("Creating %s %s entry" % (dept, courseid))
#    djangocourse = Course(title=title, description=desc, credits=credits,
#        dept=dept, courseid=courseid, catalogyear=year, uniqname=uniqname)
#    djangocourse.save()

print("Entries added, beginning prereq/coreq pass")
for course in data:
    uniqname = '%s%s%s' % (course['subject'], course['course'],
        year)
    djangocourse = Course.objects.get(uniqname=uniqname)
    print("Adding prereqs for %s %s" % (course['subject'], course['course']))
    if 'prerequisites' in course.keys():
        for prereq in course['prerequisites']:
            try:
                prerequniq = '%s%s%s' % (prereq['subject'], prereq['course'],
                    year)
                prereqcourse = Course.objects.get(uniqname=prerequniq)
                print(">> Adding prereq %s %s" % (prereq['subject'], prereq['course']))
                djangocourse.prerequisites.add(prereqcourse)
            except:
                continue
    if 'corequisites' in course.keys():
        for coreq in course['corequisites']:
            try:
                corequniq = '%s%s%s' % (coreq['subject'], coreq['course'],
                    year)
                coreqcourse = Course.objects.get(uniqname=corequnique)
                print(">> Adding coreq %s %s" % (coreq['subject'], coreq['course']))
                djangocourse.corequisites.add(coreqcourse)
            except:
                continue
    djangocourse.save()
