
import numpy, json
from mutants import db, ma
from sqlalchemy import Integer, String, Boolean, Text

class Human(db.Model):

    human_id = db.Column(db.Integer, primary_key = True)
    dna = db.Column(db.Text())
    mutant = db.Column(db.Boolean())  

    def __init__(self, human_id=None, dna=None):
        self.human_id = human_id
        self.dna = dna
        self.mutant = False

    def is_mutant(self):
        try:
            #Se convierte el JSON con la lista de letras
            li = self.dna
            li = json.loads(li)
            dna_list = li.get("dna")
            #Se convierte la lista en una matriz
            matrix = [list(x) for x in dna_list]
            #Luego se convierte en un numpy array para usar la funcion de diagonales
            matrix = numpy.array(matrix)
            #DIAGONALES IZQUIERDA A DERECHA
            secuencias = [ "".join(matrix.diagonal(i)) for i in range( ((len(matrix)*-1)+1) , len(matrix) ) if len(matrix.diagonal(i)) >= 4]
            #DIAGONALES DERECHA A IZQUIERDA
            matrix_inversa = matrix[::-1,:]
            secuencias.extend( [ "".join(matrix_inversa.diagonal(i)) for i in range(  ((len(matrix)*-1)+1) , len(matrix) ) if len(matrix.diagonal(i)) >= 4])
            #FILAS
            secuencias.extend( [ "".join(matrix[i,:])  for i in range(0, len(matrix) ) if len( matrix[i,:] ) >= 4  ])
            #COLUMNAS
            secuencias.extend( [ "".join(matrix[:,j])  for j in range(0, len(matrix) ) if len( matrix[j,:] ) >= 4  ])

            letras =  ("AAAA","TTTT","CCCC","GGGG") 
            
            concurrencies = 0
            for n in secuencias:
                
                concurrencies += (n.count(letras[0]) + n.count(letras[1]) + n.count(letras[2]) +n.count(letras[3]) )  
                if concurrencies > 1:
                    self.mutant = True
                    break

            return self.mutant
        except Exception as e:
            return self.mutant


class HumanSchema(ma.ModelSchema):
    class Meta:
        model = Human