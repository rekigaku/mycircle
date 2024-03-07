import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming the CSV file 'Data_circle.csv' is correctly formatted and accessible
data = pd.read_csv('Data_circle.csv')

def main():
    # Display the app's title and description on the main page
    st.title('Orbit Cross')
    st.markdown("""
    **At the moment when individualities intersect, new possibilities are created.**  
    <small>個性の交差する瞬間に、新たな可能性が創出される。</small>

    **Let's cherish our unique paths of thought and action, and find crosspoints with others.**  
    <small>独自の思考と行動の軌道を大切にし、他者とのクロスポイントを見つけましょう。</small>
    """, unsafe_allow_html=True)

# Adding color descriptions
    st.markdown("""
    <small>
    Others1: Light Cyan<br>
    Others2: Apricot<br>
    Others3: Canary Yellow<br>
    Others4: Light Green<br>
    Others5: Terracotta<br>
    Others6: Lavender Pink
    </small>
    """, unsafe_allow_html=True)


    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Sidebar inputs for Core Person and Others' Birthdays
    user_input = st.sidebar.text_input('Core Person(中軸者) Birthdayを入力ください。(ex: 1925/1/1)', '')

    additional_birthdays = []
    colors = ['#BDE4ED', '#F5CAC2', '#FFF497', '#B5D58A', '#F8C189', '#D1A8C4']
    for i in range(6):
        birthday = st.sidebar.text_input(f'Others{i+1}: Birthday (ex: 1925/1/1)', key=f'user_{i+1}')
        additional_birthdays.append(birthday)

    # Plotting section
    if user_input or any(additional_birthdays):
        fig, ax = plt.subplots()

        # Draw the Core Person's triangle
        if user_input:
            draw_triangle(user_input, "#DF9D42", ax, filled=True)

        # Draw Others' triangles
        for i, birthday in enumerate(additional_birthdays):
            if birthday:
                draw_triangle(birthday, colors[i], ax, filled=False)

        finalize_plot(ax)
        st.pyplot(fig)

def draw_triangle(birthday, color, ax, filled=False):
    # Ensure 'key' matches your CSV column name for birthday or unique identifier
    row = data[data['key'] == birthday]
    if not row.empty:
        marks = [row['num1'].values[0], row['num2'].values[0], row['num3'].values[0]]

        points = []
        for mark in marks:
            angle = 2 * np.pi * ((15 - (mark - 1)) / 60)
            x = 0.5 + 0.4 * np.cos(angle)
            y = 0.5 + 0.4 * np.sin(angle)
            points.append((x, y))

        if filled:
            triangle = plt.Polygon(points, edgecolor=color, facecolor=color)
        else:
            triangle = plt.Polygon(points, edgecolor=color, facecolor='none')
        
        ax.add_artist(triangle)

def finalize_plot(ax):
    circle_color = "#d8d7cd"
    axis_color = "#d8d7cd"
    
    circle = plt.Circle((0.5, 0.5), 0.4, fill=False, color=circle_color, linewidth=1)
    ax.add_artist(circle)

    for i in range(4):
        angle = np.pi / 2 * i
        x = 0.5 + 0.4 * np.cos(angle)
        y = 0.5 + 0.4 * np.sin(angle)
        ax.plot([0.5, x], [0.5, y], color=axis_color, linewidth=1)


    # Set plot properties
    ax.set_aspect('equal')
    plt.axis('off')

# Run the app
if __name__ == '__main__':
    main()
