def dataset_summary(df):
    print(df.describe())

def missing_values(df):
    print(df.isnull().sum())

def correlation_matrix(df):
    print(df.corr(numeric_only=True))

def duplicate_rows(df):
    print(df.duplicated().sum())