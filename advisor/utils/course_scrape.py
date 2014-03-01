import re
import json
import requests
from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=2)
all_data = []

def scrape(course_soup):
    # Extract relevant data from a course into a dict
    crs_data = {}

    # The title string is the first passed in element. It contains subject,
    # course, and title data in a format like this:
    # CS 650 - Advanced Database Management
    titlePattern = r"(?P<sub>[A-Z]+) (?P<crs>\d{3}) - (?P<title>.+)"
    m = re.match(titlePattern, course_soup.string)
    crs_data['subject'], course, crs_data['title'] = m.groups()
    crs_data['course'] = int(course)

    if crs_data['course'] >= 500:
        return

    # The next sibling element is a string containing the course's credits:
    # Credits: 3 (RT)
    credit_string = course_soup.nextSibling.string.lstrip()
    creditsPattern = r"Credits: (?P<cred>\d+)"
    m = re.match(creditsPattern, credit_string)
    if m:
        crs_data['credits'] = int(m.group('cred'))

    # The text after the "hr" element contains the course description
    course_soup = course_soup.find_next('hr')
    m = re.match(r".+\s*(?=Prerequisite\(s\))", course_soup.text)
    crs_data['description'] = m.group() if m else course_soup.text

    # Find all prerequsite courses
    course_soup = course_soup.find_next('br')
    m = re.search(r"Prerequisite\(s\).*\.", course_soup.text)
    if m:
        # Extract the prereqs and split them from the coreq section
        preReqText = m.group(0).split("Corequisite")[0]
        preReqPattern = r"(?P<sub>[A-Z]{2,4}) (?P<crs>\d{3})"
        preReqs = re.findall(preReqPattern, preReqText)

        # Extract some of the strangely formatted pre reqs
        m = re.findall(r"(?<!...)[A-Z]{2,4} \d{3},[a-z0-9,\s]*\d{3}", preReqText);
        preReqPattern = r"(?P<sub>[A-Z]{2,4}),.*(?P<crs>\d{3}"
        for text in m:
            sub = re.search(r"[A-Z]{2,4}", text).group();
            crss = re.findall(r"\d{3}", text);
            for crs in crss:
                preReqs.append((sub, crs))

        # Remove duplicates
        preReqs = list(set(preReqs))
        preReqs = [{'course': int(crs), 'subject': sub} for sub, crs in preReqs]
        crs_data['prerequisites'] = preReqs

    # Find corequsite courses
    m = re.search(r"Corequisite\(s\).*\.", course_soup.text)
    if m:
        coReqText = m.group(0)
        coReqPattern = r"(?P<sub>[A-Z]{2,4}) (?P<crs>\d{3})"
        coReqs = re.findall(coReqPattern, coReqText)
        coReqs = list(set(coReqs))
        coReqs = [{'course': int(crs), 'subject': sub} for sub, crs in coReqs]
        crs_data['corequisites'] = coReqs
    pp.pprint(crs_data)

    all_data.append(crs_data)

def get_page(page_num):
    url = (
    "http://catalog.gmu.edu/content.php?catoid=22&navoid=4550&expand=1&cpage={}".format(page_num))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    courses = soup.find_all('h3')
    for course in courses:
      scrape(course)

def main():
    # Fetch 68 pages of course data
    for i in range(1, 69):
        get_page(i)
    with open('data.json', 'w') as outfile:
          json.dump(all_data, outfile, indent=2)

if __name__ == "__main__":
  main()
