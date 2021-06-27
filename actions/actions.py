# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import logging

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ActionSetFaqSlot(Action):
    def name(self) -> Text:
        return "action_set_faq_slot"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        full_intent = (
            tracker.latest_message.get("response_selector", {})
                .get("faq", {})
                .get("full_retrieval_intent")
        )
        logger.info(f"intent: {full_intent}")

        if full_intent:
            topic = full_intent.split("/")[1]
        else:
            topic = None
        return [SlotSet("faq", topic)]


class ActionExplainFaqs(Action):
    def name(self) -> Text:
        return "action_explain_faq"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        topic = tracker.get_slot("faq")

        if topic in ["rasax"]:
            dispatcher.utter_message(template=f"utter_faq_{topic}_more")
        else:
            dispatcher.utter_message(template="utter_no_further_info")

        return []
