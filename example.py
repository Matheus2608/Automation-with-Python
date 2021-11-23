#!/usr/bin/ev python3

import emails
import os
import reports

table_data = [
    ["Name", "Amount", "Value"],
    ["elderberries", 10, 0.45],
    ["figs", 5, 3],
    ["apples", 4, 2.75],
    ["durians", 1, 25],
    ["bananas", 5, 1.99],
    ["cherries", 23, 5.80],
    ["grapes", 13, 2.48]]

reports.generate("./automatingRealWorldTasks/project3/tmp/report.pdf", "A Complete Inventory of Myfruit",
                 "This is all my fruits", table_data)

"""sender = "sender@example.com"
receiver = "{}@example.com".format(os.environ.get("USER"))
subject = "List of fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body,
                          "/automatingRealWorldTasks/project3/tmp/report.pdf")
emails.send(message)"""
