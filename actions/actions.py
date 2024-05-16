# This files contains your custom actions which can be used to run
# custom Python code.

import requests

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# dispatcher - used to send messages back to the user
# Tracker - the state tracker for the current user. You can access slot values using.


class AskForService(Action):
    def name(self) -> Text:
        return "action_ask_for_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ask_again_value = tracker.get_slot('ask_again')
        if ask_again_value:
            dispatcher.utter_message(response="utter_ask_again")
        else:
            dispatcher.utter_message(response="utter_ask_first")

        return [SlotSet("ask_again", True)]


class ActionTerminateBot(Action):
    def name(self) -> Text:
        return "action_terminate_bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_terminate_approve")

        return []


class ScholarshipValidate(Action):
    def name(self) -> Text:
        return "action_set_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        scholarship = tracker.get_slot('scholarship_choice')

        if scholarship:
            message = f"What do you want to know about {scholarship} scholarship? Deadlines, prerequisites or official website?."
        else:
            message = "You haven't mentioned a scholarship."

        dispatcher.utter_message(text=message)
        return []


class ScholarshipRequestProcess(Action):
    def name(self) -> Text:
        return "action_scholarship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        scholarship_name = tracker.get_slot('scholarship_choice')
        last_intent = tracker.get_intent_of_latest_message()
        print(last_intent)

        data = requests.get(f'http://127.0.0.1:5000/scholarships')
        message = ""
        if data.status_code != 404:
            scholarships = data.json()

            for scholarship in scholarships:

                if scholarship["name"] == scholarship_name:

                    if last_intent == 'scholarship_deadlines':
                        message = scholarship["deadline"]
                    elif last_intent == 'scholarship_link':
                        message = scholarship["website"]
                    elif last_intent == 'scholarship_prerequisites':
                        message = scholarship["prerequisites"]
                    else:
                        message = "Sorry, i can not do that"
                    break
                else:
                    message = ("Sorry, such scholarship is not found in our database, please check the spelling."
                               " The right spelling could be found by requesting the list of scholarships")
        else:
            message = "Sorry, we could not get information from our data base."

        dispatcher.utter_message(text=message)
        return []


class StoryValidate(Action):
    def name(self) -> Text:
        return "action_set_block"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        block = tracker.get_slot('story_block')  # tracker.latest_message.get('entities', {}).get('s', None)

        if block:
            # Set the 'location' slot with the extracted value
            return [SlotSet("story_block", block)]

        # If the entity wasn't extracted, return an empty list of events
        return []


class ActionGetScholarships(Action):
    def name(self) -> Text:
        return "action_get_scholarships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = requests.get(f'http://127.0.0.1:5000/scholarships')
        if (data.status_code != 404):
            scholarships = data.json()

            dispatcher.utter_message(text="Found the following scholarships: ")
            for scholarship in scholarships:
                dispatcher.utter_message(text=scholarship['name'])

        return []

