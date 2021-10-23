import numpy as np
import pandas as pd

# split numpy array into equal sized chunks, with remainder row chunk
def split_given_size(a, size):
    return np.split(a, np.arange(size, len(a), size))

# fast mapping of numpy arrays using a dictionary
def vec_translate(a, d):    
    return np.vectorize(d.__getitem__)(a)

# turn a pandas series with lists as value to 1D to get high level information
def to_1D(series):
    return pd.Series([x for _list in series for x in _list])
# e.g., to_1D(fruits[“favorite_fruits”]).value_counts()

# for correlations between objects in a list
def boolean_df(item_lists, unique_items):
# Create empty dict
    bool_dict = {}
    
    # Loop through all the tags
    for i, item in enumerate(unique_items):
        
        # Apply boolean mask
        bool_dict[item] = item_lists.apply(lambda x: item in x)
            
    # Return the results as a dataframe
    return pd.DataFrame(bool_dict)

# e.g., fruits_bool = boolean_df(fruits[“favorite_fruits”], unique_items.keys())
#       fruits_corr = fruits_bool.corr(method = "pearson")