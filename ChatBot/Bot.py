from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt',quiet=True)

#Get Article:
article=Article("https://www.wordstream.com/blog/ws/2017/10/04/chatbots","https://ai.googleblog.com/2020/01/towards-conversational-agent-that-can.html","https://discover.bot/bot-talk/human-like-chatbots-benefits-and-dangers/")
article.download()
article.parse()
article.nlp()
corpus=article.text
#Tokenization:
text=corpus
sentence_list=nltk.sent_tokenize(text)

#fn for greetings from user
def greeting_response(text):
    text=text.lower()

    #Bot greetings
    bot_greeting=['hello','hi','hey','hola','howdy']
    # User greetings
    user_greeting = ['hello', 'hi', 'hii', 'heyy','hey', 'hola', 'howdy','wassup']

    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)

def index_sort(list_var):
    length=len(list_var)
    list_index=list(range(0,length))
    x=list_var

    for i in range(length):
        for j in range(length):
            if x[list_index[i]]>x[list_index[j]]:
                #temp
                temp=list_index[i]
                list_index[i]=list_index[j]
                list_index[j]=temp
    return list_index
#Bot response
def bot_response(user_input):
    user_input=user_input.lower()
    sentence_list.append(user_input)
    bot_response=""
    cm=CountVectorizer().fit_transform(sentence_list)
    similarity_scores=cosine_similarity(cm[-1],cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    response_flag=0

    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]]>0.0:
            bot_response=bot_response+" "+sentence_list[index[i]]
            response_flag=1
            j=j+1
            if j>2:
                break
    if response_flag==0:
            bot_response=bot_response+" "+"I apologize,I don't understand"
    sentence_list.remove(user_input)
    return bot_response
#Chat
print("I am your personal AI Bot. I will answer all your questions.\n"
      "If you want to exit,either type"+" exit"+" or see you later"+" or bye"+" or quit"+" or break")
exit_list=["exit","see you later","bye","quit","break"]
create_list = ["who created you", "who made you", "who is your owner"]
while(True):
    user_input=input()
    if user_input.lower() in create_list:
        print("Bot: I am created by Shivam Tandon using Python 3.8.5")
    else:
        if user_input.lower() in exit_list:
            print("BOT: Chat with you later.Bye!")
            break
        else:
            if greeting_response(user_input)!=None:
                print("Bot: "+greeting_response(user_input))
            else:
                print("Bot: "+bot_response(user_input))