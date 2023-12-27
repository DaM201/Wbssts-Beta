import socket
import Resource.message as message
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from colorama import *
import threading


running = True

class NoColorCodeAtFileScannerIPSocketCode:
     def WriteStatus(s="",ip=""):
            running = True
            if s=="Not Connected":
                if running==True:
                    ipaddress = socket.gethostbyname(ip)
                    response = DbIpCity.get(ipaddress, api_key="free")
                    message.NoColorMessage.Information(f"""Connection Info: NOT CONNECTED TO SERVER""")
                    try:
                        message.NoColorMessage.Information(f"Connection with socket: {ip}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Connection with socket: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Information About Connection: None")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Information About Connection: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"HostByName: {socket.gethostbyname(ip)}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"HostByName: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"DefaultTimeout: {socket.getdefaulttimeout(ip)}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"DefaultTimeout: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"HostByAddr: {socket.gethostbyaddr(ip)}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"HostByAddr: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"City: {response.city}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"City: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Country: {response.country}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Country: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Region: {response.region}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Region: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Latitude: {response.latitude}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Latitude: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Longitude: {response.longitude}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Longitude: None. Output: {e}")
                    def tryHTTPNoColor():
                        message.NoColorMessage.Information("Trying HTTP")
                        message.NoColorMessage.Information("Trying Put Together http:// and IP ADDRESS")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            lines = output_text.split('\n')

                            for line in lines:
                                message.NoColorMessage.Information(f"{Fore.RED}HTTP{Fore.RESET}- {line}")
                        except Exception as e:
                            message.NoColorMessage.Error(f"There was a connection error or invalid \"http\".")
                            message.NoColorMessage.Information(f"Output: {e}")
                    
                    try:
                        host = "https://" + str(ip)
                        r = requests.get(host)
                        message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                        message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                        headers_dict = r.headers

                        output_text = ""
                        for key, value in headers_dict.items():
                            output_text += f"{key}: {value}\n"
                        lines = output_text.split('\n')

                        for line in lines:
                            message.NoColorMessage.Information(f"{Fore.RED}HTTPS{Fore.RESET}- {line}")
                        threading.Thread(target=tryHTTPNoColor).start()
                    except Exception as e:
                        message.NoColorMessage.Error(f"There was a connection error or invalid \"https\".")
                        message.NoColorMessage.Error(f"Testing \"http\"")
                        message.NoColorMessage.Information(f"Output: {e}")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            print(output_text)
                        except Exception as e:
                            message.NoColorMessage.Error(f"There was a connection error or invalid \"http\".")
                            message.NoColorMessage.Information(f"Output: {e}")
                            
                    running = False
                else:
                    pass
                
            elif s=="Connected":
                if running==True:
                    ipaddress = socket.gethostbyname(ip)
                    response = DbIpCity.get(ipaddress, api_key="free")
                    message.NoColorMessage.Information(f"""Connection Info: CONNECTED TO SERVER""")
                    try:
                        message.NoColorMessage.Information(f"Connection with socket: {ip}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Connection with socket: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Information About Connection: {server_socket}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Information About Connection: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"HostByName: {socket.gethostbyname(ip)}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"HostByName: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"DefaultTimeout: {socket.getdefaulttimeout()}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"DefaultTimeout: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"HostByAddr: {socket.gethostbyaddr(ip)}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"HostByAddr: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"City: {response.city}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"City: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Country: {response.country}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Country: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Region: {response.region}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Region: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Latitude: {response.latitude}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Latitude: None. Output: {e}")
                    try:
                        message.NoColorMessage.Information(f"Longitude: {response.longitude}")
                    except Exception as e:
                        message.NoColorMessage.Information(f"Longitude: None. Output: {e}")
                    message.NoColorMessage.Warning(f"Trying Scanning Website Information (http or https)")
                    
                    def tryHTTPNoColor():
                        message.NoColorMessage.Information("Trying HTTP")
                        message.NoColorMessage.Information("Trying Put Together http:// and IP ADDRESS")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            lines = output_text.split('\n')

                            for line in lines:
                                message.NoColorMessage.Information(f"{Fore.RED}HTTP{Fore.RESET}- {line}")
                        except Exception as e:
                            message.NoColorMessage.Error(f"There was a connection error or invalid \"http\".")
                            message.NoColorMessage.Information(f"Output: {e}")
                    try:
                        host = "https://" + str(ip)
                        r = requests.get(host)
                        message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                        message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                        headers_dict = r.headers

                        output_text = ""
                        for key, value in headers_dict.items():
                            output_text += f"{key}: {value}\n"
                        lines = output_text.split('\n')

                        for line in lines:
                            message.NoColorMessage.Information(f"{Fore.RED}HTTPS{Fore.RESET}- {line}")
                        threading.Thread(target=tryHTTPNoColor).start()
                    except Exception as e:
                        message.NoColorMessage.Error(f"There was a connection error or invalid \"https\".")
                        message.NoColorMessage.Error(f"Testing \"http\"")
                        message.NoColorMessage.Information(f"Output: {e}")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.NoColorMessage.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.NoColorMessage.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            print(output_text)
                        except Exception as e:
                            message.NoColorMessage.Error(f"There was a connection error or invalid \"http\".")
                            message.NoColorMessage.Information(f"Output: {e}")

                    running = False
                else:
                    pass


class CodeAtFileScannerIPSocketCode:
    def WriteStatus(s="",ip=""):
            running = True
            if s=="Not Connected":
                if running==True:
                    ipaddress = socket.gethostbyname(ip)
                    response = DbIpCity.get(ipaddress, api_key="free")
                    message.Message.Information(f"""Connection Info: NOT CONNECTED TO SERVER""")
                    try:
                        message.Message.Information(f"Connection with socket: {ip}")
                    except Exception as e:
                        message.Message.Information(f"Connection with socket: None. Output: {e}")
                    try:
                        message.Message.Information(f"Information About Connection: None")
                    except Exception as e:
                        message.Message.Information(f"Information About Connection: None. Output: {e}")
                    try:
                        message.Message.Information(f"HostByName: {socket.gethostbyname(ip)}")
                    except Exception as e:
                        message.Message.Information(f"HostByName: None. Output: {e}")
                    try:
                        message.Message.Information(f"DefaultTimeout: {socket.getdefaulttimeout(ip)}")
                    except Exception as e:
                        message.Message.Information(f"DefaultTimeout: None. Output: {e}")
                    try:
                        message.Message.Information(f"HostByAddr: {socket.gethostbyaddr(ip)}")
                    except Exception as e:
                        message.Message.Information(f"HostByAddr: None. Output: {e}")
                    try:
                        message.Message.Information(f"City: {response.city}")
                    except Exception as e:
                        message.Message.Information(f"City: None. Output: {e}")
                    try:
                        message.Message.Information(f"Country: {response.country}")
                    except Exception as e:
                        message.Message.Information(f"Country: None. Output: {e}")
                    try:
                        message.Message.Information(f"Region: {response.region}")
                    except Exception as e:
                        message.Message.Information(f"Region: None. Output: {e}")
                    try:
                        message.Message.Information(f"Latitude: {response.latitude}")
                    except Exception as e:
                        message.Message.Information(f"Latitude: None. Output: {e}")
                    try:
                        message.Message.Information(f"Longitude: {response.longitude}")
                    except Exception as e:
                        message.Message.Information(f"Longitude: None. Output: {e}")
                    message.Message.Warning(f"Trying Scanning Website Information (http or https)")
                    def tryHTTP():
                        message.Message.Information("Trying HTTP")
                        message.Message.Information("Trying Put Together http:// and IP ADDRESS")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.Message.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            lines = output_text.split('\n')

                            for line in lines:
                                message.Message.Information(f"{Fore.RED}HTTP{Fore.RESET}- {line}")
                        except Exception as e:
                            message.Message.Error(f"There was a connection error or invalid \"http\".")
                            message.Message.Information(f"Output: {e}")
                    
                    try:
                        host = "https://" + str(ip)
                        r = requests.get(host)
                        message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                        message.Message.Information("Successfully Getting Information About Website without: http or https")
                        headers_dict = r.headers

                        output_text = ""
                        for key, value in headers_dict.items():
                            output_text += f"{key}: {value}\n"
                        lines = output_text.split('\n')

                        for line in lines:
                            message.Message.Information(f"{Fore.RED}HTTPS{Fore.RESET}- {line}")
                        threading.Thread(target=tryHTTP).start()
                    except Exception as e:
                        message.Message.Error(f"There was a connection error or invalid \"https\".")
                        message.Message.Error(f"Testing \"http\"")
                        message.Message.Information(f"Output: {e}")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.Message.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            print(output_text)
                        except Exception as e:
                            message.Message.Error(f"There was a connection error or invalid \"http\".")
                            message.Message.Information(f"Output: {e}")

                    running = False
                else:
                    pass
                
            elif s=="Connected":
                if running==True:
                    ipaddress = socket.gethostbyname(ip)
                    response = DbIpCity.get(ipaddress, api_key="free")
                    message.Message.Information(f"""Connection Info: CONNECTED TO SERVER""")
                    try:
                        message.Message.Information(f"Connection with socket: {ip}")
                    except Exception as e:
                        message.Message.Information(f"Connection with socket: None. Output: {e}")
                    try:
                        message.Message.Information(f"Information About Connection: {server_socket}")
                    except Exception as e:
                        message.Message.Information(f"Information About Connection: None. Output: {e}")
                    try:
                        message.Message.Information(f"HostByName: {socket.gethostbyname(ip)}")
                    except Exception as e:
                        message.Message.Information(f"HostByName: None. Output: {e}")
                    try:
                        message.Message.Information(f"DefaultTimeout: {socket.getdefaulttimeout()}")
                    except Exception as e:
                        message.Message.Information(f"DefaultTimeout: None. Output: {e}")
                    try:
                        message.Message.Information(f"HostByAddr: {socket.gethostbyaddr(ip)}")
                    except Exception as e:
                        message.Message.Information(f"HostByAddr: None. Output: {e}")
                    try:
                        message.Message.Information(f"City: {response.city}")
                    except Exception as e:
                        message.Message.Information(f"City: None. Output: {e}")
                    try:
                        message.Message.Information(f"Country: {response.country}")
                    except Exception as e:
                        message.Message.Information(f"Country: None. Output: {e}")
                    try:
                        message.Message.Information(f"Region: {response.region}")
                    except Exception as e:
                        message.Message.Information(f"Region: None. Output: {e}")
                    try:
                        message.Message.Information(f"Latitude: {response.latitude}")
                    except Exception as e:
                        message.Message.Information(f"Latitude: None. Output: {e}")
                    try:
                        message.Message.Information(f"Longitude: {response.longitude}")
                    except Exception as e:
                        message.Message.Information(f"Longitude: None. Output: {e}")
                    running = False
                    message.Message.Warning(f"Trying Scanning Website Information (http or https)")
                    def tryHTTP():
                        message.Message.Information("Trying HTTP")
                        message.Message.Information("Trying Put Together http:// and IP ADDRESS")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.Message.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            lines = output_text.split('\n')

                            for line in lines:
                                message.Message.Information(f"{Fore.RED}HTTP{Fore.RESET}- {line}")
                        except Exception as e:
                            message.Message.Error(f"There was a connection error or invalid \"http\".")
                            message.Message.Information(f"Output: {e}")
                    
                    try:
                        host = "https://" + str(ip)
                        r = requests.get(host)
                        message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                        message.Message.Information("Successfully Getting Information About Website without: http or https")
                        headers_dict = r.headers

                        output_text = ""
                        for key, value in headers_dict.items():
                            output_text += f"{key}: {value}\n"
                        lines = output_text.split('\n')

                        for line in lines:
                            message.Message.Information(f"{Fore.RED}HTTPS{Fore.RESET}- {line}")
                        threading.Thread(target=tryHTTP).start()
                    except Exception as e:
                        message.Message.Error(f"There was a connection error or invalid \"https\".")
                        message.Message.Error(f"Testing \"http\"")
                        message.Message.Information(f"Output: {e}")
                        host = "http://" + str(ip)
                        try:
                            r = requests.get(host)
                            message.Message.Information("Successfully We Put Together https:// and IP ADDRESS")
                            message.Message.Information("Successfully Getting Information About Website without: http or https")
                            headers_dict = r.headers

                            output_text = ""
                            for key, value in headers_dict.items():
                                output_text += f"{key}: {value}\n"
                            print(output_text)
                        except Exception as e:
                            message.Message.Error(f"There was a connection error or invalid \"http\".")
                            message.Message.Information(f"Output: {e}")

                else:
                    pass
                    
         
class TryConnectNoColor:
    def ToServer(ip=None):
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                server_socket.settimeout(5)
                try:
                    server_socket.connect((ip,1))
                    message.NoColorMessage.Information(f"Successfully Connected to: {ip}")
                except Exception as e:
                    message.NoColorMessage.Error(f"An error occurred while connecting to the server... Output: {e}") 
                
                ipaddress = socket.gethostbyname(ip)
                response = DbIpCity.get(ipaddress, api_key="free")
                try:
                        message.NoColorMessage.Information(f"City: {response.city}")
                except Exception as e:
                        message.NoColorMessage.Information(f"City: None. Output: {e}")
                try:
                        message.NoColorMessage.Information(f"Country: {response.country}")
                except Exception as e:
                        message.NoColorMessage.Information(f"Country: None. Output: {e}")
                try:
                        message.NoColorMessage.Information(f"Region: {response.region}")
                except Exception as e:
                        message.NoColorMessage.Information(f"Region: None. Output: {e}")

class TryConnect:
    def ToServer(ip=None):
                socket.inet_aton(ip)
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.settimeout(5)
                try:
                    s.connect((ip, 1))
                    message.Message.Information(f"Successfully Connected to: {ip}")
                except Exception as e:
                    message.Message.Error(f"An error occurred while connecting to the server... Output: {e}") 
                
                ipaddress = socket.gethostbyname(ip)
                response = DbIpCity.get(ipaddress, api_key="free")
                try:
                        message.Message.Information(f"City: {response.city}")
                except Exception as e:
                        message.Message.Information(f"City: None. Output: {e}")
                try:
                        message.Message.Information(f"Country: {response.country}")
                except Exception as e:
                        message.Message.Information(f"Country: None. Output: {e}")
                try:
                        message.Message.Information(f"Region: {response.region}")
                except Exception as e:
                        message.Message.Information(f"Region: None. Output: {e}")
class TryConnect_SocketCode:
    def Nothing(CfUgCuPjCB56NE304BcmnmW="",ip=""):
                message.Message.Information(message=f"Victim ip address (server): {ip}")

                try:
                    global server_socket
                    server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                    server_socket.settimeout(5)
                    server_socket.connect((ip,1))
                    CodeAtFileScannerIPSocketCode.WriteStatus(s="Connected",ip=f"{ip}")
                except Exception as e:
                     message.Message.Error(message=f"""Server is not running. try again later... Output: {e}""")
                     CodeAtFileScannerIPSocketCode.WriteStatus(s="Not Connected",ip=f"{ip}")




















class TryConnect_SocketCodeNoColor:
    def Nothing(CfUgCuPjCB56NE304BcmnmW="",ip=""):
                message.NoColorMessage.Information(message=f"Victim ip address (server): {ip}")

                try:
                    global server_socket
                    server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                    server_socket.settimeout(5)
                    server_socket.connect((ip,1))
                    NoColorCodeAtFileScannerIPSocketCode.WriteStatus(s="Connected",ip=f"{ip}")
                except:
                     message.NoColorMessage.Error(message="""Server is not running. try again later...""")
                     NoColorCodeAtFileScannerIPSocketCode.WriteStatus(s="Not Connected",ip=f"{ip}")
    
