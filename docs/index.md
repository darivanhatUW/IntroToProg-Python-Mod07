![Blog Header with Pickle Rick from the cartoon Rick and Morty.](https://github.com/darivanhatUW/IntroToProg-Python-Mod07/blob/main/docs/Im%20a%20pickle-80.jpg)

Today, I’ll be introducing you to a Python module called pickle and handling error exceptions, both are means we can use to communicate between ourselves and computers. In every learning journey I have taken, I’ve always learned best through a project-based pedagogy which is how I’ll be presenting the pickle module and error exceptions. 

Let’s get started with our project!

**Background:** Rick and Morty, an adult animated television show, created by Justin Roiland and Dan Harmond need a revised script of the Season 3, Episode 3 show previously written by Jessica Gao called “Pickle Rick.”

**The Project:** Jessica Gao has sent us the script but it’s been pickled and takes in two prompts for the name of the character and the character’s line. It’s our job to program unpickle the binary file containing the start to her revised script and add a few lines. 

**Tasks:** We’ll need a few actions that will allow us to add lines to the script, view the script, and then save the file when we’re done.


## Pickle and Unpickle
Jessica Gao has sent us a file, called script.dat, and we need to unpickle it. Let’s explore what we need to know before we start the pickling and unpickling process. 

The pickle module allows users to save and transmit Python binary files, or binary-like objects, by processes called serializing and de-serializing. Some examples of binary file extensions are .pickle, .pkl, .db, and, what we’ll be using for our project, .dat.

### Unpickling Jessica Gao's File
For those beginning their journey into programming a few of those words may be unfamiliar. We'll break down what it means to pickle, or serialize, and unpickling, or de-serialize, a Python object structure. NERDfirst of the [0612 TV w/ NERDfirst](https://www.youtube.com/watch?v=uS37TujnLRw&ab_channel=0612TVw%2FNERDfirst![image]:https://user-images.githubusercontent.com/78838344/109901569-2978ad80-7c4e-11eb-8473-c98838bc0f7a.png)
) channel on YouTube.com, breaks down the process in simple everyday language and provides visuals that explain how each object is converted from a human readable structure into a byte stream, which is a from the computer can understand. The reverse then occurs in the de-serialization process, where the byte stream, or computer language, is converted into a human readable structure. Which is a long-winded way of saying when we need to talk to the computer we have to convert what we have into something the computer can understand, and when we need something from the computer we convert it to something we can understand. Below, Figure 1, is a screenshot of the binary language from the .dat file that we'll pickle and unpickle. 

Figure 1, below, we see that some of the data is human-readable but the rest is the structure is not human-readable.
[Screenshot of a pickled file]:(https://github.com/darivanhatUW/IntroToProg-Python-Mod07/blob/main/docs/Screen%20Shot%202021-03-03%20at%201.09.10%20AM.png)

```
file_obj = open(script.dat, “rb”)
pickle.load(file_obj)
file_obj.close()
```
Breakdown:
```
file_obj = open(script.dat, “rb”)
```
**What's happening:** We're *open*ing the **script.dat** file to **"rb"** (read from a binary file) and then store that into the **file_obj** variable in order to use that function elsewhere. In this case, we're applying it to the pickle.load function.
```
pickle.load(file_obj)
```
**What's happening:** We're calling the pickle module to **load** the file we want to read.
```
file_obj.close()
```
**What's happening:** Once we've opened the file we need to **close** it. According to Randal Root's lecture February 23, 2021 for the University of Washington's Intro to Programming - Python class, forgetting to close files will bog down your computer and slow it down.

Once we've loaded the file we are then able to **print** a human-readable file. We can do that with the following **print** function, see code below:
```
file_obj = open(script.dat, “rb”)
print(pickle.load(file_obj))
file_obj.close()
```
```
[['Rick', 'Boom! I'm a pickle.'],['Morty','And?']]
```
Looks a lot better than the crazy byte data we saw before we saw earlier, right?

### References
NERDfirst. 0612 TV w/ NERDfirst. YouTube.com. 20 May 2014. YouTube.com.https://www.youtube.com/watch?v=uS37TujnLRw&ab_channel=0612TVw%2FNERDfirst. 27 February 2021

Kinsley, Harrison. Sendex. YouTube.com. 22 May 2015. https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex. 27 February 2021

Root, Randall. Zoom. 23 February 2021. https://www.youtube.com/watch?v=jiXmXhwgHp8&feature=youtu.be&ab_channel=IntelliJIDEAbyJetBrains. 23-28 Feb 2021.

Dawson, Michael. Python Programming for the Absolute Beginner, Third Edition. Boston, MA, Course Technology, a part of Cengage Learning, 2010.

Sharma, Aditya. “Exception and Error Handling in Python”. Datacamp.com. 22 November 2019. https://www.datacamp.com/community/tutorials/exception-handling-python. 28 February 2021

https://stackoverflow.com/questions/12761991/how-to-use-append-with-pickle-in-python. 28 February 2021

“pickle – Python object serialization”. GeeksforGeeks.com. 22 November 2020. https://www.geeksforgeeks.org/pickle-python-object-serialization/ 1 March 2021


Pickle – Python object serialization. 2001 – 2021. Python Software Foundation. 02 March 2021. https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy. 27 February 2021

“Pickle Rick.” Rick and Morty, created by Justin Roiland and Dan Harmon, written by Jessica Gao, Season 3, Episode 3, Adult Swim, Cartoon Network, 6 August 2017.


Our code to open Jessica Gao’s binary file should include pickle.load(file_name). What that means is that we want the computer to look in the pickle module and tell it that we want to load the byte stream from the file Jessica Gao sent us called script.dat. She’s an amazing writer, not the best at naming binary files.

In order to load the file, we’ll need to direct the computer to open the file and load it to a more human-readable format.  See code below:
