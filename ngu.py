from flask import Flask, jsonify, request

app = Flask(__name__)

#Creation of Items
items = [
{'id': '1',
'name': 'chips',
'price': '15'},

{'id': '2',
'name':'biscuits',
'price':'30'},

{'id':'3',
'name':'sugar',
'price':'20'},

]

#displaying all items
@app.route('/items/all',methods=['GET'])
def getAllItems():
	return jsonify(items)

# to get specific items based on its id

@app.route('/items/<item_id>', methods=['GET'])
def getItems(item_id):
	item_list = [items for items in item if (items['item_id'] == item_id)]
	if 'item_name' in request.json:
		item_list[0]['item_name'] = request.json['item_name']
	if 'item_price'	in request.json:
		item_list[0]['item_price'] = request.json['item_price']
	return jsonify(item_list[0])
		
#to create an item by user
@app.route('/items/all', methods=['POST'])	
def createItems():
	new_item = {
	'item_id': request.json['item_id'],
	'item_name':request.json['item_name'],
	'item_price': request.json['item_price']
	}
	items.append[new_item]
	return jsonify(new_item)

#To delete an item
@app.route('/items/<item_id>', methods=['DELETE'])
def deleteItems(item_id):
	item_list = [items for items in item if (item['item_id'] == item_id)]
	if len(item_list) == 0:
		abort(404)

	items.remove(item_list[0])
	return jsonify('Succcess! deleted')


#run app
if __name__ == '__main__':
	app.run(debug = True)