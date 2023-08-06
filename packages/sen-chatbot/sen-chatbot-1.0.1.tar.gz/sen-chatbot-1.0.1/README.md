# sen-chatbot
Python Package for Chatbot

# How to import
>>> from sen_chatbot import ChatBot 
# How to use
>>> cb = ChatBot()
# ChatBot Initialized in cb
# reply(user_query_string) function
>>> cb.reply('hi')      
# gives reply based on the given string and data which is set
'Hi there'                
# quickReply(user_query_string) function
>>> cb.quickReply('hi') 
# same as reply(argument) but returns faster. Recommended in case of huge data. 
'Hello'

# 
# In case of reply(argument) when any of the input strings is found to be a subset of the given argument then it will consider it and show anyone of the matching results randomly. In case of quickReply(argument) it will only show the result which is fully matching with the given argument and it returns a response immediately once it finds a match.

# Adding Data
>>> input_list = ['new user','do not have account'] 
# 

>>> output_list = ['register','create one!']
# running addData(input_list,output_list) using input_list and output_list
>>> cb.addData(input_list,output_list)       
# Two lists must be passed as inputs and respective outputs.
>>> cb.reply('new user')
# output
'register'
# If any of the inputs matches with the argument of reply(argument) function then it returns a response among the outputs randomly.

# Set or Reset Data
>>> data = {'1':{'input':['hi','hello'],'output':['hello']},'2':{'input':['bye'],'output':['goodbye','tata']}}
# running setData(data) using data as argument
>>> cb.setData(data)    
# The data should be in given dictionary format.
>>> cb.showData()
# output
{'1': {'input': ['hi', 'hello'], 'output': ['hello']}, '2': {'input': ['bye'], 'output': ['goodbye', 'tata']}}    

# 
>>> cb.quickReply('bye')
# output
'tata'

# In case of adding or setting data try to keep the proper format. Previously some data is set for basic use but we can customize it according to our needs.

# Showing data
>>> cb.showData()
# output
{'1': {'input': ['hi', 'hello'], 'output': ['hello', 'hi there']}, '2': {'input': ['bye'], 'output': ['goodbye', 'tata']}}

# In case of setData(dict_data) you need to pass a dictionary in the above format.

# wikipedia feature
>>> cb.reply('Sourav Ganguly')
# output
'Sourav Chandidas Ganguly ( (listen); born 8 July 1972), affectionately known as Dada (meaning "elder brother" in Bengali), is an Indian former cricketer, commentator and administrator who played as a left-handed opening batsman and was captain of the Indian national team. He is the 39th and current president of the Board of Control for Cricket in India and President of the Editorial Board with Wisden India...    
# Wikipedia summery will be shown as a result

# It shows wikipedia results as a default output and by default wikipedia feature is enabled. If you want to disable it you can do it this way.
>>> cb.enableWikipedia(False)      
# If you pass True as an argument then it will be enabled again.
>>> cb.reply('Sourav Ganguly')
# output
'Try something else...'             
# Showing default results
>>> cb.quickReply('Sourav Ganguly')
# default output
"I am sorry! I did't understand you"

# Developer info
>>> cb.authorName()
# 

'Sourav Sen'
>>> cb.authorEmail()
# 

'bubai666sen@gmail.com'

