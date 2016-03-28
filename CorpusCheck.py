#  snippets
from collections import Counter
import re

# set corpus files to work with

corpus_file1 = "/Users/jacqueline/Dropbox/Central Data/NACC_Corpus-v1/NACC_Corpus-v1.corpus"
corpus_file2 ="/Users/jacqueline/Dropbox/Central Data/X-ArchiveData/GNACC_Corpus-v1/GNACC_Corpus-v1.corpus"

# read in files
corpus1 = open(corpus_file1).read()

# get word counts
word_count1 = len(corpus1.split())


# article counts
print "NACC-v1 articles :", corpus1.count("START_FILE"),  word_count1,

# find article count per newspaper
nacion_count = corpus1.count("/jacqueline/Desktop/Corpus_Texts/nacion/")

clarin_count = corpus1.count("/jacqueline/Desktop/clarin/")

cronica_count = corpus1.count("/jacqueline/Desktop/cronica_clean")

print nacion_count, clarin_count, cronica_count

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
output_file = "/Users/jacqueline/Dropbox/Central Data/NACC_Corpus-v2/NACC_Corpus-v2.txt"
with open(output_file, "w") as output:
    pattern = re.compile(ur'^\s+|\s+$', re.MULTILINE)
    for index, unique_article in seen.items():
        #remove excess whitespace
        cleaned_article = re.sub(pattern, ' ', unique_article)
        output.write(article_headers[index] + cleaned_article + "\n\n")

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