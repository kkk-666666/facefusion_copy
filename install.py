#!/usr/bin/env python3

import subprocess

subprocess.call([ 'pip', 'install' , 'inquirer', '-vv' ])

from facefusion import installer

if __name__ == '__main__':
	installer.cli()
