# Example of condition used in Python

answer = input("Tell me: how are you doing, Good or Bad")                         # inocuous question to get user to open up
response = ()                                                                     # empty string for later use
if answer == 'Good':
    print ("\n", "Well that is great")

    print ("\n", "Let us quantify that feeling")
    scale = int(input("On a scale of one to ten, ten being the best"))            # next transition to conditional statement
    
    if scale > 5:
        print ("\n", "Oh wow tell me why")
        response = input('Do tell why you')                                       # user input for end of script
    else:
        print ("\n", "Well maybe try harder")
        next

else:
    print ("That's a shame")

print ("If you ever less happy just remember you said you were doing good today because of:", response)
