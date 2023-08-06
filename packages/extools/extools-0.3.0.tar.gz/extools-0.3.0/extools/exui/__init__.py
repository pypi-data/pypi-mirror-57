from .bare import BareUI, bareui

try:
    from accpac import UI
except ImportError:
    UI = object
    pass


class ExUI(UI):
    """An enhanced UI class for extender.

    ``ExUI`` adds additional helpers to the standard Extender UI class.
    """

    # Custom control constants
    BUTTON_WIDTH = 1065
    BUTTON_SPACE = 150

    def __init__(self, title="exui"):
        super().__init__()
        self.title = title

    def input_with_button(self, caption, callback, default="", label="Button"):
        """Create a compound field with an input field and a button::

                     +-------------------------+  +----------+
            caption  | <input field>           |  | <button> |
                     +-------------------------+  +----------+

        :param caption: input field caption
        :type caption: str
        :param callback: callback function for the button
        :type callback: function
        :param default: default value for the input field
        :type default: str
        :param label: label for the button
        :type label: str
        :returns: (input_field, button)
        :rtype: (accpac.UIField, accpac.UIButton)

        To create a file browse input and button:

        .. code-block:: python

            file_path_fld, file_browse_btn = self.input_with_button(
                    "File", self.on_browse_click, label="Browse")
        """

        # Create labeled text input field
        _id = caption.title().replace(" ", "")
        f = self.addUIField("fileField" + _id)
        f.controlType = "EDIT"
        f.size = 250
        f.width = 5000
        f.labelWidth = 60
        f.caption = caption
        f.hasFinder = False
        if default:
            f.setValue(default)

        # Add the browse button.
        bb = self.addButton("btn{}".format(_id), label)
        bb.top = f.top
        bb.width = self.BUTTON_WIDTH
        bb.left = f.left + f.width + self.BUTTON_SPACE
        bb.onClick = callback

        f.btn = bb

        return (f, bb)
