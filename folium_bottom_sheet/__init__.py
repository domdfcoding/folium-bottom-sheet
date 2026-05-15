#!/usr/bin/env python3
#
#  __init__.py
"""
Adds a toggleable panel to the bottom of the screen, such as to display marker information like a popup.
"""
#
#  Copyright © 2026 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# 3rd party
import folium
from folium.elements import JSCSSMixin
from folium.template import Template

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2026 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0b1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["BottomSheetDialog"]


class BottomSheetDialog(JSCSSMixin, folium.MacroElement):
	"""
	Adds a toggleable panel to the bottom of the screen, such as to display marker information like a popup.
	"""

	default_js = [
			(
					"folium-bottom-sheet-js",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-bottom-sheet@v{__version__}/folium_bottom_sheet/folium-bottom-sheet.min.js",
					),
			]

	_template = Template(
			"""
		{% macro html(this, kwargs) %}
			<bottom-sheet-dialog-manager>
				<dialog id="bottomSheetDialog">
					<bottom-sheet expand-to-scroll nested-scroll swipe-to-dismiss tabindex="0" id="bottomSheetContent">
					</bottom-sheet>
				</dialog>
            </bottom-sheet-dialog-manager>

		{% endmacro %}
		{% macro script(this, kwargs) %}
			L.setupBottomSheet();
		{% endmacro %}

    """,
			)
