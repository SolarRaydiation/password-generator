# Password Generator
An open-source, simple Python-based CLI and GUI script that allows a quick and easy way to generate strong passwords without hassle.

## Project Rationale
Most password generators I found such as [LastPass](https://www.lastpass.com/features/password-generator), [Norton](https://my.norton.com/extspa/passwordmanager?path=pwd-gen), and [Dashlane](https://www.avast.com/en-ph/random-password-generator#pc) do not show its users how they generate their passwords. However, I generally don't trust these third-parties to generate strong passwords for me because **(a)** I can't see the code they used to generate passwords and **(b)** I don't trust these third parties anymore after LastPass suffered two [data](https://cybernews.com/news/lastpass-confirms-breach/) [breaches](https://cybernews.com/news/lastpass-second-breach/) and Norton's [password manager was compromised](https://cybernews.com/security/hackers-compromise-norton-password-manager/).

I also find it difficult to just trust the companies running these password managers. Am I supposed to just hand over my passwords to them and believe that they will keep my passwords safe and not accidentally leak them on the dark web or use it for malicious purposes? From my perspective, its like handing over the key of my house to a stranger and hoping they will keep my key safe.

As a computer science major I thought to myself 'How am I going to generate safe and secure passwords now?' to which I then realized 'I'm a Computer Science major! I can build one myself!'

## Project Features
The project revolves around the generation of secure and strong passwords based on five parameters - the length of the password, and whether or not uppercase, lowercase, special characters, and digits are included in password generation. A command line interface built using the `argparse` module is provided to easily interface with the script.

![A screenshot of what the commandline interface looks like.](/.img/cli-may092024.png)

Uppercase, lowercase, special characters, and digits are included in password generation by default as they make a password much safer. However, options are included to remove them while generating passswords. This is not recommended, however.

## Installation and Running the Project
Aside from installing Python on your computer, there is no need to install  packages using `pip` or with other package installers. This project uses only modules found in the Python Standard Library.

Installation can easily done as cloning this repo to your computer, then running `python pwedgenerator.py` on command line. Run `python pwedgenerator.py -h` for details on how to interface witht he script. Additionally, you can refer to the picture above for help.

## Quickstart
To generate a password, run this command on your command line:

`python pwedgenerator.py 12`

This will create a password twelve characters long, which can be a mix of uppercase, lowercase, special characters, and digits. You may change the length of the password with any you desire.

## Future Features
This project is planned to have GUI equivalent built using Python's built-in `Tkinter` module. The library `CustomTkinter` may be included to give the planned GUI a modern feel.

The project may also include a password strength estimator feature, though it may be built separately from this project.

## License
This project is licensed under the terms of the MIT license.