# a simple python script that converts english to jungle language or whatever
# so let's get started
run = True


class Converter:
	def __init__(self):
		self.user_input = ""
		self.converted_text = ""
		self.vowels = {"a":1, "e":2, "i":3, "o":4, "u":5}
		self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		self.convert = []

	def collect_user_input(self):
		self.user_input = input("enter the sentence you want to convert to jungle words\n")
		self.user_input = self.user_input.strip()
		self.user_input = self.user_input.lower()

	def convert_text(self):
		for char in self.user_input:
			if char not in self.consonants:
				if char not in self.vowels.keys():
					self.converted_text += char

			for vowel in self.vowels.keys():
				if char == vowel:
					char = str(self.vowels[vowel])
					self.converted_text += char

			if char in self.consonants:
				char = char + "a"
				self.converted_text += char

	def print_new_text(self):
		print(self.converted_text)
		self.converted_text = ""


jungle_l = Converter()		

while run:
	jungle_l.collect_user_input()
	jungle_l.convert_text()
	jungle_l.print_new_text()