
# The formal grammar that I have programmed consits of four components: subjet, object, verb, and location. 
# This formal grammar allows only for three types of sentences:
	# Type 1: subject + verb + object + location
	# Type 2: subject + verb + object
	# Type 3: subject + verb + location
# Please pay attention that not all sentences are necessarily meaningful!
import random
subject = ["Australopithecus","Homo habilis", "Homo rudolfensis", "Homo ergaster", "Homo erectus", "Homo heidelbergensis", "Neanderthal", "anatomically modern humans"] 
objects = ["seeds", "shells", "meat", "vegetables", "fish", "bison", "horses", "mammoth", "lions"]
Locations = ["caves", "open-air sites", "rock-shelters","mountains"]
verb = ["lived", "ate", "hunted", "hated", "loved", "appreciated", "provided"]
 # The following codes result in correct sentences based on this formal grammer.

 # Below are some examples for Type 1 sentences!
 
for counter in range(0,5):
	sentence = random.choice(subject) + "  " + random.choice(verb)+ "  " + random.choice(objects)+ " in " + random.choice(Locations) +"."
	print (sentence)

 # And now examples of type 2 sentences!

for i in range(0,5):
	sentence = random.choice(subject) + "  " +random.choice(verb) +  "  " + random.choice(objects) +"."
	print (sentence)


 # Examples for type 3 sentences.
for i in range(0,5):
	sentence = random.choice(subject)+ "  " + random.choice(verb) + " in "+ random.choice(Locations) +"."
	print (sentence)




 
