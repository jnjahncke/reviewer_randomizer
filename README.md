# reviewer_randomizer

This script takes in a list of applicants, a list of reviewers, and the number of people to be assigned to each applicant. Reviewers are then randomly assigned to the applicants. Reviewers can be either faculty or non-faculty ("trainees"). Only one non-faculty reviewer can be assigned to each applicant at maximum. Two output tables and one text file are saved: (1) a table of applicants followed by assigned reviewers and (2) a table of reviewers followed by assigned applicants and (3) text file of reviewers and their assigned applicants. *Output files all contain the same information in different formats.* 

Example output files: [applicants_reviewers.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/applicants_reviewers.csv), [reviewer_applicants.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.csv), [reviewer_applicants.txt](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.txt)

To run the script from an editable jupyter notebook in your web browser use [this google colab link](https://colab.research.google.com/drive/1BwNiAB5Pw-tr2n84-bI_EGcn1M7KSTvN). Note that this is EDITABLE. If you break it, it's up to you to fix it. The original version is [saved in this github](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_randomizer_GoogleColab.ipynb) - use that to fix the shared notebook.

The `reviewer_randomizer.py` script can be run from the command line but the script needs to be edited first to change the inputs since they are hard coded.

#### *Old version(s): did not incorporate trainee reviewers; division of labor not optimized*

*To run the old script from an editable jupyter notebook in your web browser use [this google colab link](https://colab.research.google.com/drive/17uKKnFAhS8MqKoNv1NC1AT_mjG3Ue4nh). Note that this is EDITABLE. If you break it, it's up to you to fix it. The original version is [saved in this github](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_randomizer_GoogleColab_old.ipynb) - use that to fix the shared notebook.*

*The `reviewer_randomizer_old.py` script can be run from the command line but the script needs to be edited first to change the inputs since they are hard coded.*
