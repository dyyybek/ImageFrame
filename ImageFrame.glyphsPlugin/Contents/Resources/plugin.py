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
from vanilla import *
from AppKit import NSColor, NSFocusRingTypeNone, NSBundle, NSScreen, NSImageView
from GlyphsApp import *
from GlyphsApp.plugins import *

class DYDraggingImageView(NSImageView):
	def mouseDownCanMoveWindow(self):
		return True
class DYDraggingImageView(ImageView):
	nsImageViewClass = DYDraggingImageView
	pass

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
		try: 
			# new API in Glyphs 2.3.1-910
			newMenuItem = NSMenuItem(self.name, self.showWindow_)
			Glyphs.menu[WINDOW_MENU].append(newMenuItem)
		except:
			mainMenu = Glyphs.mainMenu()
			s = objc.selector(self.showWindow_,signature='v@:@')
			newMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(self.name, s, "")
			newMenuItem.setTarget_(self)
			mainMenu.itemWithTag_(5).submenu().addItem_(newMenuItem)
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

		w = FloatingWindow((width, height), self.name, minSize=(minWidth,minHeight), maxSize=(maxWidth,maxHeight))
		w.center()

		window = w.getNSWindow()
		window.setTitlebarAppearsTransparent_(1)
		window.setStandardWindowTitleButtonsAlphaValue_(0.00001)
		window.setBackgroundColor_(NSColor.textBackgroundColor())
		window.setAlphaValue_(0.9)
		window.setMovableByWindowBackground_(1)

		w.im = DYDraggingImageView((10,10,-10,-10), horizontalAlignment='center', verticalAlignment='center', scale='proportional')
		w.im.setImage(imageObject=self.icon)
		imview = w.im.getNSImageView()
		imview.setEditable_(True)
		imview.setFocusRingType_(NSFocusRingTypeNone)
		
		w.open()
		w.select()
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__

