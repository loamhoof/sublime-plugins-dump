import sublime
import sublime_plugin


class SplitLine(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel_region in self.view.sel():
            line_start = self.view.find_by_class(sel_region.a, forward=False, classes=sublime.CLASS_LINE_START)

            if sel_region.a == sel_region.b:
                line_end = self.view.find_by_class(sel_region.b, forward=True, classes=sublime.CLASS_LINE_END)
                region_to_move = sublime.Region(sel_region.a, line_end)
            else:
                region_to_move = sel_region

            text_to_move = self.view.substr(region_to_move)

            self.view.erase(edit, region_to_move)
            self.view.insert(edit, line_start, text_to_move + '\n')
