from flask import Flask, jsonify, render_template, request
app=Flask(__name__)

users = [
  {
    "id": 1,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 70
  },
  {
    "id": 2,
    "first_name": "Josephine",
    "last_name": "Darakjy",
    "company_name": "Chanay, Jeffrey A Esq",
    "city": "Brighton",
    "state": "MI",
    "zip": 48116,
    "email": "josephine_darakjy@darakjy.org",
    "web": "http://www.chanayjeffreyaesq.com",
    "age": 48
  },
  {
    "id": 3,
    "first_name": "Art",
    "last_name": "Venere",
    "company_name": "Chemel, James L Cpa",
    "city": "Bridgeport",
    "state": "NJ",
    "zip": 80514,
    "email": "art@venere.org",
    "web": "http://www.chemeljameslcpa.com",
    "age": 80
  },
  {
    "id": 4,
    "first_name": "Lenna",
    "last_name": "Paprocki",
    "company_name": "Feltz Printing Service",
    "city": "Anchorage",
    "state": "AK",
    "zip": 99501,
    "email": "lpaprocki@hotmail.com",
    "web": "http://www.feltzprintingservice.com",
    "age": 99
  },
  {
    "id": 5,
    "first_name": "Donette",
    "last_name": "Foller",
    "company_name": "Printing Dimensions",
    "city": "Hamilton",
    "state": "OH",
    "zip": 45011,
    "email": "donette.foller@cox.net",
    "web": "http://www.printingdimensions.com",
    "age": 45
  },
  {
    "id": 6,
    "first_name": "Simona",
    "last_name": "Morasca",
    "company_name": "Chapman, Ross E Esq",
    "city": "Ashland",
    "state": "OH",
    "zip": 44805,
    "email": "simona@morasca.com",
    "web": "http://www.chapmanrosseesq.com",
    "age": 44
  },
  {
    "id": 7,
    "first_name": "Mitsue",
    "last_name": "Tollner",
    "company_name": "Morlong Associates",
    "city": "Chicago",
    "state": "IL",
    "zip": 60632,
    "email": "mitsue_tollner@yahoo.com",
    "web": "http://www.morlongassociates.com",
    "age": 60
  },
  {
    "id": 8,
    "first_name": "Leota",
    "last_name": "Dilliard",
    "company_name": "Commercial Press",
    "city": "San Jose",
    "state": "CA",
    "zip": 95111,
    "email": "leota@hotmail.com",
    "web": "http://www.commercialpress.com",
    "age": 95
  },
  {
    "id": 9,
    "first_name": "Sage",
    "last_name": "Wieser",
    "company_name": "Truhlar And Truhlar Attys",
    "city": "Sioux Falls",
    "state": "SD",
    "zip": 57105,
    "email": "sage_wieser@cox.net",
    "web": "http://www.truhlarandtruhlarattys.com",
    "age": 57
  },
  {
    "id": 10,
    "first_name": "Kris",
    "last_name": "Marrier",
    "company_name": "King, Christopher A Esq",
    "city": "Baltimore",
    "state": "MD",
    "zip": 21224,
    "email": "kris@gmail.com",
    "web": "http://www.kingchristopheraesq.com",
    "age": 21
  }
]

@app.route("/")
def welcome():
    return render_template("index.html",users = users)

@app.route("/users?page=1&limit=5&name=james&sort=_age", methods = ["GET"])
def get_all_users():
      args = request.args
      print(args)

      for key,value in args.items():
            print(key,value)

      if "first_name" in args.keys():
            print(args.get("first_name"))
      return jsonify(users)

@app.route("/users/<int:id>", methods = ["GET"])
def get_one_user(id):
    return jsonify(users[id])

@app.route("/users", methods = ["POST"])
def creating_new_user():
    user = {
    "id": 11,
    "first_name": "Minna",
    "last_name": "Amigon",
    "company_name": "Dorl, James J Esq",
    "city": "Kulpsville",
    "state": "PA",
    "zip": 19443,
    "email": "minna_amigon@yahoo.com",
    "web": "http://www.dorljamesjesq.com",
    "age": 19
    }
    users.append(user)
    return jsonify(user)

@app.route("/users/<int:id>", methods = ["PUT"])
def update_user(id):
    users[id]["first_name"] = "Jeevitha",
    users[id]["last_name"] = "Dasari",
    users[id]["age"] = 27
    return jsonify(users[id])

@app.route("/users/<int:id>", methods = ["DELETE"])
def delete_user(id):
    users.remove(users[id])
    return jsonify(True)

if __name__ == "__main__":
    app.run(debug=True)