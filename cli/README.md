# Torizon Development Tool - Command line interface

Command line client to control applications, platforms and devices in the Torizon ecosystem.  
The command line interface allows users to perform most of the operations that can be completed using the REST api.  
The interface requires at least a command, some commands have up to two levels of sub-commands.  
- devices
- **device**
    - info
    - delete
    - images 
    - containers    
    - **image**
        - info
        - delete
    - **container**
        - info
        - start        
        - stop        
        - ps
        - mem
        - storage
    - ps
    - mem
    - storage
    - key
- platforms
- **platform**
    - info
    - compatible
- **application**
    - info
    - build
    - deploy
    - run
    - container
    - updatesdk
    - runsdk   
    - key 
- detect 
- create
- load
- pull

Commands that work on a device will require a device ID (serial-number), sub-commands that work on images and containers require SHA-ids of images and containers.
Commands working on platforms require platform-id (name).
Commands working on applications require the application-id (generated on creation).

The tool provide extensive command line help, so using --help on the subcommands will show more detailed information about each of them.
