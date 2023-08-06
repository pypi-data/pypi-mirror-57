from jupyterhub.auth import Authenticator
from tornado import gen
import json
import os
import shutil
pj = os.path.join

EXAMPLE_FOLER = os.environ.get('EXAMPLE_FOLDER', '/example')
NB_FOLDER = os.environ.get('NB_FOLDER', '/home/{username}/notebooks')

class ClassroomFileAuthenticator(Authenticator):
    def __init__(self, *args, **kwargs):
        super(ClassroomFileAuthenticator, self).__init__(self, *args, **kwargs)
        self._find_user_file()

    @gen.coroutine
    def authenticate(self, handler, data):
        name = data['username']
        if  self.USERS.get(name, '')==  data['password']:
            if self.create_user(name) == 0 or not self.check_home_exists(name):
                self.init_home_dir(name)
            return data['username']
        else:
            return None
    
    def _find_user_file(self):
        if 'USERFILE' in os.environ:
            path = os.environ['USERFILE']
        else:
            path = pj(os.getcwd(), 'users.json')
        
        if not os.path.exists(path):
            raise RuntimeError('users.json not found!')
        else:
            with open(path, 'r') as f:
                self.USERS = json.load(f)
    
    def check_home_exists(self, name):
        return os.path.exists('/home/%s' % name)
    
    def create_user(self, name):
        return os.system('useradd %s -d /home/%s' % (name, name))
    
    def init_home_dir(self, name):
        os.mkdir('/home/%s' % name)
        # add the user
        os.system("useradd %s -d /home/%s" % (name, name))
        
        # copy examples
        shutil.copytree(EXAMPLE_FOLER, NB_FOLDER.format(username=name))

        # grant permissions
        os.system("chown -R {name}:{name} /home/{name}".format(name=name))

    