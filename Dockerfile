FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application with arguments for the m3u file and output path
CMD ["python", "video_downloader.py", "--input", "download.m3u", "--output", "/downloads"]