from flask import Flask, request,jsonify
import os
app = Flask(__name__)

user_data = {}
response = ""
user_menu = {

}
@app.route('/')
def handle_home():
    user_menu[phone_number] = "home"
    response = "CON Welcome To Tuma insurance\n"
    response += "What would you like to check\n"
    response += "1.0 Insurance Products\n"

    return response


@app.route("/", methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.value.get("sessionId", None)
    service_code = request.value.get("serviceCode", None)
    phone_number = request.value.get("phoneNumber", None)
    text = request.value.get("text", "default")
    if text == "":
        if phone_number in user_data and len(user_data[phone_number])>0:
          conditions=[ussd_menu.get(phone_number)==("home")]
          if any(conditions):
              return handle_home(phone_number)
          else:
              return response
        elif phone_number in user_data and len(user_data[phone_number])==0:
            del  user_data[phone_number]
            ussd_menu[phone_number]="home"
            return handle_home()
    elif text=="1.0":
     response += "1.1 Education"
     response += "1.2 Motor Insurance"
     response += "1.3 Life Assurance"
    elif text =="1.1":
     response = "CON Enter the name of the insured\n"
     response += "Enter the Age of the insured\n"
     response += "Enter the class of the insured\n"
     response +="END Enter the Insurance term"
    elif text =="1.2":
        response ="CON Enter the Brand of your vehicle\n"
        response +="Enter the number plate of your vehicle\n"
        response+="Enter the year of manufacture\n"
        response +="END Enter the market value of your vehicle"
    elif text == "1.3":
        response ="CON Enter the name of the insured:\n"
        response +="Enter the age of the insured\n"
        response +=" END What is your  estimated networth"
    return response
@app.route("/userdata",methods=["GET"])
def get_user_data():
    return jsonify (user_data,ussd_menu)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=os.environ.get("PORT"))

