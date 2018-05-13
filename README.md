# urlValidator
This project helps in building a http proxy which will help us to determine if a given http url is safe to access or not with proper response message

Objective:
 The Objective of the project is to determine the benignity of the URL by lexically identifying, if is a known URL with potentially malicous content. This is acheived by passing the URL via a GET request to an AWS Lambda Webservice, which will compare the URL which comes as params and headers of the incoming GET Request with the available blacklisted host from the Database.

Prerequisites:
 Before executing the below steps make sure you have python 3 installed in your system

Steps to perfom:

1,Clone the repository and navigate to the 'urlValidator' directory: 

  $ git clone https://github.com/Fayazdeen/urlValidator.git
  
  $ cd urlValidator/
  
2,Execute the python file:

  $ python TestScript.py
  
3,Pass the http url to be tested(make sure you give the http:// prefix):

  $ Enter the HTTP URL:https://www.myflowertree.com/flowers
  
4,You will receive the following Message:

  $ {"URL": "www.myflowertree.com/flowers", "Message": "The URL is safe to access"}
  
