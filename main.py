from database import init_db
from gmail_scraper import scrape_gmail
from export_csv import export_to_csv
from export_excel import export_to_excel


def main():
    print("🚀 System Starting...\n")

    # Initialize database
    print("Initializing database...")
    init_db()

    # Scrape Gmail
    print("\nScraping Gmail...")
    scrape_gmail()

    # Export data
    print("\nExporting data...")

    export_to_csv()
    print("CSV exported")

    export_to_excel()
    print("Excel exported")

    print("\nSystem completed successfully!")


if __name__ == "__main__":
    main()