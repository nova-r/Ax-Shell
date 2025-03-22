import subprocess
import re

class VPNProvider():
    def __init__(self):
        self.is_connected = False
        self.name = ""
        
    def fetch_connections(self):
        try:
            # Run nmcli command
            result = subprocess.run(
                ["nmcli", "-g", "name,type,active", "connection", "show", "--order", "name"],
                capture_output=True,
                text=True,
                check=True
            )

            # Filter lines that match 'wireguard:yes' and extract connection name
            connections = [
                re.sub(r":wireguard:yes$", "", line)
                for line in result.stdout.splitlines()
                if re.search(r":wireguard:yes$", line)
            ]

            self.is_connected = False if connections.__len__() == 0 or connections[0] == "" else True
            self.name = connections[0] if self.is_connected else ""
            return self.name if self.is_connected else ""

        except subprocess.CalledProcessError as e:
            print(f"Error running nmcli: {e}")
            return ""

    def get_only_active_wireguard(self):
        """Finds the currently active WireGuard VPN."""
        try:
            result = subprocess.run(
                ["nmcli", "-g", "name,type", "connection", "show", "--active"],
                capture_output=True,
                text=True,
                check=True
            )

            for line in result.stdout.splitlines():
                if line.endswith(":wireguard"):
                    return line.replace(":wireguard", "")
            return None
        except subprocess.CalledProcessError:
            return None

    def get_all_wireguard_connections(self):
        """Retrieves a list of all WireGuard VPN connections sorted by name."""
        try:
            result = subprocess.run(
                ["nmcli", "-g", "name,type", "connection", "show", "--order", "name"],
                capture_output=True,
                text=True,
                check=True
            )

            return [re.sub(r":wireguard$", "", line) for line in result.stdout.splitlines() if ":wireguard" in line]
        except subprocess.CalledProcessError:
            return []

    def cycle_wireguard_vpn(self):
        """Cycles to the next WireGuard VPN connection."""
        active_vpn = self.get_only_active_wireguard()
        all_vpns = self.get_all_wireguard_connections()

        activate_next = False

        for vpn in all_vpns:
            if active_vpn is None:
                # No active VPN, activate the first one
                subprocess.run(["nmcli", "connection", "up", vpn], check=True)
                print(f"Activated: {vpn}")
                break
            elif active_vpn == vpn:
                # Found the active VPN, deactivate it
                activate_next = True
                subprocess.run(["nmcli", "connection", "down", vpn], check=True)
                print(f"Deactivated: {vpn}")
            elif activate_next:
                # Activate the next VPN in the list
                subprocess.run(["nmcli", "connection", "up", vpn], check=True)
                print(f"Activated: {vpn}")
                break

    def disconnect(self):
        try:
            # Get active connections
            result = subprocess.run(
                ["nmcli", "-g", "name,type", "connection", "show", "--active"],
                capture_output=True,
                text=True,
                check=True
            )

            # Extract active WireGuard VPN name
            active_vpn = [
                re.sub(r":wireguard$", "", line)
                for line in result.stdout.splitlines()
                if ":wireguard" in line
            ]

            if not active_vpn:
                print("No active WireGuard VPN found.")
                return

            # Bring down the active WireGuard VPN connections
            for vpn in active_vpn:
                subprocess.run(["nmcli", "connection", "down", vpn], check=True)
                print(f"Disconnected: {vpn}")

        except subprocess.CalledProcessError as e:
            print(f"Error running nmcli: {e}")
