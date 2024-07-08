import math

#Separador
nome = 'luan@rodrigues'
print(nome.split('@'))

#Divisao inteira
numero1 = int(input("Inserir numero inteiro: "))
numero2 = int(input("Inserir numero inteiro: "))
resultado = numero1 // numero2
print(resultado)

#cauclo do raio com duas casas decimais
raio_circulo = float(input("digite o raio: "))
area_circulo = math.pi * raio_circulo ** 2

#metodo antigo
area_circulo_formatada = "{:.2f}".format(area_circulo)
print(area_circulo_formatada)

#novo
print(f"{area_circulo:.2f}" )

data_usuario = input('Insira uma data no formato dd/mm/aaaa: ')
lista_dia_mes_ano = data_usuario.split("/")
print(f"O elemento 1 da lista é o:  {lista_dia_mes_ano[0]}")
print(f"O elemento 1 da lista é o:  {lista_dia_mes_ano[1]}")
print(f"O elemento 1 da lista é o:  {lista_dia_mes_ano[2]}")


