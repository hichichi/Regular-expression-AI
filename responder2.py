# -*- coding: utf-8 -*-

import random 
import re

class Responder(object):
    def __init__(self,name):
        self.name = name
        def response(self,input):
            return''
            
class RepeatResponder(Responder):
    def __init__(self,name):
        super().__init__(name)
    
    def response(self,input,mood):
        return '{}ってなに'.format(input)
    
class RandomResponder(Responder):
    def __init__(self,name,dic_random):
        super().__init__(name)
        self.random = dic_random
    
    def response(self,input,mood):
        return random.choice(self.random)
            
class PatternResponder(Responder):
    def __init__(self,name,dictionary):
        super().__init__(name)
        self.dictionary = dictionary
        
    def response(self,input,mood):
        
        
        resp = None
        
        for ptn_item in self.dictionary.pattern:
            m = ptn_item.match(input)
                
            if m:
                resp = ptn_item.choice(mood)
                
            if resp != None:
                return re.sub('%match%',m.group(),resp)
        return random.choice(self.dictionary.random)
        
"""   
        for ptn,prs in zip(
                self.dictionary.pattern['pattern'],
                self.dictionary.pattern['phrases']
                 ):
            print("Pattern:", ptn)
            print("Response:", prs)
            print("Input:", input)
            print("Pattern:", ptn)
            m = re.search(ptn, input)
            if m:
                resp = random.choice(prs.split('|'))
                return re.sub('%match%', m.group(), resp)
            print("Search result:", m)
        return random.choice(self.dictionary.random)
        
"""
    


