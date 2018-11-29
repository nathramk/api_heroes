from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

heroe = [
    {
        "nombre": "batman",
        "casa": "DC",
		"bio":"es un cojudo"
    }
]

#@app.route("/")
#def home():
#    return render_template('index.html')
    #return "<h1>sadasd</h1>"

@app.route("/heroe", methods = ['POST'])
def create_heroe():
    request_data = request.get_json()
    new_store = {
            'nombre': request_data['nombre'],
            'casa': request_data['casa'],
			'bio': request_data['bio']
        }
    heroe.append(new_store)
    return jsonify(new_store)

@app.route("/heroe/<string:nombre>")
def get_store_name(nombre):
    for heroes in heroe:
        if heroes['nombre'] == nombre:
            return jsonify(heroes)
    return jsonify({"Error 404": "heroe not found"})


@app.route("/heroes")
def get_store():
    #return jsonify({'heroe': heroe})
	return jsonify(heroe)

@app.route('/heroe/<string:nombre>', methods=["PUT"])
def edit_heroes(nombre):
	heroess = [heroess for heroess in heroe if heroess["nombre"] == nombre]
	#heroess = heroess[0]
	#framework["id"] = request.json["id"]
	#heroess["nombre"] = request.json["nombre"]
	#heroess["nombre"] = request.json["nombre"]
	framework = heroess[0]
	#framework["id"] = request.json["id"]
	framework["nombre"] = request.json["nombre"]
	framework["casa"] = request.json["casa"]
	framework["bio"] = request.json["bio"]

	return jsonify(framework)	

	#return jsonify(heroess)

#@app.route("/store/<string:name>/item", methods=['POST'])
#def add_items_in_stores(name):
#    item_data = request.get_json()
#    for stores in store:
#        if stores['name'] == name:
#            new_item = {
#                "name": item_data["name"],
#                "price": item_data["price"]
#            }
#            stores["item"].append(new_item)
#            return jsonify(new_item)
#    return jsonify({"erro 404: Store not found"})


#@app.route("/store/<string:name>/item")
#def get_item_in_store(name):
#    for stores in store:
#        if stores['name'] == name:
#            return jsonify({"item": stores["item"]})
#    return jsonify({"Error 404": "Store not found"})


if __name__=='__main__':
    app.run(debug=True)