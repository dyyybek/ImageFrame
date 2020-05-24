# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

import objc
from AppKit import NSColor, NSFocusRingTypeNone, NSBundle, NSScreen, NSImageView, NSPanel, NSViewWidthSizable, NSViewHeightSizable, NSFloatingWindowLevel, NSTitledWindowMask, NSUtilityWindowMask, NSResizableWindowMask, NSClosableWindowMask
from GlyphsApp import *
from GlyphsApp.plugins import *

class DYDraggingImageView(NSImageView):
	def mouseDownCanMoveWindow(self):
		return True

class floatingImageFrame(GeneralPlugin):
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Image Frame',
			'de': 'Bilderrahmen',
			'fr': 'Cadre photo',
			'es': 'Marco de imagen',
			'pt': 'Moldura',
			'ja': '額縁',
			'ko': '액자',
			'zh': '画框',
		})
	
	@objc.python_method
	def start(self):
		newMenuItem = NSMenuItem(self.name, self.showWindow_)
		Glyphs.menu[WINDOW_MENU].append(newMenuItem)
		try:
			bundle = NSBundle.bundleWithIdentifier_("com.dyb.floatingImageFrame")
			self.icon = bundle.imageForResource_("icon.png")
			self.icon.setTemplate_(True)
		except:
			pass

	def showWindow_(self, sender):
		width, height = 400,300
		minWidth, minHeight = 100,100
		maxWidth, maxHeight = 500,500
		
		# max size of window = size of largest screen:
		for screen in NSScreen.screens():
			screenSize = screen.visibleFrame().size
			maxWidth = max(int(screenSize.width), maxWidth)
			maxHeight = max(int(screenSize.height), maxHeight)
		
		window = NSPanel.new()
		window.setMinSize_(NSMakeSize(minWidth, minHeight))
		window.setStyleMask_(NSTitledWindowMask | NSUtilityWindowMask | NSResizableWindowMask | NSClosableWindowMask)
		window.setTitlebarAppearsTransparent_(1)
		window.setStandardWindowTitleButtonsAlphaValue_(0.00001)
		window.setBackgroundColor_(NSColor.textBackgroundColor())
		window.setAlphaValue_(0.9)
		window.setMovableByWindowBackground_(1)

		if window.stringWithSavedFrame() is not None:
			window.setFrameUsingName_("com.dyb.floatingImageFrame")
		else:
			window.setFrame_display_(NSMakeRect(0, 0, width, height), True)
			window.center()

		window.setFrameAutosaveName_("com.dyb.floatingImageFrame")
		window.setLevel_(NSFloatingWindowLevel)

		imview = DYDraggingImageView.alloc().initWithFrame_(window.contentView().frame())
		imview.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)
		imview.setEditable_(True)
		imview.setFocusRingType_(NSFocusRingTypeNone)
		imview.setImage_(self.icon)
		window.contentView().addSubview_(imview)
		window.makeKeyAndOrderFront_(self)
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__

