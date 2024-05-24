import pandas as pd
import numpy as np

def DataFrame_01():
    data = [10, 20, 30, 40]
    df = pd.DataFrame(data)
    print(f"df: \n{df}")
    print(f"type(dfe): {type(df)}")
    
def dict_to_dataframe():
    dict = {'books':['C', 'Python', 'R'], 'count':[5, 10, 4]}
    df = pd.DataFrame(dict)
    
    print(f"dataframe df :\n{df}")

def series_to_dataframe():
    data = [10, 20, 30, 40]
    series1 = pd.Series(data, index = ['a', 'b', 'c', 'd'])
    print(f"series1: \n{series1}")
    print(f"type(series1): {type(series1)}")
    
    df = pd.DataFrame(series1)
    print(f"dataframe df :\n{df}")
    
def numpy_to_dataframe():
    
    nparr = np.array([[100, 200],['Python','C']])
    print(f"nparr :\n{nparr}")
    print(f"nparr[1] : {nparr[1]}")
    print(f"nparr[0] : {nparr[0]}")
    
    df = pd.DataFrame({'name': nparr[1], 'count': nparr[0]}, index=['a', 'b'])
    print(f"dataframe df :\n{df}")

def create_merged_dataframe():
    books1 = ['C', 'Python', 'R']
    count1 = [5, 10, 4]
    category1 = ['SysLang', 'Scripting', 'Scientific']

    books2 = ['C++', 'Python', 'Tcl']
    count2 = [2, 6, 4]
    category2 = ['OOP', 'Scripting', 'Scripting']

    print()
    df1 = pd.DataFrame({'BookNames': books1, 'BookCount':count1, 'category': category1})
    print(f"Df1:\n{df1}")
        
    df2 = pd.DataFrame({'BookNames': books2, 'BookCount':count2, 'category': category2})
    print(f"Df2:\n{df2}")
    
    return df1, df2
    
def merge_dataframes():
    df1, df2 = create_merged_dataframe()
    print()
    merged_df = df1.merge(df2, on='category', how = 'inner')
    print(f"Inner Merged on 'category' df :\n{merged_df}")

    print()
    merged_df = df1.merge(df2, on='category', how = 'left')
    print(f"Left Merged on 'category' df :\n{merged_df}")

    print()
    merged_df = df1.merge(df2, on='category', how = 'right')
    print(f"Right Merged on 'category' df :\n{merged_df}")

    print()
    merged_df = df1.merge(df2, on='category', how = 'outer')
    print(f"Outer Merged on 'category' df :\n{merged_df}")

def create_join_frame():
    books1 = ['C', 'Python', 'R']
    count1 = [5, 10, 4]
    category1 = ['SysLang', 'Scripting', 'Scientific']

    books2 = ['C++', 'Python', 'Tcl']
    count2 = [2, 6, 4]
    category2 = ['OOP', 'Scripting', 'Scripting']

    df1 = pd.DataFrame({'BookNames': books1, 'BookCount':count1, 'category': category1}, index=['Lib1', 'Lib2', 'Lib3'])
    print(f"Df1:\n{df1}")
    print()
        
    df2 = pd.DataFrame({'BookNames': books2, 'BookCount':count2, 'category': category2}, index=['Lib2', 'Lib3', 'Lib4'])
    print(f"Df2:\n{df2}")
    return df1, df2


def join_dataframes():
    df1, df2 = create_join_frame()
    print()
    joined_df = df1.join(df2, how = 'inner', lsuffix='_left', rsuffix='_right')
    print(f"Inner Joined df :\n{joined_df}")

    print()
    joined_df = df1.join(df2, how = 'left', lsuffix='_left', rsuffix='_right')
    print(f"Left Joined df :\n{joined_df}")
    
    print()
    joined_df = df1.join(df2, how = 'right', lsuffix='_left', rsuffix='_right')
    print(f"Right Joined df :\n{joined_df}")

    print()
    joined_df = df1.join(df2, how = 'outer', lsuffix='_left', rsuffix='_right')
    print(f"Outer Joined df :\n{joined_df}")
    return

def main():
    # DataFrame_01()
    # dict_to_dataframe()
    # series_to_dataframe()
    # numpy_to_dataframe()
    merge_dataframes()
    # join_dataframes()
    

if (__name__ == "__main__"):
    main()
