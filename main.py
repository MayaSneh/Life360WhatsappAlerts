from life360 import life360
import datetime
import Whatsapp as Whatsapp
import time
import geopy.distance
from creds import *

if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        curr_time = str(now.time())[0:5]

        if curr_time == '19:00':
            # this is a googleable or sniffable value. I imagine life360 changes this sometimes.
            authorization_token = life360_token
            api = life360(authorization_token=authorization_token)

            # Get all circles you're a member of
            circles = api.get_circles()

            # Gets all info from first circle (should be your family circle)
            circle_id = circles[0]['id']
            circle = api.get_circle(circle_id)

            # Gets Places for this circle
            places = api.get_places(circle_id)

            # Gets latitude and longitude of 'Home'
            for place in places['places']:
                if place['name'] in ['Home', 'home']:
                    home_location = (place['latitude'], place['longitude'])

            # Create a list of all members (name, phone number, distance from home)
            # and a list of members who are at home
            members = []
            at_home = []
            for m in circle['members']:
                # Can't send myself a whatsapp message from my own account
                if m['firstName'] != 'Maya':
                    location = (round(float(m['location']['latitude']), 3), round(float(m['location']['longitude']), 3))
                    members.append((m['firstName'], m['loginPhone'],
                                    geopy.distance.geodesic(home_location, location).km))
                    if m['location']['name'] == 'Home':
                        at_home.append((m['firstName'], m['loginPhone']))

            # Send a message to everyone who is at home to feed Spike
            if at_home != []:
                message_content = "It is now "+curr_time+". Kindly feed Mr. Spike if you haven't done so already"
                Whatsapp.messenger(message_content, at_home)

            # If no one is home, send a message to the members closest to home
            else:
                members.sort(key=lambda tup: tup[2])
                threshold = members[1][2]  # the distance of the second-closest member to home
                closest = [m[:2] for m in members if m[2] <= threshold + 0.5]
                message_content = "No one is home to feed Spike! Make sure someone gets home to feed him soon."
                Whatsapp.messenger(message_content, closest)
        time.sleep(60)
