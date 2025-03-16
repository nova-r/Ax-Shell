from gi.repository import GLib, Gdk
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.core.fabricator import Fabricator

from services.vpn import VPNProvider
import modules.icons as icons

class VPNStatus(Button):
    def __init__(self, **kwargs):
        super().__init__(
            name="vpn-off-button",
            orientation="h",
            on_clicked=lambda *_: self.disconnect_vpn(),
            **kwargs
        )
        
        self.vpn_provider = VPNProvider()

        self.label = Label(name="vpn-label", markup=icons.loader)
        self.add(self.label)
        self.show_all()
        self.connect("enter-notify-event", self.on_button_enter)
        self.connect("leave-notify-event", self.on_button_leave)

        self.fabricator = Fabricator(
            poll_from=lambda v: self.vpn_provider.fetch_connections(),
            on_changed=lambda f, v: self.update_vpn_display,
            interval=5000,
            stream=False,
            default_value=""
        )
        self.fabricator.changed.connect(self.update_vpn_display)
        GLib.idle_add(self.update_vpn_display, None, self.vpn_provider.name)

    def on_button_enter(self, widget, event):
        window = widget.get_window()
        if window:
            window.set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))

    def on_button_leave(self, widget, event):
        window = widget.get_window()
        if window:
            window.set_cursor(None)


    def update_vpn_display(self, sender, data):
        if data == "":
            self.add_style_class("hidden")
        else:
            self.remove_style_class("hidden")

        self.label.set_label(data)
        
    def disconnect_vpn(self):
        self.vpn_provider.disconnect()
        self.update_button()

    def update_button(self):
        self.update_vpn_display("manual update", self.vpn_provider.fetch_connections())
