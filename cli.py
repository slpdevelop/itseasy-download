import argparse


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
    attempts = args.attempts

    # process(args.value)


if __name__ == "__main__":
    # "https://drive.google.com/uc?export=download&id=1wD_Z9kNehqTx1uyLBKUb40TChyaO7qzi"
    cli()