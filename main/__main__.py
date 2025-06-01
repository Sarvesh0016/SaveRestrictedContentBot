
import os
import threading
from pyrogram import Client
from http.server import BaseHTTPRequestHandler, HTTPServer

# Fetch BOT_TOKEN from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable not set!")

# Initialize the bot client
app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Define a simple HTTP handler for health checks
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

# Function to run the health check server
def run_health_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    print("🩺 Health check server running on port 8080")
    server.serve_forever()

# Start the health check server in a separate thread
threading.Thread(target=run_health_server, daemon=True).start()

# Start the bot
print("🚀 Starting Telegram bot...")
app.run()
