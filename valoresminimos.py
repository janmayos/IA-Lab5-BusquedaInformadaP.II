import random

def generaxy_rand(rango_inferior,rango_superior):
	
	x = random.uniform(rango_inferior,rango_superior)
	y = random.uniform(rango_inferior,rango_superior)
	return round(x,5),round(y,5)

def part1(x,y):
	return pow(pow(x,2)+y-11,2)
	
def part2(x,y):
	return pow(x+pow(y,2)-7,2)
	

	
	
def eval_f_xy(x,y):
	return round(part1(x,y)+part2(x,y),4)

def run_minimos():
	valorminimo = 0
	xaux=0
	yaux=0
	iaux=0
	for i in range(0,1000000):
		x,y = generaxy_rand(-5,5)
		res = eval_f_xy(x,y)
		#print(i)
		#print(x,y,res)
		if valorminimo > res or i == 0:
			valorminimo = res
			xaux = x
			yaux = y
			iaux = i
		if valorminimo == 0:
			print(valorminimo)
			break
	print("Valor minimo es:"+str(valorminimo)+" X:"+str(xaux)+ " Y:"+str(yaux)+" Iteración: "+str(iaux))
#X:3 Y:2
#X:2.99885 Y:2.00055
if __name__ == "__main__":
	run_minimos()