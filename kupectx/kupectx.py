import os
import argparse
import sys
import yaml
from . import DEFAULT_KUBECONFIG

class Kupectx(object):
    """
    Main Kupectx class
    """

    def __init__(self):
        parser = argparse.ArgumentParser(description="Command-line utility to manage Kubernetes contexts")
        parser.add_argument('-v','--version', action='version', version="0.1")
        parser.add_argument('-l', '--list', help='List contexts', dest='list', action='store_true')
        parser.add_argument('-d', '--delete', help='Delete context', dest='delete')
        self.args = parser.parse_args()
        self.main()

    def main(self):
        if self.args.list:
            self.list_contexts()
        if self.args.delete:
            deleteContext = self.args.delete
            print("Deleting context", deleteContext)
        else:
            self.list_contexts()
    
    def list_contexts(self):
        """
        List existing contexts
        """
        print("Showing list of contexts")
        defaultPath = os.path.expanduser(DEFAULT_KUBECONFIG)
        with open(defaultPath) as stream:
            #print (yaml.dump(yaml.safe_load(stream)))
            my_dict = yaml.safe_load(stream)
            print(my_dict['current-context'])
        sys.exit(0)