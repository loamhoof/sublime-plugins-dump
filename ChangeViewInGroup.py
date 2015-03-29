import sublime_plugin

class ChangeViewInGroup(sublime_plugin.TextCommand):
    def run(self, _, step=1):
        window = self.view.window()
        views = window.views_in_group(window.active_group())
        index = views.index(self.view)
        window.focus_view(views[(index + step) % len(views)])
