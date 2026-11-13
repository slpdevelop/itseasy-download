from dataclasses import dataclass
import time
import requests


@dataclass
class DownloadResult:
    time_start: float
    time_end: float
    size: int
    status_code: str

    @property
    def duration(self):
        return self.time_end - self.time_start


class Downloader:
    def download(self, url: str) -> DownloadResult:
        time_start = time.perf_counter()
        
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            time_end = time.perf_counter()
            size = int(len(response.content))
            status_code = response.status_code
            
            return DownloadResult(
                time_start=time_start,
                time_end=time_end,
                size=size,
                status_code=status_code
            )
        
        except requests.RequestException:
            time_end = time.perf_counter()
            return DownloadResult(
                time_start=time_start,
                time_end=time_end,
                size=0,
                status_code=response.status_code
            )
        
