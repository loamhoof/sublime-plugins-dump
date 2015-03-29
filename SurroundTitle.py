import sublime_plugin


default_char = "#"
caption = "Surround line(s) with:"


class SurroundTitle(sublime_plugin.TextCommand):
	def run(self, edit, char=default_char):
		sel = self.view.sel()

		for region in sel:
			line = self.view.line(region)
			chars = char * ((line.b - line.a) + 4)
			to_insert = " " + char + "\n" + chars
			self.view.insert(edit, line.b, to_insert)
			self.view.insert(edit, line.a, to_insert[::-1])


class SurroundTitlePanel(sublime_plugin.TextCommand):
	def run(self, _):
		self.view.window().show_input_panel(caption, default_char,
			on_done=self.on_done,
			on_change=None,
			on_cancel=None
		)

	def on_done(self, char):
		self.view.run_command("surround_title", {"char": char})
