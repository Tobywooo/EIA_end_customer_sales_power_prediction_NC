# EIA_end_customer_sales_power_prediction_NC
UNCC DSBA 5122 &amp; 6276 Class project. U.S Energy Information Administration data. Megawatt hours sold for Electricity sales for ultimate customers for the state of NC. This repository is a personal repo to hold data for power prediction projects on this data that will be used across multiple classes/projects

In order to commit code github via VSCode, make sure to do the following commmands 

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

***GET STARTED***
If you are in VSCode, create a virtual environment to isolate your installations and workflow.
  *python -m venv .venv* 
  *\.venv\Scripts\Activate.ps1*
  
If you are in google colab, mount your drive and run the notebook that way
  -Instructions not provided here because im lazy

***IF YOU HAVE ISSUES WITH PYTHON PACKAGES***
MAKE SURE TO SELECT YOUR INTERPRETER WITH ctrl+shift+p -> Python:Select Interpreter -> Enter Interpreter Path -> Browse to \EIA_end_customer_sales_power_prediction_NC\.venv\Scripts

***GET TO KNOW THE DATA***
In the notebook analysis/starter_analysis, this is a starter notebook with code that shows you how I view the data. Read this file for information on the version 1 data. 

***GETTING DATA READY FOR MODELING***
check out the ETL.ipynb notebook under the analysis directory to test logic for a dataset for your modeling
Add your ETL.ipynb logic into the ETL_modeling_methods.py if you want to use an organized directory for calling methods
