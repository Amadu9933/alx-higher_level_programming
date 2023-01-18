#we’ll call active (though you can call it anything), will monitor whether or 

#not the program should continue running














prompt = "\nTell me something, and I will repeat it back to you:"

prompt += "\nEnter 'quit' to end the program. "

 

u active = True

v while active:

 message = input(prompt)

 

w if message == 'quit':

 active = False

x else:

 print(message)


