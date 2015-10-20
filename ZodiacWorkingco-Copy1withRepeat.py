
# coding: utf-8

# In[10]:

# zodiacsteup will do all the opening, loading an closing of files/data
def ZodiacSetup(): 


    # open the zodic descriptions file

    ZodiacText = open('zodiacDescriptions.txt','r')
    #for line in ZodiacText:
    #print(line)
    # Load the file. we are going to make a list with each line of the file
    # as  a lsit item
    ZodiacListTemp= []
    for animal in ZodiacText:
        if animal != '\n':
            ZodiacListTemp.append(animal)
    # Close the file as soon we are done with it 
    ZodiacText.close()
    return ZodiacListTemp 
#ZodiacCalaculation will collect a birth year and determine the chinese zodiac animal and then display it.
def ZodaicCalculation():
    # Ask the user for input
    birthYear = input("What year were you born? ")
    try:
        birthYear = int(birthYear)
    # Do some math
    #john lied about the list and we have to figure out a way offest the mistake by substracting
        zodiacIndex = (birthYear-4) % 12
    # Tell user the result
        print("Your Chinese Zodiac Animal is a", ZodiacList[zodiacIndex])

       
    except ValueError:
        print("put a year.")
    return birthYear


# Repeat
ZodiacList = ZodiacSetup()
birthYear = 0
while type(birthYear) is int :
    birthYear = ZodaicCalculation()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



