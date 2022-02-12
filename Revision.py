import requests

response=requests.post('http://216.10.245.166/Library/Addbook.php',json={

"name":"Learn tteddt Automation with Java",
"isbn":"59309056",
"aisle":"227",
"author":"John foe"
},)

print(response.json())