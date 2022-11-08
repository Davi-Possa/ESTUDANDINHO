### **IF – ELSE – ELIF**: 
Estrutura de condição, usada para que um determinado bloco de códigos, seja apenas executado se tal condição for verdadeira, falsa, ou algo determinado a ela.

Exemplo: 
```python
nota = float(input('Digite sua nota:'))

if (nota >= 7) and (nota <= 10):
	print("Aprovado")

elif (nota >= 0) and (nota <= 6):
	print("Reprovado")

else:
	print("Vai a MERDA!")
```

|=-=-=-=-=-=-=-=-=-=-=-=|

### **FOR – WHILE**: 
Estrutura de repetição, usada para quando é necessário repetir a execução de uma instrução, enquanto certa condição é atendida.

Exemplo: 
```python
x = int(input("Digite um valor para o contador:"))

while (x >= 1) and (x <= 20):
	print(x)
	x += 1
else:
	print("O contador acabou")
```
```python
comida = ['Xuxu', 'Pizza', 'Risoto', 'Churras']

for AEEEH in comida:
	print(AEEEH)

print("Acabou a comida")
```

|=-=-=-=-=-=-=-=-=-=-=-=|

### **RANGE**: 
Função, usada para retornar uma série numérica, quando o intervalo for enviado como argumento, o retornado será um objeto iterável tipo range, tendo seus elementos gerados sob demanda. 

Exemplo: 
```python
numero = int(input("Digite um numero que lhe darei a tabela:"))
i = 11

for tabela in range(i):
	multi = numero * tabela
	print(numero, "x", tabela, "=", multi)
```

|=-=-=-=-=-=-=-=-=-=-=-=|

### **LEN**: 
Função interna, usada para retornar o cumprimento de um determinado objeto, podendo contar o número de itens presentes em uma lista ou tupla.

Exemplo: 
```python
comida = ['Xuxu', 'Pizza', 'Risoto', 'Churras', 'Bacalhau']

print(comida, len(comida), "itens")
```

|=-=-=-=-=-=-=-=-=-=-=-=|

#### **BREAK - CONTINUE**:
Duas ferramentas da estrutura de repetição, 

#### **BREAK**: Interrompe o loop e encerra ele.

Exemplo:
```python
n = int(input("Digite um número:"))
x = 1
for x in range(n):
	print(x)

	if x >= 4:
		print("É os guri")
		break
```

#### **CONTINUE**: Interrompe o loop e continua ou vai para a próxima iteração.

Exemplo:
```python
n = 25
x = 1
for x in range(n):
	print(x)

	if x == 1 or x == 10 or x == 15 or x == 20 or x == 25:
		print("É os guri")
		continue
```

|=-=-=-=-=-=-=-=-=-=-=-=|

### **FUNÇÕES**:
Blocos de código, geralmente utilizadas para realizar determinada tarefa, repetidas vezes, com fim a evitar a repetição de um certo bloco de código.

Exemplo: 
```python
def salve(meu_nome,idade):
   print('Olá',meu_nome,'\nSua idade é:',idade)

salve('Davi', '16')
```

ou

```python
altura = int(input('Digite a altura do quadrado:'))
base = int(input('Digite o tamanho da base do quadrado:'))

area = altura * base

if altura == base:
	print("A área desse quadrado é:", area)

else:
	print("A área desse retangulo é:", area)
```

|=-=-=-=-=-=-=-=-=-=-=-=|

### **LISTA - TUPLAS - CONJUNTOS**: 
Estrutura de armazenamento de dados.

#### LISTA:
Representada por [], a lista é mutável, ordenada, permite elementos duplicados, armazena os elementos em uma única linha ou várias linhas e coluna, pode ser criada usando a função `nome_lista = ['item', 'outro item']`.

```python 
comida = ['Feijão', 'Arroz', 'Xuxu', 'Risoto']
print(comida)
```

#### METODOS DE LISTA:

list.**append**(x) - Adiçiona item a lista;
list.**remove**(x) - Remove item da lista;
list.**extend**(iterable) - Junta duas listas;
list.**insert**(i,x) - Adiçiona item a lista em uma determinada posição;
list.**pop**([i]) - Remove item da lista em uma determinada posição;
list.**clear**() - Remove todos os itens da lista;
list.**count**() - Conta a quantidade de vezes que o item aparece na lista;
list.**index**() - Informa indice do item determinado pelo usuário;
list.**sort**() - Ordena os itens de uma lista de acordo com a informação passada pelo usuário.
list.**reverse**() - Inverte a ordem da lista;
list.**copy**() - Faz a cópia rasa da lista.


#### TUPLA:
Representada por (), a tupla é imutável, ordenada, permite elementos duplicados, armazena os elementos em uma única linha ou várias linhas e coluna, pode ser criada usando a função `nome_tupla = ('item', 'outro item')`.

```python 
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)
```


#### CONJUNTO:
Representado por {}, o conjunto é mutavel, não ordenado, não permite elementos duplicados, armazena os elementos em uma única linha, pode ser criado usando a função `nome_conjunto = {'item', 'outro item'}`.

```python
conjunto = {'Arroz', 'Feijão', 'Xuxu'}
print(conjunto)
```

*Obs: Caso armazene um item repetido, ele irá retornar o conjunto, mas não irá imprimir tal item.*

|=-=-=-=-=-=-=-=-=-=-=-=|


