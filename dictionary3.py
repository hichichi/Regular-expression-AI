# -*- coding: utf-8 -*-
import random
import re

class Dictionary(object):
    def __init__(self):
        self.random = self.makeRandomList()
        self.pattern = self.makePatternDictionary()
        
    def makeRandomList(self):
        rfile = open("C:\\Users\hichichi\Desktop\技術者倫理.txt",'r',
                     encoding = 'utf_8')
        r_lines = rfile.readlines()
        rfile.close()
        
        randomList = []
        
        for line in r_lines:
            str = line.rstrip('\n')
            if(str!=''):
                randomList.append(str)
        return randomList
    
    def makePatternDictionary(self):
        pfile = open("C:\\Users\hichichi\pattern.txt",'r',
                     encoding = 'utf_8')
        p_lines = pfile.readlines()
        pfile.close()
        new_lines = []
        
        for line in p_lines:
            str = line.rstrip('\n')
            if(str!=''):
                new_lines.append(str)
                
        patternItemList = []
            
        for line in new_lines:
            ptn,prs = line.split('\t')
            patternItemList.append(PatternItem(ptn,prs))
        return patternItemList
    

class PaternItem:
    SEPARATOR = '^((-?\d+)##)?(.*)$'
    
    def __init__(self,pattern,phrases):
        self.initModifyAndPattern(pattern)
        self.initPhrases(phrases)
        
    def initModifyAndPattern(self,pattern):
        m = re.findall(PatternItem.SEPARATOR,phrase)
        self.modity = 0
        if m[0][1]:
            self.modity = int(m[0][1])
        self.pattern = m[0][2]
            
    def initPharase(self,phrases):
        self.phrases = []
        dic = {}
        for phrase in phrases.split('|'):
            m = re.findall(PatternItem.SEPARATOR,phrase)
            dic['need'] = 0
            if m[0] [1]:
                dic['need'] = int(m[0] [1])
            dic['phrase'] = m[0] [2]
            self.phrases.append(dic.copy())
            
        
    def match(self,str):
        return re.search(self.pattern,str)
    
    def choice(self,mood):
        choices = []
        for p in self.phrases:
            if (self.suitable(p['need'],mood)):
                choices.append(p['phrase'])
                
        if (len(choices) == 0):
            return None
        return random.choice(choices)
    
    def suitable(self,need,mood):
        if (need == 0):
            return True
        elif (need > 0):
            return(mood > need)
        else:
            return (mood < need)
                
    
        
        
    