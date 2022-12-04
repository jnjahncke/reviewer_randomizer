## ---------------------------- ##
## Load packages                ##
## ---------------------------- ##
from random import randrange
from math import floor
import re


## ---------------------------- ##
## Define function              ##
## ---------------------------- ##

def assign_reviewer(reviewers, applicants, eyes):

    reviewers = reviewers.replace("\t", " ").split("\n")
    applicants = applicants.replace("\t"," ").split("\n")

    reviewers = [x.rstrip().lstrip() for x in reviewers]
    applicants = [x.rstrip().lstrip() for x in applicants]

    ## ---------------------------- ##
    ## Calculate assignment lengths ##
    ## ---------------------------- ##
    reviewer_num = len(reviewers)
    applicant_num = len(applicants)
    min_num = floor(applicant_num * eyes / reviewer_num)
    remainder = (applicant_num * eyes) % reviewer_num
    # how many reviewers will be assigned the max_num, how many min_num?
    assign_max = remainder
    assign_min = reviewer_num - remainder

    ## ---------------------------- ##
    ## Build up empty lists/dicts   ##
    ## ---------------------------- ##
    reviewer_counts = {} # keep track of how many students each reviewer is assigned
    reviewer_dict = {} # keep a list of each applicant assigned to each reviewer
    reviewer_list = [] # list of all reviewers
    faculty_list = [] # subset list of faculty reviewers
    trainee_list = [] # subset list of trainee (non-faculty) reviewers
    
    # parse reviewer names, roles; build up reviewer lists/dictionaries
    for reviewer in reviewers:
        # parse name, role
        for found in re.finditer(r"^([\S\s]+)\s(\S+)$",reviewer):
            reviewer_counts[found.group(1).rstrip()] = 0
            reviewer_dict[found.group(1).rstrip()] = []
            reviewer_list.append(found.group(1).rstrip())
            # assign to faculty_list or trainee_list
            if found.group(2).lower().lstrip().rstrip() == "faculty":
                faculty_list.append(found.group(1).rstrip())
            else:
                trainee_list.append(found.group(1).rstrip())

    # assign reviewer to either be assigned the max or min number of applicants
    # based on calculations above
    max_list = reviewer_list[:assign_max]
    min_list = reviewer_list[assign_max:]
    
    applicant_dict = {} # keep a list of each reviewer assigned to each applicant
    applicant_counts = {} # keep track of how many reviewers have been assigned
    for applicant in applicants:
        applicant_counts[applicant] = 0
        applicant_dict[applicant] = []

    ## ------------------------------ ##
    ## Assign applicants to reviewers ##
    ## ------------------------------ ##
    
    # trainees first
    i = 0
    for trainee in trainee_list:
        rev_list = []
        if trainee in min_list:
            assign_num = min_num
        elif trainee in max_list:
            assign_num = min_num + 1
        while len(reviewer_dict[trainee]) < assign_num: 
            i += 1
            temp = applicants[randrange(applicant_num)]
            while temp in rev_list or applicant_counts[temp] != 0:
                i += 1
                temp = applicants[randrange(applicant_num)]
                if i > applicant_num * len(trainee_list) * eyes * 10:
                   return(False) 
            if applicant_counts[temp] == eyes:
                applicants.remove(temp)
                applicant_num = len(applicants)
            rev_list.append(temp)
            applicant_counts[temp] += 1
            reviewer_counts[trainee] += 1
            applicant_dict[temp].append(trainee)
            reviewer_dict[trainee].append(temp)

    # faculty
    i = 0
    for faculty in faculty_list:
        rev_list = []
        if faculty in min_list:
            assign_num = min_num
        elif faculty in max_list:
            assign_num = min_num + 1
        while len(reviewer_dict[faculty]) < assign_num: 
            i += 1
            temp = applicants[randrange(applicant_num)]
            while temp in rev_list or applicant_counts[temp] == eyes:
                i += 1
                temp = applicants[randrange(applicant_num)]
                if i > applicant_num * len(reviewer_list) * eyes * 10:
                   return(False)
            if applicant_counts[temp] == eyes:
                applicants.remove(temp)
                applicant_num = len(applicants)
            rev_list.append(temp)
            applicant_counts[temp] += 1
            reviewer_counts[faculty] += 1
            applicant_dict[temp].append(faculty)
            reviewer_dict[faculty].append(temp)
    return(applicant_dict, reviewer_dict)


def main():

    attempt = False
    while attempt == False:
        attempt = assign_reviewer(reviewers, applicants, eyes)
    applicant_dict, reviewer_dict = attempt

if __name__ == '__main__':
    main()
