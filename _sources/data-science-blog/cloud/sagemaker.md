
# AWS Sagemaker

## AWS Sagemaker Serverless

Major cost savings on ML endpoints with AWS Sagemaker!

-   In the past when you deploy an ML model as a Real-Time Inference
    endpoint on Sagemaker, you’ve had to keep the deployment instance
    running 24\*7
-   This is a waste of money if your ML model receives sporadic traffic
    with some periods of 0 traffic as your instance is running idle

Enter Sagemaker serverless!

-   During times when there is no traffic, Serverless Inference scales
    your endpoint down to 0, helping you to minimize your costs!
-   There will be some cold start when there is traffic after a long
    period of inactivity. In my experience with scikit-learn models, the
    cold start is &lt;2s!
-   Implement with just one line of code change

📖 Docs:
<https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html>

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:77.70270270270271%"></div><iframe width="740" height="575" title="Code snippet - sagemaker_serverless" src="https://snappify.io/embed/0183efa9-d63a-405a-ba15-6eb1d7a8c5d3?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>

## AWS Sagemaker Inference

AWS Sagemaker is one of the easiest ways I’ve come across for deploying
Machine Learning models as a Data Scientist.

-   [x] Create a simple `serve.py` file with just four functions
-   [x] model\_fn: To load the model from a file
-   [x] input\_fn: Convert input JSON data into a pandas dataframe. Do
    any other preprocessing BEFORE model predictions here
-   [x] predict\_fn: Run the model predictions
-   [x] output\_fn: Post-process the predictions and convert them to
    JSON
-   [x] As a pre-requisite, your trained model should be zipped as a
    tar.gz file on S3

Use the same `http://serve.py` for all of the below deployment methods!

-   [x] Real-time inference
-   [x] Multi-model endpoint
-   [x] Serverless inference (the topic of yesterday’s post)
-   [x] Batch transform

The entire process is massively simplified if you use the JSON lines
format (a topic for another post).

📖 Docs:
<https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html>

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:67.56756756756756%"></div><iframe width="740" height="500" title="Code snippet - sagemaker_serve.py" src="https://snappify.io/embed/eb166da8-d11e-4192-ac64-36499dae6c89?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>
