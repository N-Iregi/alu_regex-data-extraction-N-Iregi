from regex_functions import *

# Load input with normal and edge cases
with open("sample_data.txt", "r") as file:
    sample_text = file.read()

print("=== TEST RESULTS ===")
print("Emails:", email_extractor(sample_text))
print("URLs:", urls_extractor(sample_text))
print("Phone Numbers:", phone_numbers_extractor(sample_text))
print("Credit Cards:", credit_card_extractor(sample_text))
print("Times:", time_extractor(sample_text))
