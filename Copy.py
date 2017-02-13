import sublime
import sublime_plugin


class CopyTo(sublime_plugin.TextCommand):
    def run(self, _, forward=True):
        start = self.view.sel()[0].b
        end = self.view.find_by_class(start, forward, sublime.CLASS_LINE_END if forward else sublime.CLASS_LINE_START)

        to_copy = self.view.substr(sublime.Region(start, end))

        sublime.set_clipboard(to_copy)
