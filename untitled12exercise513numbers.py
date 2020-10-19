# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:40:41 2020

@author: User
"""

#numerouno(1)k
def list_tuple(data):
    sample_list=list(data.split(","))
    sample_tuple=tuple(sample_list)
    print('List:',sample_list)
    print('Tuple:',sample_tuple)
    
if __name__ == "__main__":
    mysample=input('enter number using commas:')
    list_tuple(mysample)
#number2
def translate(text):
    mytext=""
    for j in text:
        if j  not in (["a","e","i","u","o"]):
            mytext += mytext +j+'o'+j
        else:
            mytext= mytext+j
            return mytext

if __name__ == "__main__":
    user_input=input('enter the sentence:')
    print(translate(user_input))

    
#number 3k
import calendar

def the_calendar(year,month):
    whole_year=calendar.month(year,month,w=0,l=0)
    return whole_year

if __name__ == "__main__":   
    year=int(input('enter the year:'))
    month=int(input('enter the month:'))
    print(the_calendar(year,month))
#number 4
def is_member(x,a):
    if x==a:
        return True
    else:
        return False
    
if __name__ == "__main__":
    x=str(input('any value:'))
    a=list(input('any list:'))
    print(is_member(x,a))
#number 5
def overlapping(lst1,lst2):
        for n in lst1:
             for j in lst2:
                if n==j:
                    return True
                else:
                    return False
                       
if __name__ == "__main__":
   print(overlapping(['red','blue','gold'] , ['blue','black','violet']))
#number 6
def histogram(lst):
    for i in lst:
        print(i * '*')
    
if __name__ == "__main__":
    the_data=list(eval(input('enter my list:')))
    print(histogram(the_data))
    
#number 7k
def wordlength(list_of_words):
    return list(map(lambda x:len(x),list_of_words))
if __name__ == "__main__":
    list_of_words=["pizza","noodles","pancake"]
    print('the length of the corresponding words:',(wordlength(list_of_words)))
#number 8k
def find_longest_words(lwords):
    return max(map(len,lwords))
    

if __name__ == "__main__":
    word=list(input('my words:').split(","))
    print('the longest one:',find_longest_words(word))
    
#number 9
def filter_long_words(lwords,n):
    the_word=[]
    for i in lwords:
        the_word.append(i)
        return the_word
    
if __name__ == "__main__":
    my_word=list(input('enter the words:').split(","))
    n=int(input('enter a number:'))
    print("")
    print('the last answer:',filter_long_words(my_word,n))
#number 10k
import string

def pangram(sentence):
    alphabet=string.ascii_uppercase
    for i in alphabet:
        if i not in alphabet:
            return False
        else:
            return True
                
if __name__ == "__main__":
    user_input=input('enter the sentence:')
    print(pangram(user_input))

#number 11
def char_freq(string):
    freq={}
    for i in string:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
            return freq
        

if __name__ == "__main__":
    the_sentence=input('enter sentence here:')
    print(char_freq(the_sentence))
    

#number 12
#try
#brush
#run
#fix
def makeForms(verb):
    if verb.endswith('y'):
        return verb[:-1] + 'ies'
    elif verb.endswith(list['o','ch','s','sh','x','z']):
        return verb + 'es'
    else:
        return verb + 's'
    
if __name__ == "__main__":
    input_text=input('enter a word:')
    print(makeForms(input_text))
       
#number 13
#lie
#see
#move
#hug
def makeForming(verb):
    vowel=['a','i','u','e','o']
    consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    if  verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif verb.endswith('ee'):
        return verb + 'ing'
    elif verb=='be':
        return verb + 'ing'
    elif not vowel(verb[:-1]) and vowel(verb[:-2]) and not vowel(verb[:-3]):
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'
              
if __name__ == "__main__":
  input_text=input('enter a word:')   
  print(makeForming(input_text))
    
    

    
    