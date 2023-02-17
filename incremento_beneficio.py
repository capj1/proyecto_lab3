#!/usr/bin/env python
# coding: utf-8

# In[151]:


import pandas as pd
import numpy as np
import datetime
from dateutil import relativedelta

def incremento_beneficio(fecha_inicio,edad,incremento,fecha_corte="01-06-2022",omega=115):
    #fecha corte default: 1ro de junio 2022
    #se asume que ya cumplió años en el presente mes

    meses_restantes=12*(omega-edad)

    fechainicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
    fechacorte = datetime.datetime.strptime(fecha_corte, "%d-%m-%Y")
    deltaa = relativedelta.relativedelta(fechacorte, fechainicio)
    meses_entre_fechas=deltaa.years*12+deltaa.months+1

    longitud_vector=min(meses_restantes,meses_entre_fechas)

    incremento_1=1+incremento

    fechainicio_mes=fechainicio.month
    mes_quiebre=fechainicio_mes % 12
    vector=np.zeros(longitud_vector)


    comp_meses=12-mes_quiebre
    periodos=int(longitud_vector/12)

    for i in range(0,longitud_vector):
        vector[i]=(incremento_1)**(int((i+mes_quiebre)/12))
    
    for i in range(0,periodos):
        vector[(12*i+comp_meses)]=2*vector[(12*i+comp_meses-1)]

    return(vector)


# In[147]:


incremento_beneficio("01-02-2020",57,0.06)


# In[148]:


incremento_beneficio("01-02-2019",114,1)


# In[149]:


incremento_beneficio("01-02-2021",70,.0000001)


# In[ ]:




