import sublime_plugin


class CloseViewsInGroup(sublime_plugin.WindowCommand):
    def run(self):
        active_group = self.window.active_group()
        for view in self.window.views_in_group(active_group):
            self.window.focus_view(view)
            self.window.run_command('close_file')
