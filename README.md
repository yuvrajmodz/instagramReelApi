# Instagram Video Downloader API

This Project Is A Simple Flask Api That Allows Users To Download Instagram Videos By Providing A Link. It Uses Playwright And Beautifulsoup To Retrieve The Download Link From The [Fastvideosave](Https://Fastvideosave.Net) Website.

## Features

- Supports downloading videos only from Instagram links
- Uses Playwright for automated interaction with the download website
- Returns a direct download link if the video is found

## Requirements

- Python 3.8 or higher
- Playwright
- BeautifulSoup
- Flask

## Example Request

- http://localhost:5016/download?link={reel link}