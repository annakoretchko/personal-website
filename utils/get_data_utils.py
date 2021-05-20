
import numpy as np
import pandas as pd
import sys

def rename_cols(df):
    
    """[This function takes in a df, subsets the desired column and renames them to have no spaces.
        It also replaces "--" with 0 when no data is given]

    Args:
        df ([df]): [raw original df needing to be cleaned]

    Returns:
        [df]: [properly subsetted and renamed df]
    """

    # subset the columsn of interest
    df = df[['Time Period','Average Distance','Average Pace','Average Heart Rate','Average Run Cadence','Average Speed','Avg Elevation Gain','Activities']]

    # rename
    df = df.rename(columns={'Time Period':'Time_Period'})
    df = df.rename(columns={'Average Distance':'Average_Distance'})
    df = df.rename(columns={'Average Pace':'Average_Pace'})
    df = df.rename(columns={'Average Heart Rate':'Average_Heart_Rate'})
    df = df.rename(columns={'Average Run Cadence':'Average_Run_Cadence'})
    df = df.rename(columns={'Average Speed':'Average_Speed'})
    df = df.rename(columns={'Avg Elevation Gain':'Avg_Elevation_Gain'})


    # # replace '--' with 0's
    df = df.replace("--", 0)   
  

    # sys.exit()
    # df = df.fillna(0)    
    # df = df.replace("--", 0)   
    # df = df.replace(np.nan, 0)

    return df


def remove_units(df):

    """[Removes the string units for each column]

    Args:
        df ([df]): [df with units]

    Returns:
        [df]: [df with string units removed]
    """
   
    # remove units
    df['Average_Distance'] = df['Average_Distance'].str.rstrip('mi')
    df['Average_Pace'] = df['Average_Pace'].str.rstrip('min/mi')
    df['Average_Heart_Rate'] = df['Average_Heart_Rate'].str.rstrip('bpm')
    df['Average_Run_Cadence'] = df['Average_Run_Cadence'].str.rstrip('spm')
    df['Average_Speed'] = df['Average_Speed'].str.rstrip('mph')
    df['Avg_Elevation_Gain'] = df['Avg_Elevation_Gain'].str.rstrip('ft')



    return df


def convert_type(df):
    """[Changes each column to its appropriate type]

    Args:
        df ([df]): [df with all inputs as strings]

    Returns:
        [df]: [df wtih each column with appropriate data type]
    """

    # cleans again since this drops after str removal
    df['Average_Heart_Rate'] = pd.to_numeric(df['Average_Heart_Rate'], errors='coerce')
    df = df.dropna(subset=['Average_Heart_Rate'])

    ## convert data from sting to float/int
    df['Average_Distance'] = df['Average_Distance'].astype(float)
    df['Average_Speed'] = df['Average_Speed'].astype(float)
    df['Average_Heart_Rate'] = df['Average_Heart_Rate'].astype(int)
    df['Average_Run_Cadence'] = df['Average_Run_Cadence'].astype(int)
    df['Avg_Elevation_Gain'] = df['Avg_Elevation_Gain'].astype(int)
    df['Activities'] = df['Activities'].str.replace(',', '').astype(int)

    # create month/day into two columns
    df[['Month','Year']] = df.Time_Period.str.split(expand=True)
    df['Month'] = df['Month'].astype(str)
    df['Year'] = df['Year'].astype(str)




    return df