import requests

country_url = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"
response = requests.get(country_url)
country_data = response.json()

country_to_find = input("Please enter the country you wish to find: ")
for country in country_data:
    if country["name"]["common"] == country_to_find or country["name"]["official"] == country_to_find:
        country_name = country["name"]["official"]
        country_capital = country["capital"][0]
        country_currency = ""
        for currency in country["currencies"]:
            if country_currency == "":
                country_currency = currency
            else:
                country_currency = f'{currency}, {country_currency}'

        print(f'{country_name}: the capital is {country_capital} and the official currency is {country_currency}.')
