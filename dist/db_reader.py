import sqlite3



BIGBOY = ""

class DB_READER:

    def db_writerconny(self):
        self._connection = sqlite3.connect("tabble.db")
        self._cursor = self._connection.cursor()

    def db_readerconny(self):
        self.connection = sqlite3.connect("base.db")
        self.cursor = self.connection.cursor()
    

    def createCompany(self,*arg, **karg):
        self.db_readerconny()
        query = f"""
        CREATE TABLE "{arg[0]}" 
        ( "JAN" INTEGER NOT NULL, 
        "FEB" INTEGER NOT NULL, 
        "MAR" INTEGER NOT NULL, 
        "APR" INTEGER NOT NULL, 
        "MAY" INTEGER NOT NULL, 
        "JUN" INTEGER NOT NULL, 
        "JUL" INTEGER NOT NULL, 
        "AUG" INTEGER NOT NULL, 
        "SEP" INTEGER NOT NULL, 
        "OCT" INTEGER NOT NULL, 
        "NOV" INTEGER NOT NULL, 
        "DEC" INTEGER NOT NULL);
    """
        self.connection.execute(query)

    def insertExpectedTax(self,cname,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec):
        self.db_readerconny()
        self.connection.execute(f'''INSERT INTO {cname} (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC) VALUES ({jan},{feb},{mar},{apr},{may},{jun},{jul},{aug},{sep},{oct},{nov},{dec})''')
        
        self.connection.commit()
        self.connection.close()

    def insertActualTax(self,cname,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec):
        self.db_readerconny()
        self.connection.execute(f'''INSERT INTO {cname} (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC) VALUES ({jan},{feb},{mar},{apr},{may},{jun},{jul},{aug},{sep},{oct},{nov},{dec})''')
        
        self.connection.commit()
        self.connection.close()

    def selectTaxes(self,month,company):
        self.db_readerconny()
        taxes=[]
        meow = self.connection.execute(f"SELECT {month} FROM {company}").fetchall()
        if not meow:
            pass
        else:
                
            expected_tax = str(meow[0])[1:-2]
            actual_tax = str(meow[1])[1:-2]
            # print(f'''Expected Tax - {int(expected_tax)}
            # Actual Tax - {actual_tax}''')
            taxes.append(int(expected_tax))
            taxes.append(int(actual_tax))



            self.connection.close()
            return taxes
        
    def addtotabble(self,business_name,Tax_id,Expected_tax,Actual_tax,Tax_Diff,taxgrowth_rate):
        self.db_writerconny()

        query = f'''INSERT INTO COMPANY_INFO (Business_Name, Tax_id, Expected_Tax, Actual_Tax, Tax_Diff, taxgrowth_rate) VALUES ('{business_name}',{Tax_id},{Expected_tax},{Actual_tax},{Tax_Diff},{taxgrowth_rate})'''

        self._connection.execute(query)
        self._connection.commit()

        pass
        
        
    def errHandler(self,func):
        try:
            func()
        except Exception as e:
            print(f"Woah! Slight error there! \n {e}")
        pass
