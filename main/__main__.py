import os
import threading
from pyrogram import Client
from http.server import BaseHTTPRequestHandler, HTTPServer

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable not set!")

# Telegram bot client
app = Client("my_bot", bot_token=BOT_TOKEN)

@app.on_message()
def handle(client, message):
    print("📩 Message received:", message.text)

# Dummy HTTP server for health checks
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    port = 8080
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    print(f"✅ Health check server running on port {port}")
    server.serve_forever()

# Start health server in background
threading.Thread(target=run_http_server, daemon=True).start()

# Start the Telegram bot
print("🚀 Starting bot...")
app.run()
