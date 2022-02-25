def compute_statistics(df):
    common = df['Name'].mode().values[0]
    mean_age = df['Age'].mean()
    quantile1 = df['Rating'].quantile(0.25)
    quantile2 = df['Rating'].quantile(0.75)
    IQR = float(quantile2 - quantile1)

    return common,mean_age,IQR