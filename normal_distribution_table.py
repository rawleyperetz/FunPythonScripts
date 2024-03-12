# A python code that generates the standard normal distribution table in [-4,4]
import numpy as np
from scipy.integrate import quad
import pandas as pd

# Normal Distribution ~ N(0,1)
horizontal = np.linspace(0.0,0.1,11)
print(horizontal)
vertical = np.linspace(-4,4.0,81)
print(vertical)

def cum_normal(x):
    return (1/np.sqrt(2*np.pi))*np.exp((-1/2)*pow(x,2))

val = []
for i in vertical:
    for j in horizontal:
        x = i+j
        if x <=0:
            integrand = quad(cum_normal, x, np.Inf)
            val.append(1 - float(round(integrand[0],4))) 
        else: 
            integrand = quad(cum_normal, x, np.Inf)
            val.append(float(round(integrand[0],4)))

val = np.array([val], dtype='f').reshape(-1,11)
print(val)

into_df = pd.DataFrame(data=val,columns=horizontal, index=vertical)
print(into_df)
