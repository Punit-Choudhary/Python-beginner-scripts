from textblob import TextBlob 
  
a = "comuter progrming is great"
print(f"original text: {a}") 
  
b = TextBlob(a) 
print(f"corrected text: {str(b.correct())}")
