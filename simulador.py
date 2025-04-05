import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎡 Simulador de Capacidad del Carrusel de Equipaje")

st.markdown("Simula la capacidad del carrusel con parámetros personalizables y visualiza resultados con Monte Carlo.")

# Entradas del usuario
v_min = st.slider("Velocidad mínima (m/min)", 5, 20, 8)
v_max = st.slider("Velocidad máxima (m/min)", v_min, 30, 15)
t_min = st.slider("Tiempo mínimo (min)", 10, 60, 30)
t_max = st.slider("Tiempo máximo (min)", t_min, 120, 90)
d_min = st.slider("Distancia mínima entre maletas (m)", 0.2, 1.0, 0.5)
d_max = st.slider("Distancia máxima entre maletas (m)", d_min, 2.0, 1.0)
p_min = st.slider("Porcentaje mínimo NO retirado", 0.0, 0.5, 0.05)
p_max = st.slider("Porcentaje máximo NO retirado", p_min, 0.9, 0.25)

n = st.number_input("Número de simulaciones", min_value=100, max_value=100000, value=5000)

# Simulación Monte Carlo
V = np.random.uniform(v_min, v_max, n)
T = np.random.uniform(t_min, t_max, n)
D = np.random.uniform(d_min, d_max, n)
P = np.random.uniform(p_min, p_max, n)

C = (V * T / D) * (1 - P)

# Resultados
st.metric("Capacidad Promedio", f"{np.mean(C):.0f} maletas")
st.metric("Capacidad Máxima", f"{np.max(C):.0f}")
st.metric("Capacidad Mínima", f"{np.min(C):.0f}")

# Histograma
fig, ax = plt.subplots()
ax.hist(C, bins=50, color='skyblue', edgecolor='black')
ax.set_title("Distribución de la Capacidad (Monte Carlo)")
ax.set_xlabel("Capacidad (maletas)")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
