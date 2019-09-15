# CaseFox-Upload-Automation
A simple python script that automates the process of uploading the timesheet to CaseFox

If you are using CaseFox to record your work time, often time you might be using an Excel spreadsheet to record your time as well.
As for myself, I use a spreadsheet to record my time and upload the time to Case/Fox on a weekly basis.
However, it is not a pleasant process to manually copy and paste the time to CaseFox.

This script takes the columns in the spreadsheet and input the value to CaseFox.

## The process is simple:
1. Record your time on a spreadsheet
2. Run the script to upload the time
3. Done

The idea behind the script is to use a loop to read the value in the timesheet and find corresponding field on CaseFox.

## How to:
1. Before getting started, you will need to setup **Selenium** and your **browser driver**.
I am using Chrome so I have the Chrome driver installed and setup.
2. Make sure you have your time recorded in the spreadsheet appropriately so your script can read. If not, adjust the code in the script to match your need.
3. Run the script and you can sit back and enjoy a cup of coffee

