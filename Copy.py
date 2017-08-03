import sublime
import sublime_plugin


class CopyTo(sublime_plugin.TextCommand):
    def run(self, edit, forward=True, cut=False):
        start = self.view.sel()[0].b
        end = self.view.find_by_class(start, forward, sublime.CLASS_LINE_END if forward else sublime.CLASS_LINE_START)
        region = sublime.Region(start, end)

        to_copy = self.view.substr(region)

        sublime.set_clipboard(to_copy)

        if cut is True:
            self.view.erase(edit, region)
