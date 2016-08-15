def find_second(search, target):

	return search.find(target, search.find(target)+ 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')