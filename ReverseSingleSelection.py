import sublime_plugin


class ReverseSingleSelection(sublime_plugin.TextCommand):
    def run(self, _):
        last_selection = self.view.sel()[-1]

        self.view.sel().clear()
        self.view.sel().add(last_selection)

        self.view.show_at_center(last_selection)
