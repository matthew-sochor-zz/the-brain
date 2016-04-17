from __future__ import print_function
from the_brain_helper import *

# Secrets I don't want to share with GitHub, sorry jerks
app_id = 'app_id'

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if (event['session']['application']['applicationId'] != app_id):
        raise ValueError("Invalid Application ID")
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    print(event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent "+intent_request['intent']['name']+" requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    # Dispatch to your skill's intent handlers
    if intent_name == "takeNote":
        intent['timestamp'] = intent_request['timestamp']
        return take_note(intent, session)
    elif intent_name == "findNote":
        return find_note(intent, session)
    elif intent_name == "getTime":
        return get_time(intent, session)
    elif intent_name == "getNext":
        return get_next(intent, session)
    elif intent_name == "getPrevious":
        return get_previous(intent, session)
    elif intent_name == "findStub":
        return find_stub()
    elif intent_name == "takeStub":
        return take_stub()
    elif intent_name == "save":
        return save_session(session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.YesIntent":
        return get_welcome_response()
    elif ((intent_name == "AMAZON.NoIntent")
        or (intent_name == "AMAZON.StopIntent")
        or (intent_name == "AMAZON.CancelIntent")):
        return end_session()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])