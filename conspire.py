import yaml, random

with open("corpus.yaml") as fp:
    blob = yaml.load(fp.read())

# pick a name
name = random.choice(blob['names'])
scandal = random.choice(blob['scandals'])
scandal_word = random.choice(blob['synonyms-for-scandals'])
place = random.choice(blob['places'])

print "%s caught in %s %s in %s" % (name, scandal, scandal_word, place)
