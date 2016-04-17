class elasticsearch_helper:
    def elasticsearch_post(user, text, timestamp):
        data = {
            'user': user,
            'text': text,
            'timestamp': timestamp
        }
        # have to send the data as JSON
        data = json.dumps(data)
        
        req = urllib2.Request(endpoint + '/' + index + '/' + mapping, data)
        out = urllib2.urlopen(req)
        return json.loads(out.read())

    def elasticsearch_find(user, search):
        query = {
            "filter":{ "term":  { "user": user}},
            "query":{"match": {"text": search}}
        }

        url = endpoint+ '/' + index +'/_search?'

        req = urllib2.Request(url, json.dumps(query), {'Content-Type': 'application/json'})
        out = urllib2.urlopen(req)
        datastr = out.read()
        return json.loads(datastr), json.dumps(query)
        
    def build_query(intent):
        token = 'x'
        message = [intent['slots'][token]['value']]
        token += 'x'
        while 'value' in intent['slots'][token]:
            message.append(intent['slots'][token]['value'])
            token += 'x'
        return ' '.join(message)