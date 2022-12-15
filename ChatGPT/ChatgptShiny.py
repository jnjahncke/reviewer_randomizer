#!/usr/bin/env python

import random
import pandas as pd
from math import ceil
from io import StringIO

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Import the assign_reviewers function from the assign_reviewers.py script
from assign_reviewers import assign_reviewers

# reviewers: dictionary with keys 'faculty' and 'trainee', where the value for each key is a list of reviewers
# applicants: list of applicants (strings)
# num_reviewers_per_applicant: number of reviewers to be assigned to each applicant

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-faculty-reviewers', type='text'),
    dcc.Input(id='input-trainee-reviewers', type='text'),
    dcc.Input(id='input-applicants', type='text'),
    dcc.Input(id='input-num-reviewers-per-applicant', type='number'),
    html.Button('Go!', id='button-go'),
    html.Div(id='output-reviewer-assignment'),
    html.Div(id='output-reviewer-text'),
])

@app.callback(
    [
        Output('output-reviewer-assignment', 'children'),
        Output('output-reviewer-text', 'children'),
    ],
    [
        Input('button-go', 'n_clicks'),
    ],
    [
        State('input-faculty-reviewers', 'value'),
        State('input-trainee-reviewers', 'value'),
        State('input-applicants', 'value'),
        State('input-num-reviewers-per-applicant', 'value'),
    ],
)
def assign_reviewers_callback(n_clicks, faculty_reviewers, trainee_reviewers, applicants, num_reviewers_per_applicant):
    # Parse the input strings into lists of reviewers and applicants
    faculty_reviewers = faculty_reviewers.split(',')
    trainee_reviewers = trainee_reviewers.split(',')
    applicants = applicants.split(',')

    # Call the assign_reviewers function
    df, text = assign_reviewers(
        {'faculty': faculty_reviewers, 'trainee': trainee_reviewers},
        applicants,
        num_reviewers_per_applicant,
    )

    # Return the dataframe and text output as Dash components
    return (
        dcc.DataTable(
            id='table-reviewer-assignment',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records'),
        ),
        html.Pre(text),
    )

if __name__ == '__main__':
    app.run_server(debug=True)

