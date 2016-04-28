import numpy as np
import Image
import os

f = open("entrada.txt",'r')
l = f.readlines()
l[0] = l[0].split("\n")[0]
if(len(l[0])>0):
	l[0] += "/"
l[1] = l[1].split("\n")[0]
l[2] = l[2].split("\n")[0]
l[3] = l[3].split("\n")[0]
l[4] = l[4].split("\n")[0]
try:
	os.mkdir(l[0] + l[1])
	print "Criando Pasta ..."
except Exception, e:
	print "Pasta Ja Criada"

# img1 = Image.open('paisagem1.jpg').convert('RGBA')
img1 = Image.open(l[2]).convert('RGBA')
arr1 = np.array(img1)
# img2 = Image.open('paisagem2.jpg').convert('RGBA')
img2 = Image.open(l[3]).convert('RGBA')
arr2 = np.array(img2)
# tam = input()
tam = int(l[4])
xy1 = img1.size
xy2 = img2.size
if(tam<2):
	print "A quantidade de interacoes deve ser pelo menos 2"
elif(xy1!=xy2):
	print "As dimensoes das imagens devem ser iguais"
else:
	for t in range(tam):
		print "criando imagem " + str((t + 1)) + " de " + str(tam) + " com " + str(float("{:.2f}".format(float(t)/float(tam-1)*100))) + "% da imagem 1 e " + str(float("{:.2f}".format(float(tam-1-t)/float(tam-1)*100))) + "% da imagem 2."
		valor1 = arr1 * (float(tam-1-t)/float(tam - 1))
		valor2 = arr2 * (float(t)/float(tam - 1))
		arr = valor1 + valor2
		img = np.array(arr,np.uint8)
		img = Image.fromarray(img, 'RGBA')
		img.save(l[0] + l[1] + "/" + str(t+1) +".png")