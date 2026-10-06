import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Esercizio 1
arr= np.arange(1,11)

quadrati= arr**2
cubi= arr**3

df= pd.DataFrame({
     "Numero":arr,
     "Quadrato": quadrati,
     "Cubi": cubi
 })

print(df)


plt.plot(df["Numero"],df["Quadrato"],label= "Quadrati")
plt.plot(df["Numero"],df["Cubi"],label= "Cubi") 
plt.xlabel("Numero")
plt.ylabel("Valore")
plt.title("Quadrati e Cubi")
plt.legend()
plt.show()

#Esercizio 2

date = pd.date_range(start="2026-04-01",periods=30,freq="D")
print(date)
valori=np.random.rand(30)
print(valori)

df=pd.DataFrame({
    "Valore":valori},
    index=date
)

print(df)

plt.plot(
    df.index, df["Valore"], marker="o", color="blue"
)
plt.xlabel("Date")
plt.ylabel("Valore")
plt.title("Valori casuali nel tempo")
plt.xticks(rotation=45) 
plt.tight_layout()  
plt.show()