![Blog Header with Pickle Rick from the cartoon Rick and Morty.](https://github.com/darivanhatUW/IntroToProg-Python-Mod07/blob/main/docs/Im%20a%20pickle-80.jpg)

Today, I’ll be introducing you to a Python module called pickle and handling error exceptions, both are means we can use to communicate between ourselves and computers. In every learning journey I have taken, I’ve always learned best through a project-based pedagogy which is how I’ll be presenting the pickle module and error exceptions. 

Let’s get started with our project!

Background: Rick and Morty, an adult animated television show, created by Justin Roiland and Dan Harmond need a revised script of the Season 3, Episode 3 show previously written by Jessica Gao called “Pickle Rick.”

The Project: Jessica Gao has sent us the script but it’s been pickled and takes in two prompts for the name of the character and the character’s line. It’s our job to program unpickle the binary file containing the start to her revised script and add a few lines. 

Tasks: We’ll need a few actions that will allow us to add lines to the script, view the script, and then save the file when we’re done.


## Pickle and Unpickle
Jessica Gao has sent us a file, called script.dat, and we need to unpickle it. Let’s explore what we need to know before we start the pickling and unpickling process. 

The pickle module allows users to save and transmit Python binary files, or binary-like objects, by processes called serializing and de-serializing. Some examples of binary file extensions are .pickle, .pkl, .db, and, what we’ll be using for our project, .dat.
 
For those beginning their journey into programming a few of those words may be unfamiliar. We'll break down what it means to pickle, or serialize, a Python object structure. NERDfirst of the [0612 TV w/ NERDfirst](https://www.youtube.com/watch?v=uS37TujnLRw&ab_channel=0612TVw%2FNERDfirst![image](https://user-images.githubusercontent.com/78838344/109901569-2978ad80-7c4e-11eb-8473-c98838bc0f7a.png)
) channel on YouTube.com, breaks down the process in simple everyday language and provides visuals that explain how each object is converted from a human readable structure into a byte stream, which is a from the computer can understand. The reverse then occurs in the de-serialization process, where the byte stream, or computer language, is converted into a human readable structure. Which is a long-winded way of saying when we need to talk to the computer we have to convert what we have into something the computer can understand, and when we need something from the computer we convert it to something we can understand. Below, Figure 1, is a screenshot of the binary language from the .dat file we’ll use to pickle and unpickle our script. As you can see some of it is recognizable but the rest is the structure is unreadable to humans.



Our code to open Jessica Gao’s binary file should include pickle.load(file_name). What that means is that we want the computer to look in the pickle module and tell it that we want to load the byte stream from the file Jessica Gao sent us called script.dat. She’s an amazing writer, not the best at naming binary files.

In order to load the file, we’ll need to direct the computer to open the file and load it to a more human-readable format.  See code below:
```
file_obj = open(script.dat, “rb”)
pickle.load(file_obj)
file.obj.close()
```

