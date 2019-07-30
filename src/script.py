import poefixer as p

VOLUME_PATH_PREFIX = "data/"

api = p.PoeApi(next_id="457655933-474459305-447398401-512121627-486185425")

f= open(VOLUME_PATH_PREFIX + "PoeAtziri.txt","w+")

i=0;

while(i<10):
    for stash in api.get_next():
        if(stash.public==True):
            for item in stash.items:
                if "~price" in str(str(item.note).encode('utf-8')):
                    f.write("Account Name\t" + str(str(stash.accountName).encode('utf-8')) + "\n")
                    f.write("Category\t" + str(item.category) + "\n")
                    f.write("Name:\t" + str(item.name) + "\n")
                    f.write("TypeLine\t" + str(item.typeLine) + "\n")
                    f.write("Stash:\t" + str(str(stash.stash).encode('utf-8')) + "\n")
                    f.write("Note:\t" + str(str(item.note).encode('utf-8')) + "\n\n")
    print(api.next_id)
    api=p.PoeApi(next_id=api.next_id)
    i=i+1
