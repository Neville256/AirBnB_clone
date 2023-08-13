This is a group project to write a command interpreter to manage our AirBnB objects.The project is the first step towards building our first full webapplication: The AirBnB clone. This step is important because we will use what we build during this project with these future projects:
- HTML/CSS templating
- Database storage
- API
- Front-end integration
The command line interpreter inteprets texts or commands inputed by a user or read from a file. It works by using a loop called cmdloop to read inputand parse them into two parts. The first part is the command part which is then send to appropriate command handler for execution. The second part is one or more arguments accompanying the command.
To start a cli, type in ./ followed by th e name of your cli e.g. "console.py". Then type your command into the prompt and wait for execution. Examples of commands are "help" which returns a list of functions inside the command when inputted without an argument. When inputed wth an argument, it return documentation of that command.
