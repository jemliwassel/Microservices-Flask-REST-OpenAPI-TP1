from flask import Flask, request, jsonify, make_response
import requests
import json

app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/user/<user_id>", methods=['GET'])
def get_user_infos(user_id):
   for user in users:
      if user['id'] == user_id:
         res = make_response(jsonify(user), 200)
         return res
   return make_response(jsonify({"error": "User was not found"}), 400)

@app.route("/user/reservations/<user_id>", methods=['GET'])
def get_user_reservation(user_id):
   if request.args:
      req = request.args
      reservation_date = req["date"]
      all_reservations_for_user = requests.get(f"http://127.0.0.1:3201/bookings/<user_id>", params={user_id: user_id}).json()
      reservations = []
      for dates in all_reservations_for_user['dates']:
         if dates['date'] == reservation_date:
            reservations.append(dates)
      res = make_response(jsonify(reservations), 200)
      return res
   else:
      return make_response(jsonify({"error": "reservation date not found"}), 400)

@app.route("/user/reservation_details/<user_id>", methods=['GET'])
def get_user_reservation_details(user_id):
   all_reservations_for_user = requests.get(f"http://127.0.0.1:3201/bookings/{user_id}").json()
   details = []
   print("All reserv", all_reservations_for_user)
   for reservation in all_reservations_for_user['dates']:
      reservation_details = {"date": reservation['date'], "movies": []}
      for movie_id in reservation['movies'] : 
         print("ID : ", movie_id)
         movie_details = requests.get(f"http://127.0.0.1:3200/movies/{movie_id}").json()
         print("Details: ", movie_details)
         reservation_details['movies'].append(movie_details)
      details.append(reservation_details)
      res = make_response(jsonify(reservation_details), 200)
      return res

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT, debug=True)
