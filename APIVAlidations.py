import requests
import json
response = requests.get('http://216.10.245.166/Library/GetBook.php',
                      params={'AuthorName':'Rahul Shetty'},)


dict_response=json.loads(response.text)


for i in range(len(dict_response)):
    if dict_response[i]['isbn']=='RGHCC':
        print(i)


for book in dict_response:
    if book['isbn']=='RGHCC':
        print(book)
        break
expectedbook={
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "2223355"
    }

assert book==expectedbook
