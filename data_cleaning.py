import csv
import pandas as pd
import numpy as np




with open('bio_latest.csv',encoding='utf8') as input, open('bio_clean.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)