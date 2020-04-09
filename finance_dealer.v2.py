#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando pacotes
import pandas as pd


# In[2]:


txt = open("extrato (12).rtf",newline = '\r').read()


# In[3]:


#Formatando as linhas
txt = (txt.split(sep = '\n')) 


# In[4]:


txt


# In[5]:


#Separando creditos e de qual seguradoras eles pertencem

creditos = []
seguradoras = []
contador = 0
for i in txt:        
    contador += 1
    if i[len(i)-1:] == 'C' and 'SALDO DO DIA' not in i:
        creditos.append(i)
        seguradoras.append(txt[contador])


# In[6]:


seguradoras


# In[7]:


creditos


# In[8]:


#Separando debitos e suas descrições
debitos = []
descricao_deb = []
contador = 0
for i in txt:
    if i[len(i)-1:] == 'D' and 'SALDO DO DIA' not in txt[contador+1]:
        debitos.append(i)
        descricao_deb.append(txt[contador+1])
    if i[len(i)-1:] == 'D' and 'SALDO DO DIA' in txt[contador+1]:
        debitos.append(i)
        descricao_deb.append('     VAZIO')
    contador += 1


# In[9]:


txt


# In[10]:


descricao_deb


# In[11]:


debitos


# # Trabalhando créditos

# In[12]:


#Agrupando cada crédito com sua respectiva seguradora
cred_e_seg = []
contador = 0
for i in range(len(creditos)):
    cred_e_seg.append(creditos[i] + seguradoras[i])


# In[13]:


cred_e_seg


# In[14]:


#Separando por seguradoras
porto = []
sulamerica = []
mapfre = []
azul=[]
suhai = []
tokio=[]
bradesco = []
liberty = []
hdi = []
ituran =[]
sompo = []
carro_facil = []

for i in cred_e_seg:
    if 'PORTO' in i and 'LOCADORA' not in i:
        porto.append(i)
    if 'PORTO' in i and 'LOCADORA' in i:
        carro_facil.append(i)
    if 'SUL AMERICA' in i:
        sulamerica.append(i)
    if 'MAPFRE' in i:
        mapfre.append(i)
    if 'AZUL' in i:
        azul.append(i)
    if 'SUHAI' in i:
        suhai.append(i)
    if 'TOKIO' in i:
        tokio.append(i)
    if 'BRADESCO' in i:
        bradesco.append(i)
    if 'LIBERTY' in i:
        liberty.append(i)
    if 'HDI' in i:
        hdi.append(i)
    if 'ITURAN' in i:
        ituran.append(i)
    if 'SOMPO' in i:
        sompo.append(i)


# In[15]:


#Juntando todos em lista unica
lista_seguradoras = [porto, sulamerica,mapfre,azul,suhai,tokio,bradesco,liberty,hdi,ituran,sompo,carro_facil]


# In[16]:


#Separando conteudo de cada transação
listagem = []
for j in lista_seguradoras:
    for i in j:
        listagem.append(i.split(sep = '     ')) 


# In[17]:


listagem


# In[18]:


#Transformando em DF
df = pd.DataFrame(listagem)


# In[19]:


#Criando coluna com a data da transação
for i in range(len(df[0])):
    df[0][i] = (df[0][i][:2])


# In[20]:


df


# In[21]:


#Dropando colunas desnecessárias
df.drop(columns = [1,2,5,6,7,8], inplace=True)


# In[22]:


df


# In[23]:


for i in range(len(df)):
    df[3][i] = df[3][i].strip('C')


# In[24]:


df


# In[25]:


df.to_csv('creditos.csv')


# # Trabalhando débitos

# In[26]:


debitos


# In[27]:


dia = []

for i in debitos:
    if 'PREVISÃO' in i:
        break
    
    cell = i[0] + i[1]
    
    dia.append(cell)


# In[28]:


descricao_lista = []

num = 12
for i in debitos:
    if 'PREVISÃO' in i:
        break
    cell = i[12]+i[13]+i[14]+i[15]+i[16]+i[17]+i[18]+i[19]+i[20]+i[21]+i[22]+i[23]+i[24]+i[25]+i[26]+i[27]+i[28]+i[29]+i[30]
    
    descricao_lista.append(cell)


# In[29]:


desc_deb = []

for i in descricao_deb:
    if ('PREVISÃO' in i):
        break
    desc_deb.append(i)


# In[30]:


valor = []

for i in debitos:
    if 'PREVISÃO' in i:
        break
    cell = ""
    cell = i[len(i)-9] + i[len(i)-8] + i[len(i)-7] + i[len(i)-6] + i[len(i)-5] + i[len(i)-4] + i[len(i)-3] + i[len(i)-2]
    
    valor.append(cell)


# In[31]:


#tira os Debitos duplicados na descricao
desc_deb2 = []

for i in desc_deb:
    if (i.endswith('D')==True):
        i = i[:i.rfind("D")-5]
    desc_deb2.append(i)


# In[32]:


debituuu = pd.DataFrame()


# In[33]:


debituuu["dia"] = dia
debituuu["descricao"] = descricao_lista
debituuu["descricao2"] = desc_deb2
debituuu["valor"] = valor


# In[34]:


debituuu


# In[35]:


debitos


# In[36]:


debituuu.to_csv('debitos.csv')


# In[37]:


debituuu.valor.sum(axis=0)


# In[ ]:




