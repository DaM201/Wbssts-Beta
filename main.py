import requests, argparse, os, sys, threading, socket, platform, re
from colorama import Fore,Back,Style
running = True
class Tools:
   import update
   import ScannerIP.scannerip as scannerip
   import Resource.message as message
   import ReceiveMessage.ReceiveMessageFromServer as ReceiveMessageFromServer
   import Analyzis.analyzisIPV4 as analyzisIPV4

parser = argparse.ArgumentParser(description=f"")
parser.add_argument("-l",type=str,help="")
parser.add_argument("-update", action="store_true", help=f"")
parser.add_argument("-info", action="store_true", help=f"")
parser.add_argument("-w", action="store_true", help=f"")
parser.add_argument("-no-color",action="store_true",help=f"")
parser.add_argument("-snpt",action="store_true",help=f"")
parser.add_argument("-range-port",type=str,help="")

args = parser.parse_args()

if args.no_color:
  
  if args.l:
   if running==True:
      Tools.message.NoColorMessage.Warning(f"We will split the text into IP ADDRESS and PORT")
   if args.w:
         if running==True:
            Tools.message.NoColorMessage.Information(f"""Victim: {args.l}""")
            try:
               Tools.message.NoColorMessage.Information(f"Splitting the IP ADDRESS and PORT")
               ip,port = str(args.l).split(":")
               Tools.message.NoColorMessage.Information(f"Successfully Split the IP ADDRESS - {ip} and PORT - {port}")
               print("\n\n")
               Tools.ReceiveMessageFromServer.start_clientNoColor(ip,int(port))
               running = False
            except Exception as e:
               Tools.message.NoColorMessage.Error(f"There was a problem in Splitting text on IP ADDRESS and PORT. Output: {e}")
               port = 8000
               ip = args.l
               Tools.message.NoColorMessage.Warning(f"The IP ADDRESS will be : {args.l}. PORT will now be: {port}")
               print("\n\n")
               Tools.ReceiveMessageFromServer.start_clientNoColor(ip,int(port))
               running = False
   elif args.info:
            if running==True:
                  Tools.message.NoColorMessage.Information(f"""Victim: {args.l}""")
                  ip = str(args.l)
                  print("\n\n")
                  Tools.scannerip.TryConnect_SocketCodeNoColor.Nothing(ip=ip)
                  running = False
      
   else:
      if running==True:
         Tools.message.NoColorMessage.Information(f"""Information: {args.l}""")
         try:
               Tools.message.NoColorMessage.Information(f"Splitting the IP ADDRESS and PORT")
               ip,port = str(args.l).split(":")
               Tools.message.NoColorMessage.Information(f"Successfully Split the IP ADDRESS - {ip} and PORT - {port}")
               print("\n\n")
               Tools.scannerip.TryConnectNoColor.ToServer(ip=ip)
               running = False
         except Exception as e:
               Tools.message.NoColorMessage.Error(f"There was a problem in Splitting text on IP ADDRESS and PORT.")
               port = 8000
               ip = args.l
               Tools.message.Message.Warning(f"The IP ADDRESS will be : {args.l}. PORT will now be: {port}")
               print("\n\n")
               Tools.scannerip.TryConnectNoColor.ToServer(ip=ip)
               running = False



if args.l:
   if running==True:
      Tools.message.Message.Warning(f"We will split the text into IP ADDRESS and PORT")
   if args.w:
      if running==True:
            
            Tools.message.Message.Information(f"""Victim: {args.l}""")
            try:
               Tools.message.Message.Information(f"Splitting the IP ADDRESS and PORT")
               ip,port = str(args.l).split(":")
               Tools.message.Message.Information(f"Successfully Split the IP ADDRESS - {ip} and PORT - {port}")
               print("\n\n")
               Tools.ReceiveMessageFromServer.start_client(ip,int(port))
               running = False
            except Exception as e:
               Tools.message.Message.Error(f"There was a problem in Splitting text on IP ADDRESS and PORT. Output: {e}")
               port = 8000
               ip = args.l
               Tools.message.Message.Warning(f"The IP ADDRESS will be : {args.l}. PORT will now be: {port}")
               print("\n\n")
               Tools.ReceiveMessageFromServer.start_client(ip,int(port))
               running = False
   elif args.snpt:
     if args.range_port:
       if running==True:
         Tools.message.Message.Information(f"Victim: {args.l}\nPort Range: {args.range_port}")
         Tools.message.Message.Information(f"Trying Victim...")
         ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
         port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
         if ip_add_pattern.search(str(args.l)):
            Tools.message.Message.Information(f"{args.l} is a Valid IP ADDRESS")
            Tools.analyzisIPV4.ScanPort(ip_add_entered=str(args.l),port_range=str(args.range_port))
            running = False
         else:
            Tools.message.Message.Error(f"There was an error in dictating IP ADDRESSES. try again...")
            running = False

         Tools.analyzisIPV4.ScanPort(ip_add_entered=str(args.l),port_range=str(args.range_port))
   elif args.info:
      if running==True:
               Tools.message.Message.Information(f"""Victim: {args.l}""")
               ip = str(args.l)
               print("\n\n")
               Tools.scannerip.TryConnect_SocketCode.Nothing(ip=ip)
               running = False
      
   else:
      if running==True:
               Tools.message.Message.Information(f"""Information: {args.l}""")
         
               ip = str(args.l)
               print("\n\n")
               running = False
               Tools.scannerip.TryConnect.ToServer(ip=ip)

