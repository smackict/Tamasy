from dist import calc,db_reader 
  
cl = calc.TAX_CALCULATOR()
db = db_reader.DB_READER()

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
                # print(list(tx)[curposx+1])
                # print(list(mn)[curposy+1])
                tdiffs.append(cl.tax_diff(list(tx)[curposx+1],list(mn)[curposy+1]))          
                curposx -= 1
                curposy -= 1                  
                tgrowths.append(cl.taxgrowth_rate(list(tx)[curposx+1],list(mn)[curposy+1],db.selectTaxes("Bawulira",db.getCurrentmonth())[0]))
                # tgrowths.append(cl.taxgrowth_rate(list(tx)[curposx+1],list(mn)[curposy+1],db.selectTaxes(item,db.getCurrentmonth()))[0])
            except IndexError:
                break

expected_taxes = etaxes

print(expected_taxes)
actual_taxes = atuals
print(actual_taxes)
tax_diffs = tdiffs
print(tax_diffs)
tax_growth_rates = tgrowths
print(tax_growth_rates)