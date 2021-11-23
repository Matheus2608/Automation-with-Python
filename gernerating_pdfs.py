# There's a few tools in Python that let you generate PDFs with the content that you want. Here, we'll learn about one of them: ReportLab.

# Let's say that I have an awesome collection of fruit, and I want to create a PDF report of all the different kinds of fruit I have! I can easily represent the different kinds of fruit and how much of each I have with a Python dictionary. It might look something like this:

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.platypus import SimpleDocTemplate
fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

report = SimpleDocTemplate("/report.pdf")

# Now, let's add some content to it!
# For that, we're going to use what reportlab calls Flowables. Flowables are sort of like chunks of a document that reportlab can arrange to make a complete report. Let's import some Flowable classes.


# We have to tell reportlab what style we want each part of the document to have, so let's import some more things from the module to describe style.
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
# report.build([report_title])

# To make a Table object, we need our data to be in a list-of-lists
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
# graphs

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report_pie = Pie(width=3*inch, height=3*inch)

# To add data to our Pie chart, we need two separate lists: One for data, and one for labels. Once more, we’re going to have to transform our fruit dictionary into a different shape. For an added twist, let's sort the fruit in alphabetical order

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# The Pie object isn’t Flowable, but it can be placed inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])

# Alright, and with that, you've seen a few examples of what we can do with the ReportLab library.  There's a ton more things that can be done that we won't cover here. You'll want to refer to the ReportLab User Guide for more details on the features we've seen, and to see what else you can create with it. https://www.reportlab.com/docs/reportlab-userguide.pdf
