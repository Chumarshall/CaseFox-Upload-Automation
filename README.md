# CaseFox-Upload-Automation
A simple python script that automates the process of uploading the timesheet to CaseFox

If you are using CaseFox to record your work time, it can be a tedious process to make sure you record your time properly. Im my case, I used to document my time in an Excel spreadsheet and manually upload the time to CaseFox on a weekly basis.
However, manual work is one of the biggest enemies of efficiency.

So I played around and built my first Python automation script using selenium. 

The idea behind the script is to use a loop to read the value in the timesheet and find the corresponding field on the CaseFox website.

## How to:
1. Before getting started, you will need to set up **Selenium** and your **browser driver**.
I am using Chrome so I have the Chrome driver installed and setup.
2. Make sure you have your time recorded in the spreadsheet appropriately so your script can read. If not, adjust the code in the script to match your need.
3. Run the script and you can sit back and enjoy a cup of coffee

