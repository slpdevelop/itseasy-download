from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from itseasy_download.executor import Statistic
    from itseasy_download.downloader import DownloadResult



class Reporter:
    """Class responsible for reporting download progress and final statistics."""

    def report_progress(self, result: "DownloadResult", statistic: "Statistic"):
        """Report the progress of a single download.

        Args:
            result: The DownloadResult object with current download info
            statistic: The Statistic object with overall download statistics
        """
        common = f"Request: {statistic.current_attempt}/{statistic.total_attempts}:"

        if result.status == "ERROR":
            print(f"{common} {result.status} | {result.status_code}", end="\r")
            return
        
        size_mb = result.size / (1024 * 1024)
        speed = size_mb / result.duration if result.duration > 0 else 0

        if result.size < 1024:
            size_str = f"{result.size} bytes"
        elif result.size < 1024 * 1024:
            size_str = f"{result.size / 1024:.2f} KB"
        elif result.size < 1024 * 1024 * 1024:
            size_str = f"{size_mb:.2f} MB"
        else:
            size_str = f"{size_mb / 1024:.2f} GB"

        print(f"{common} {size_str} | {speed:.2f} MB/s")

    def report_final(self, statistic: "Statistic"):
        """Print final statistics after all downloads are completed.

        Args:
            statistic: The Statistic object with all download results
        """
        print(
            f"Requests completed: {len(statistic.result_container)}\n"
            f"Average response time: {statistic.avg_duration:.3f} sec\n"
            f"Total downloaded: {statistic.total_size:.2f} MB\n"
            f"Average download speed: {statistic.avg_downloaded_speed:.2f} MB/s\n"
        )
