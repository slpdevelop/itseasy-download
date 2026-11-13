from downloader import DownloadResult
from main import Statistic


class Reporter:
    def report_progress(self, result: DownloadResult, statistic: Statistic):
        common = f"Request: {statistic.current_attempt}/{statistic.total_attempts}:"

        if result.status == "ERROR":
            print(f"{common} {result.status} | {result.status_code}", end="\r")
            return
        
        speed = result.size / result.duration
        print(f"{common} {result.size} | {speed}", end="\r")

    def report_final(self, statistic: Statistic):
        print(
            f"Requests completed: {len(statistic.result_container)}\n"
            f"Average response time: {statistic.avg_duration:.3f} sec\n"
            f"Total downloaded: {statistic.total_size:.2f} MB\n"
            f"Average download speed: {statistic.avg_downloaded_speed:.2f} MB/s\n"
        )
