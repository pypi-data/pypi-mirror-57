v0.0.3a4
    (HOTFIX)
    
    - previous hotpatches failed, attempted manual adjustment of the archive... again *sobs*

v0.0.3a3
    
    (HOTFIX)
    
    - previous hotpatches failed, attempted manual adjustment of the archive.

v0.0.3a2
    
    (HOTFIX)
    
    - made quick fix to junkyard/__init__.py and setup.py that was preventing install
    - attempting to resolve missing garbage basket

v0.0.3a1
    
    (HOTFIX)
        
    - dropped versioning rework
    - made quick fix to junkyard/__init__.py and setup.py that was preventing install

v0.0.03a0
    
    MAJOR UPDATE:
    
    - versioning rework, stepping down from X.X.Xa0 to X.X.XXa0
    - moved development environment over to PyCharm/Anaconda with Python 3.7
    - reworked setup.py, and junkyard/__init__.py
    - overhauled README.md
    - added a changelog.md file (this file)
    
    - PLAYGROUND * NEW (WIP / NOT PUSHED)
        - added a new folder to host a set of pygame handlers
            - AudioHandler.MX() added as a pygame audio mixer * NEW
            - CharacterHandler * PLANNED
            - PlayerController * PLANNED
            - SceneHandler * PLANNED
            - WindowManager (WM) * PLANNED
    
    - CYBERDYNE
        - removed cyberdyne.py and moved its guts into the new cyberdyne folder
            - split SkynetCore class into Skynet.py as the Core class
            - added a yolo_v3 image recognition model NEW * WIP
                - based on work by @zzh8829 ( thank you )
                    - ( https://github.com/zzh8829/yolov3-tf2 ) 
    
    
    - GARBAGEBASKET
        - renamed garbagebasket.py to garbagebasket_legacy.py
        - 'declassed' all functions and moved them into seperate coorepsonding python files
          under the new "garbagebasket" directory
            - CryptoHandler.py * NEW * WIP (NOT PUSHED)
                - encrypt * TODO
                - decrypt * TODO
            - DiagnosticsHandler.py * NEW * BROKENGARBAGE (NOT PUSHED)
                - speed_test
                - speed_comparison_test
            - FileHandler.py * UPDATED
                - touched up current functions and added new functions 
                - reworked write function to use temp files in order to prevent file corruption
                  during file writes
                - overhauled print statements and function help tags
                - added additional error handling
                - added new functions
                    - file_verification
                    - generate_temp_filename
                    - uniform_filename
                    - copy_file
                    - copy_dir * TODO
                    - mass_copy
                    - find_files
                    - download_file
            - MathHandler.py * NEW
                - is_float
                - safe_sum
                - safe_average
                - is_prime * todo
                - get_horizon
                - emc2 (e=mc2)
            - PrintHandler.py * NEW
                - write_log
                - c_print
            - SystemHandler.py * NEW
                - collapse_list
                - handle_errors * WIP (ON HOLD)
    

v0.0.2a0 
    
    - initial release hotfix
    - corrected an issue with having the wrong LICENSE file present in the repository
        - switched from the incorrect GNU LICENSE file to the correct MIT LICENSE file
    - minor changes to setup.py, and .gitignore files
    - unspecified changes to the FileHandler() class in garbagebasket.py
    - added a touch of padding and fluff to cyberdyne.py, <- still a useless placeholder file


v0.0.1a0 
    
    - Initial commit
    - first itteration of the FileHandler class in garbagebasket.py
