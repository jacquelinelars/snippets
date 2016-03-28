f = open("/Users/jacqueline/Google Drive/Bullock Serigos Toribio/Bilingual Annotation/Data/Killer Crónicas/Killer_Cronicas-Sans_Titres.txt").read()
words = f.split()
output = f = open("/Users/jacqueline/Google Drive/Bullock Serigos Toribio/Bilingual Annotation/Data/Killer_Cronicas_annotated.csv", "w")
for word in words:
    output.write(word + "\n")
output.close()
