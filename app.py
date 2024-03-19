from flask import Flask, Response,request
import plivo 
from plivo import plivoxml 
import os

port = int(os.getenv('PORT', 8000))

app = Flask(__name__)
@app.route('/')
def Hello_World():
     return 'Hello World'
@app.route('/text-to-speech/<stan>', methods=['GET','POST'])
def speak_xml(stan):
    # Generate a Speak XML with the details of the text to play on the call.
    #r = plivoxml.Response()
    r = plivoxml.ResponseElement()

    # Add Speak XML Tag with English text
    body1 = '%s'%stan
    params1 = {
        'language': "en-GB", # Language used to read out the text.
        'voice': "WOMAN" # The tone to be used for reading out the text.
    }
    r.add_speak(body1, **params1)

    #print (r.to_xml)
    print (r.to_string())
    #return Response(str(r), mimetype='text/xml')
    return Response(r.to_string())
	
@app.route('/hangup/', methods=['GET','POST'])
def hangup():
	#response = plivoxml.Response()
	response = plivoxml.ResponseElement()
	params = {
		'schedule' : "1",
		'reason' : "rejected"
	}
	
	response.addHangup(**params)
	params2 = {
		'loop' : "0"
	}
	response.add_speak("This call will hang up as it is voice mail.",
		**params2)
	return Response(response.to_string())

if __name__ == "__main__":
    app.run()
