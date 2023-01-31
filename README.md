# reviewer_randomizer

This script takes in a list of applicants, a list of reviewers, and the number of people to be assigned to each applicant. Reviewers are then randomly assigned to the applicants. Reviewers can be either faculty or non-faculty ("trainees"). Only one non-faculty reviewer can be assigned to each applicant at maximum. 

There are multiple ways to run this code. Fair warning that for longer lists of applicants it can take a *while* to run. (It could take 1 minute it could take 20 minutes. Make a coffee.)

## Running as a Shiny App

Definitely the most user friendly method of running the code. Follow [this link](https://jennifer-jahncke.shinyapps.io/reviewer_randomizer/) to run the code on shinyapps.io.

To run:

* Enter reviewer names. The format must be `Name Role`.
   * You should be able to copy-paste from a word/text/excel document.
   * Each reviewer name/role should be on a new line.
   * `Name`: Can be first name only, last name only, or first and last (doesn't matter).
   * `Role`: Faculty must be denoted "faculty" (case does not matter); other roles can be anything (ie. "student", "postdoc", "president", anything!).
   * `Name` and `Role` must be separated by whitespace (tab or space).
* Enter applicant names. 
   * You should be able to copy-paste from a word/text/excel document.
   * Each applicant name should be on a new line.
* Enter the number of reviewers you want assigned to each applicant.
* Press the "Go!" button. If the output appears greyed out that means the code is running, give it some time. Pressing the go button again while it's already running won't do anything - either wait for it to finish or refresh the page.

Outputs:

* Table in format Applicant:Reviewers. You should be able to copy this and paste it into an excel document with formatting preserved.
* Text block in format Reviewer:Applicants.

## Running in a Google Colab Jupyter Notebook

To run the script from an editable jupyter notebook in your web browser use [this google colab link](https://colab.research.google.com/drive/1BwNiAB5Pw-tr2n84-bI_EGcn1M7KSTvN). Note that this is EDITABLE. If you break it, it's up to you to fix it. The original version is [saved in this github](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_randomizer_GoogleColab.ipynb) - use that to fix the shared notebook.

Two output tables and one text file are saved: (1) a table of applicants followed by assigned reviewers and (2) a table of reviewers followed by assigned applicants and (3) text file of reviewers and their assigned applicants. *Output files all contain the same information in different formats.* 

Example output files: [applicants_reviewers.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/applicants_reviewers.csv), [reviewer_applicants.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.csv), [reviewer_applicants.txt](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.txt)

The `reviewer_randomizer.py` script can be run from the command line but the script needs to be edited first to change the inputs since they are hard coded.
