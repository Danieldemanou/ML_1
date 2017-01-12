# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:03:24 2016

@author: DEMANOU
"""
#%%
import string
import collections
import nltk
##nltk.download() 
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
#%%
 
def preprocessing(text, stem=True):
    
## ici je suprime tous les signes de ponctuations 
    text = text.translate(string.punctuation)
## la tokenisation permet de transfromer les pharses en vecteur par exemple si j'ai I am 12 years old apres tokenisation j'ai un vecteur ['I', 'am', '12', 'years', 'old'] 
    tokens = word_tokenize(text)
## la j'utilise Stemmer pour avoir le racine de chaque mots par exemple lorsque je fais stemmer.stem('am') il me dira que c'est le verbe 'be'  
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens
 
 
def clusterisation(texts, clusters=3):
  
    ## j'utilise la TFIDF pour trouver les mots qui comptent dans les corpus et ainsi les utiliser pour mon algo de clusterin  
    vectorizer = TfidfVectorizer(tokenizer=preprocessing,stop_words=stopwords.words('english'),max_df=0.5, min_df=0.1, lowercase=True)
    # stop_words permet d'eliminer les stopword c'est à dire des mots t'elle que ['and','to','the','of']
    tfidf_model = vectorizer.fit_transform(texts)
    ## Kmean est utiliser ici pour faire du clustering 
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
  
    clustering = collections.defaultdict(list)
 
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)
 
    return clustering
## je compte faire un script en python 3 qui traduira les mails en francais et tout automatiser car watson ne marche pas avec python 2 
#%% 
#import json
#from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslation
#
#language_translation = LanguageTranslation(
#    username='{username}', 
#    password='{password}')
#    
#translation = language_translation.translate(
#    with open("mail.csv") as infile:
#        for line in infile:
#            text = line,
#            source='fr', 
#            target='en')
#    
#print(json.dumps(translation, indent=2, ensure_ascii=False))
# aritcle= []
#    with open("mail.csv") as infile :
#        for line in infile:
#            aritcle.append(line)
#%%
if __name__ == "__main__":
    # ceci est un echantillon de mail que j'ai traduit en anglais et que j'ai utiliser pour tester mon script
    articles = ["Hi I'm going to do operate cataract Grade BFGA004: 580 & #x80; reimbursement SS 271 & #x80; How will I have mutual?  Thanks","Madam, Sir, You find attachment, the act of death of Ms. Rosalie Martin my mother, health contract 00400190.32.    Regards Chantal Martin","Please note that Ms. Georgette DAVID died on 08/02/2015 and therefore terminate its subscription.  Regards, Administrative Service Residence of the Father Laurent 39 rue du Père Laurent 44410 HERBIGNAC bonperelaurent@wanadoo.fr 02 51 76 95 00","Bonjour. Ci joint remboursement CPAM pour pue vous effectuer le remboursement vous concernant. Dans l'attente sincères salutations.         Mr Cherfaoui Ali","Hello, On the letter of ProBTP, I note for 1 euro more an option allows you to receive assistance at home in case of unexpected hospitalization.  I would like to know the details on this option knowing that I am 100% (disability card). Remaining the campaign with medical services reduced, how should we proceed?  Can I receive help me move medical consultation knowing that I'm not and that my wife has also difficulties?  Furthermore, I am obliged to have recourse to aid (for example size of trees, computer assistance, possibly household) but are not taxable, I do not enjoy the credit  Tax.  Can I enjoy using the fund?  You thanking in advance, please receive my greetings.","Hello I wish to know what amount is your participation you will find a quote for an apparatus cordially","Ms. DEJEAN Louisette ,rue 2 Chènevières 55000 LONGEVILLE IN BARROIS with my mother Mrs. BELLOSSAT Andrée Hello I just ask you to speak directly all e-mails concerning  My mother.  It has a stroke on April 6 and therefore cannot manage its files.  I can send additional credentials.  Pending, I thank you.  Regards."]
    clusters = clusterisation(articles, 4)
    pprint(dict(clusters))
#%%
#with open("mail.csv") as infile, open("outfile.csv", "w") as outfile:
#    for line in infile:
#        outfile.write(line.replace(",", ""))