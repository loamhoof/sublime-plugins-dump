import sublime_plugin


class ToCamelCase(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()

        for region in sel:
            words = self.view.substr(region).split('_')
            camel_cased = words[0] + ''.join(map(str.capitalize, words[1:]))
            self.view.replace(edit, region, camel_cased)
