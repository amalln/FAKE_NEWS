import pickle
import pandas as pd
import re
import string

GB = pickle.load(open('gbmodel.pkl','rb'))
DT = pickle.load(open('dtmodel.pkl','rb'))
LR = pickle.load(open('lrmodel.pkl','rb'))
vectorization = pickle.load(open('vectorisation.pkl','rb'))



def wordopt(text):
         text = text.lower()
         text = re.sub('\[.*?]','',text)
         text = re.sub('\\W'," ",text)
         text = re.sub('https?//\S+[www\.\S+]','',text)
         text = re.sub('<.*?>+','',text)
         text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
         text = re.sub('\n','',text)
         text = re.sub('\w*\d\w','',text)
         return text

def manuel_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    
    # Use the correct model for prediction, e.g., DT for Decision Tree
    pred_GB = GB.predict(new_xv_test)

    if pred_GB==[1]:
        return 'True News',"#3fa50b"

    else:
        return 'Fake News',"#ff1c3b"


s = manuel_testing("""JAKARTA (Reuters) - Indonesia will buy 11 Sukhoi fighter jets worth $1.14 billion from Russia in exchange for cash and Indonesian commodities, two cabinet ministers said on Tuesday. The Southeast Asian country has pledged to ship up to $570 million worth of commodities in addition to cash to pay for
""")

print(s)