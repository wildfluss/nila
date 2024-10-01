import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D  # ???
import numpy as np
def FUNC_Z(x_plot, y_plot):
    return 50 - (x_plot**2 + y_plot**2)
sb.set_style('whitegrid')
num = 40
x_plot1 = np.linspace(-4, 4, num)
y_plot1 = np.linspace(-4, 4, num)
plot1, plot2 = np.meshgrid(x_plot1, y_plot1)
plot3 = FUNC_Z(plot1, plot2)
fig = plt.figure(figsize=(10, 4))
axes = fig.add_axes([-4, -4, 4, 4], projection='3d')
axes.plot_surface(plot1, plot2, plot3)
# plot.show ()
age = st.slider("How old are you?", 0, 130, 25)
# st.write("I'm ", age, "years old")
st.pyplot(fig)
