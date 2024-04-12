import pandas as pd
import plotly.express as px

def _get_dataset():
    data = {'date': ['2018-01', '2018-02', '2018-03', '2018-04', '2018-05'],
            'tax amount': [1200, 150, 300, 450, 200]
            }
    return pd.DataFrame(data)


def taxes(indexed=False, datetimes=False):
    df = _get_dataset()
    if datetimes:
        df["date"] = df["date"].astype("datetime64[ns]")
    if indexed:
        df = df.set_index("date")
        df.columns.name = "tax amount"
    return df

def ret_graph():
    dfz = taxes(datetimes=True)
    fig = px.scatter(dfz, x="date", y="tax amount", trendline="ols")
    fig.show()