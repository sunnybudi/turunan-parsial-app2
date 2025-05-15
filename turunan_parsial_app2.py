import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("📈 Aplikasi Turunan Parsial")

# Mendefinisikan simbol x dan y
x, y = sp.symbols('x y')

# Input fungsi dari pengguna
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**3 + y + y**2")

try:
    # Mengubah string fungsi menjadi ekspresi simbolik
    f = sp.sympify(fungsi_str)

    # Turunan parsial terhadap x dan y
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Tampilkan fungsi dan turunannya
    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    # Input titik (x0, y0)
    x0 = st.number_input("Nilai x₀:", value=1.0)
    y0 = st.number_input("Nilai y₀:", value=2.0)

    # Evaluasi fungsi dan turunan di titik (x0, y0)
    f_val = f.subs({x: x0, y: y0})
    fx_val = fx.subs({x: x0, y: y0})
    fy_val = fy.subs({x: x0, y: y0})

    # Tampilkan hasil evaluasi
    st.write(f"Nilai fungsi di titik (x₀, y₀): {f_val}")
    st.write(f"Gradien di titik (x₀, y₀): ({fx_val}, {fy_val})")

    # Buat grafik permukaan dan bidang singgung
    st.subheader("Grafik Permukaan & Bidang Singgung")

    x_vals = np.linspace(x0 - 2, x0 + 2, 50)
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Konversi fungsi ke fungsi numerik
    f_lambdified = sp.lambdify((x, y), f, 'numpy')
    Z = f_lambdified(X, Y)

    # Hitung bidang singgung secara numerik
    Z_tangent = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

    # Plot menggunakan matplotlib
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis', label='Permukaan')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red', label='Bidang Singgung')
    ax.set_title("Permukaan f(x, y) dan bidang singgungnya")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
