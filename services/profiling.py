def profile_dataframe(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "dtypes": df.dtypes.astype(str),
        "missing": df.isnull().sum(),
        "describe": df.describe(include="all")
    }
