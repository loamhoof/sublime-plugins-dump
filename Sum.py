import sublime, sublime_plugin

class Sum(sublime_plugin.TextCommand):
    def run(self, _):
        sublime.message_dialog(
            str(sum(
                int(self.view.substr(region))
                for region in self.view.sel()
            ))
        )
