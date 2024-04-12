# Importing required functions 
from flask import Flask, request, render_template,redirect, url_for
from dist import calc
from dist import db_reader

cl = calc.TAX_CALCULATOR()
db = db_reader.DB_READER()

company_name = ""
tax_id = 0
expected_tax = 0
actual_tax = 0
tax_diff = 0
tax_growth_rate =0 

jan = 0
feb = 0
mar = 0
apr = 0
may = 0
jun = 0
jul = 0
aug = 0
sep = 0
oct = 0
nov = 0
dec = 0

# Flask constructor 
app = Flask(__name__) 

# Root endpoint 
@app.route('/', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('index.html') 

# @app.route('/table')
# def table():
# 	connection =  sqlite3.connect("tabble.db")
# 	cursor = connection.cursor()    
# 	cursor.execute("SELECT * FROM COMPANY_INFO")
# 	data = cursor.fetchall()

# 	return data

# `read-form` endpoint 
@app.route('/read-form', methods=['POST','GET']) 
def read_form(): 

	# Get the form (data) as Python ImmutableDict (data)type 
	data = request.form
	print(data)

	company_name  = data['userCompanyName']
	tax_id = data['userTaxID']

	jan=data['jan']
	feb=data['feb']
	mar=data['mar']
	apr=data['apr']
	may=data['may']
	jun=data['jun']
	jul =data['jul']
	aug=data['aug']
	sep=data['sep']
	oct=data['oct']
	nov=data['nov']
	dec=data['dec']

	db.createCompany(company_name)
	db. insertExpectedTax(company_name,cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values(),cl.rnd_values())
	db.insertActualTax(company_name,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)
			# 'email'      :     data['userEmail'], 
		# 'password'	 :     data['userPassword'], 
	## Return the extracted information 
	# return { 
	# 	'companyName':     data['userCompanyName'], 
	# 	'Tax ID'     :     data['userTaxID'],

	# 	'jan' 		 :     data['jan'],
	# 	'feb'        :     data['feb'],
	# 	'mar'        :     data['mar'],
	# 	'apr'        :     data['apr'],
	# 	'may'        :     data['may'],
	# 	'jun'        :     data['jun'],
	# 	'jul'        :     data['jul'],
	# 	'aug'        :     data['aug'],
	# 	'sep'        :     data['sep'],
	# 	'oct'        :     data['oct'],
	# 	'nov'        :     data['nov'],
	# 	'dec'        :     data['dec']
	# } 

	return redirect(url_for('table2'))

@app.route('/table2', methods=['GET']) 
def table2(): 
	## Display the HTML form template 
	return render_template('table.html',company_name=company_name,tax_id=tax_id,expected_tax=expected_tax,actual_tax=actual_tax,tax_diff=tax_diff,tax_growth_rate=tax_growth_rate) 

# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run()
