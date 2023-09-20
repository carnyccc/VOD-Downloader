# VOD-Downloader
A video on demand downloader for IPTV providers that provide an M3U file.

## Usage
1. Copy a M3U file with series contents into the same directory as the script. 
2. Change the filename or change it in the download script. The default name is "download.m3u".
3. Then run the script: **python3 ./VOD-Downloader.py**

A valid M3U file should be structured as follows.


`#EXTINF:-1 xui-id="schnuff" tvg-id="" tvg-name="Das A-Team (1983) S01 E01" tvg-logo="https://image.tmdb.org/t/p/w185/uTTSBv371TYv8ZC8lWHsBnhrzQk.jpg" group-title="DE",Das A-Team (1983) S01 E01`<br>
`http://vod.xyz:8080/series/234556/dfgtjh/3456.mkv`<br>
`#EXTINF:-1 xui-id="schnuff" tvg-id="" tvg-name="Das A-Team (1983) S01 E02" tvg-logo="https://image.tmdb.org/t/p/w185/bqpjL3avru23SW2q1Ox1Cgh0jZt.jpg" group-title="DE,Das A-Team (1983) S01 E02`<br>
`http://vod.xyz:8080/series/234556/dfgtjh/3457.mkv`<br>
`#EXTINF:-1 xui-id="schnuff" tvg-id="" tvg-name="Das A-Team (1983) S01 E03" tvg-logo="https://image.tmdb.org/t/p/w185/pvunqB6X6WgEdjhRQDurYAq9iE.jpg" group-title="DE",Das A-Team (1983) S01 E03`<br>
`http://vod.xyz:8080/series/234556/dfgtjh/3458.mkv`<br>

## Requirements
the dependencies can be easily installed using the following command.

`pip install -r requirements.txt`
