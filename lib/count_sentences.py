#!/usr/bin/env python3
import re
class MyString:
   
    def __init__(self, value=''):
      
          self.value = value
    @property
    def value(self):
         return self._value
    @value.setter
    def value(self, new_value):
         if isinstance(new_value,str):
              self._value =new_value 
         else:
              print('The value must be a string.')
              self._value=''
                       
    def is_sentence(self):
        return self._value.endswith('.')
    def is_question(self):
         return self._value.endswith('?')
    def is_exclamation(self):
         return self._value.endswith('!')
    def count_sentences(self):
         sentences = re.split(r'[!?.]', self._value)
         return len([s for s in sentences if s.strip()])
      
string = MyString("This is a string! It has three sentences. Okey.Right?")
print(string.count_sentences()) 
# my_string =MyString('Hello World.')
# print(my_string.is_sentence())

# my_string2 =MyString('Hello World!')
# print(my_string2.is_sentence())