import numpy as np
import pandas as pd

# Question 1
hitters = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Hitters.csv', sep=',', header=0)
hitters.info()
hitters = hitters.dropna()
hitters.describe()
# Create dataframe with 3 columns
data = hitters[["Hits", "HmRun", "Runs"]]
data.describe()

# Question 2
def test_create_dataframe(df):
    """
    Input: df - pandas DataFrame variable
    Output: True if the following conditinos hold:
        * The DataFrame contains only the columns that I specified in #1
        * The columns contain the correct data type
        * There are at least 10 rows in the DataFrame
    """
    ret = True
    
    # Condition 1: The DataFrame contains only the columns that I specified in #1
    if (sorted(list(df)) != sorted(list(data)) and ret == True):
        ret = False
        print("The DataFrame does not contain only the columns specified in #1.")
    
    # Condition 2: The columns contain the correct data type
    elif (np.any(data.dtypes != df.dtypes) and ret == True):
        ret = False
        print("The columns do not contain the correct data type.") 

    # Condition 3: There are at least 10 rows in the DataFrame
    elif len(df.index) < 10:
        ret = False
        print("There are less than 10 rows in the DataFrame.")
        
    if (ret == True):
        print("The input DataFrame meets the requirements.")
    return ret

# Question 2 Test Case 1: subset of Hitters 3-column dataset
# Expected result: False
data_subset = data.loc[hitters['HmRun'] > 10]
test_create_dataframe(data_subset)

# Question 2 Test Case 2: Does not contain only the columns specified in #1
# Expected result: False
data_diffcol = hitters[["Hits", "Runs", "RBI"]]
test_create_dataframe(data_diffcol)

# Question 2 Test Case 3: Does not contain the correct data type
# Expected result: False
convert_dict = {'Hits': float}  
data_subset2 = data_subset.astype(convert_dict)
test_create_dataframe(data_subset2)

# Question 2 Test Case 34: Less than 10 rows in DataFrame
# Expected result: False
data_subset3 = data_subset.head()
test_create_dataframe(data_subset3)