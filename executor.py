from typing import Optional, Dict

from downloader import DownloadResult


class Executor:
    """Class for performing HTTP requests."""

    def __init__(self, downloader, reporter):
        """Initialize the executor.

        Args:
            url: URL address to download from
            att: Optional authorization header (e.g., cookie or token)
        """
        self.downloader = downloader
        self.reporter = reporter
        self.statistic = Statistic()

    def execute(self, url, attempts: int) -> Dict[str, any]:
        """Execute sequential HTTP requests to the URL.

        Args:
            max_requests: Maximum number of requests to execute

        Returns:
            Dictionary with execution results
        """
        self.statistic.clear()
        self.statistic.set_attempts(attempts)

        for i in range(attempts):
            result: DownloadResult = self.downloader.download(url)
            self.statistic.add_result(result)
            self.statistic.up_attempt(i)
            self.reporter.report_progress(result, self.statistic)

        self.reporter.report_final(self.statistic)


class Statistic:
    """Class for collecting and storing statistics."""

    def __init__(self):
        """Initialize the statistics collector."""
        self.result_container: list = []
        self.total_attempts: Optional[int] = None
        self.current_attempt: Optional[int] = None


    @property
    def avg_duration(self) -> int:
        return sum([a.duration for a in self.result_container]) / len(self.result_container)

    @property
    def total_size(self) -> float:
        return sum([a.size for a in self.result_container])

    @property
    def avg_downloaded_speed(self) -> float:
        return self.total_size / self.avg_duration


    def add_result(self, result: DownloadResult) -> None:
        self.result_container.append(result)

    def set_attempts(self, attempts: int) -> None:
        self.total_attempts = attempts

    def up_attempt(self, curr_attempt: int) -> None:
        self.current_attempt = curr_attempt

    def clear(self) -> None:
        self.result_container = []
        self.total_attempts = 0
        self.current_attempt = 0