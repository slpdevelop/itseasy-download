# itseasy-download

Command-line tool for downloading files from HTTP URLs with automatic retry logic and progress reporting.

## Installation

The tool requires Python 3.9+ and the following dependencies:

### Requirements
```
requests>=2.31.0
```

### Setup Steps

1. **Clone the repository or copy source files to your project directory**
   ```bash
   git clone <repository-url>
   cd itseasy-download
   ```

2. **Create a virtual environment**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   
   # Windows (Command Prompt)
   py -3.9 -m venv venv
   
   # Linux/macOS
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Windows (Command Prompt)
   venv\Scripts\activate.bat
   
   # Linux/macOS
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


## Usage

After installation, use the command-line tool:

```bash
itseasy_downloader -u <URL> [-a <ATTEMPTS>]
```


### Parameters

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--url` | `-u` | Yes | - | The URL to download the file from (must start with http:// or https://) |
| `--attempts` | `-a` | No | 10 | Number of times to retry the download if it fails. **Must be between 1 and 100** |

### Limitations

- **Maximum attempts**: 100 (default: 10). The tool will not accept more than 100 retry attempts.
- **Minimum attempts**: 1. At least one attempt must be made per URL.

### Examples

```bash
# Download from a single URL with default 10 attempts
itseasy_downloader -u "https://example.com/file.zip"

# Custom number of attempts (max: 100)
itseasy_downloader -u "https://example.com/file.zip" -a 3

# Maximum attempts allowed
itseasy_downloader -u "https://example.com/file.zip" -a 100

# Local file path
itseasy_downloader -u "E:\downloads\file.zip"

# Example error (attempts > 100)
```
# Output:
# Error: Invalid number of attempts: 101. Must be between 1 and 100.



## Output Statistics

The tool reports progress and final statistics in a specific format. Here are the metrics shown in the report:

### Final Report Format

```
Requests completed: <COUNT>
Average response time: <TIME> sec
Total downloaded: <SIZE> MB
Average download speed: <SPEED> MB/s
```

### Metric Definitions

| Metric | Description | Unit | Notes |
|--------|-------------|------|-------|
| **Requests completed** | Number of successful HTTP requests made | Count | Only successful downloads are counted; failed requests don't contribute |
| **Average response time** | Mean time taken to complete all successful downloads | seconds | Calculated as: `sum(duration) / count`, rounded to 3 decimal places |
| **Total downloaded** | Cumulative size of all successfully downloaded files | megabytes (MB) | All values converted to MB, rounded to 2 decimal places |
| **Average download speed** | Overall data transfer rate across all downloads | megabytes per second (MB/s) | Calculated as: `total_size_MB / total_duration_sec`, rounded to 2 decimal places |

### Speed Display

Progress updates show:
- **Size**: As formatted above ( MB )
- **Speed**: Always in MB/s with 2 decimal places

Example progress line:
```
Request: 3/10: 85.45 MB | 29.69 MB/s
```

## Error Handling

The tool handles various HTTP errors gracefully:
- Connection timeouts
- HTTP error responses (4xx, 5xx)
- Network interruptions

Failed requests are retried up to the specified number of attempts (`--attempts`). If all attempts fail for a single URL, the request is marked as `ERROR` in the progress output.

## Performance Notes

### Timing Measurement
- Uses Python's `time.perf_counter()` for high-resolution timing
- Duration includes: DNS lookup, TCP connection, TLS handshake (if HTTPS), HTTP header reading, and content transfer
- Does not include post-processing or file saving time

### Streaming Downloads
- Large files are downloaded using `stream=True` with chunk-based processing
- Default chunk size is 8KB for memory efficiency
- The tool does not save files to disk by default; you can add that functionality if needed

## Author

Created by: Team Name (add your team name here)
