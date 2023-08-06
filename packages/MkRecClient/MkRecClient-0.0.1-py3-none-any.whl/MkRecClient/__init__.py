import requests, essentials, json, base64, time
from PIL import Image
from io import BytesIO

"""Created by Mark @ MkNxGn"""


__host__ = "https://mkrec.mknxgn.pro/"
__client_r__ = False

class Result:

    def __init__(self, data):
        self.error = data['error']
        if self.error == False:
            self.result = data['data']['result'][0]
            self.data = data
            self.all_results = data['data']['result']
            self.time = data['data']['time']
            self.remaing_points = data['points']
            if data['heap_tk'] != False:
                self.heap = True
                self.heap_tk = data['heap_tk']['tk']
                self.possible_titles = data['heap_tk']['tiltes']
            else:
                self.heap = False
                
            
    def correct(self, title):
        if self.error == False and self.heap == True:
            resp = requests.post(__host__ + "heap?tk=" + self.heap_tk, data=json.dumps({"class": title})).text
            return resp
        else:
            raise ValueError("This image was not appended to heap, or there was an error")
    


class Machine:

    def __init__(self, name, data):
        self.name = name
        self.speed = data['speed']
        self.training = data['train']
        self.train_acc = data['train']['acc'] * 100
        self.train_dur = data['train']['dur']
        self.current_uses = data['uses']
        self.titles = data['titles']


def Register_Client(username="", key=False):
    """Register this application to use Your MK Rec Account.

    :param username: Your account's username
    :param key: An optional key to encrypt your access. Best usaged as Register_Client(username, key=input("Password: "))"""
    global __client_r__
    try:
        if key:
            __client_r__ = essentials.read_file("auth.mkrec.dat", encrypt=key)
        else:
            __client_r__ = essentials.read_file("auth.mkrec.dat")
    except:
        if username == "" or type(username) != type(""):
            raise ValueError("Please pass the username string.")
        print("Requesting Access From HOST", end="\r")
        resp = requests.post(__host__ + "regclient?username=" + username)
        if resp.status_code != 200:
            raise ConnectionError("Connection to MK Rec Failed.")
        userT = resp.text.split(":")[1]
        print("Please check the email inbox you used to sign up this account.       ", end="\r")
        time.sleep(2)
        Timeout = 50
        activated = requests.post(__host__ + "ckclient?t=" + userT).text
        while activated == "False":
            time.sleep(5)
            activated = requests.post(__host__ + "ckclient?t=" + userT).text
            Timeout -= 1
            if Timeout <= 0:
                requests.post(__host__ + "dlclient?t=" + userT)
                raise TimeoutError("Pending Approval was not met in the given time.")
            print("Waiting for approval - ID: ", userT ,". Check your email inbox: " + username, "                                        ", end="\r")
        print("Machine has been approved. Saving Credentials.                                                             ")
        if key:
            essentials.write_file("auth.mkrec.dat", userT, encrypt=key)
        else:
            essentials.write_file("auth.mkrec.dat", userT)

        __client_r__ = userT
        

def get_machines():
    machines = {}
    datas = requests.get(__host__ + "getmachines").json()
    for machine in datas:
        machines[machine] = Machine(machine, datas[machine])
    return machines

def prep_img(file_location, resize=300):
    """Prepare an image to be sent to a machine. Machines take base64 data.

    :param file_location: the destination of the file you are trying to send
    :param resize: the maximum dimension of the image, it is recommended to keep low image sizes to speed up image transfer times over the network. set to False for no resize"""
    if resize:
        img = Image.open(file_location)
        img.thumbnail((resize, resize))
    else:
        img = file_location
    return base64.b64encode(open(img, "rb").read()).decode('UTF-8')

def pil_to_imgfile(pil_img):
    """Converts a PIL image to a file to be sent to prep_img

    :param pil_img: a PIL image - opened with Image.open() from the PIL module"""

    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG')
    img_io.seek(0)

    return img_io

def get_points():
    """Get the current point value of the logged in account."""
    if __client_r__ == False:
        raise PermissionError("Please register this client to proceed")
    return requests.get(__host__ + "getp", headers={'Mkt': __client_r__}).text

def PredictImage(img, machine_name, heap=True):
    """Predicts the classification of the image by sending it to Mk Rec Machines

    :param img: The preped image that's returned from prep_img or a base64 image
    :param machine_name: The name of the machine you want to use. Get names from get_machine"""

    if __client_r__ == False:
        raise PermissionError("Please register this client to proceed")
    resp = requests.post(__host__ + "classify/" + machine_name, data=json.dumps({'data': img, 'heap': heap}), headers={'Mkt': __client_r__}).json()
    result = Result(resp)
    return result
