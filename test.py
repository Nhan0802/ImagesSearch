from flask import Flask, request, jsonify
from model.search import Searcher


class App:

	def __init__(self):
		self.__fields = {
			'id' : False, 
			'title' : True
		}
		self.__searcher = Searcher("data/correct.pickle")
		self.__docs = list()
		self.__map = dict()

		for line in open("data/translateOutput.txt", encoding="utf8"):
			key, value = line.split("\t")
			item = {
				"id" : key,
				"title" : value
			}
			self.__map[key] = value
			self.__docs.append(item)
			self.__searcher.set_fields(self.__fields)
			self.__searcher.fit(self.__docs)

	def search(self, text):
		data = self.__searcher.search(text)["results"]
		result = list()
		check = set()
		for items in data:
			fileName = items[0][0]
			if fileName not in check:
				result.append((fileName, self.__map[fileName]))
				check.add(fileName)
		return result

_app = App()
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form.get('query')
        data = _app.search(query)
        return jsonify(isError=False, message="Success", statusCode=200, data=data), 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)