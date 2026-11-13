
from itseasy_download.downloader import Downloader
from itseasy_download.executor import Executor
from itseasy_download.reporter import Reporter


def process(url: str, attempts: int):
    """Main entry point of the console script."""
    downloader = Downloader()
    reporter = Reporter()
    executor = Executor(downloader, reporter)
    executor.execute(url, attempts)

