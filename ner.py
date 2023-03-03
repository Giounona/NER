# Import the spaCy library
import spacy
# Example sentences to test spaCy and its language models.
from spacy.lang.xx.examples import sentences

# Load the small language model for English and assign it to the variable 'nlp'
# nlp = spacy.load('en_core_web_sm')

#multilingual form hugging face
nlp = spacy.load('xx_ent_wiki_sm')

def ner_sys(in_text):
    # Feed the string object under 'text' to the Language object under 'nlp'
    # Store the result under the variable 'doc'
    doc = nlp(in_text)

    # initialize a list of entities
    list_of_ents = []
    # Loop over the named entities in the Doc object
    for ent in doc.ents:
        # put the named entity and its label to the dict
        ent_dict = {"text": ent.text, "type": ent.label_, "start_pos": ent.start, "end_pos": ent.end}
        # append to the list
        list_of_ents.append(ent_dict)

    return list_of_ents

# test an English language case
print(ner_sys(sentences[8]))

# test a German language case
print(ner_sys(sentences[1]))
