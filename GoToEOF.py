import sublime
import sublime_plugin


class GoToEof(sublime_plugin.TextCommand):
    def run(self, _):
        size = self.view.size()

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(size, size))
        self.view.show_at_center(size)
