import pandas as pd
import os

def save_to_files(email):
    df = pd.DataFrame([email])

    if email["category"] == "Spam":
        file = "spam_emails.csv"
    else:
        file = "authentic_emails.csv"

    df.to_csv(file, mode='a', header=not os.path.exists(file), index=False)