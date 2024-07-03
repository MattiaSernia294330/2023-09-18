from database.DB_connect import DBConnect
from model.Retailer import Retailer



class DAO():
    def __init__(self):
        pass
    @staticmethod
    def get_Nations():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT Country 
from go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getNodi(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gr.Retailer_code as code, gr.Retailer_name as name 
from go_retailers gr 
where gr.Country =%s"""

        cursor.execute(query,(nazione,))

        for row in cursor:
            result.append(Retailer(row["code"],row["name"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi(nazione, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds.Retailer_code as r1, gds2.Retailer_code as r2, count(distinct gds2.Product_number) as nr
from go_retailers gr 
join go_retailers gr2 on gr.Country = gr2.Country 
join go_daily_sales gds on gds.Retailer_code =gr.Retailer_code 
JOIN go_daily_sales gds2 on gds2.Retailer_code =gr2.Retailer_code 
where year(gds.`Date`)=YEAR (gds2.`Date`) and gr.Retailer_code <gr2.Retailer_code and year(gds2.`Date`)=%s and gds.Product_number = gds2.Product_number and gr2.Country =%s
group by gds.Retailer_code, gds2.Retailer_code
"""

        cursor.execute(query, (anno,nazione))

        for row in cursor:
            result.append((row["r1"], row["r2"], row["nr"]))

        cursor.close()
        conn.close()
        return result