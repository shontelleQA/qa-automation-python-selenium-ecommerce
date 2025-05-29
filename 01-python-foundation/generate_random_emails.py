"""
Exercise: Generate Random Emails (V2)

- Create 100 random email addresses using lowercase strings.
- Domains are randomly selected from a predefined list.
- Output is saved to a CSV file (1 email per line, ends with comma).
"""

import random
import string

# List of valid domains
list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

# Config
length_of_email = 10
total_number_of_emails = 100
output_file = 'out_generate_random_email_with_list_of_domains_v2.csv'
letters = string.ascii_lowercase

# Write to file
with open(output_file, 'w') as f:
    for _ in range(total_number_of_emails):
        random_string = ''.join(random.choice(letters) for _ in range(length_of_email))
        rand_domain = random.choice(list_of_domains)
        rand_email = f"{random_string}@{rand_domain}"
        f.write(rand_email + ',\n')
