help = """
Your project has been created!
_____________________________________________________________________________
                            ___________ _
  \/                    __/   .::::.-'-(/-/)
                     _/:  .::::.-' .-'\/\_`*******            __ (_))
        \/          /:  .::::./   -._-.  d\|                 (_))_(__))
                     /: ("'"'/    '.  (__/||             (_))__(_))--(__))
                      \::).-'  -._  \/ \\/\|
              __ _ .-'`)/  '-'. . '. |  (i_O
          .-'      \       -'      '\|
     _ _./      .-'|       '.  (    \\                           % % %
  .-'   :      '_  \         '-'\  /|/      @ @ @               % % % %
 /      )\_      '- )_________.-|_/^\      @ @ @@@             % %\/% %
 (   .-'   )-._-:  /        \(/\'-._ `.     @|@@@@@              ..|........
  (   )  _//_/|:  /          `\()   `\_\     |/_@@               )'-._.-._.-
   ( (   \()^_/)_/             )/      \\    /                  /   /
    )  _.-\\.\(_)__._.-'-.-'-.//_.-'-.-.)\-'/._                /       
.-.-.-'   _o\ \\\     '::'   (o_ '-.-' |__\'-.-;~ ~ ~ ~ ~ ~ ~~/   /\   
          \ /  \\\__          )_\    .:::::::.-'\            '- - -|
     :::''':::::^)__\:::::::::::::::::'''''''-.  \                  '- - - - 
    :::::::  '''''''''''   ''''''''''''':::. -'\  \       C. SWANSIGER
_____':::::_____________________________________\__\_________________________

If you have not done so already, create a conda environment for your new 
project with:

>> cd {{cookiecutter.repo_name}}
>> conda create --name {{cookiecutter.repo_name}} python=3.9
>> conda activate {{cookiecutter.repo_name}}
>> conda env export > environment.yml

Install your new project in your local conda environment with:

>> pip install -e .

Don't forget to sync to GitHub by doing the following:

>> git init
>> git add --all
>> git commit -m "First commit"
>> git branch -M main
>> git remote add origin https://[remote repository URL]
>> git push -u origin main

Have fun!
"""
print(help)
