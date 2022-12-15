Here's an example of how you could use the function:

```
reviewers = {
    'faculty': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'trainee': ['Eve', 'Frank'],
}
applicants = ['app1', 'app2', 'app3', ..., 'app130']
num_reviewers_per_applicant = 2

assign_reviewers(reviewers, applicants, num_reviewers_per_applicant)
```

This would output a CSV file with the assignment of reviewers to applicants and print text output in the format specified in the question. The order of the applicants and reviewers in the output may differ from run to run because of the random shuffling.
