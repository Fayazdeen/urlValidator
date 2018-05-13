# urlValidator
This project helps in building a http proxy which will help us to determine if a given http url is safe to access or not with proper response message

Objective:
 The Objective of the project is to determine the benignity of the URL by lexically identifying, if is a known URL with potentially malicous content. This is acheived by passing the URL via a GET request to an AWS Lambda Webservice, which will compare the URL which comes as params and headers of the incoming GET Request with the available blacklisted host from the Database.
