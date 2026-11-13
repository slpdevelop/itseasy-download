
from itseasy_download.downloader import Downloader
from itseasy_download.executor import Executor
from itseasy_download.reporter import Reporter


def process(url: str, attempts: int):
    """Main entry point of the console script.
    
    Initializes the downloader, reporter and executor components,
    then executes the download with the specified parameters.
    
    Args:
        url: The URL to download from
        attempts: Number of retry attempts for downloads
        
    Returns:
        None
    """
    downloader = Downloader()
    reporter = Reporter()
    executor = Executor(downloader, reporter)
    executor.execute(url, attempts)

