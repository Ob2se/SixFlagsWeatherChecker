import requests

# weather api
weatherAPI = "https://api.open-meteo.com/v1/forecast"


# six flag locations
locations = [
    ("Six Flags Over Texas", "33.0054,-97.0271"),
    ("Six Flags Fiesta Texas", "29.5994,-98.6097"),
    ("Six Flags Over Georgia", "33.7706,-84.5513"),
    ("Six Flags Magic Mountain", "34.4259,-118.5973"),
    ("Six Flags Great Adventure/Hurricane Harbor", "40.1340,-74.4403"),
    ("Six Flags Great America", "42.3706,-87.9366"),
    ("Six Flags New England", "42.0360,-72.6685"),
    ("Six Flags America", "38.9076,-76.7722"),
    ("Six Flags St. Louis", "38.5096,-90.3935"),
    ("Six Flags Discovery Kingdom", "38.1041,-122.2566"),
    ("Six Flags Hurricane Harbor Phoenix", "33.5319,-112.2626"),
    ("Six Flags Hurricane Harbor Los Angeles", "34.4259,-118.5973"),
    ("Six Flags Hurricane Harbor Chicago", "42.3706,-87.9366"),
    ("Six Flags Hurricane Harbor Arlington", "32.7555,-97.0728"),
    ("Six Flags Hurricane Harbor Concord", "38.0049,-121.9657"),
    ("Six Flags Hurricane Harbor Splashtown", "30.0038,-95.4479"),
    ("Six Flags Hurricane Harbor Rockford", "42.3706,-87.9366"),
    ("Six Flags Hurricane Harbor Jackson", "40.1340,-74.4403"),
    ("Six Flags Hurricane Harbor Oklahoma City", "35.4634,-97.5355")
]

# ask user if they would like to check the weather of another location
def goAgain():
    choice = input("Would you like to check the weather of another location? (Y/N)").lower()
    match choice:
        case "y":
            main()
        case "n":
            print("Goodbye!")
            exit()
        case _:
            print("Invalid input. Please enter Y or N.")
            goAgain()


# print the weather for the day
def printWeather(days, weather, rain, humidity, precipitation_probability):
    for i in range(int(days)):
        print("Day", i+1, "average temperature:", weather[i], "F", ", average rain:", rain[i], "mm", ", average humidity:", humidity[i], "%", ", average precipitation probability:", precipitation_probability[i], "%")
    return


#get average temperature, humidity, and precipitation for each day


def get_weather(longlat, days):
    params = {
        "latitude": longlat.split(",")[0],
        "longitude": longlat.split(",")[1],
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability,rain",
        "temperature_unit": "fahrenheit",
        "forecast_days": days
    }
    req = requests.get(weatherAPI, params=params)
    weatherDays = []
    humidityDays = []
    rainDays = []
    precipitation_probabilityDays = []

    for key in req.json():
        if key == "hourly":
            if "temperature_2m" in req.json()[key]:
                print("Averages for each day:")
                for i in range(0, len(req.json()[key]["temperature_2m"]), 24):
                    weatherDays.append(round(sum(req.json()[key]["temperature_2m"][i:i+24]) / len(req.json()[key]["temperature_2m"][i:i+24]), 2))

            if "relative_humidity_2m" in req.json()[key]:
                for i in range(0, len(req.json()[key]["relative_humidity_2m"]), 24):
                    humidityDays.append(round(sum(req.json()[key]["relative_humidity_2m"][i:i+24]) / len(req.json()[key]["relative_humidity_2m"][i:i+24]), 2))

            if "precipitation_probability" in req.json()[key]:
                for i in range(0, len(req.json()[key]["precipitation_probability"]), 24):
                    precipitation_probabilityDays.append(round(sum(req.json()[key]["precipitation_probability"][i:i+24]) / len(req.json()[key]["precipitation_probability"][i:i+24]), 2))

            if "rain" in req.json()[key]:
                for i in range(0, len(req.json()[key]["rain"]), 24):
                    rainDays.append(round(sum(req.json()[key]["rain"][i:i+24]) / len(req.json()[key]["rain"][i:i+24]), 2))
                    
    printWeather(days, weatherDays,rainDays, humidityDays, precipitation_probabilityDays)
    return

#ask user what location and how many days they want to check the weather for
def choice():
    print("Which location would you like to check the weather for?")
    print("1. Six Flags Over Texas")
    print("2. Six Flags Fiesta Texas") 
    print("3. Six Flags Over Georgia")
    print("4. Six Flags Magic Mountain")
    print("5. Six Flags Great Adventure/Hurricane Harbor")
    print("6. Six Flags Great America")
    print("7. Six Flags New England")
    print("8. Six Flags America")
    print("9. Six Flags St. Louis")
    print("10. Six Flags Discovery Kingdom")
    print("11. Six Flags Hurricane Harbor Phoenix")
    print("12. Six Flags Hurricane Harbor Los Angeles")
    print("13. Six Flags Hurricane Harbor Chicago")
    print("14. Six Flags Hurricane Harbor Arlington")
    print("15. Six Flags Hurricane Harbor Concord")
    print("16. Six Flags Hurricane Harbor Splashtown")
    print("17. Six Flags Hurricane Harbor Rockford")
    print("18. Six Flags Hurricane Harbor Jackson")
    print("19. Six Flags Hurricane Harbor Oklahoma City")
    choice1 = input("Enter the number of the location you would like to check the weather for: ")
    if choice1.isnumeric() == False:
        print("Invalid input. Please enter a number between 1 and 19.")
        main()
    if int(choice1) > 19 or int(choice1) < 1:
        print("Invalid input. Please enter a number between 1 and 19.")
        main()
    
    choice2 = input("Enter the number of days you would like to check the weather for: ")

    if choice2.isnumeric() == False:
        print("Invalid input. Please enter a number.")
        main()
    if int(choice2) > 19 or int(choice2) < 1:
        print("Invalid input. Please enter a number between 1 and 19.")
        main()
    
    choice = [choice1, choice2]

    return choice


#main function
def main():
    location = choice()
    for i in range(len(locations)):
        if i+1 == int(location[0]):
            print("You chose", locations[i][0])
            print("The weather for", locations[i][0], "is:")
            get_weather(locations[i][1], location[1])
            break
    goAgain()
    
print("""
                                           o
                                         o |
                                         |
      .       .           ._._.    _                     .===.
      |`      |`        ..'\ /`.. |H|        .--.      .:'   `:.
     //\-...-/|\         |- o -|  |H|`.     /||||\     ||     ||
 ._.'//////,'|||`._.    '`./|\.'` |\\\||:. .'||||||`.   `:.   .:'
 ||||||||||||[ ]||||      /_T_\   |:`:.--'||||||||||`--..`=:='...
      """)


print("Six Flags Weather Checker")
main()