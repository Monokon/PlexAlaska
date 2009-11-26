import xbmc

oldtheme = xbmc.executehttpapi("getguisetting(3;lookandfeel.skincolors)") 
currenttheme = xbmc.getInfoLabel("Skin.String(theme)")

if (currenttheme == "default"):
	if (oldtheme != "<li>SKINDEFAULT"):
		xbmc.executehttpapi("setguisetting(3;lookandfeel.skincolors;SKINDEFAULT)") 
		xbmc.executebuiltin("xbmc.ReloadSkin()")

if (currenttheme == "dark"):
	if (oldtheme != "<li>dark.xml"):
		xbmc.executehttpapi("setguisetting(3;lookandfeel.skincolors;dark.xml)") 
		xbmc.executebuiltin("xbmc.ReloadSkin()")
