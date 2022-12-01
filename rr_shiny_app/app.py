#!/usr/bin/env python


## ---------------------------- ##
## Load packages                ##
## ---------------------------- ##
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
from random import randrange
from math import floor
import re

## ---------------------------- ##
## Get inputs                   ##
## ---------------------------- ##
app_ui = ui.page_fixed(
    ui.h2("Reviewer Randomizer"),
    ui.input_text_area("eyes","Number Reviewers per Applicant:",3,rows=1),
    ui.input_text_area("reviewers","Reviewers:","""Gary Westrbook\tFaculty
Jennifer Jahncke\tStudent""",rows=20),
    ui.input_text_area("applicants","Applicants:","""Beyonce Knowles
Taylor Swift
Ryan Renolds""",rows=20),
    ui.output_text_verbatim("app_rev"),
    ui.output_text_verbatim("rev_app")
)

## ------------------------------ ##
## Print/save results             ##
## ------------------------------ ##
def server(input, output, session):

    @output
    @render.text
    def app_rev():
        return(input.applicants().split("\n"))
    
    @output
    @render.text
    def rev_app():
        return(input.reviewers().split("\n"))

app = App(app_ui, server)
