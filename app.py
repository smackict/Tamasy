
from flask import Flask, render_template
from dist import calc,db_reader 
  
cl = calc.TAX_CALCULATOR()
db = db_reader.DB_READER()

app = Flask(__name__) 
  
companies =db.fetchCompanies()
tax_ids = [] 
tax_id = 0
etaxes = []
atuals = []
tdiffs = []
tgrowths = []
curposx = -1
curposy = -1

for item in db.fetchCompanies():
    etaxes.append(db.selectTaxes(item)[0])
    atuals.append(db.selectTaxes(item)[1])
    for tx in etaxes:
        for mn in atuals:
            try:    
                tdiffs.append(cl.tax_diff(list(tx)[curposx+1],list(mn)[curposy+1]))          
                curposx -= 1
                curposy -= 1    
                tax_id+=1   
                tax_ids.append(str(tax_id))          
                tgrowths.append(cl.taxgrowth_rate(list(tx)[curposx+1],list(mn)[curposy+1],db.selectTaxes("Bawulira",db.getCurrentmonth())[0]))
            except IndexError:
                break

expected_taxes = etaxes
actual_taxes = atuals

tax_diffs = tdiffs
tax_growth_rates = tgrowths
  
@app.route('/') 
def homepage(): 

    return render_template("index2.html", len = len(companies), Companies = companies,tax_ids = tax_ids,expected_taxes=expected_taxes,actual_taxes=actual_taxes,tax_diffs=tax_diffs,tax_growth_rates=tax_growth_rates) 

app.run(use_reloader = True, debug = True, port="1234") 