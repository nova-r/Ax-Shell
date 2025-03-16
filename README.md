## A ʜᴀᴄᴋᴀʙʟᴇ sʜᴇʟʟ ꜰᴏʀ Hʏᴘʀʟᴀɴᴅ, ᴘᴏᴡᴇʀᴇᴅ ʙʏ [Fᴀʙʀɪᴄ](https://github.com/Fabric-Development/fabric/).

This is my own Fork of [Axenide's Ax-Shell](https://github.com/Axenide/Ax-Shell)

**There's a lot of stuff in here that probably wont work out of the box for anyone trying to use this.**

If you want to just run a script and have it work, take a look at the original Ax-Shell instead.

## Stuff i've changed from Axenide's implementations

- Notch opens and closes on hover (without click)
  - Exceptions:
    - When playing music; to still be able to use the player controls
    - When looking at kanban; to be able to drag Tasks better
- Implemented a sidebar:
  - Contains workspace switcher now
  - Has a download buttons that's implemented with aria2 to show progress and open ariang
  - Includes a VPN button to easily switch connected VPNs
- The network button opens a new terminal with nmtui
- Added matugen vesktop integration, so my discord theme changes as well
- Wallpaper picker changes wallpapers on a single click
- Ability to download wallpapers right from the wallpaper picker
- Added battery gauge to the notch (Thank you [nova](https://github.com/nova-r/)<3)
- New battery icons
- Changed scroll direction in small circular sliders for volume etc
- Margin and gap changes
- Increased max volume to 200
- Changed paths for files to make them work for myself
- Changed screen corners a bit
- Removed pins tab cause it doesnt work for me
- Removed the coming soon tab
- Removed example images to make the clone on nixos rebuild more slim (maybe)

### Dependencies
- [Fabric](https://github.com/Fabric-Development/fabric)
- [fabric-cli](https://github.com/Fabric-Development/fabric-cli)
- [Gray](https://github.com/Fabric-Development/gray)
- [Matugen](https://github.com/InioX/matugen)
- `brightnessctl`
- `cava`
- `gnome-bluetooth-3.0`
- `gobject-introspection`
- `gpu-screen-recorder`
- `grimblast`
- `hypridle`
- `hyprlock`
- `hyprpicker`
- `hyprsunset`
- `imagemagick`
- `libnotify`
- `noto-fonts-emoji`
- `playerctl`
- `swappy`
- `swww`
- `tesseract`
- `uwsm`
- `wl-clipboard`
- `wlinhibit`
- `foot`
- Python dependencies:
    - ijson
    - pillow
    - psutil
    - requests
    - setproctitle
    - toml
    - watchdog
- Fonts:
    - Zed Mono
    - Tabler Icons (included in [assests](https://github.com/HeyImKyu/Ax-Shell/tree/main/assets/fonts/tabler-icons))
