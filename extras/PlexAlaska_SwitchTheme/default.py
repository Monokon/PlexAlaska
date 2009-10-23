import xbmc

oldtheme = xbmc.getInfoLabel("Skin.String(oldtheme)")
currenttheme = xbmc.getInfoLabel("Skin.String(theme)")

if (currenttheme == "default"):
	xbmc.executehttpapi("setguisetting(3;lookandfeel.skincolors;SKINDEFAULT)") 
	if (oldtheme != currenttheme):
		xbmc.executebuiltin("xbmc.ReloadSkin()")
else:
	xbmc.executehttpapi("setguisetting(3;lookandfeel.skincolors;dark.xml)") 
	if (oldtheme != currenttheme):
		xbmc.executebuiltin("xbmc.ReloadSkin()")
