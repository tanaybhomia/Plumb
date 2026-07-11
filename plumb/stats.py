import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib
from plumb.database import db

class StatsPage(Gtk.Box):
    def __init__(self, main_window):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.main_window = main_window

        # Add a scrollable window so stats can grow
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_hexpand(True)
        scrolled.set_vexpand(True)
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.append(scrolled)

        # Adw.Clamp keeps the content centered and readable
        clamp = Adw.Clamp()
        clamp.set_maximum_size(500)
        clamp.set_margin_top(32)
        clamp.set_margin_bottom(32)
        clamp.set_margin_start(16)
        clamp.set_margin_end(16)
        scrolled.set_child(clamp)

        # Main container inside clamp
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        clamp.set_child(self.main_box)

        # Header Stack Switcher (Today / Week / Month / All Time)
        self.time_switcher = Gtk.StackSwitcher()
        self.time_switcher.set_halign(Gtk.Align.CENTER)
        self.time_switcher.set_margin_bottom(12)
        self.main_box.append(self.time_switcher)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.main_box.append(self.stack)
        
        self.time_switcher.set_stack(self.stack)

        # Build individual pages
        self.stack.add_titled(self._build_stats_view("today"), "today", "Today")
        self.stack.add_titled(self._build_stats_view("week"), "week", "This Week")
        self.stack.add_titled(self._build_stats_view("month"), "month", "This Month")
        self.stack.add_titled(self._build_stats_view("all"), "all", "All Time")

    def _build_stats_view(self, time_range):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)

        # Filters Row
        filters_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Date selector mock
        date_btn = Gtk.Button()
        date_btn.add_css_class("flat")
        date_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        date_box.append(Gtk.Label(label="Select Date"))
        date_box.append(Gtk.Image.new_from_icon_name("pan-up-symbolic"))
        date_btn.set_child(date_box)
        
        spacer = Gtk.Box()
        spacer.set_hexpand(True)
        
        # Project Dropdown
        model = Gtk.StringList.new(["All Projects", "Default Project"])
        project_dropdown = Gtk.DropDown(model=model)
        
        filters_box.append(date_btn)
        filters_box.append(spacer)
        filters_box.append(project_dropdown)
        
        box.append(filters_box)

        # Graph Placeholder
        graph_frame = Gtk.Frame()
        graph_frame.set_vexpand(True)
        graph_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        graph_box.set_margin_top(24)
        graph_box.set_margin_bottom(24)
        graph_box.set_halign(Gtk.Align.CENTER)
        graph_box.set_valign(Gtk.Align.CENTER)
        graph_box.append(Gtk.Image.new_from_icon_name("utilities-system-monitor-symbolic"))
        graph_box.append(Gtk.Label(label="Graph Widget", margin_top=12))
        graph_frame.set_child(graph_box)
        box.append(graph_frame)

        # Heatmap Placeholder
        heatmap_frame = Gtk.Frame()
        heatmap_frame.set_vexpand(True)
        heatmap_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        heatmap_box.set_margin_top(24)
        heatmap_box.set_margin_bottom(24)
        heatmap_box.set_halign(Gtk.Align.CENTER)
        heatmap_box.set_valign(Gtk.Align.CENTER)
        heatmap_box.append(Gtk.Image.new_from_icon_name("view-grid-symbolic"))
        heatmap_box.append(Gtk.Label(label="Heatmap Widget", margin_top=12))
        heatmap_frame.set_child(heatmap_box)
        box.append(heatmap_frame)

        return box

    def update_stats(self):
        # We will call this whenever a timer finishes or the page is viewed
        # TODO: Hook up with real database queries
        pass
