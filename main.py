# API - https://api.opencovid.ca/
# CANADIAN (AS OF RIGHT NOW) COVID-19 CASE DATA
# CREATED BY LAM, ADRIAN & PATEL, HARSH

# IMPORTS
import requests

# ASCII ART / WELCOME
print('''
 ██████╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
██║     ███████║██╔██╗ ██║███████║██║  ██║██║███████║██╔██╗ ██║
██║     ██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██╔══██║██║╚██╗██║
╚██████╗██║  ██║██║ ╚████║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                               
 ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗      ██████╗ █████╗ ███████╗███████╗███████╗
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║    ██║     ███████║███████╗█████╗  ███████╗
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║    ██║     ██╔══██║╚════██║██╔══╝  ╚════██║
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝    ╚██████╗██║  ██║███████║███████╗███████║
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                                                                   ''')
# DEFAULT API
custom_api = 'https://api.opencovid.ca/'

# DEFINE NULL OBJECT
covid_data = None

# USER CHOICE TO START
choice = input("Fetch data from API/URL? y/n\n")

# while loop
while choice != 'y' and choice != 'n':
    choice = input("\nInvalid entry! Enter either: y/n\n")

if choice == 'n':
    exit()

# MAIN FUNCTION
def main_func():
    choice = True

    while choice == True: # while loop
        try: # REQUEST DATA
            covid_data = requests.get(custom_api)
            print("\nData fetched from https://api.opencovid.ca/!\n")
            covid_data = covid_data.json() # CONVERT TO JSON FILE
            covid_summary = covid_data['summary']
            
            for item in covid_summary: # EXTRACTING DATA FROM DICTIONARY
                print('Date of Data:', item['date'])
                print('Total Cases:', item['cumulative_cases'])
                print('Total Deaths:', item['cumulative_deaths'])
                print('Total Recovered:', item['cumulative_recovered'])
                print('Total Tested:', item['cumulative_testing'])
                break
            break

        except: # FAILED REQUEST DATA
            print("Error occurred while fetching data.")
            choice = input("\nRetry? y/n\n")
            choice.islower()
            if choice == 'y':
                main_func()
            elif choice == 'n':
                break

# MAIN PROGRAM
main_func() # CALL IN MAIN FUNCTION
 

                    
