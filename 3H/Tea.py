x = str(input('who is the student : '))

name = ['Edelgard','Hubert','Ferdinand','Linhardt','Caspar','Bernadetta','Dorothea','Petra','Dimitri','Dedue','Felix','Ashe','Sylvain','Mercedes','Annette','Ingrid','Claude','Lorenz','Raphael','Ignatz','Lysithea','Marianne','Hilda','Leonie','Seteth','Flayn','Hanneman','Manuela','Gilbert','Alois','Catherine','Shamir','Cyril','Jeritza','Anna','Yuri','Balthus','Constance','Hapi','Rhea']

for index, s in enumerate(name):
	if(x.upper() == s.upper()):
		pos = index

print(name[pos])




