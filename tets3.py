class Note:
	def__init__(self, text, tag):
		self.text = text
		self.tag = tag


	def__str__(self):
		string = 'Note(text="{}", tag="{}")'
		return string.format(self.text, self.tag)



class Notebook:
	 def__init__(self):
	 	self.data = {}
	 	self.counter = 0

	 def add(self, note):
	 	uid = self.counter
	 	self.data[uid] = note
	 	self.counter +=1
	 	return uid

	 def get(self, note):
	 	note = self.data[uid]
	 	return note

	def delete(self, uid):
		note = self.data[uid]
		del self.data[uid]
		return note

	def update(self, uid **kwargs):
		note = self.data[uid]
		for k, v in kwargs.items(): setattr(note, k, v)
		return note	


