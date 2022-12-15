Here's an example of how you could use the functions:

```
reviewers = {
    'faculty': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'trainee': ['Eve', 'Frank'],
}
applicants = ['app1', 'app2', 'app3', ..., 'app130']
num_reviewers_per_applicant = 2

assign_reviewers(reviewers, applicants, num_reviewers_per_applicant)
```

For v1: This would output a CSV file with the assignment of reviewers to applicants and print text output in the format specified in the question. The order of the applicants and reviewers in the output may differ from run to run because of the random shuffling.

For v2: This would return a dataframe and list in the same format as below but you need to specify how to print.

Unfortunately neither of these codes actually run! They don't assign applicants properly and the data frame throws an error. I also had ChatGPT write a Shiny app but because these scripts don't run I don't even know if the app would run.
