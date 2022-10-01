from textblob import TextBlob 
  
a = "comuter progrming is gret"
print(f"original text: {a}") 
  
b = TextBlob(a) 
print(f"corrected text: {str(b.correct())}")