from nltk.sentiment.vader import SentimentIntensityAnalyzer


### TAKES IN A SENTENCE AND DECIDES WHETHER IT IS POS, NEG, or NEU 
def sentiment_scores(sentence):
    ### CREATE AN ANALYZER OBJECT
    analyzer = SentimentIntensityAnalyzer()
    ### ANALYZE THE sentence PARAMETER
    sentiment_dict = analyzer.polarity_scores(sentence)
    
    ### PRINT THE ANALYSIS RESULTS
    print("Overall sentiment dictionary is : ", sentiment_dict)
    
    ### MAKING THE RESULTS MORE CLEAR
    print("\nsentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    
    ### ANALYZING WHAT THE OVERALL RESULT IS
    if sentiment_dict['compound'] >= 0.05:
        overall = 'Positive'
    elif sentiment_dict['compound'] <= -0.05:
        overall = 'Negative'
    else:
        overall = 'Neutral'
        
    print("\nSentence Overall Rated As: ", overall)
    

sentence = input("Input Text for Sentiment Analysis: ")

print(sentence, '\n')
sentiment_scores(sentence)