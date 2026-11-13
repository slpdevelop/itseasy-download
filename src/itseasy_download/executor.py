from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from itseasy_download.downloader import DownloadResult, Downloader
    from itseasy_download.reporter import Reporter


class Executor:
    """Class for executing HTTP download requests with statistics tracking."""

    def __init__(self, downloader: "Downloader", reporter: "Reporter"):
        """Initialize the executor with a downloader and reporter.

        Args:
            downloader: An instance of Downloader class
            reporter: An instance of Reporter class
        """
        self.downloader: "Downloader" = downloader
        self.reporter: "Reporter" = reporter
        self.statistic: "Statistic" = Statistic()

    def execute(self, url: str, attempts: int):
        """Execute multiple HTTP download requests to the given URL.

        Args:
            url: The URL address to download from
            attempts: Number of times to retry the download

        Returns:
            None
        """
        self.statistic.clear()
        self.statistic.set_attempts(attempts)

        for _ in range(attempts):
            result: DownloadResult = self.downloader.download(url)
            self.statistic.add_result(result)
            self.statistic.up_attempt()
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
    def avg_duration(self) -> float:
        """Calculate the average duration of all successful downloads in seconds."""
        return sum(a.duration for a in self.result_container) / len(self.result_container)

    @property
    def total_size(self) -> float:
        """Calculate the total size of all downloaded files in MB."""
        return sum(a.size for a in self.result_container) / (1024 * 1024)

    @property
    def avg_downloaded_speed(self) -> float:
        """Calculate the average download speed across all downloads in MB/s."""
        sum_duration = sum(a.duration for a in self.result_container)
        if sum_duration == 0:
            return 0.0
        return self.total_size / sum_duration

    def add_result(self, result: "DownloadResult") -> None:
        """Add a download result to the statistics.

        Args:
            result: The DownloadResult object to add
        """
        self.result_container.append(result)

    def set_attempts(self, attempts: int) -> None:
        """Set the total number of download attempts.

        Args:
            attempts: Number of attempts to be made
        """
        self.total_attempts = attempts

    def up_attempt(self) -> None:
        """Increment current attempt counter."""
        self.current_attempt += 1

    def clear(self) -> None:
        """Reset all statistics counters and results."""
        self.result_container = []
        self.total_attempts = 0
        self.current_attempt = 0
