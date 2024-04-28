import pandas as pd

def data_preprocessing():
    df = pd.read_csv('data/mxmh_survey_results.csv')
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.to_csv('data/processed_results.csv')
    return df

if __name__ == '__main__':
    data_preprocessing()
