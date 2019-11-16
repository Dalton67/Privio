from django.shortcuts import render

from django.http import HttpResponse
from .elements import EmailForm

from piplapis.search import SearchAPIRequest

import requests
import json


names = "John Aaron Doe"
usernames = "jdoe70"
emails = "john.aaron@gmail.com"
addresses = "4301 College Road, Houston, Texas"
phones = "(976)-584-9090"
educations = "Texas A&M University"
jobs = "Process Operator at Dow Chemical"
relationships = "Jane Ashley Doe Josh Jacob Jameson"
ethnicities = "Caucasian"
gender = "Male"


def getPrivacyIndex():  # TODO Test correctly by commenting and uncommenting the appropriate code
        privacyIndex = 0

        if names != "":
            privacyIndex += 5

        if usernames != "":
            privacyIndex += 5  # TODO comment this section uncomment below to run with full functionality
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
                privacyIndex += usernamesIndexCap

            # if len(currentPerson.usernames) <= 4:  # TODO comment this if-else and uncomment section above to test with hard-coded valuse
            #     privacyIndex += (5*len(currentPerson.usernames))
            # else:
            #     privacyIndex += 20

        if emails != "":
            privacyIndex += 5  # up to 10
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
                privacyIndex += emailsIndexCap

            # if len(currentPerson.emails) <= 2:  # TODO comment this if-else and uncomment section above to test with hard-coded values
            #     privacyIndex += (5*len(currentPerson.emails))
            # else:
            #     privacyIndex += 10

        if addresses != "":
            privacyIndex += 15

        if phones != "":
            privacyIndex += 15

        if educations != "":
            privacyIndex += 5

        if jobs != "":
            privacyIndex += 15

        if relationships != "":
            privacyIndex += 1  # up to 5
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
                privacyIndex += relationshipsIndexCap

            # if len(currentPerson.relationships) <= 5:  # TODO comment this if-else and uncomment line above to test with hard-coded values
            #     privacyIndex += (1*len(currentPerson.relationships))
            # else:
            #     privacyIndex += 5

        if ethnicities != "":
            privacyIndex += 10

        return privacyIndex


def privacyRatingCalculator():
    privacyRating = 100 - getPrivacyIndex()
    print(privacyRating)
    return privacyRating


def index(request):
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        email = email_form.data["user_email"]
        print(email)

        # IP Data API
        requests1 = requests.get('http://api.ipapi.com/api/check?access_key=3ce7a3e12763ba9551d020fa5a4b1117&output=json')
        response_dict = json.loads(requests1.text)
        # print(response_dict)

        # Reverse GeoCoding
        # key = "AIzaSyD7q2PVhT2SDl9jJCq8qiciuusZ_Z09AwQ"
        # requests3 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&result_type=street_address&key={}'.format(response_dict["latitude"], response_dict["longitude"], key))
        # response_dict1 = json.loads(requests3.text)
        # print(response_dict1['results'])

        # People Data API
        # request2 = SearchAPIRequest(email=email, api_key='')  # raw_name or email GET APIs FROM ME
        # response2 = request2.send()
        # currentPerson = response2.person

        # ip = response_dict["ip"]

        # VPN Detection API
        # response = requests.get('https://api.ip2proxy.com/?ip={}&key=WU5VWACYRB&package=PX1'.format(ip))
        # response_dict2 = json.loads(response.text)

        if email_form.is_valid():
            return HttpResponse(render(request, "securityApp/results.html", {
                "email_form": email_form,
                "ipAddress": response_dict["ip"],
                "ipType": response_dict["type"],
                "ipProxy": "YES",  # response_dict2['isProxy'],
                "continentCode": response_dict["continent_code"],
                "continentName": response_dict["continent_name"],
                "countryCode": response_dict["country_code"],
                "countryName": response_dict["country_name"],
                "regionCode": response_dict["region_code"],
                "regionName": response_dict["region_name"],
                "ipCity": response_dict["city"],
                "ipZip": response_dict["zip"],
                "ipLatitude": response_dict["latitude"],
                "ipLongitude": response_dict["longitude"],
                # "currentPerson": response2.person,
                "names": "John Aaron Doe",  # "\n".join(map(str, currentPerson.names)),
                "usernames": "jdoe70",  # "\n".join(map(str, currentPerson.usernames)),
                "emails": "john.aaron@gmail.com",  # "\n".join(map(str, currentPerson.emails)),
                "addresses": "4301 College Road, Houston, Texas",  # "\n".join(map(str, currentPerson.addresses)),
                "phones": "(976)-584-9090",  # "\n".join(map(str, currentPerson.phones)),
                "educations": "Texas A&M University",  # "\n".join(map(str, currentPerson.educations)),
                "jobs": "Process Operator at Dow Chemical",  # "\n".join(map(str, currentPerson.jobs)),
                "relationships": "Jane Ashley Doe",  # "\n".join(map(str, currentPerson.relationships)),
                "ethnicities": "Caucasian",  # "\n".join(map(str, currentPerson.ethnicities)),
                "gender": "Male",  # "\n".join(str(currentPerson.gender))
                "privacyRating": privacyRatingCalculator()
            }))
    else:
        email_form = EmailForm()
        # return HttpResponse("...")
        return HttpResponse(render(request, "securityApp/index.html", {"email_form": email_form}))


def results(request):
    return HttpResponse(render(request, "securityApp/index.html"))
