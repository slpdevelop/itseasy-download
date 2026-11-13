import argparse
import re

from itseasy_download.main import process

# "https://drive.google.com/uc?export=download&id=1wD_Z9kNehqTx1uyLBKUb40TChyaO7qzi"


def validate_url(url):
    """Validate that the URL starts with http:// or https:// and is a valid format.

    Args:
        url: The URL string to validate

    Raises:
        ValueError: If the URL is empty or has invalid format
    """
    if not url:
        raise ValueError("URL cannot be empty")

    pattern = r"^(https?)://[^\s/$.?#].[^\s]*$"
    if not re.match(pattern, url):
        raise ValueError(f"Invalid URL format: {url}")


def validate_attempts(attempts):
    """Validate that the number of attempts is a positive integer between 1 and 100.

    Args:
        attempts: The number of download attempts to make

    Raises:
        ValueError: If attempts is not a positive integer or exceeds maximum limit
    """
    if not isinstance(attempts, int) or attempts <= 0 or attempts > 100:
        raise ValueError(f"Invalid number of attempts: {attempts}. Must be between 1 and 100.")


def main() -> None:
    """Parse command-line arguments and start the download process.

    Reads URL and attempt count from command line, validates them,
    and initiates the download via process().

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="File loader")

    parser.add_argument("-u", "--url", type=str, required=True, help="Link to download the file")

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
    validate_attempts(attempts)

    process(url, attempts)


if __name__ == "__main__":
    main()
