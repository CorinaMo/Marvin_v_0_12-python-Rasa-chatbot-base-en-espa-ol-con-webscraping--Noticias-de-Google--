from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

########## MÓDULO outofscope ###############
############################################
# Clase para establecer mensajes por defecto si el sistema no puede predecir la entrada del usuario

from rasa_sdk.events import UserUtteranceReverted

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return 'utter_out_of_scope'

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="my template")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]



########## MÓDULO NOTICIAS ###############
##########################################
# La clase que sigue llama a la función apiBuscaGoogleNews() de api_news.py y le pasa
# el slot con la categoría de noticias que dice el usuario (querynews)

from actions import api_news 

class ActionGetNews(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        param = tracker.get_slot('querynews')                    
        message = api_news.apiBuscaGoogleNews(param)

        for m in message:
            dispatcher.utter_message(m) 
        param = '' 
        return[]

