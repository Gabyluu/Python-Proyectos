 #clasesObjetos.py
 class MixinsData(object);
 def__init__(self, 
 	  user="anonimo",
 	  password="patito",
 	  port="1234", 
 	  ost="localhost", 
 	  db="sqlite3");

      self.user = user
 	  self.password = password
 	  self.port = port 
 	  self.ost = host
 	  self.db = db

 #metodos para recuperar datos 

 	  def get_username(self):
 	  	return self.user

 	  	def get_password(self):
 	  	return self.password

 	  	def get_port(self):
 	  		return self.port

 	  	def get_host(self):
 	  		return self.host

 	  	def get_db(self):
 	  		return self.db


#atributos

usuario= str(input("Nombre del usuario? :_____")) 
 
password = str(input("Password?:___ "))

 obj = MixinsData(password= password, user=usuario)
   
    print(obj.user)
    print(obj.password)

    print(obj.get_username())

    	user = obj.get_username()

    	print(user*10)

  
