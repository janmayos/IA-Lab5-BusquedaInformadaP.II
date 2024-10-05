import random

def generaxyRand(rango_inferior,rango_superior):
	
	x = random.uniform(-4.5, 4.5)
	y = random.uniform(-4.5, 4.5)
	return round(x,4),round(y,4)

def part1(x,y):
	return pow((1.5-x+x*y),2)
	
def part2(x,y):
	return pow((2.25-x+x*pow(y,2)),2)
	
def part3(x,y):
	return pow((2.625-x+x*pow(y,3)),2)
	
	
def evalFxy(x,y):
	return round(part1(x,y)+part2(x,y)+part3(x,y),4)

def runMinimos():
	valorminimo = 0
	xaux=0
	yaux=0
	iaux=0
	for i in range(0,10000):
		x,y = generaxyRand()
		res = evalFxy(x,y)
		print(i)
		print(x,y,res)
		if valorminimo > res or i == 0:
			valorminimo = res
			xaux = x
			yaux = y
			iaux = i
		
	print("Valor minimo es:"+str(valorminimo)+" X:"+str(xaux)+ " Y:"+str(yaux)+" Iteración: "+str(iaux))

if __name__ == "__main__":
	runMinimos()