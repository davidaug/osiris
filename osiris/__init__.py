import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('osiris', localedir, fallback=True)
_ = translate.gettext
