#import vlc
#import pafy
#url = "https://www.youtube.com/watch?v=7KbY8QT0CGI"
#video=pafy.new(url)
#best=video.streams(0)
#media=vlc.MediaPlayer(best.url)
#media.play()

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
x=input('Digite algo para parar: ')