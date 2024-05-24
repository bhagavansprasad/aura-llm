import pandas as pd

def example_01():
    data = [10, 20, 30, 40]
    series1 = pd.Series(data)
    print(f"series1: \n{series1}")
    print(f"type(series1): {type(series1)}")

def change_index():
    data = [10, 20, 30, 40]
    series1 = pd.Series(data, index = ['a', 'b', 'c', 'd'])
    print(f"series1: \n{series1}")

def main():
    example_01()
    change_index()

if (__name__ == "__main__"):
    main()
