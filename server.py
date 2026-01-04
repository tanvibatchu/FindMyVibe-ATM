#!/usr/bin/env python3
"""
Simple HTTP server for localhost development
Serves the frontend directory on http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Change to the frontend directory
FRONTEND_DIR = Path(__file__).parent / 'frontend'
os.chdir(FRONTEND_DIR)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server running at http://localhost:{PORT}")
        print(f"📁 Serving files from: {FRONTEND_DIR}")
        print("Press Ctrl+C to stop the server")
        try:
            # Optionally open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

