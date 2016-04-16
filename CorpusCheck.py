#  snippets
from collections import Counter
import re
import os
os.chdir("/Users/jacqueline/Dropbox/Central Data/")

# set corpus files to work with

corpus_file1 = "NACC_Corpus-v2/NACC_Corpus-v2.corpus"

corpus1 = open(corpus_file1).read()


corpus_file2 ="/X-ArchiveData/GNACC_Corpus-v1/GNACC_Corpus-v1.corpus"

# read in files


# get word counts
corpus_count1 = len(corpus1.split())


# article counts
print "NACC-v2 articles :", corpus1.count("START_FILE"),  word_count1,

# find article count per newspaper
nacion_count = corpus1.count("START_FILE:/nacion/")

clarin_count = corpus1.count("START_FILE:/clarin/")

cronica_count = corpus1.count("START_FILE:/cronica/")

print nacion_count, clarin_count, cronica_count

nacion_count + clarin_count + cronica_count



# find word count per newspaper
# creat word count function for string input
def word_count(x):
    return len(x.split())
#create lists of articles for each newspaper
articles = re.split("START_FILE:/", corpus1)
nacion = 0
clarin = 0
cronica = 0
# loop through articles to separate by newspaper
# subtract 1 from word count to remove the header count
for article in articles:
    if article.startswith("nacion"):
        nacion += word_count(article) - 1
    elif article.startswith("clarin"):
        clarin += word_count(article) - 1
    elif article.startswith("cronica"):
        cronica += word_count(article) - 1

print "{:,}".format(nacion)
print "{:,}".format(clarin)
print "{:,}".format(cronica)
print "{:,}".format(sum([cronica, clarin, nacion]))

# alternative
articles = re.split("START_FILE:/", corpus1)
nacion = []
clarin = []
cronica = []
for article in articles:
    if article.startswith("nacion"):
        nacion.append(article)
    elif article.startswith("clarin"):
        clarin.append(article)
    elif article.startswith("cronica"):
        cronica.append(article)
    else:
        print article
Nsum = sum(map(word_count, nacion)) - len(nacion)
Clsum = sum(map(word_count, clarin))
Crsum = sum(map(word_count, cronica))
Total1 = sum([Nsum, Clsum, Crsum])
Total2 = word_count(corpus1)

"{:,}".format(Total1)
"{:,}".format(Total2)


print "Nacion: ", "{:,}".format(len(nacion)), Nsum

# find all non-standard START_FILE patterns
starts = re.findall("\d+START_FILE:.*", corpus1)
nonlinks = re.findall("\d+START_FILE:([^h].*)", corpus1)
articles = re.findall("\d+START_FILE:http:\/\/(.*?)\/", corpus1)
article_links = Counter(articles)
non_link_set = Counter(nonlinks)


#### check for repeating articles

# create list of article text only
articles = re.split("START_FILE:.*", corpus1)
# ignore the first line which contains metadata
revised_articles = articles[1:]
# create list of article headers only
article_headers = re.findall("START_FILE:.*", corpus1)

# loop through text for find repeating articles
seen = {}
repeats = []
for index, art in enumerate(revised_articles):
    if art in seen.values():
        repeats.append(art)
    else:
        seen[index] = art


# output non-repeated articles to file
output_file = "NACC_Corpus-v2/NACC_Corpus-v2.corpus"
with open(output_file, "w") as output:
    # identify pattern to delete white spacde
    pattern = re.compile(ur'^\s+|\s+$', re.MULTILINE)
    # create a counter to number each article in the output file
    count = 0
    # loop through the order items in seen dictionary
    for index, unique_article in seen.items():
        #increase the count by 1
        count += 1
        # remove excess whitespace
        cleaned_article = re.sub(pattern, ' ', unique_article)
        # clean article title, removing middle directory
        rename_headers = re.sub("/cronica_clean/", "/cronica/", article_headers[index])
        clean_header = re.sub("START_FILE:.*(?=\/.*\/.*\/.*)", "START_FILE:", rename_headers)
        output.write(str(count) + clean_header + cleaned_article + "\n\n")

corpus3 = open(output_file).read()
len(corpus3.split())

pattern = re.compile(r'\s+')

sample = seen.values()[:4]
for x in sample:
    print re.sub(pattern, ' ', x)

for x in sample:
    print x.strip()

for x in sample:
    print x