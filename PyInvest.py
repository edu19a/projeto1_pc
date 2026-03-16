import math as m
import random as r
import statistics as s
import locale as l
import datetime as d

#CONFIGURAÇÃO LOCALE
l.setlocale(l.LC_ALL, 'pt_BR.VTF-8')

#ENTRADAS
cp = float(input('Capital inicial (R$): '))
ap = float(input('Aporte mensal (R$): '))
ms = int(input('Prazo do investimento (em meses): '))
cdi = float(input('CDI anual (%): ')) / 100
cdb = float(input('Percentual do CDI aplicado ao CDB (%): ')) / 100
lci = float(input('Percentual do CDI aplicado à LCI (%): ')) / 100
t = float(input('Rentabilidade mensal esperada do FII (%): ')) / 100
mt = float(input('Meta financeira desejada (R$): '))

#CÁLCULOS
#CDI mensal composto
cdi_mensal = m.pow((1 + cdi), 1 / 12) - 1

#Total investido
total_investido = cp + (ap * ms)

#CDB
taxa_cdb = cdi_mensal * cdb
montante_cdb_bruto = (cp * m.pow((1 + taxa_cdb), ms) + (ap * ms))
lucro_cdb = montante_cdb_bruto - total_investido
montante_cdb = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * lci
montante_lci = (cp * m.pow((1 + taxa_lci), ms) + (ap * ms))

#Poupança
montante_poupanca = (cp * m.pow((1 + 0.005), ms) + (ap * ms))

#FII
base_fii = cp * m.pow((1 + t), ms) + (ap * ms)
sim1 = base_fii * (1 + r.uniform(-0.03, 0.03))
sim2 = base_fii * (1 + r.uniform(-0.03, 0.03))
sim3 = base_fii * (1 + r.uniform(-0.03, 0.03))
sim4 = base_fii * (1 + r.uniform(-0.03, 0.03))
sim5 = base_fii * (1 + r.uniform(-0.03, 0.03))

fii_media   = s.mean((sim1, sim2, sim3, sim4, sim5))
fii_mediana = s.median((sim1, sim2, sim3, sim4, sim5))
fii_desvio  = s.stdev((sim1, sim2, sim3, sim4, sim5))

#Datas
data_simulacao = d.datetime.now().strftime('%d/%m/%Y')
data_resgate   = (d.datetime.now() + d.timedelta(days=ms * 30)).strftime('%d/%m/%Y')

#RELATÓRIO FINAL
print("Simulador de Investimentos")
print("=" * 50)
print(f"Data da simulação: {data_simulacao}")
print(f"Data estimada de resgate: {data_resgate}")
print("=" * 50)
print(f"Total investido: {l.currency(total_investido, grouping=True)}")
print("RESULTADOS FINANCEIROS")

#CDB
print(f"CDB: {l.currency(montante_cdb, grouping=True)}")
print('#' * int(montante_cdb // 1000))

#LCI
print(f"LCI: {l.currency(montante_lci, grouping=True)}")
print('#' * int(montante_lci // 1000))

#Poupança
print(f"Poupança: {l.currency(montante_poupanca, grouping=True)}")
print('#' * int(montante_poupanca // 1000))

#FII
print(f"FII (média): {l.currency(fii_media, grouping=True)}")
print('#' * int(fii_media // 1000))
print("ESTATISTICAS FII")
print(f"Mediana: {l.currency(fii_mediana, grouping=True)}")
print(f"Desvio padrão: {l.currency(fii_desvio, grouping=True)}")

#Meta
print(f"Meta atingida? {fii_media >= mt}")
print("=" * 50)
