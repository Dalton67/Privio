from pip._vendor.distlib.compat import raw_input
from piplapis.search import SearchAPIRequest
import requests
import json

# emailAddress = raw_input("Enter your e-mail address: ")

# TODO Uncomment IP Info Request and Parsing and Printing Response to obtain IP info
# IP Info Request
print("\n")
print("IP Info:")
requests = requests.get('http://api.ipapi.com/api/check?access_key=3ce7a3e12763ba9551d020fa5a4b1117&output=json')
response_dict = json.loads(requests.text)

# Storing IP Info For Ease of Access
ipAddress = response_dict["ip"]
ipType = response_dict["type"]
continentCode = response_dict["continent_code"]
continentName = response_dict["continent_name"]
countryCode = response_dict["country_code"]
countryName = response_dict["country_name"]
regionCode = response_dict["region_code"]
regionName = response_dict["region_name"]
ipCity = response_dict["city"]
ipZip = response_dict["zip"]
ipLatitude = response_dict["latitude"]
ipLongitude = response_dict["longitude"]

# Parsing and Printing Response
for i in response_dict:
    print(i, ":", response_dict[i])
print("\n")


# TODO Uncomment Lines 26-55 to access Pipl database and to test with real data (Uncomment the specified lines in Person class)
# People Info Request
request2 = SearchAPIRequest(email=emailAddress, api_key='')  # raw_name or email GET APIs FROM ME
response2 = request2.send()

if response2.person:
    currentPerson = response2.person
    names = "\n" .join(map(str, currentPerson.names))
    usernames = "\n" .join(map(str, currentPerson.usernames))
    emails = "\n" .join(map(str, currentPerson.emails))
    addresses = "\n" .join(map(str, currentPerson.addresses))
    phones = "\n" .join(map(str, currentPerson.phones))
    educations = "\n" .join(map(str, currentPerson.educations))
    jobs = "\n" .join(map(str, currentPerson.jobs))
    relationships = "\n" .join(map(str, currentPerson.relationships))
    ethnicities = "\n" .join(map(str, currentPerson.ethnicities))
    gender = "\n" .join(str(currentPerson.gender))


# TODO Uncomment these following lines to run hard-coded people data CHANGE VALUES WITH SPACES SEPARATING EACH ITEM IN THE STRING TO TEST DIFFERENT SCENARIOS
names = "Danny Short DeVito"                                    # privacyIndex = 5
usernames = "danny.s.devito shortboi iamgroot ichbinshort"      # privacyIndex = 5 per username up to 20
emails = "dannyboi@hotmail.com"                                 # privacyIndex = 5 per up to 10
addresses = "4300 Commando Trl, Denver, Colorado"               # privacyIndex = 15
phones = "979-822-9354"                                         # privacyIndex = 15
educations = "Texas A&M University"                             # privacyIndex = 5
jobs = "Process Operator at Dow Chemical Company"               # privacyIndex = 15
relationships = "John Some Dude Jim Another Dude"               # privacyIndex = 1 per person up to 5
ethnicities = "Hispanic"                                        # privacyIndex = 10


class Person:
    def __init__(self, names, usernames, emails, addresses, phones, educations, jobs, relationships, ethnicities):
        self.names = names
        self.usernames = usernames
        self.emails = emails
        self.addresses = addresses
        self.phones = phones
        self.educations = educations
        self.jobs = jobs
        self.relationships = relationships
        self.ethnicities = ethnicities
        self.privacyIndex = 0
        self.privacyRating = 0

    def printPersonInfo(self):
        print("Name(s): " + names)
        print("Username(s): " + usernames)
        print("Emails(s): " + emails)
        print("Adresses: " + addresses)
        print("Phones: " + phones)
        print("Educations: " + educations)
        print("Jobs: " + jobs)
        print("Relationships: " + relationships)
        print("Ethnicities: " + ethnicities)
        print("\n")

    def getPrivacyIndex(self):  # TODO Test correctly by commenting and uncommenting the appropriate code
        if self.names != "":
            self.privacyIndex += 5

        if self.usernames != "":
            self.privacyIndex += 5  # TODO comment this section uncomment below to run with full functionality
            usernamesIndexCap = 0
            spaceCount = 0
            for c in usernames:
                if c == " ":
                    spaceCount += 1
            if spaceCount > 0:
                while spaceCount > 0:
                    spaceCount -= 1
                    if usernamesIndexCap < 15:
                        usernamesIndexCap += 5  # up to 20
                self.privacyIndex += usernamesIndexCap

            # if len(currentPerson.usernames) <= 4:  # TODO comment this if-else and uncomment section above to test with hard-coded valuse
            #     self.privacyIndex += (5*len(currentPerson.usernames))
            # else:
            #     self.privacyIndex += 20

        if self.emails != "":
            self.privacyIndex += 5  # up to 10
            emailsIndexCap = 0
            spaceCount = 0
            for c in emails:
                if c == " ":
                    spaceCount += 1
            if spaceCount > 0:
                while spaceCount > 0:
                    spaceCount -= 1
                    if emailsIndexCap < 5:
                        emailsIndexCap += 5  # up to 10
                self.privacyIndex += emailsIndexCap

            # if len(currentPerson.emails) <= 2:  # TODO comment this if-else and uncomment section above to test with hard-coded values
            #     self.privacyIndex += (5*len(currentPerson.emails))
            # else:
            #     self.privacyIndex += 10

        if self.addresses != "":
            self.privacyIndex += 15

        if self.phones != "":
            self.privacyIndex += 15

        if self.educations != "":
            self.privacyIndex += 5

        if self.jobs != "":
            self.privacyIndex += 15

        if self.relationships != "":
            self.privacyIndex += 1  # up to 5
            relationshipsIndexCap = 0
            spaceCount = 0
            for c in relationships:
                if c == " ":
                    spaceCount += 1
            if spaceCount > 3:
                while spaceCount > 0:
                    spaceCount -= 3
                    if relationshipsIndexCap < 5 and spaceCount >= 2:
                        relationshipsIndexCap += 1  # up to 5
                self.privacyIndex += relationshipsIndexCap

            # if len(currentPerson.relationships) <= 5:  # TODO comment this if-else and uncomment line above to test with hard-coded values
            #     self.privacyIndex += (1*len(currentPerson.relationships))
            # else:
            #     self.privacyIndex += 5

        if self.ethnicities != "":
            self.privacyIndex += 10

        return self.privacyIndex

    def privacyRatingCalculator(self):
        self.privacyRating = 100 - self.getPrivacyIndex()
        return self.privacyRating

    def privacyRatingAssessment(self):
        if self.privacyRating <= 25 and self.privacyRating > 0:
            print("You should definitely start working on your online privacy.")
        if self.privacyRating <= 50 and self.privacyRating > 25:
            print("You should probably start working on your online privacy.")
        if self.privacyRating <= 75 and self.privacyRating > 50:
            print("You are doing okay, but more privacy and better security is always better.")
        if self.privacyRating <= 100 and self.privacyRating > 75:
            print("You are a privacy god. Keep up the good work.")


# TODO Proxy/VPN/Tor/etc Detection API (MAYBE?) ipqualityscore.com
response = requests.get('https://www.ipqualityscore.com/api/json/ip/API_KEY_HERE!!!!!!!!!!!!!!/IP_ADDRESS_HERE!!!!!!!!!!!?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true')
data = response.json()
for i in data:
    print(i, ":", data[i])


person = Person(names, usernames, emails, addresses, phones, educations, jobs, relationships, ethnicities)
print("Person Info:")
person.printPersonInfo()
privacyRating = person.privacyRatingCalculator()
print("Your Privacy Rating: " + str(privacyRating) + "/100")
person.privacyRatingAssessment()
