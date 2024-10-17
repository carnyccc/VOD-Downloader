FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Environment variable to determine script (movies or series)
ENV SCRIPT_TYPE "movies"

# Run the appropriate script based on the SCRIPT_TYPE environment variable
CMD ["/bin/sh", "-c", "if [ \"$SCRIPT_TYPE\" = \"movies\" ]; then python VOD-Downloader-movies.py --input download.m3u --output /downloads; else python VOD-Downloader-series.py --input download.m3u --output /downloads; fi"]