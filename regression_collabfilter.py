import pandas as pd
import numpy as np

from scipy.optimize import fmin_cg
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error

args = None

def load_data(filename, exclusion = False):
    users = {}
    with open(filename) as reader:
        #skip first line
        next(reader)
        for line in reader:
            if len(line.strip()) == 0:
                continue
            # Divide the line into user, movieid, and rating
            split_line = line.split(",")
            user = int(split_line[0])
            if user not in users:
                users[user] = {}
            user = users[user]
            movie_id = int(split_line[1])
            rating = float(split_line[2])
            if exclusion:
                if len(user) < 10:
                    user[movie_id] = rating
            else:
                user[movie_id] = rating
    return users