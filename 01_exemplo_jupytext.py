# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: projeto_novo
#     language: python
#     name: projeto_novo
# ---

# %% [markdown]
# Um exemplo simples abaixo:

# %%
2 + 2

# %% [markdown]
# O mesmo exemplo com a classe soma:

# %%
from exemplo import soma
resultado = soma(2, 2)
print(resultado)

# %%
import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)
plt.show()

# %%
