import requests
import sys



def init():
	URL=input("Enter the HTTP URL:")
	URL_sliced=URL.split('/')
	try:
	 hostname_and_port=URL_sliced[2]
	except Exception as Message:
	 if str(Message.args[0]) == 'list index out of range':
	  print("Enter the URL with http:// prefix : Retry with new request")
	  sys.exit(0)
	original_path_and_query_string_str=str(URL_sliced[3:])
	original_path_and_query_string_str_final=original_path_and_query_string_str.replace("'","")
	print("hostname_and_port",hostname_and_port)
	print("original_path_and_query_string",str(original_path_and_query_string_str_final))
	count_of_q_path= len(URL_sliced[3:])
	print("Length",count_of_q_path)
	baseurl='https://98qj5ijvik.execute-api.us-east-2.amazonaws.com/urlValidator/urlinfo/1/'+ str(hostname_and_port) + '/' + str(count_of_q_path)

	headers = {
	'original_path_and_qs': str(original_path_and_query_string_str_final)

	}

	print('\n****************************************************\n')
	print(baseurl)
	r = requests.get(baseurl,headers=headers)
	res=str(r)
	print( r.text)

if __name__ == '__main__':
	init()
