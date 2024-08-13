from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


class Font(object):
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

    def try_load(self, default=None):
        try:
            pdfmetrics.registerFont(TTFont(self.name, self.filename))
            return self.name
        except Exception as e:
            import warnings
            warnings.warn(f'Undocumented exception on tia/rlab/font: {e}', category=ResourceWarning)
            return default
