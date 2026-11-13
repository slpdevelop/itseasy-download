import sys
from downloader import Downloader
from executor import Executor
from reporter import Reporter


def main(url: str, attempts: int):
    """Main entry point of the console script."""
    downloader = Downloader()
    reporter = Reporter()
    executor = Executor(downloader, reporter)
    executor.execute(url, attempts)

