from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

process_data = True

print('Please snure that you are connected to the internet.\n')

# User enters details
first_name = input('Enter your first name: \n')
last_name = input('Enter your last name: \n')

while process_data:
    email = input('Enter your email: \n')
    email_confirmation = input('Confirm your email: \n')

    if email_confirmation != email:
        print('Your emails are not the same. Try again')
    else:
        data_mamager = DataManager()
        
        try:
            user_data = data_mamager.users
            
            # get all user emails an store in a list
            email_list = [user['email'] for user in user_data]
            
            if len(user_data) > 0:
                if email in email_list:
                    print('This email already exists. Try a different one')
                else:
                    # update the google sheets with the user data
                    data_mamager.add_new_users(first_name=first_name, last_name=last_name, email=email)
                    
                    print('\nSuccessfully signed up, you\'ll begin to receive updates about cheap flights.\nEnsure you check the email you used to sign up. Thank you.')
                    process_data = False
                        
            else:
                data_mamager.add_new_users(first_name=first_name, last_name=last_name, email=email)
                
                print('\nSuccessfully signed up, you\'ll begin to receive updates about cheap flights.\nEnsure you check the email you used to sign up. Thank you.')
                
                process_data = False
        
        except AttributeError as e:
            print(f'Exception occured: {e}\n\nCheck your internet connection\n\n')
            process_data = False
            exit()
        # catch exception relating to email_list
        except NameError:
            email_list = []
            exit()
        except Exception as exception:
            print(f'Exception occured: {exception}\n\nCheck your internet connection')
            exit()

# --------------------------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #

try:
    # get all cities and their data
    sheet_data = data_mamager.city_data

    for city in sheet_data:
        city_iata_code = city['iataCode']
        city_name = city['city']
        
        # check if city iata code field is empty
        if len(city_iata_code) == 0:
            # pass each city name to the FlightSearch class
            flight_search = FlightSearch(city_name=city_name)
            iata_code = flight_search.run_flight_search()
            
            # update google sheets iata code values from data manager class
            data_mamager.update_iata_code(city_id=city['id'], iata_code=iata_code)
        
        flight_data = FlightData(destination_iata=city['iataCode'])
        
        # get all flight data
        flight_list = flight_data.get_flight_data()
        
        print(flight_list)
        
        # I noticed that the flights are arranged in order of cost so the least priced flight will be the first element
        least_priced_flight = flight_list[0]
        min_price = least_priced_flight['price']
        
        # get all relevant data from the cheapest flight data to use in sending notifications
        city_from = least_priced_flight['cityFrom']
        fly_from = least_priced_flight['flyFrom']
        city_to = least_priced_flight['cityTo']
        fly_to = least_priced_flight['flyTo']
        outbound_date = least_priced_flight['route'][0]['local_departure'].split('T')[0]
        inbound_date =  least_priced_flight['route'][1]['local_departure'].split('T')[0]
        
        # message to send
        message = f"Subject: Flight Price Alert\n\nLow price alert!\nOnly {min_price} GBP to fly from {city_from}-{fly_from} to {city_to}-{fly_to}, from {outbound_date} to {inbound_date}"
        
        # check if email list is empty
        if len(email_list) > 0:
            notification_manager = NotificationManager()
            # send notification
            notification_manager.send_notification(flight_budget=city['lowestPrice'], min_flight_price=min_price, message=message, email_list=email_list)
        else:
            print('No emails to send to')

        
        # ------------------------------------------------------ #
        # ------------------------------------------------------ #
        # ------------------------------------------------------ #
        
        # THIS WAY WORKS ALSO BUT IT WILL ONLY GET THE MINIMUM FLIGHT PRICE....ACCESS TO OTHER ELEMENTS NEEDED FOR SENDING NOTIFICATIONS WILL BE RESTRICTED
        
        # flight_prices = {}
        
        # # store all the flight prices in a dictionary where the key is the city to travel to
        # flight_prices[city_name] = [flight_list[flight_no]['price'] for flight_no in range(len(flight_list))]
        
        # min_flight_price = min(flight_prices[city_name])
        
# catch exception relating to 
except AttributeError as e:
    print(e)
