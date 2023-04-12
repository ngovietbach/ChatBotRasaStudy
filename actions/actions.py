# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
import mysql.connector
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
def get_name(id):
    cnx = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='study')
    cursor = cnx.cursor()
    query = f"SELECT Ten_HP FROM bang1 WHERE Ma_lop = '{id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    if result is None:
        return None
    return result[0]
class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = tracker.get_slot("id")
        subject_name = get_name(id)
        if id is None:
            dispatcher.utter_message(text=f"Sorry, I couldn't find the name of subject with id {id}.")
        else:
            dispatcher.utter_message(text=f"The name of subject with id {id} is {subject_name}.")

        return []


