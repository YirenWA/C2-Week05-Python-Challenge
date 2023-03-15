#!/usr/bin/env python
# coding: utf-8

# In[9]:


from IPython.display import Image
Image("F:\Term2\coding two\python/python c.jpg",width=700,height=800)


# In[8]:


#Poem: Yearning for your warmth so bright. Only you could shine this light. Understanding, with heart so pure.
#All my days and nights aglow. Radiating love, you've felt. Encompassing all who're near. Love, compassion you make clear.
#In my sky, you are a guide. Kindness you so selflessly provide. Every moment, you make me see. Always brilliant, just for me.
#So, my dear, continue to shine. Truly, you're one of a kind. And always know, no matter how far. Radiant, always come what may.

#Clue: The answer is hidden throughout the poem. “There is a phrase that has been in my head.”

text = "Yearning for your warmth so bright. Only you could shine this light. Understanding, with heart so pure. All my days and nights aglow. Radiating love, you've felt. Encompassing all who're near. Love, compassion you make clear. In my sky, you are a guide. Kindness you so selflessly provide. Every moment, you make me see. Always brilliant, just for me. So, my dear, continue to shine. Truly, you're one of a kind. And always know, no matter how far. Radiant, always come what may."
sentences = text.replace('"', '').split('. ')
first_letters = [] 

for sentence in sentences:
    words = sentence.split()
    first_word = words[0]
    first_letters.append(first_word[0])
first_letters = [sentence[0] for sentence in sentences] 
output = ' '.join(first_letters)

print(output)

