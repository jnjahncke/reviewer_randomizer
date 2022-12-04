## ---------------------------- ##
## Load packages                ##
## ---------------------------- ##
from shiny import * 
from random import randrange
from math import floor
import pandas as pd
import re
from reviewer_randomizer import *

## ---------------------------- ##
## Get inputs                   ##
## ---------------------------- ##
app_ui = ui.page_fixed(
    ui.h2("Reviewer Randomizer"),
    ui.p("Enter a list of reviewers (and their role), a list of applicants, and the number of reviewers to be assigned to each applicant. Applicants will be randomly assigned such that they only have at maximum one non-faculty reviewer."),
    ui.row(
        ui.column(5,ui.input_text_area("reviewers","Reviewers:","""Kevin Wright\tFaculty
Kelly Monk\tFaculty
Jennifer Jahncke\tStudent""",rows=20)),
        ui.column(5, ui.input_text_area("applicants","Applicants:","""Beyonce Knowles
Taylor Swift
Ryan Reynolds""",rows=20)),
        ui.column(2,ui.input_text_area("eyes","Number of Reviewers per Applicant:",3,rows=1))),
    ui.p("FYI: This can take a few minutes."),
    ui.input_action_button("go", "Go!", class_="btn-success"),
    ui.output_table("app_rev"),
    ui.output_text_verbatim("rev_app")
)

## ------------------------------ ##
## Print/save results             ##
## ------------------------------ ##
def server(input, output, session):
    
    @reactive.Calc
    @reactive.event(lambda: input.go(), ignore_none=False)
    def assignment():
        reviewers = input.reviewers()
        applicants = input.applicants()
        eyes = int(input.eyes())

        attempt = False
        while attempt == False:
            attempt = assign_reviewer(reviewers, applicants, eyes)
        applicant_dict, reviewer_dict = attempt
        return(applicant_dict, reviewer_dict)

    @output
    @render.table
    def app_rev():
        
        applicant_dict = assignment()[0]
        eyes = int(input.eyes())

        students = list(applicant_dict.keys())

        revs = ["Reviewer "] * eyes
        nums = [str(x) for x in range(1,eyes+1)]
        rev_names = [x+y for x,y in zip(revs,nums)]

        col_name_dict = {}
        for x in range(eyes):
            col_name_dict[x] = rev_names[x]

        result = pd.DataFrame(applicant_dict.items(),
                columns = ["Applicant", "Reviewers"])
        result = pd.concat([result, pd.DataFrame(result.Reviewers.tolist())],
                axis = 1)
        result = result.rename(col_name_dict, axis=1)
        result = result.drop(labels="Reviewers", axis=1)

        return(result)
    
    @output
    @render.text
    def rev_app():

        reviewer_dict = assignment()[1]

        result = ""
        for reviewer in reviewer_dict:
            result += reviewer + "\n"
            for applicant in reviewer_dict[reviewer]:
                result += "\t" + applicant + "\n"

        return(result)

app = App(app_ui, server)
