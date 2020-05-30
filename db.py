import pymysql

class DataBase:

	def __init__(self):
		self.connection = pymysql.connect(
			host='localhost',
			user='root',
			password='Gerson',
			db='xdface'
		)

		self.cursor = self.connection.cursor()
	def true_user(self, id):
                sql = 'SELECT carnet, nombre, edad, facultad FROM estudiante WHERE carnet = {}'.format(id)
                try:
                        self.cursor.execute(sql)
                        if(self.cursor.execute(sql)!=1):
                            print("Desconocido")
                        else:
                            user=self.cursor.fetchone()
                            return user[1]
                        
                except Exception as e:
                        raise e