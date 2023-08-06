class Cat:
    description = '"The cat (Felis catus) is a small carnivorous mammal. It '\
	  + 'is the only domesticated species in the family Felidae and often '\
	  + 'referred to as the domestic cat to distinguish it from wild members '\
	  + 'of the family. The cat is either a house cat or a farm cat, which '\
	  + 'are pets, or a feral cat, which ranges freely and avoids human contact. '\
	  + 'House cats are valued by humans for companionship and for their ability '\
	  + 'to hunt rodents. About 60 cat breeds are recognized by various cat '\
	  + 'registries." (Wikipedia)'

    def __init__(self, name=None, breed=None, gender=None, age=None):
    	if gender != None:
    		if not gender in ['male', 'female']:
    			raise 'Gender must be "male" or "female".';

    	if age != None and type(age) != int:
    		raise 'Age must be an integer value.';

    	self.name = name
    	self.breed = breed
    	self.gender = gender
    	self.age = age

    def __repr__(self):
    	return(f'[Cat]\n - name: {self.name}\n - breed: {self.breed}\n - gender: {self.gender}\n - age: {self.age} ')

