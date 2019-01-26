import math
numero=math.pi
dividendo=11
decimalesPI=77


while dividendo<77:
	print('*'*(dividendo%10),"%.*f"%(decimalesPI%10,numero)) 
	dividendo=dividendo+11
	decimalesPI=decimalesPI-11


 