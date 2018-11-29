import sublime
import sublime_plugin


class CopyTo(sublime_plugin.TextCommand):
    def run(self, edit, forward=True, cut=False):
        to = sublime.CLASS_LINE_END if forward else sublime.CLASS_LINE_START

        to_copy = []

        for sel in self.view.sel():
            start = sel.b
            end = self.view.find_by_class(start, forward, to)
            region = sublime.Region(start, end)

            to_copy.append(self.view.substr(region))

            if cut is True:
                self.view.erase(edit, region)

        sublime.set_clipboard("\n".join(to_copy))
