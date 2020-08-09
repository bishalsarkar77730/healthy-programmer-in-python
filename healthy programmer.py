from pygame import mixer
import time
def healthy():
   while 'true':
      print("affter 27 min you have to drink water\n",
            "affter 30 min you have to do eye exersice\n",
            "affter 45 min you have to do some physical work\n")
      print("for stop drink water tone type drank\n",
            "for stop eye exersice type eyeex\n",
            "for stop physicsl song type phyex\n")
      time.sleep(1620)
      mixer.init()
      mixer.music.load("songs/water.mp3")
      mixer.music.rewind()
      mixer.music.set_volume(0.7)
      mixer.music.play()
      query = input(" ")
      if query == 'drank':
         mixer.music.stop()
         print("you drinks yoour water")
      else:
         mixer.music.play()
         print("wrong input try again")
      time.sleep(180)
      mixer.init()
      mixer.music.load("songs/eyes.mp3")
      mixer.music.rewind()
      mixer.music.set_volume(0.7)
      mixer.music.play()
      query = input(" ")
      if query == 'eyeex':
         mixer.music.stop()
         print("your eyes workout done")
      else:
         mixer.music.play()
         print("wrong input try again")
      time.sleep(900)
      mixer.init()
      mixer.music.load("songs/physical.mp3")
      mixer.music.rewind()
      mixer.music.set_volume(0.7)
      mixer.music.play()
      query = input(" ")
      if query == 'phyex':
         mixer.music.stop()
         print("your physical workout done")
      else:
         mixer.music.play()
         print("wrong input try again")
      break
   again()

def again():
   cal_again = input('''
    do you want to do it again y for Yes and
    N for noo
    ''')
   if cal_again == "y":
      healthy()
   elif cal_again == "n":
      print("see you later")
   else:
      again()
healthy()