# Media Assisted Photo-based Task manager

"""
Why?
    So that i can have a collection of memories for every goal/task i would acheive 

What?
    A todo app that complete tasks when atleast one photo is given and it will all be availaible to other users! also, later it will be able to also schedule these tasks for me

How?

    Functionalities:
        
        User Management
            - Registration
                - Username
                - Email
                - Password

            - Login
                - Username
                - Password
        
        Tasks CRUD
            - Creating Tasks
                Gets:
                - Task
                - Task Details
                - Task Deadline (Does Nothing For Now [Just For Sorting])
                
                - UserId Automatically
                - Media That Will Be Later Inputted Using This Task's Id As Foreign Key
                
            - Displaying Tasks With A Compilation
                - In A Card
                With:
                - Media / Slideshow Of Medias
                - Task 
                - Task Details
                - Task Deadline
            
            - Updating Task's Details / Completing Or Updating Pictures
                
                - Complete Button / Only Availaible When One Media Is Present
                - Upload Media Button
                
                Able To Update:

                - Display Of Medias With Update Or Replace Button Underneath

                - Task
                - Task Details
                - Task Deadline (Does Nothing For Now [Just For Sorting])
                
                - UserId Automatically

            - Deleting Tasks
                - Deleting Entry Only
            
"""