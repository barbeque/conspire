import yaml, random

with open("corpus.yaml") as fp:
    blob = yaml.load(fp.read())

# pick a name
name = random.choice(blob['names'])
scandal = random.choice(blob['scandals'])
place = random.choice(blob['places'])

print "%s caught in %s scandal in %s" % (name, scandal, place)
