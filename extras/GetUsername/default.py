import xbmc
import getpass
username = getpass.getuser()
string = "Skin.SetString(osxusername,%s)" % (username)
xbmc.executebuiltin(string)