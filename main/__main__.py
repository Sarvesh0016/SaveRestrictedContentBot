import os
from pyrogram import Client
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create Pyrogram bot client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Health check handler for Koyeb
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

# Run health server on port 8080
def run_health_server():
    try:
        server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
        print("✅ Health check server running on port 8080")
        server.serve_forever()
    except Exception as e:
        print(f"❌ Failed to start health server: {e}")

# Start health check server in a background thread
threading.Thread(target=run_health_server, daemon=True).start()

# Start the bot
print("🚀 Starting bot...")
app.run()
