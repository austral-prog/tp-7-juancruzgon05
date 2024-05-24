def enumerate_list(list):
    nuevalista=[]
	for index,palabra in enumerate(list):
		if palabra != "":
			nuevalista.append(f"{len(nuevalista)}. {palabra}")
	return nuevalista


def enumerate_backwards(list):
    nuevalista=[]
	for index,palabra in enumerate(list):
		if palabra != "":
			nuevalista.append(f"{len(nuevalista)}. {palabra[::-1]}")
	return nuevalista
