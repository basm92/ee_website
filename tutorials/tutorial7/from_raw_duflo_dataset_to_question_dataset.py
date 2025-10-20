import pandas as pd
url = "https://github.com/droodman/Duflo2001/raw/refs/heads/main/inpresdata.dta"
data = pd.read_stata(url)
# 1. Create the 'post' variable
# Initialize it with a missing value for all rows
data['cohort'] = None
# Assign Post for the 'post' (younger) cohort
data.loc[(data['p607'] >= 23) & (data['p607'] <= 27), 'cohort'] = 'Post'
# Assign -1 for the 'pre' (older) cohort
data.loc[(data['p607'] >= 33) & (data['p607'] <= 38), 'cohort'] = -1
# Assign -2 for the 'pre-pre' cohort
data.loc[(data['p607'] >= 38) & (data['p607'] <= 43), 'cohort'] = -2
# Assign -3 for the 'pre-pre-pre' cohort
data.loc[(data['p607'] >= 43) & (data['p607'] <= 48), 'cohort'] = -3
# Assign -4 for the 'pre-pre-pre-pre' cohort
data.loc[(data['p607'] >= 48) & (data['p607'] <= 53), 'cohort'] = -4
# Get an order
cohort_order = ['-4', '-3', '-2', '-1', 'Post']
data['cohort'] = data['cohort'].astype(str)

# 3. Convert the column to an ordered Categorical type
data['cohort'] = pd.Categorical(data['cohort'],
                                    categories=cohort_order,
                                    ordered=True)

# 2. Create the 'treated' variable
# First, find the median of the program intensity variable (e.g., wsppc)
median_construction = data['wsppc'].median()

# Now, create 'treated'
data['treated'] = 0
data.loc[data['wsppc'] > median_construction, 'treated'] = 1

# 3. Filter the dataset for the DiD analysis
# Keep only the observations where 'post' is either 0 or 1
did_data = data.dropna(subset=['cohort'])

did_data.to_stata("tutorials/datafiles/duflo_did_data.dta")