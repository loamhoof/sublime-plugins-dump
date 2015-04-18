import sublime, sublime_plugin
import os, time, shutil


class DuplicateFile(sublime_plugin.ApplicationCommand):
    @staticmethod
    def run(paths):
        file_ = paths[0]
        file_name, file_ext = os.path.splitext(file_)
        copy = "%s_%d%s" % (file_name, int(time.time()), file_ext)
        shutil.copy2(file_, copy)
        print(os.path.basename(copy))
        sublime.active_window().open_file(os.path.basename(copy))

    @staticmethod
    def is_visible(paths):
        return os.path.isfile(paths[0])
