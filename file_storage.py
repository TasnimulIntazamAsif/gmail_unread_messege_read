import csv, os

def save_to_files(email):

    filename = "spam_emails.csv" if email["category"]=="Spam" else "authentic_emails.csv"

    exists = os.path.exists(filename)

    with open(filename,"a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)

        if not exists:
            writer.writerow(["Sender","Subject","Summary","Category","Time"])

        writer.writerow([
            email["sender"],
            email["subject"],
            email["body"],   # summary
            email["category"],
            email["timestamp"]
        ])