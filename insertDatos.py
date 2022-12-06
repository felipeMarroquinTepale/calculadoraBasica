import datetime
import random
import mysql.connector

def fecha_numero_aleatoria():
    fecha_inicio = datetime.date.today().replace(day=1,month=1).toordinal()
    fecha_final = datetime.date.today().toordinal()
    fecha = datetime.date.fromordinal(random.randint(fecha_inicio,fecha_final))

    numero = random.randrange(500,20000)
    print(fecha)
    print(numero)

    return fecha,numero


mydb = mysql.connector.connect(
  host="db-apibeekepeer.cdqxvmj3d7xx.us-east-1.rds.amazonaws.com",
  user="admin",
  passwd="datamin3",
  database="Tienda"
)
mycursor = mydb.cursor()

for _ in range(1000):
    ds,y = fecha_numero_aleatoria()
    sql = "INSERT INTO Tienda.price(ds,y) VALUES (%s,%s)"
    val = (ds,y);
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


