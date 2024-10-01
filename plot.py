import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D  # ???
import numpy as np
sb.set_style('whitegrid')
def slider_callback():
    param = st.session_state['param']
    def FUNC_Z(x_plot, y_plot):
        return 50 - (x_plot**param + y_plot**param)
    num = 40
    x_plot1 = np.linspace(-4, 4, num)
    y_plot1 = np.linspace(-4, 4, num)
    plot1, plot2 = np.meshgrid(x_plot1, y_plot1)
    plot3 = FUNC_Z(plot1, plot2)
    fig = plt.figure(figsize=(10, 4))
    axes = fig.add_axes([-4, -4, 4, 4], projection='3d')
    axes.plot_surface(plot1, plot2, plot3)
    # plot.show ()
    st.pyplot(fig)
age = st.slider("Param?", 0, 4, 2,
                on_change=slider_callback,
                key='param')
st.write("I'm ", age, "years old")
