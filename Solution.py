input_file =open("e_so_many_books.txt")
first_line= input_file.readline().replace("\n","").split(" ")
books_number  = int(first_line[0])
librairies_number = int(first_line[1])
scanning_days = int(first_line[2])



books_array = input_file.readline().replace("\n","").split(" ")
books  = [ [index , 0 , int(book), 0 , False ] for  index , book in enumerate(books_array)]
libraries =[]
books_listed_in_libraries = []
for i in range(librairies_number): 
	library_info = input_file.readline().replace("\n", "").split(" ")
	books_line = input_file.readline().replace("\n","").split(" ")
	books_listed_in_libraries = books_listed_in_libraries+books_line

	cout =sum([ books[int(book)][2] for book in books_line ])
	libraries.append([i , int(library_info[1]) , int(library_info[2])  , cout , 0 , books_line , 0]  )
# remplissage repetition 
for i , book in enumerate(books): 
	rep = books_listed_in_libraries.count(str(books[i][0]))
	books[i][1] = rep
	books[i][3] = books[i][2]+54*rep



# remplissage librarie 
for i , library in enumerate(libraries):
	sume = 0
	k=0
	books_in_library = dict()
	for book in libraries[i][5]: 
		priority = books[int(book)][3]
		sume = sume +priority
		books_in_library[int(book)] = priority
		k=k+1
	libraries[i][5]= books_in_library
	libraries[i][4] = sume
	libraries[i][6] = (50*sume + libraries[i][3]+libraries[i][2])/ libraries[i][1] 

## afficher tableeau
libraries = sorted(libraries, key=lambda colonnes: colonnes[6], reverse=True)



nbBiblio=0
nbBiblio1=0
f = open("resultat7.txt","w")

def bestBooks(idl):
	listBooks = []
	global scanning_days
	scanning_days=scanning_days-libraries[idl][1]
	v = scanning_days*libraries[idl][2]
	nb = 0
	dic = libraries[idl][5]
	for book,value in sorted(dic.items(), key=lambda item: item[1], reverse=True):
		if(books[book][4]==False):
			listBooks.append(book)
			books[book][4]=True
			nb=nb+1
		if (nb==v):
			break
	return listBooks

file_text = ""
while(scanning_days!=0 and nbBiblio<librairies_number):
	chaine = ""
	books_tr = bestBooks(nbBiblio)	
	if len(books_tr )!=0:
		file_text = file_text +str(libraries[nbBiblio][0])+" "+str(len(books_tr))+"\n"
		nbBiblio1=nbBiblio1+1
		for x in books_tr:
			chaine=chaine+" "+str(x)
		chaine=chaine+"\n"
		file_text = file_text +  chaine[1:]
	nbBiblio=nbBiblio+1

file_text = str(nbBiblio1)+"\n" +file_text
f.write(file_text)
f.close()
