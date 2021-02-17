# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def calculate_performance_metrics(y_true, y_predicted):
    """
    Calculate the R2 score and root mean squared error
    :param y_true: ground truth value
    :param y_predicted: predicted value
    :return:
    """
    r2 = r2_score(y_true, y_predicted)
    rmse = mean_squared_error(y_true, y_predicted, squared=False)
    print(f"R2 Score: {r2}")
    print(f"RMSE: {rmse}")


def clean_google_trends_data(df, start_date, max_date):
    """
    Convenience function to truncate and interpolate Google Trends data. We use linear
    interpolation, since the trends data only supplies information on a per-month, rather
    than per-day basis

    :param df: trends dataframe
    :param start_date: start date of the dataframe
    :param max_date: end date of the dataframe
    :return:
    """
    trends = df.copy()
    trends["Date"] = pd.to_datetime(trends["Month"], format="%Y-%m")
    trends.drop("Month", axis=1, inplace=True)

    # ensure maximum date matches up with price data
    trends = trends.loc[trends["Date"] >= start_date]
    trends = pd.concat(
        [trends, pd.DataFrame(data={"Date": [max_date], "Interest": [np.NaN]})],
        ignore_index=True,
    )

    # perform linear interpolation
    trends = trends.set_index("Date")
    trends = trends.resample("D").mean()
    trends = trends.interpolate()
    trends = trends.reset_index()
    return trends


def set_nonnegative_forecasts(forecast):
    """
    Set all FB Prophet values that are negative to 0

    :param forecast: time series input with yhat, yhat_lower, yhat_upper
    :return:
    """
    forecast.loc[forecast["yhat"] < 0, "yhat"] = 0
    forecast.loc[forecast["yhat_lower"] < 0, "yhat_lower"] = 0
    forecast.loc[forecast["yhat_upper"] < 0, "yhat_upper"] = 0
