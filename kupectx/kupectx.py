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
        defaultPath = os.path.expanduser(DEFAULT_KUBECONFIG)
        stream = open(defaultPath, "r")
        self.kubeConfig = yaml.safe_load(stream)
        self.numContexts = len(self.kubeConfig['contexts'])
        self.numClusters = len(self.kubeConfig['clusters'])
        self.numUsers = len(self.kubeConfig['users'])
        print("No. of Contexts = ", self.numContexts)
        print("No. of Clusters = ", self.numClusters)
        print("No. of Users = ", self.numUsers)
        if self.args.list:
            self.list_contexts()
        if self.args.delete:
            deleteContext = self.args.delete
            print("Deleting context", deleteContext)
        else:
            self.list_contexts()
        stream.close()
    
    def list_contexts(self):
        """
        List existing contexts
        """

        for ctx in range(0,self.numContexts):
            print("Context:", self.kubeConfig['contexts'][ctx]['name'])
            print(" Cluster:", self.kubeConfig['contexts'][ctx]['context']['cluster'])
            print(" User:", self.kubeConfig['contexts'][ctx]['context']['user'])

        # for clus in range(0, self.numClusters):
        #     print("Clusters:", self.kubeConfig['clusters'][clus]['name'])

        sys.exit(0)