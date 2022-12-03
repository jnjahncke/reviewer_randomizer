#!/usr/bin/env python

## ---------------------------- ##
## Load packages                ##
## ---------------------------- ##
from random import randrange
from math import floor
import re

## ---------------------------- ##
## Get inputs                   ##
## ---------------------------- ##

# Number of people assigned to each applicant.
eyes = 3

# Input list of reviewers. Need 3 quotation marks at beginning and end of list only. Each reviewer should be on a new line.
reviewers = """Gary   Faculty
Tianyi   Faculty
Kevin    Faculty
Larry  Faculty
Henrique    Faculty
Eric    Faculty
Kelly  Faculty
Yessica Student
Nina  Student
Jennifer    Student
Marissa  Postdoc"""
reviewers = reviewers.replace("\t", " ").split("\n")


# Input list of applicants. Need 3 quotation marks at beginning and end of list only. Each reviewer should be on a new line.
applicants = """Yura	Kosmatka
Jarl	Dunn
Juli	Marshall
Elicia	Moss
Cillin	Jankovic
Mahihkan	Alan
Agata	Confortola
Snezhana	Hadaway
Ekwueme	Rake
Deidra	Treacy
Ambrosius	Eldred
Ansgar	Karl
Stanislava	Ivankov"""
applicants = applicants.replace("\t", " ").split("\n")


def assign_reviewer():

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
    max_list = [] # reviewers to be assigned the max number of applicants
    min_list = [] # reviewers to be assigned the min number of applicants
    # parse reviewer names, roles; build up reviewer lists/dictionaries
    for reviewer in reviewers:
        # parse name, role
        for found in re.finditer(r"^([\w\s]+)\s(\w+)$",reviewer):
            reviewer_counts[found.group(1).rstrip()] = 0
            reviewer_dict[found.group(1).rstrip()] = []
            reviewer_list.append(found.group(1).rstrip())
            # assign to faculty_list or trainee_list
            if found.group(2).lower() == "faculty":
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
        for x in range(assign_num):
            i += 1
            temp = applicants[randrange(applicant_num)]
            while temp in rev_list or applicant_counts[temp] != 0:
                i += 1
                temp = applicants[randrange(applicant_num)]
                if i > applicant_num * len(trainee_list) * eyes * 1000:
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
        for x in range(assign_num):
            i += 1
            temp = applicants[randrange(applicant_num)]
            while temp in rev_list or applicant_counts[temp] == eyes:
                i += 1
                temp = applicants[randrange(applicant_num)]
                if i > applicant_num * len(reviewer_list) * eyes * 1000:
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

attempt = False
while attempt == False:
    attempt = assign_reviewer()
applicant_dict, reviewer_dict = attempt

## ------------------------------ ##
## Print/save results             ##
## ------------------------------ ##

# save table of applicant: reviewers
with open("applicants_reviewers.csv","w") as output:
  output.write("Applicant,Reviewers" + ","*(eyes-1) + "\n")
  print("\n\nApplicant\tReviewers")
  for applicant in applicant_dict:
      line = applicant
      for reviewer in applicant_dict[applicant]:
          line += "," + reviewer
      output.write(line + "\n")
      print(line.replace(",","\t"))


# save table of reviewer: applicants
with open("reviewer_applicants.csv","w") as output, open("reviewer_applicants.txt","w") as txt:
  output.write("Reviewer,Applicants" + ","*(min_num) + "\n")
  print("\n\nReviewer\tApplicants")
  for reviewer in reviewer_dict:
      line = reviewer
      txt.write(reviewer + "\n")
      for applicant in reviewer_dict[reviewer]:
          line += "," + applicant
          txt.write("\t" + applicant + "\n")
      while line.count(",") < min_num+1:
        line += ","
      output.write(line + "\n")
      print(line.replace(",","\t"))
