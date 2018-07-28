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
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+file_to_be_checked) as response:

        output = response.read()
        print(output)

    if output == b'true':
        print('PROFANITY ALERT!')
    elif output == b'false':
        print('No Curse Words')
    else:
        print('Problem scanning Document')

read_file()

#
