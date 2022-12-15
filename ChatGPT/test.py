#!/usr/bin/env python

from assign_reviewers import assign_reviewers

reviewers = {"faculty":["Kevin Wright","Kelly Monk","Gary Westbrook"],"trainee":["Jennifer Jahncke", "Yessica Santana"]}
applicants = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
num_reviewers_per_applicant = 3

df, output = assign_reviewers(reviewers, applicants, num_reviewers_per_applicant)

print(*output)
