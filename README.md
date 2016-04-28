Para o programar funcionar é preciso esta instaladas as bibliotecas numpy e Image. 

Para instalar o numpy use:

	sudo apt-get install python-numpy

a biblioteca Image ja vem instalada no python2 do ubuntu

Antes de executar o arquivo foto.py, abra o arquivo entrada.txt:
	
	1. coloque na primeira linha o endereço onde vai ser salvo as fotos resultantes das interações do programa, ex: "/home/user/Documentos", sem as aspas, ou para salvar no mesmo diretorio deixe a primeira linha em branco.

	2. Na segunda linha coloque o nome da pasta onde vai ser salvo as fotos resultantes, ex:"fotos", sem as aspas.

	3. Na terceira linha colocar o endereço onde esta a primeira imagem, ex:"/home/user/picture/image1.png",sem as aspas

	4. Na quarta linha colocar o endereço onde esta a segunda imagem, ex:"/home/user/picture/image2.png", sem as aspas

	5. Na quinta linha colocar a quantidade de interações do programa, ex:"10", sem as aspas
	
Depois de fazer isso execute o arquivo "foto.py".
Ao terminar a execução as fotos resultantes ficaram salvas no endereço especificado, dentro da pasta com o nome especificado e enumeradas de 1 até n, considerando que 1 é 100% da imagem 1 e 0% da imagem 2 e n é 0% da imagem 1 e 100% da imagem 2.

Obs: Quanto maior a resolução da imagem mais tempo vai passar para a imagem ser processada.
