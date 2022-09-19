
# Spike Alerts

This is a project I created so that we never miss my dog's feeding time!

This automation checks Life360 at 19:00, which is Spike's feeding time, and sends a whatsapp message to whoever is at home reminding them to feed Spike.



## How It Works
First, I implemented the Life360 API to get the circle info (ie. the locations of all circle members).

Then I created a whatsapp automation that sends your chosen message to a list of contacts (by phone number and name).

The program activates at 19:00, creates a list of circle members who are at home, and sends them all messages.
If no one is home, then it sends messages to the two members closest to home (or more members if more than two are approximately the same distance from home).
## Usage

```
pip3 install -r requirements.txt
```
After installing the requirements, you will need to change several things in the code:
- Line 15 in main.py: replace life360_token with your token (as a string). This can be found by logging into your life360 account online.
- Lines 48 and 56 in main.py: replace with your message.
- Line 23 in Whatsapp.py: replace chromedriver_profile with your path.

Optional: I didn't want to send myself messages, so I added line 39 in main.py to prevent this. You can remove or change to your name.
