# # ? TESTING DB...
from db_reader import DB_READER
from calc import TAX_CALCULATOR

dr = DB_READER()
tc = TAX_CALCULATOR()


etax = dr.selectTaxes("JAN","Samsung")
atax = dr.selectTaxes("JAN", "Samsung")
tax_diff = tc.tax_diff(etax[0], atax[1])
dr.addtotabble('Samsung',22,etax[0],atax[1],tax_diff,10)
print("Added to table successsfully!!!!!!!!")

# import sqlite3

# connection = sqlite3.connect("tabble.db")
# cursor = connection.cursor()

# query = '''
#     CREATE TABLE COMPANY_INFO
#          (Business_Name TEXT    NOT NULL,
#          Tax_id         INT    NOT NULL,
#          Expected_Tax   INT    NOT NULL,
#          Actual_Tax     INT   NOT  NULL,
#          Tax_Diff    INT     NOT NULL,
#          taxgrowth_rate   INT    NOT NULL);    
# '''

# cursor.execute(query)

# connection.close()