import sublime_plugin


default_char = "-"
caption = "Fill line(s) with:"


class DashLine(sublime_plugin.TextCommand):
	def run(self, edit, char=default_char):
		sel = self.view.sel()

		for region in sel:
			line = self.view.line(region)
			self.view.insert(edit, line.b, "\n" + char * (line.b - line.a))


class DashLinePanel(sublime_plugin.TextCommand):
	def run(self, _):
		self.view.window().show_input_panel(caption, default_char,
			on_done=self.on_done,
			on_change=None,
			on_cancel=None
		)

	def on_done(self, char):
		self.view.run_command("dash_line", {"char": char})
