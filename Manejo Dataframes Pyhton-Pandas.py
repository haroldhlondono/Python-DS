#!/usr/bin/env python
# coding: utf-8

# # Manejo de Dataframes en Python-Pandas
# ## Censo de población 2018 por departamentos
# 

# ### Lo primero que se debe hacer es importar la librería Pandas

# In[37]:


import pandas as pd


# ### Se traen archivos DANE que están en CSV

# In[38]:


censo_Valle = pd.read_csv("/Users/hlondono/Desktop/Proyectos la cartilla/Tutorial proyectos/CensoSur/VIV_Valle.csv")


# In[39]:


censo_Cauca = pd.read_csv("/Users/hlondono/Desktop/Proyectos la cartilla/Tutorial proyectos/CensoSur/VIV_Cauca.csv")


# In[40]:


censo_Nariño = pd.read_csv("/Users/hlondono/Desktop/Proyectos la cartilla/Tutorial proyectos/CensoSur/VIV_Narino.csv")


# In[41]:


censo_Putumayo = pd.read_csv("/Users/hlondono/Desktop/Proyectos la cartilla/Tutorial proyectos/CensoSur/VIV_Putumayo.csv")


# ### Se revisa tamaño de archivos

# In[42]:


censo_Valle.shape


# In[43]:


censo_Cauca.shape


# In[67]:


censo_Nariño.shape


# In[69]:


censo_Putumayo.shape


# ### Se concatenan los archivos

# In[44]:


censo_Sur = pd.concat([censo_Valle, censo_Nariño, censo_Cauca, censo_Putumayo])


# ### Comandos para revisar Dataframe

# In[45]:


censo_Sur.shape


# In[46]:


censo_Sur.info()


# In[47]:


censo_Sur.head()


# In[48]:


censo_Sur.tail()


# In[49]:


censo_Sur.size


# In[50]:


censo_Sur.columns


# In[51]:


censo_Sur.describe()


# In[52]:


censo_Sur_index = censo_Sur.index


# In[53]:


censo_Sur.index


# In[54]:


censo_Sur.columns


# In[55]:


censo_Sur.values


# Data Types

# In[56]:


censo_Sur.dtypes


# In[57]:


censo_Sur.dtypes.value_counts()


# ### Contar elementos en la serie

# In[58]:


censo_Sur.shape


# In[59]:


len(censo_Sur)


# In[60]:


censo_Sur.size


# In[61]:


censo_Sur.count()


# ### Identificar y cambiar valores nulos

# In[62]:


censo_Sur.isnull()


# In[63]:


censo_Sur.isna().sum()


# In[64]:


censo_Sur["UVA2_CODTER"].hasnans


# ### Qué hacer si queremos cambiar los NaN

# In[71]:


import numpy as np


# Recomedable crear copia de archivo original para trabajar sobre él

# In[72]:


censo_Sur1 = censo_Sur


# In[73]:


censo_Sur1.shape


# In[74]:


censo_Sur.shape


# Una opción es eliminar las filas donde hay NaN

# Ejemplo 

# In[88]:


from numpy import nan as NA


# In[91]:


data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA],[NA, 6.5, 3.]])

data


# In[93]:


datos_limpios = data.dropna()
datos_limpios


# In[96]:


censo_Sur1_limpio = censo_Sur1.dropna()
censo_Sur1_limpio.head()


# In[97]:


data.dropna(how="all")


# In[98]:


censo_Sur1.dropna(how="all")


# In[100]:


#eliminar columnas

data[4] = NA
data


# In[101]:


data.dropna(axis=1, how="all")


# Rellenar datos

# In[102]:


data.fillna(0) #rellena con cero


# In[113]:


data.fillna({0: 8.5, 1: 1.5, 2: 3})


# In[115]:


censo_Sur1.fillna(0)


# In[116]:


censo_Sur1


# Eliminar duplicados ???

# In[ ]:





# ### Limpieza de datos

# Consejo: trabajar únicamente con columnas que vamos a trabajar

# In[ ]:




