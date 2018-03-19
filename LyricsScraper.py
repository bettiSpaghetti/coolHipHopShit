from PyLyrics import *
import os, re

def getLyricsAsText(artist):
  songs = []
  allAlbums = []
  albums = PyLyrics.getAlbums(singer=artist)
  for album in albums:
    cleanedAlbumName = re.sub(r'[/\\:*?"<>|]', '', album.name)
    makeNewDirectory(cleanedAlbumName)
    tracks = album.tracks()  # or PyLyrics.getTracks(myalbum)
    for track in tracks:
      print(track.name)
      cleanedTrackName = re.sub(r'[/\\:*?"<>|]', '', track.name)
      #songs.append(track.name)  # Each track is a track object
      writeToSpecLocation(track.name, cleanedTrackName, cleanedAlbumName, artist)
    #for song in songs:
      #writeToSpecLocation(song, artist)


# creates new subdirectories with the album name as the title
def makeNewDirectory(FolderName):
  newpath = r'G:\NLTK_Inputs' + "\\" + FolderName
  if not os.path.exists(newpath):
      os.makedirs(newpath)

"""
    Writes all the songs in an album as txt files to a directory 

    Parameters
    ----------
    arg1 : songName
        name of a song used to lookup the lyrics in PyLyrics.getLyrics
    arg2 : cleanedTrackName
        Song title with invalid windows file naming character removed
    arg3 : cleanedAlbumName
           name of the album cleaned to be used in the file path created 
           to write the songs to the correct location
    arg4 : artist
           name of the artist used to look up the lyrics in PyLyrics.getLyrics
    Returns
    -------
    void
  """

def writeToSpecLocation(songName, cleanedTrackName, album, artist):
  filename = cleanedTrackName + '.txt'
  filepath = os.path.join('G:/NLTK_Inputs/', album, filename )
  print(songName)
  print(artist)
  f = open(filepath, "w")
  try:
    f.write(PyLyrics.getLyrics(artist, songName))
  except ValueError:
    print("Song not found")
  f.close()