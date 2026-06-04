# 20260601-DE5M5
for data engineering apprenticeship module 5


Scenario:
A library wants to replace its slow, manual spreadsheet reviews with an automated data pipeline. A brief inspection of the library's raw data shows severe data quality issues that make manual reporting unreliable. 

Preliminary issues spotted:
1. Erroneous dates e.g. 10/04/2063 and 32/05/2023
2. Similar to #1 there are some return dates listed as prior to checkout dates
3. Formatting issues such as dates being surrounded by excess speechmarks
4. Many blank rows at bottom of file
5. Duplicated entries e.g. Little Women which shows twice with all the same field values
6. Missing references e.g. The Hobbit was checked out to customer ID 4 but this was not in the customer data

Solution will be to automatically clean the data every time the data updates, ensuring that a reliable dataset is sent to Power BI for reporting. 


User Stories or Backlog:
1. As a data analyst for the library I want to work with clean core data, without duplicate records, trailing blank spaces and extra speech marks so that the core dataset is clean.
2. As a data analyst for the library I want erronenous dates such as impossible dates and chronologically impossible dates filtered out so that that data is realistic.
3. As a data engineer I want a workflow to run automated tests and clean the data automatically so that zero manual effort is required. 
4. As a library manager I want clean and reliable data fed into a Power BI visual so that I can see accurate metrics.


Solutions Diagram:
![Solutions Diagram](Images/Solutions%20Diagram.drawio.png)

Dashboard Screenshot:
![Dashboard Screenshot](Images/Dashboard.png)
