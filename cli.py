import argparse
import re

from main import main


def validate_url(url):
    """Validate that the URL starts with http:// or https://"""
    if not url:
        raise ValueError("URL cannot be empty")
    
    pattern = r'^(https?)://[^\s/$.?#].[^\s]*$'
    if not re.match(pattern, url):
        raise ValueError(f"Invalid URL format: {url}")
    

def validate_attempts(attempts):
    """Validate that the number of attempts is a positive integer"""
    if not isinstance(attempts, int) or attempts <= 0:
        raise ValueError(f"Invalid number of attempts: {attempts}")
    


def cli() -> None:
    parser = argparse.ArgumentParser(
        description="File loader"
    )

    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=True,
        help="Link to download the file"
    )

    parser.add_argument(
        "-a",
        "--attempts",
        type=int,
        required=False,
        help="Number of download attempts (default: 10)",
        default=10,
        
    )

    args = parser.parse_args()

    url = args.url
    validate_url(url)

    attempts = args.attempts
    validate_attempts()

    main(url, attempts)


if __name__ == "__main__":
    # "https://drive.google.com/uc?export=download&id=1wD_Z9kNehqTx1uyLBKUb40TChyaO7qzi"
    cli()
