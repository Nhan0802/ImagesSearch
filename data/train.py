
import correct, pickle

class Train:
	"""docstring for Train"""
	def __init__(self, dataPath, outputPath):
		self.dataPath, self.outputPath = dataPath, outputPath
		self.readData()
		self.trainData()
		# self.saveModel()
		while True:
			text = input("Enter your query: ")
			print(self.model.predict([text]))

	def readData(self):
		self.dataset = open(self.dataPath,  encoding="utf8").read().split("\n")

	def trainData(self):
		self.model = correct.model.CorrectVietnameseSentence(default=False)
		self.model.fit(self.dataset)

	def saveModel(self):
		pickle.dump(self.model, open(self.outputPath, 'wb'))


		
trainer = Train("separate.txt", "correct.pickle")