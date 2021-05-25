#!python

import gpiod
import sys
import time
import platform
import os
import distro

if __name__ == "__main__":
    print("Hello world!")
    
    print("""linux_distribution: %s
    system: %s
    machine: %s
    platform: %s
    uname: %s
    version: %s
    """ % (
    distro.linux_distribution(),
    platform.system(),
    platform.machine(),
    platform.platform(),
    platform.uname(),
    platform.version(),
    ))


    print("TORIZON :: %s" % (os.environ.get("TORIZON")))

    chip = gpiod.chip(1)    

    print(F"Inspecting GPIO chip {chip.name}")

    for line in gpiod.line_iter(chip):        
        print(F"{line.offset}\t{line.name}\t{line.consumer}\t{line.direction}")

    