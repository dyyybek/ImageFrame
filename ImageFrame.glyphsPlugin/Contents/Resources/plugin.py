# encoding: utf-8

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


from GlyphsApp.plugins import *
from vanilla import *
from AppKit import NSColor, NSFocusRingTypeNone, NSBundle

class floatingImageFrame(GeneralPlugin):
	def settings(self):
		self.name = Glyphs.localize({'en': u'Image Frame'})
	
	def start(self):
		try: 
			# new API in Glyphs 2.3.1-910
			newMenuItem = NSMenuItem(self.name, self.showWindow)
			Glyphs.menu[WINDOW_MENU].append(newMenuItem)
		except:
			mainMenu = Glyphs.mainMenu()
			s = objc.selector(self.showWindow,signature='v@:@')
			newMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(self.name, s, "")
			newMenuItem.setTarget_(self)
			mainMenu.itemWithTag_(5).submenu().addItem_(newMenuItem)
		try:
			bundle = NSBundle.bundleWithIdentifier_("com.dyb.floatingImageFrame")
			resourcesPath = bundle.resourcePath()
			self.iconPath = resourcesPath + "/icon.png"
		except:
			pass

	def showWindow(self, sender):

		width, height = 400,300
		minWidth, minHeight = 100,100
		maxWidth, maxHeight = 1000,1000

		w = FloatingWindow((width, height),"Image Frame",minSize=(minWidth,minHeight),maxSize=(maxWidth,maxHeight))
		w.center()

		window = w.getNSWindow()
		window.setTitlebarAppearsTransparent_(1)
		window.setStandardWindowTitleButtonsAlphaValue_(0.00001)
		window.setBackgroundColor_(NSColor.whiteColor())
		window.setAlphaValue_(0.9)
		window.setMovableByWindowBackground_(True)

		w.im = ImageView((10,10,-10,-10), horizontalAlignment='center', verticalAlignment='center', scale='proportional')
		w.im.setImage(imagePath=self.iconPath)
		imview = w.im.getNSImageView()
		imview.setEditable_(True)
		imview.setFocusRingType_(NSFocusRingTypeNone)

		w.open()
		w.select()
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	