import sublime
import sublime_plugin


class Executor:
    def run(self, edit):
        view = self.view
        if view.has_non_empty_selection_region():
            regions = reversed(view.sel())
        else:
            regions = [sublime.Region(0, view.size())]
        for reg in regions:
            src = view.substr(reg)
            try:
                res = self.convert(src)
                view.replace(edit, reg, res)
            except Exception as e:
                sublime.error_message(f"Convert failed:\n{str(e)}")
                return


class ConvertHexToAsciiCommand(Executor, sublime_plugin.TextCommand):
    def convert(self, text):
        return bytes.fromhex(text).decode(errors="ignore")


class ConvertAsciiToHexCommand(Executor, sublime_plugin.TextCommand):
    def convert(self, text):
        return bytes(text, encoding='utf-8').hex()
