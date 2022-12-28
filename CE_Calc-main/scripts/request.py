from html_to_list import parsers
import requests
import json

# Function for csv generation
# def csv_generator(header,data,fileName="unknowm.logs"):
#     with open(f"logs\{fileName}.csv", 'a', encoding='UTF8') as f:
#         writer = csv.writer(f)
#         writer.writerow(header)
#         for row in data:
#             writer.writerow(row)
        
        # writer.writerow(["This", "Above", "CSV", "Data", "Was", "Added", "At", datetime.now()])
        # writer.writerow([])
#         writer.writerow([])

#     return f"logs\{fileName}.csv"


for parser in parsers:
        data = parser.get_ru()
        muid = data[0][-1]
        print("**************Status OF RU***********")
        data = json.dumps(data)
        response = requests.post('http://127.0.0.1:8000/api/post_br_data/', data)
        print(response.status_code)
        print(response.text)

        data = parser.get_bu()
        print("**************Status OF BU***********")
        data = json.dumps(data)
        response = requests.post('http://127.0.0.1:8000/api/post_br_data/', data)
        print(response.status_code)
        print(response.text)

        # last_timestamp =  requests.get(f'http://127.0.0.1:8000/api/get_br_data/{muid}/lts').text
        # print(f"Last Time Stamp for '{muid}' is = {last_timestamp} \n\n")