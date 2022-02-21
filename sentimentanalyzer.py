

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative ")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral ")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive ")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive 👍✅ \n😀🙂")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative 👎❌ \n😠😡")

    else:
        print("Neutral ☑️ \n😐")

    # Driver code


if __name__ == "__main__":
    sentence = input("Enter the Statement:\n");

    # function calling
    sentiment_scores(sentence)

    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)

    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)
    
    sentence = input("\nEnter the Statement:\n")
    sentiment_scores(sentence)