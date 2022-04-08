import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
# print( df.groupby(["student_id", "level"], as_index=False)["attempt"].mean())
fig = px.scatter(
    mean, 
    x="student_id", 
    y="level", 
    size="attempt", 
    color="attempt",
    title='Student Levels chart',
    labels={
        'student_id':"Student's ID",
        'level':'Levels',
        'attempt':'Attempts'
        })

fig.update_layout(
    title_text='Student Levels chart', 
    title_x=0.5,
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    font_family="Courier New",
    font_color="black"
    )
fig.show()