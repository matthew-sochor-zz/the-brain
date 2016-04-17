class response_helper:
    def build_speech(output):
        return {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            }
        }

    def build_card(output, timestamp,title='Bernie remembered something', ):
        return {
            'type': 'Simple',
            'title': title,
            'content': 'At ' + timestamp + ' I remembered:\n' + output
        }

    def build_response(session_attributes, output, should_end_session, reprompt_text=False, card=False, version='1.0'):
        response = build_speech(output)
        response['shouldEndSession'] = should_end_session
        if card:
            response['card'] = card
        if reprompt_text:
            response['reprompt'] = build_speech(reprompt_text)
        
        return {
            'version': version,
            'sessionAttributes': session_attributes,
            'response': response
        }