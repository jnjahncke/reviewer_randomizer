#!/usr/bin/env python

# Load packages
from random import randrange
from math import ceil

# Number of people assigned to each applicant.
eyes = 3

# Input list of reviewers. Need 3 quotation marks at beginning and end of list only. Each reviewer should be on a new line.
reviewers = """Gary
Tianyi
Kevin
Larry
Henrique
Eric
Kelly
Haining
John"""
reviewers = reviewers.replace("\t", " ").split("\n")

# Input list of applicants. Need 3 quotation marks at beginning and end of list only. Each reviewer should be on a new line.
applicants = """A	B
C	D
E	F
G	H
I	J
K	L
M	N
O	P
Q	R
S	T
U	V
W	X
Y	Z"""
applicants = applicants.replace("\t", " ").split("\n")

"""### Run Script, Export Excel Sheets"""

reviewer_num = len(reviewers)
applicant_num = len(applicants)
max_num = ceil(applicant_num * eyes / reviewer_num)

reviewer_counts = {} # keep track of how many students each reviewer is assigned
reviewer_dict = {} # keep a list of each applicant assigned to each reviewer
applicant_dict = {} # keep a list of each reviewer assigned to each applicant
for reviewer in reviewers: # build reviewer dictionaries
    reviewer_counts[reviewer] = 0
    reviewer_dict[reviewer] = []

# save table of applicant: reviewers
with open("applicants_reviewers.csv","w") as output:
  output.write("Applicant,Reviewers" + ","*(eyes-1) + "\n")
  print("\n\nApplicant\tReviewers")
  for applicant in applicants:
      applicant_dict[applicant] = []
      rev_list = []
      line = applicant
      for x in range(eyes):
          temp = reviewers[randrange(reviewer_num)]
          while temp in rev_list or reviewer_counts[temp] >= max_num:
              temp = reviewers[randrange(reviewer_num)]
          rev_list.append(temp)
          reviewer_counts[temp] += 1
          reviewer_dict[temp].append(applicant)
          applicant_dict[applicant].append(temp)
          line += "," + temp
      output.write(line + "\n")
      print(line.replace(",","\t"))

# check distribution of work
print("\n\n")
for reviewer, count in reviewer_counts.items():
    print(f"{reviewer}\t{count}")

# save table of reviewer: applicants
with open("reviewer_applicants.csv","w") as output:
  output.write("Reviewer,Applicants" + ","*(max_num-1) + "\n")
  print("\n\nReviewer\tApplicants")
  for reviewer in reviewer_dict:
      line = reviewer
      for applicant in reviewer_dict[reviewer]:
        line += "," + applicant
      while line.count(",") < max_num:
        line += ","
      output.write(line + "\n")
      print(line.replace(",","\t"))
