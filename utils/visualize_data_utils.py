

import os


def create_line_graph(df,output_path, show = False):
    """[Creates a line graph from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """
    

    # df.plot.line(x ='Month',y = 'Average_Distance')
    # if show:
    #     plt.show()
    
    # fname = "line_graph.png"
    # pout = os.path.join(output_path,fname)
    # plt.savefig(pout)


def create_combo_chart(df):

    df = df.groupby(['Year']).mean()
    df = df.round(1)
    ls = df.values.tolist()
    print(ls)
    for i in ls:
        print(i)
    
    return df

def create_combo_HR_cadence(df):

    df = df[['Year','Average_Speed','Average_Run_Cadence']]
    df = df.groupby(['Year']).mean()
    df = df.round(1)
    ls = df.values.tolist()
    print(ls)
    for i in ls:
        print(i)

    return df


def create_combo_speed_distance(df):

    df = df[['Year','Average_Speed','Average_Distance']]
    df = df.groupby(['Year']).mean()
    df = df.round(1)
    ls = df.values.tolist()
    print(ls)
    for i in ls:
        print(i)

    return df
    
def create_combo_chart_Avgerage_Distance(df):

    df = df.round(0)
    df = df.groupby(['Average_Distance']).mean()
    df = df.round(1)


    # copy the data
    df_max_scaled = df.copy()
    
    # apply normalization techniques
    for column in df_max_scaled.columns:
        df_max_scaled[column] = df_max_scaled[column]  / df_max_scaled[column].abs().max()
        
    # view normalized data
    
    
    print(df)
    print(df_max_scaled)
    ls = df.values.tolist()
    print(ls)
    for i in ls:
        print(i)

    return df
    
   



