import gradio as gr


# importing the requests library
import requests
import json

# api-endpoint
URL = "http://127.0.0.1:8000/"



def sendToServer(name, intensity,agility):

    #Get
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'name':name,'intensity':intensity,'agility':agility}
    # sending get request and saving the response as response object
    r = requests.get(url = URL+"GetPractice", params = PARAMS)
    # extracting data in json format
    Get_Response = r.json()
    
    #======================================
    #Post
    # data to be sent to api
    PARAMS = {'name':name,'intensity':intensity,'agility':agility}
    # sending post request and saving response as response object
    #json= parameter (which takes a dictionary) instead of data= (which takes a string) in the call:
    r = requests.post(url=URL+"PostPractice", json=PARAMS)

    # extracting response text
    Post_Response = r.text

    return Get_Response+"\n"+Post_Response




def greet(name, intensity,agility):
    return sendToServer(name, intensity,agility)
    #return "Hello, " + name + "!" * int(intensity)+" "+str(int(agility)%6+1)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider","slider"],
    outputs=["text"],
)






demo.launch()