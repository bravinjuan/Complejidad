import xlrd
from pandas import *
from numpy import *
import time

my_sheet 	= 'Sheet1'
listarepos=[]
def buscarReposicion(idSuc,idArt):
	for i in array:
		if(i[1]==idArt):
			if(i[2]>5):
				listaaux=[idSuc,idArt,int(i[0])]
				listarepos.append(listaaux)

file_name 	= 'contSucArt.xlsx' 
contSucArt 	= read_excel(file_name, sheet_name = my_sheet, header=0)

array = contSucArt.values 
inicio=time.time()
i=0
flag=False
longi =len(array)-1
while i < longi:
	
	if (array[i][2]==0):
		
		idSuc=array[i][0]	
		idArt = array[i][1]	
		#BUSCAR REPONEDOR
		buscarReposicion(idSuc,idArt)

	#INCREMENTAR i EN BUCLE SUPERIOR
	i+=1


fin=time.time()
print("--------------------------------------------------------------------------------")
print(listarepos)
print('Tiempo total: ', (fin-inicio),' segundos')