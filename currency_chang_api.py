# import requests
# from pprint import PrettyPrinter

# # KEY = "9903d2391b72a4b331b5a616"
# printt = PrettyPrinter()
# BASE_URL = "https://v6.exchangerate-api.com/v6/9903d2391b72a4b331b5a616/latest"


# your_curreny = input(
#     "inter your curreny you have  ( EGP - ZWL  - SDG - ...ext ) ? "
# ).upper()
# convert_to = input(
#     "inter your curreny you want to convert  ( EGP - ZWL  - SDG - ...ext ) ? "
# ).upper()

# print(f'---------- convert form {your_curreny} to {convert_to} :) ')

# mony = float(input("Amount : "))

# def find_currency(currency,mony,convert):
#     printt.pprint('Loadding...')
#     full_url = f'{BASE_URL}/{currency}'
#     data = requests.get(full_url).json()
#     # print(data)

#     if convert in data["conversion_rates"]:
#         price = data["conversion_rates"][convert]
#         total = mony * price
#         return total
#     else:
#         print('not found')

# total =  find_currency(your_curreny, mony, convert_to)

# printt.pprint(f'your many = {total} {convert_to}')

dec = {"name":'mona',"age":20,'aisha':'yes'}
print(list(dec.values())[2])
print(dec.get('namee','not found'))
