import os
import requests
from tqdm.notebook import tqdm

class FileDownloader:
    def __init__(self, data_directory='../data'):
        """
        Initialize the FileDownloader with a specified directory.

        Args:
            data_directory (str): The directory where files will be downloaded. Defaults to '../data'.
        """
        self.data_directory = data_directory

        # Ensure the directory exists
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def download_file(self, url, filename):
        """
        Download a file from a given URL into the specified directory with a specified filename.

        Args:
            url (str): URL of the file to be downloaded.
            filename (str): Name of the file to be saved.

        Returns:
            str: Path to the downloaded file.
        """
        # Define the full path for the new file
        file_path = os.path.join(self.data_directory, filename)

        # Start the download
        response = requests.get(url, stream=True)
        response.raise_for_status()  # To ensure we notice bad responses

        # Get the total file size from header (if available)
        total_size = int(response.headers.get('content-length', 0))

        # Initialize the progress bar from tqdm.notebook
        with tqdm(total=total_size, unit='iB', unit_scale=True, desc=f"Downloading {filename}") as progress_bar:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive new chunks
                        progress_bar.update(len(chunk))
                        f.write(chunk)

        print(f"File downloaded successfully and saved to {file_path}")
        return file_path

# Usage Example:
# downloader = FileDownloader(data_directory='../data')
# file_path = downloader.download_file("https://example.com/file.zip", "file.zip")
