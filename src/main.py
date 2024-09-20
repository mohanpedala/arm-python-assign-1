import sqlite3
from datetime import datetime
from collections import defaultdict
import re

SQLITE_DATABASE_PATH = 'server.db'
LOG_FILE_PATH = 'server.log'

def setup_database(database_path: str) -> None:
    """
    Set up the SQLite database for storing error summaries.
    Connect to the SQLite database (or create it if it doesn't exist)
    
    :param database_path: Path to the SQLite database.
    :return: None
    """

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS error_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP,
            error_type VARCHAR(250),
            count INTEGER
        )
    ''')

    conn.commit()
    conn.close()
    
def save_to_database(summary: dict[str, int], database_path: str) -> None:
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    for error_type, count in summary.items():
        cursor.execute('''
            INSERT INTO error_summary (date, error_type, count)
            VALUES (?, ?, ?)
        ''', (datetime.now(), error_type, count))

    conn.commit()
    conn.close()

    


def summarise_errors(log_file_path: str) -> dict[str, int] | dict[None, None]:
    # dictionary to store error count
    error_summary = defaultdict(int) 

    # regex to capture error type
    error_pattern = re.compile(r"ERROR\s+(\w+):")

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                match = error_pattern.search(line)
                if match:
                    error_type = match.group(1)
                    error_summary[error_type] += 1

        if error_summary:
            return dict(error_summary)
        else:
            return {None: None}
    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
        return {None: None}




if __name__ == "__main__":
    # Set up the database
    setup_database(SQLITE_DATABASE_PATH)
    
    error_summary = summarise_errors(LOG_FILE_PATH)

    if error_summary and None not in error_summary:
        print("Error summary:", error_summary)
        
        # Save the summary to the database
        save_to_database(error_summary, SQLITE_DATABASE_PATH)
    else:
        print("No errors found or log file is missing.")
