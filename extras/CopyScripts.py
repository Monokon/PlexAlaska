import os

scriptexists = os.path.exists('/Applications/Plex.app/Contents/Resources/Plex/scripts/Alaska_OpenSubtitles_OSD')

currentdir = os.getcwd()
string = "cp -r %s/Alaska_OpenSubtitles_OSD /Applications/Plex.app/Contents/Resources/Plex/scripts/" % (currentdir)
string = string.replace("Application Support", "Application\ Support")

#if (scriptexists == 0):
#	os.system (string)