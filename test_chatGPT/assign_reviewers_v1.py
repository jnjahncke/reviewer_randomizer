#!/usr/bin/env python

import random
import pandas as pd
from math import ceil

# reviewers: dictionary with keys 'faculty' and 'trainee', where the value for each key is a list of reviewers
# applicants: list of applicants (strings)
# num_reviewers_per_applicant: number of reviewers to be assigned to each applicant

def assign_reviewers(reviewers, applicants, num_reviewers_per_applicant):
    faculty_reviewers = reviewers['faculty'].copy()
    trainee_reviewers = reviewers['trainee'].copy()
    # shuffle the list of faculty reviewers to randomize the assignment
    random.shuffle(faculty_reviewers)

    # calculate how many applicants each reviewer should be assigned
    num_reviewers = len(faculty_reviewers) + len(trainee_reviewers)
    num_applicants = len(applicants)
    applicants_per_reviewer = ceil(num_applicants / num_reviewers)

    assigned_reviewers = {}
    for applicant in applicants:
        # assign the first `num_reviewers_per_applicant` faculty reviewers to the current applicant
        assigned_reviewers[applicant] = faculty_reviewers[:num_reviewers_per_applicant]
        # remove the assigned reviewers from the list
        faculty_reviewers = faculty_reviewers[num_reviewers_per_applicant:]

        # if there are still reviewers left to assign and we haven't assigned a trainee yet, assign one
        if len(trainee_reviewers) > 0 and not any(assigned_reviewer in trainee_reviewers for assigned_reviewer in assigned_reviewers[applicant]):
            assigned_reviewers[applicant].append(trainee_reviewers.pop(0))

        # if we have assigned the maximum number of applicants to the current reviewer, move on to the next reviewer
        if len(assigned_reviewers[applicant]) == num_reviewers_per_applicant + 1:
            faculty_reviewers.append(trainee_reviewers.pop(0))
            trainee_reviewers.append(faculty_reviewers.pop(0))

    # create a dataframe with the assignment
    df = pd.DataFrame({
        'Applicant': applicants,
        **{f'Reviewer {i}': [assigned_reviewers[applicant][i] for applicant in applicants] for i in range(num_reviewers_per_applicant)}
     })

    write the dataframe to a CSV file
    df.to_csv('assignment.csv', index=False)

    # print the text output
    for reviewer in reviewers['faculty'] + reviewers['trainee']:
        print(reviewer)
        for applicant, *assigned_reviewers in assignment:
            if reviewer in assigned_reviewers:
                print(f'\t{applicant}')

