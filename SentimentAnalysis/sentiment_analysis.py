"""
Sentiment Analysis Module

This module provides functions for analyzing the sentiment of text using
a remote sentiment analysis service.
"""

import json
import requests

def sentiment_analyzer(text_to_analyze):
    """
    Analyze the sentiment of a given text using a remote sentiment analysis service.

    Args:
        text_to_analyze (str): The text for which sentiment analysis is to be performed.

    Returns:
        dict: A dictionary containing sentiment analysis results.
            - 'label' (str): The sentiment label (e.g., 'positive', 'negative', 'neutral').
            - 'score' (float): The sentiment score indicating the strength of the sentiment.
                Positive values typically indicate positive sentiment, while negative values
                indicate negative sentiment. Zero or close to zero values suggest neutrality.

    Note:
        This function sends a POST request to a remote sentiment analysis service and
        extracts sentiment information from the response.

    Example:
        >>> result = sentiment_analyzer("I love this product! It's amazing.")
        >>> print(result)
        {'label': 'positive', 'score': 0.98}
    """
    url = (
    'https://sn-watson-sentiment-bert.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=15)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
