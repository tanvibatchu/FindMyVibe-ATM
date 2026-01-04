# findmyvibe

A local web application for finding your vibe.

## Running the Local Server

### Option 1: Using Python (Recommended)
```bash
python3 server.py
```

Or use the convenience script:
```bash
./start-server.sh
```

The server will start at **http://localhost:8000** and automatically open in your browser.

### Option 2: Using Node.js
If you have Node.js installed:
```bash
npm start
```

Or directly:
```bash
npx http-server frontend -p 8000 -o
```

## Accessing the Website

Once the server is running, open your browser and navigate to:
- **http://localhost:8000**

The website includes:
- Home page with search functionality
- Navigation menu with links to:
  - Home
  - Playlist
  - Watchlist
  - Saved Playlist
  - Saved Movies
  - Profile

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the server.
