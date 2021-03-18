# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
#  print(f"subscribe to {youtuber}")
adj=input("Adjective : ")
verb1=input("Verb : ")
verb2=input("Verb : ")
femous_person=input("Famous Person  : ")

madlibs=f"Computer programming is so {adj}!It makes me excited all the  times because \
I love to{verb1} .Stay hydrated and {verb2} like you are {femous_person}!"
print(madlibs)