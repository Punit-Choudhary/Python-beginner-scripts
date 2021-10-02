# pip install textblob

from textblob import TextBlob 
  
a = "comuter progrming is gret"
print("original text: "+str(a)) 
  
b = TextBlob(a) 

print("corrected text: "+str(b.correct()))    
