# importing libraries 
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
#from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
 
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer   

 
# language and sentence count, miminising it within 90 words sometime doesn't make sense hence senetences used as paramete
LANGUAGE = "english"
SENTENCES_COUNT = 5
 
 
if __name__ == "__main__":
    
    url="https://www.wired.co.uk/article/electric-car-sales-china-vs-tesla"
   
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))>
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    
 
        
    print ("--LsaSummarizer--")    
    summarizer = LsaSummarizer()
    summarizer = LsaSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
         
    
    print ("--LuhnSummarizer--")     
    summarizer = LuhnSummarizer() 
    summarizer = LsaSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = ("I", "am", "the", "you", "are", "me", "is", "than", "that", "this",)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        
    
    print ("--EdmundsonSummarizer--")     
    summarizer = EdmundsonSummarizer() 
    words = ("car", "Tesla", "China" )
    summarizer.bonus_words = words    
         
        
    words = ("another", "and", "some", "next",)
    summarizer.stigma_words = words
    
     
    words = ("another", "and", "some", "next",)
    summarizer.null_words = words
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)