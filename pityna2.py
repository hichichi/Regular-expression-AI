# -*- coding: utf-8 -*-
import random
import responder2
import dictionary2

class Pityna(object):
    def __init__(self,name):
        self.name = name
        self.dictionary = dictionary2.Dictionary()
        self.emotion = Emotion(self.dictionary.pattern)
        self.res_repeat = responder2.RepeatResponder('Repeat?')
        self.res_random = responder2.RandomResponder(
                'Random', self.dictionary.random
                )
        self.res_pattern = responder2.PatternResponder(
                'Pattern', self.dictionary
                )
    def dialogue(self,input):
        self.emotion.update(input)
        x = random.randint(1,100)
        if x <= 60:
            self.responder = self.res_pattern
        elif 61 <= x <= 90:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        print(self.emotion.mood)
        return self.responder.response(input, self.emotion.mood)
    
    def get_responder_name(self):
        return self.responder.name
    
    def get_name(self):
        return self.name
    

class Emotion:
    
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5
    
    def __init__(self,pattern):
        self.pattern = pattern
        self.mood = 0
        
    def update (self,input):
        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY
        
        for ptn_item in self.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break
            
    def adjust_mood(self,val):
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN
    
    