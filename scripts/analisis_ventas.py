
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datos/ventas.csv')

df['total'] = df['cantidad'] * df['precio']

ventas_totales = df['total'].sum()

print("Ventas totales:", ventas_totales)

ventas_producto = df.groupby('producto')['total'].sum()

ventas_producto.plot(kind='bar')

plt.title('Ventas por producto')

plt.savefig('../resultados/grafico_ventas.png')
