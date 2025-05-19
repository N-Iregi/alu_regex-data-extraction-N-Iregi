import re

# Sample functions for data extraction
def email_extractor(text):
    return re.findall(r'\b[a-zA-Z0-9](?:[a-zA-Z0-9._%+-]{0,62}[a-zA-Z0-9])?@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+\b', text)

def urls_extractor(text):
    return re.findall(r'https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?', text)

def phone_numbers_extractor(text):
    return re.findall(r'(?:\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})', text)

def credit_card_extractor(text):
    return re.findall(r'\b(?:\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4})\b', text)

def time_extractor(text):
    return re.findall(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b', text)
