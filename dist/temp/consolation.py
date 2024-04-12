from db_reader import DB_READER
from calc import TAX_CALCULATOR

database = DB_READER()
tx_calc = TAX_CALCULATOR()

while True:
    try:
        cmd = input("cmd : ")          
        if cmd.lower() == "create":
            cmpname = input("Company Name: ")
            database.createCompany(cmpname)
            print("Company Created!")
        if cmd.lower() == "insert":
            wincsert = input("Expected or Actual? ")
            if wincsert.lower() == "expected":
                company = input("Company Name? :")
                jan = input("January Value: ")
                feb = input("February Value: ")
                mar = input("March Value: ")
                apr = input("April Value: ")
                may = input("May Value: ")
                jun = input("June Value: ")
                jul = input("July Value: ")
                aug = input("August Value: ")
                sep = input("September Value: ")
                oct = input("October Value: ")
                nov = input("November Value: ")
                dec = input("December Value: ")
                database.insertExpectedTax(company,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)
                print("Inserted !")
            elif wincsert.lower() == "actual":
                company = input("Company Name? :")
                jan = input("January Value: ")
                feb = input("February Value: ")
                mar = input("March Value: ")
                apr = input("April Value: ")
                may = input("May Value: ")
                jun = input("June Value: ")
                jul = input("July Value: ")
                aug = input("August Value: ")
                sep = input("September Value: ")
                oct = input("October Value: ")
                nov = input("November Value: ")
                dec = input("December Value: ")
                database.insertActualTax(company,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)
                print("Inserted !")
        if cmd.lower() == "select":
            company = input("Select Company: ")
            month = input("Select Month")
            tValue = input("Display Expected or Actual Tax?: ")
            if tValue.lower() == "expected":
                print(database.selectTaxes(month,company)[0])
            if tValue.lower() == "actual":
                print(database.selectTaxes(month,company)[1])
        else:
            print("Command does not exist!")
    except KeyboardInterrupt:
        print("\n  "*2 + "\n Bai baii (┬┬﹏┬┬)...")
        break