import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('dwlQgIUKQFcT3U3OS3zF0OePONoR6pemSdIqWy5v2yJp')
language_translator = LanguageTranslatorV3(
    version='2022-01-08',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a2a3654b-c5a7-4384-ba68-30da9a522aee')
def englishToFrench(englishText):
    translation= language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenchText= translation["translations"][0]["translation"]
    return frenchText
    
def frenchToEnglish(frenchText):
    translation= language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    englishText= translation["translations"][0]["translation"]
    return englishText