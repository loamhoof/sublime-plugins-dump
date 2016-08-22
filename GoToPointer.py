import sublime_plugin


class GoToPointer(sublime_plugin.TextCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.viewport_position = (0, 0)

    def run(self, _):
        viewport_position = self.view.viewport_position()
        self.view.set_viewport_position(self.viewport_position)
        self.viewport_position = viewport_position
