import requests
import os

class AriaProvider():
    def __init__(self):
        self.progress = 0

    def fetch_from_aria(self):
        RPC_URL = "http://localhost:6800/jsonrpc"
        RPC_TOKEN_PATH = os.path.expanduser(f"~/.config/sops-nix/secrets/ariarpc")

        # Read the RPC token from the file
        with open(RPC_TOKEN_PATH, "r") as f:
            RPC_TOKEN = f.read().strip()

        # JSON payload for the request
        payload = {
            "jsonrpc": "2.0",
            "id": "qwer",
            "method": "aria2.tellActive",
            "params": [f"token:{RPC_TOKEN}"]
        }

        # Send the request
        response = requests.post(RPC_URL, json=payload, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            data = response.json()
    
            # Extract progress progressages, avoiding division by zero
            try:
                progress_values = [
                    (int(item["completedLength"]) / int(item["totalLength"])) * 100
                    for item in data.get("result", [])
                    if int(item.get("totalLength", 0)) > 0
                ]
                progress = sum(progress_values) / len(progress_values) if progress_values else None
            except (KeyError, ValueError, ZeroDivisionError):
                progress = None

            # If no active downloads, output 0
            if progress is None:
                self.progress = 0
                return True

            self.progress = progress

        else:
            print("Error fetching data")
        return self.progress


