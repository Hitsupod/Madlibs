# String Concatenation (aka how to put strings together)
# We want to create a string that says "subscribe to ____"
youtuber = "Hitsupod"

# Methods 
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person")

madlib = f"COmputer programming is so {adj}! It makes me so excited all the time because I love to {verb}. \
Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)