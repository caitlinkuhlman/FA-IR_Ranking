'''
Created on Jan 24, 2017

@author: meike.zehlike
'''

import pandas as pd
from dataset_creator.candidate import Candidate


def createCompasGenderDataSet(filename, *columnsToRead):
    """
    currently working with recidivism score as qualification attribute in candidates. Change index
    to try with other columns
    """
    nonProtected = []
    protected = []
    with open(filename) as csvfile:
        data = pd.read_csv(csvfile, usecols=columnsToRead)
        for row in data.itertuples():
            # change to different index in row[.] to access other columns from csv file
            if row[4] == 1:
                nonProtected.append(Candidate(1 - row[3], []))
            else:
                protected.append(Candidate(1 - row[3], ["male"]))

    # sort candidates by decile scores in COMPAS
    protected.sort(key=lambda candidate: candidate.qualification, reverse=True)
    nonProtected.sort(key=lambda candidate: candidate.qualification, reverse=True)

    return protected, nonProtected


def createCompasRaceDataSet(filename, *columnsToRead):
    """
    currently working with recidivism score as qualification attribute in candidates. Change index
    to try with other columns
    """
    nonProtected = []
    protected = []
    with open(filename) as csvfile:
        data = pd.read_csv(csvfile, usecols=columnsToRead)
        for row in data.itertuples():
            # change to different index in row[.] to access other columns from csv file
            if row[4] == 0:
                nonProtected.append(Candidate(1 - row[3], []))
            else:
                protected.append(Candidate(1 - row[3], ["black"]))

    # sort candidates by decile scores in COMPAS
    protected.sort(key=lambda candidate: candidate.qualification, reverse=True)
    nonProtected.sort(key=lambda candidate: candidate.qualification, reverse=True)

    return protected, nonProtected



