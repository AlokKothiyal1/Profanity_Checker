import urllib.request

def read_file():
#-----------------------------------------------------------------------------
    file_doc = open("path to your file")     #Enter path to your file
#-----------------------------------------------------------------------------
    content = file_doc.read()
    print(content)
    file_doc.close()
    check_profanity(content)

def check_profanity(file_to_be_checked):
   def check_profanity(file_to_be_checked):
     file = requests.get("http://www.wdylike.appspot.com/?q="+file_to_be_checked)
     output = file.text
     print(output)

     if output == 'true':
        print('PROFANITY ALERT!')
     elif output == 'false':
        print('No Curse Words')
     else:
        print('Problem scanning Document')
read_file()

#
