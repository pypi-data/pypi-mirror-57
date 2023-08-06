import datetime, random
import wikipedia
# Create your views here.

class ChatBot:
    def __init__(self):
        self._AUTHOR_NAME = "Sourav Sen"
        self._AUTHOR_EMAIL = "bubai666sen@gmail.com"
        self._GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","let's chat", "how are you doing today")  # protected attribute
        self._GREETING_RESPONSES = ["Hi", "Hey", "Hi there", "Hello", "I am glad! You are talking to me","How can I help you?","Let's chat","Hi there","Hello there"] # protected attribute
        self._GOODBYE_MESSAGE = ["bye! take care...","good bye...","see yaa...","see you around","bye","good bye","tata","saonara","biday bondhu","bye bye"]
        self._WELCOME_MESSAGE = ["You are welcome","Most welcome","Always Welcome","My pleasure"]
        self._THANKS_MESSAGE = ["thanks","thank you","thank you very much","thanks a lot"]
        self._SUVO_BIJOYA_WISH = ["suvo bijaya","suvo vijaya","subho bijaya","subho vijaya","suvo bijoya","suvo vijoya","subho bijoya","subho vijoya"]
        self._SUVO_BIJOYA_WISH_BACK = ["Suvo Bijoya! Asche bochor abar hbe!","Suvo Bijoya","Subho bijoya dashamir priti o subhe66a","Thanks and same to you","Suvo bijoya and happy diwali ahead"]
        self._DIWALI_WISH = ["happy diwali","suvo dipaboli"]
        self._DIWALI_WISH_BACK = ["happy diwali","suvo dipaboli","Thanks...Same to you!","Happy diwali to you and your family!"]
        self._SPECIAL_CHARS = [';', ':', '!', "*",".","-","_","#","@",",","=",">","<","$","?"]
        self.DEFAULT_RESPONSES = ["I am sorry! I did't understand you","Sorry! Didn't get you","Try something else...","Sorry ?","Something went wrong!"]
        self._data = {"1": {"input": self._GREETING_INPUTS,"output": self._GREETING_RESPONSES},"2": {"input": self._THANKS_MESSAGE,"output": self._WELCOME_MESSAGE},"3": {"input": self._GOODBYE_MESSAGE,"output": self._GOODBYE_MESSAGE},"4": {"input": self._SUVO_BIJOYA_WISH,"output": self._SUVO_BIJOYA_WISH_BACK},"5": {"input": self._DIWALI_WISH,"output": self._DIWALI_WISH_BACK}}
        self._enable_wikipedia = True

    def authorName(self):
        return self._AUTHOR_NAME

    def authorEmail(self):
        return self._AUTHOR_EMAIL

    def enableWikipedia(self,val):
        self._enable_wikipedia = val

    def setData(self,data):
        for value in data:
            input_lists = []
            for val in data[value]['input']:
                for i in self._SPECIAL_CHARS :
                    val = val.lower().strip().replace(i, '')
                input_lists.append(val)
            data[value]['input'] = input_lists
        self._data = data

    def addData(self,inputs,outputs):
        input_lists = []
        for val in inputs:
                for i in self._SPECIAL_CHARS :
                    val = val.lower().strip().replace(i, '')
                input_lists.append(val)
        self._data.update({str(len(self._data)+1):{"input":input_lists,"output":outputs}})
    
    def showData(self):
        return self._data

    def quickReply(self,message):
        try:
            response = ''
            trimmed_message = message.lower().strip()
            for i in self._SPECIAL_CHARS :
                trimmed_message = trimmed_message.replace(i, '')
                            
            for value in self._data:
                #If user's input is matched, returns a respective response
                if trimmed_message in self._data[value]['input']:
                    response = random.choice(self._data[value]['output'])
                    break
            if(response==''):
                if(self._enable_wikipedia):
                    return wikipedia.summary(message)
                else:
                    return random.choice(self.DEFAULT_RESPONSES)
            else:
                return response
        except:
            return random.choice(self.DEFAULT_RESPONSES)

    def reply(self,message):
        try:
            response = []
            trimmed_message = message.lower().strip()
            for i in self._SPECIAL_CHARS :
                trimmed_message = trimmed_message.replace(i, '')
                            
            for value in self._data:
                #If user's input is matched, returns a respective response
                if trimmed_message in self._data[value]['input']:
                    response.append(random.choice(self._data[value]['output']))
                else:
                    for each_input in self._data[value]['input']:
                        if(trimmed_message.find(each_input)!=-1):
                            response.append(random.choice(self._data[value]['output']))
            if(response==[]):
                if(self._enable_wikipedia):
                    return wikipedia.summary(message)
                else:
                    return random.choice(self.DEFAULT_RESPONSES)
            else:
                return random.choice(response)
        except:
            return random.choice(self.DEFAULT_RESPONSES)
    
