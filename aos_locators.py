from faker import Faker

fake = Faker(locale='en_CA')

# ------------------ locators section-------------------------------
app = 'Advantage Online Shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = ' Advantage Shopping'
aos_add_user = 'https://advantageonlineshopping.com/#/register'
aos_add_user_title = ' Advantage Shopping'

# -------------------- data section ---------------------------------
firstname = fake.first_name()
lastname = fake.last_name()
phone = fake.phone_number()
username = f'{firstname}{lastname}'.lower()[:10]
password = fake.password()
confirm_password = f'{password}'
email = fake.email()
country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postcode = fake.postcode()

print(firstname, lastname, phone, username, password, email)
