from dataclasses import dataclass
import time
import requests


@dataclass
class DownloadResult:
    """ Result of a download operation."""
    # Unix timestamp when download started.
    time_start: float
    # Unix timestamp when download finished.
    time_end: float
    # Size of downloaded content in bytes.
    size: int
    # Status of the download: 'OK' or 'ERROR'.
    status: str
    # HTTP status code from the response.
    status_code: int
    

    @property
    def duration(self) -> float:
        """Calculate the duration of the download in seconds."""
        return self.time_end - self.time_start


class Downloader:
    """Class responsible for downloading files from URLs."""

    def download(self, url: str) -> DownloadResult:
        """Download a file from the given URL.
        
        Args:
            url: The URL to download from
            
        Returns:
            DownloadResult object with download statistics
        """
        time_start = time.perf_counter()
        
        response = None
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            time_end = time.perf_counter()
            size = len(response.content)
            status_code = response.status_code
            
            return DownloadResult(
                time_start=time_start,
                time_end=time_end,
                size=size,
                status="OK",
                status_code=status_code
            )
        
        except requests.RequestException:
            time_end = time.perf_counter()
            return DownloadResult(
                time_start=time_start,
                time_end=time_end,
                size=0,
                status="ERROR",
                status_code=response.status_code
            )
