# POTD
Grab an image and make as desktop background (windows 10/python)

setting up a schedule task with the windows task scheduler gui is fairly straight forward
use the following settings
general tab - Run only when the user is logged on
triggers - every 15 minutes from the start of the day, continue forever; another trigger to run at logon
actions - run pythonw (this supresses command window)
