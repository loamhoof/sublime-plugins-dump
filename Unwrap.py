import sublime_plugin
from sublime import Region


class UnwrapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("expand_selection", {"to": "brackets"})
        for region in reversed(self.view.sel()):
            begin, end = region.begin(), region.end()
            self.view.erase(edit, Region(end, end + 1))
            self.view.erase(edit, Region(begin - 1, begin))
