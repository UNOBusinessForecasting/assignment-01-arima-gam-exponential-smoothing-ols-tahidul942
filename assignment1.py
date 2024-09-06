# !pip install prophet # Only use this line if prophet is not already installed

import pandas as pd
from prophet import Prophet

data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/DataSets/chicagoBusRiders.csv")
