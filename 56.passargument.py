import argparse

def parseArgs():
  parser = argparse.ArgumentParser (description='Uses the ONTAP Select Deploy API to construct and deploy a cluster.') 
  parser.add_argument('-d', '--deploy', help='Hostname or IP address of Deploy server')
  parser.add_argument('-p', '--password', help='Admin password of Deploy server')
  parser.add_argument('-c', '--config_file', help='Filename of the cluster config')
  parser.add_argument('-v', '--verbose', help='Display extra debugging messages for seeing exact API calls and responses', action='store_true', default=False)
  return parser.parse_args()
  
if __name__ == '__main__':
  args = parseArgs()
  print(args)