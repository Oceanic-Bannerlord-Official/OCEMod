from ui import UIElement
from ui_layouts import versionLabelLayout

# Retrieve version number from Module.xml
version = get_mod_version()

# Create and position the UI element
versionLabel = UIElement(versionLabelLayout)
versionLabel.position = (10, 10)  # Top right corner position

# Add the UI element to the game's UI
ui.add_element(versionLabel)
