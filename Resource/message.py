from colorama import *
class Tools:
   import Resource.Mytime as Mytime
class Message:
   def Error(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {Fore.GREEN}{time}{Fore.RESET} ) [G: {Fore.RED}ERROR{Fore.RESET}] > {message}")
   def Warning(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {Fore.GREEN}{time}{Fore.RESET} ) [G: {Fore.YELLOW}WARNING{Fore.RESET}] > {message}")
   def Information(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {Fore.GREEN}{time}{Fore.RESET} ) > {message}")
class NoColorMessage:
   def Error(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {time} ) [G: ERROR] > {message}")
   def Warning(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {time} ) [G: WARNING] > {message}")
   def Information(message=""):
      time = Tools.Mytime.Clock()
      print(f" ** ( {time} ) > {message}")
