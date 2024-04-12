import pandas as pd
import plotly.express as px
import db_reader as db


def _get_dataset():
    data = {'month': [1,2,3,4,5,6,7,8,9,10,11,12],
            'tax amount': [db.selectTaxes("JAN","Huion")[1],db.selectTaxes("FEB","Huion")[1],db.selectTaxes("MAR","Huion")[1],db.selectTaxes("APR","Huion")[1],
                           db.selectTaxes("MAY","Huion")[1],db.selectTaxes("JUN","Huion")[1],db.selectTaxes("JUL","Huion")[1],db.selectTaxes("AUG","Huion")[1],
                           db.selectTaxes("SEP","Huion")[1],db.selectTaxes("OCT","Huion")[1],db.selectTaxes("NOV","Huion")[1],db.selectTaxes("DEC","Huion")[1]]
            }
    return pd.DataFrame(data)


frz = _get_dataset()
fig = px.scatter(frz, x="month", y="tax amount", trendline="ols")
fig.show()