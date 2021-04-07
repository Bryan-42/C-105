import csv
import pandas as pd
import plotly.express as px

with open("class2.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

totalMarks = 0
nStudents = len(file_data)

for x in file_data:
    totalMarks += float(x[1])

mean = totalMarks / nStudents

df = pd.read_csv("class2.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks")
fig.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean,
        y1 = mean,
        x0 = 0,
        x1 = nStudents,
    )
])
fig.show()