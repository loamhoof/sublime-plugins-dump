import sublime_plugin
from functools import partial


default_addendum = "."
default_start_from = 1
caption_addendum = "Follow numbers with:"
caption_start_from = "Start from:"


class Number(sublime_plugin.TextCommand):
    def run(self, edit, addendum=default_addendum, start_from=default_start_from):
        sel = self.view.sel()

        for region in sel:
            regions = self.view.split_by_newlines(region)
            lines = (self.view.line(region) for region in reversed(regions))
            numbers = reversed(range(start_from, start_from + len(regions)))

            for line, number in zip(lines, numbers):
                to_insert = "%d%s " % (number, addendum)
                self.view.insert(edit, line.a, to_insert)


class NumberPanel(sublime_plugin.TextCommand):
    def run(self, _):
        self.ask_addendum()

    def ask_addendum(self):
        self.view.window().show_input_panel(caption_addendum, default_addendum,
            on_done=self.ask_start_from,
            on_change=None,
            on_cancel=None
        )

    def ask_start_from(self, addendum):
        self.view.window().show_input_panel(caption_start_from, str(default_start_from),
            on_done=partial(self.on_done, addendum=addendum),
            on_change=None,
            on_cancel=None
        )

    def on_done(self, start_from, addendum):
        print(addendum)
        self.view.run_command("number", {"addendum": addendum, "start_from": int(start_from)})
