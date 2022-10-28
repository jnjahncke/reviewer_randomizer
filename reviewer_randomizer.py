#!/usr/bin/env python

from random import randrange
from math import ceil, floor

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
Y	Z""".replace("\t", " ").split("\n")

reviewers = """Gary	Westbrook
Tianyi	Mao
Kevin	Wright
Larry	Trussell
Henrique	VonGersdorf
Eric	Schnell
Kelly	Monk
Haining	Zhong
John	Williams""".replace("\t", " ").split("\n")

reviewer_num = len(reviewers)
applicant_num = len(applicants)
eyes = 3
max_num = ceil(applicant_num * eyes / reviewer_num)

reviewer_counts = {} # keep track of how many students each reviewer is assigned
reviewer_dict = {} # keep a list of each applicant assigned to each reviewer
applicant_dict = {} # keep a list of each reviewer assigned to each applicant
for reviewer in reviewers:
    reviewer_counts[reviewer] = 0
    reviewer_dict[reviewer] = []

print("\n\n")
# print applicant + assigned reviewers
print("Applicant\tReviewers")
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
        line += "\t" + temp
    print(line)


print("\n\n")
# check distribution of work
print("Reviewer\tCount")
for reviewer, count in reviewer_counts.items():
    print(f"{reviewer}\t{count}")

print("\n\n")
# print reviewer + assigned applicants
print("Reviewer\tApplicants")
for reviewer in reviewer_dict:
    line = reviewer
    for applicant in reviewer_dict[reviewer]:
        line += "\t" + applicant
    print(line)
