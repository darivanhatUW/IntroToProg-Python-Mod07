<img src="https://github.com/darivanhatUW/IntroToProg-Python-Mod07/blob/main/docs/Im%20a%20pickle-80.jpg" >

Today, I’ll be introducing you to a Python module called pickle and handling error exceptions, both are means we can use to communicate between ourselves and computers. In every learning journey I have taken, I’ve always learned best through a project-based pedagogy which is how I’ll be presenting the pickle module and error exceptions. 

Let’s get started with our project!

**Background:** Rick and Morty, an adult animated television show, created by Justin Roiland and Dan Harmond need a revised script of the Season 3, Episode 3 show previously written by Jessica Gao called “Pickle Rick.”

**The Project:** Jessica Gao has sent us her starter script but it’s been pickled. It’s our job to unpickle the file add a few lines and send it back to her. 


## Pickle and Unpickle
Jessica Gao has sent us a file, called script.dat, and we need to unpickle it. Let’s explore what we need to know before we start the pickling and unpickling process. 

The pickle module allows users to save and transmit Python binary files, or binary-like objects, by processes called serializing and de-serializing. Some examples of binary file extensions are .pickle, .pkl, .db, and, what we’ll be using for our project, .dat.

### Unpickling Jessica Gao's File
For those beginning their journey into programming a few of those words may be unfamiliar. We'll break down what it means to pickle, or serialize, and unpickling, or de-serialize, a Python object structure. NERDfirst of the [0612 TV w/ NERDfirst](https://www.youtube.com/watch?v=uS37TujnLRw&ab_channel=0612TVw%2FNERDfirst![image]:https://user-images.githubusercontent.com/78838344/109901569-2978ad80-7c4e-11eb-8473-c98838bc0f7a.png) channel on YouTube.com, breaks down the process in simple everyday language and provides visuals that explain how each object is converted from a human readable structure into a byte stream, which is a from the computer can understand. The reverse then occurs in the de-serialization process, where the byte stream, or computer language, is converted into a human readable structure. Which is a long-winded way of saying when we need to talk to the computer we have to convert what we have into something the computer can understand, and when we need something from the computer we convert it to something we can understand. Below, Figure 1, is a screenshot of the binary language from the .dat file that we'll pickle and unpickle. 

![Screenshot of a pickled file](https://github.com/darivanhatUW/IntroToProg-Python-Mod07/blob/main/docs/Screen%20Shot%202021-03-03%20at%201.09.10%20AM.png)

_Figure1: Screenshot of a pickled data._

### Unpickling Code
We first need to import the pickle module by including at the beginning of our code. (See below)
```
import pickle
```
...then we can use it in our code.
```
file_obj = open(script.dat, “rb”)
pickle.load(file_obj)
file_obj.close()
```
Breakdown:
```
file_obj = open(script.dat, “rb”)
```
**What's happening:** We're *open*ing the **script.dat** file in order to read from a binary file by selecting the binary file access mode **"rb"**, then, store that into the **file_obj** variable where we'll use that function elsewhere. In this case, we're applying it to the pickle.load function.
```
pickle.load(file_obj)
```
**What's happening:** We're calling the pickle module to use the **pickle.load()** function to read file.
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
Looks a lot better than the crazy byte stream we saw earlier, right?

## Writing to the Binary File
Now that we're able to read the existing script we have a couple of options: 1) Add lines to the the existing script or 2) Overwrite the existing script. Once we've 
finished with our portion of the script we'll need to pickle, or serialize, it before we save and send it off to Jessica Gao.

### Pickling Code
The pickle code for writing and appending to the file is similar to the unpickling code with few adjustments, we'll be changing the file access mode and the new **pickle.dump()** function. Let's say we want to keep the existing script and want to add more to it, we'll use the **"ab** file access mode, which appends to the existing binary file.

### Appending to the script:
```
file_obj = open(script.dat, “ab”)
pickle.dump(list_of_data, file_obj)
file_obj.close()
```
Breakdown:
```
file_obj = open(script.dat, “ab”)
```
**What's happening:** Just as in the unpickling code we'll be **opening** the binary file, but this time we'll be include the **"ab"** file access mode so the code knows what what want to do with the file, then save it all to a variable in use later.
```
pickle.dump(list_of_data, file_obj)
```
**What's happening:** We access the pickle module again and this time we're using the **pickle.dump()** function to let the computer know that we want to write to the file. If you look there are two arguments: the information we want to pickle and the file we want to write to.
```
file_obj.close()
```
**What's happening:** As before, since we opened access to the file we need to close it.

## Appending vs. Writing to a Binary File
The code for writing to a binary file is similar but the file access mode used would be **"wb"**, which writes to the binary file. What then is the difference between **"ab"** and **"wb"**? When you're writing to the file, the data that you save to the file overwrites any existing data within the file. That means that if you didn't like the lines Jessica Gao included in the file you could overwrite them by changing the file access mode to **"wb"**.

For more information on easy to follow and understand explanation of the pickle and unpickling process watch the video by user sentdex [Python Pickle for saving objects (serialization)](https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex).

This file can now be saved and sent to Jessica Gao as I'm sure will be the best revised episode of "Pickle Rick" the world has seen.

# Error Exceptions
As programmers just starting, it might even be true for experts, we encounter the occassional error that stops our program from running or even runs but in an unexpected way. 

How does this tie into our amazing revised "Pickle Rick" script? Well, fellow programmer, when we're writing our code and it works improperly or breaks we'll be spending more time trying to fix it rather than contributing our brilliance to the script. Besides, are you able to understand some of those crazy error messages when we break the code? Error exceptions allow us more control in handling the error and possibly display a more descriptive message.

For example, the following code asks a user to enter two numbers:
```
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))

print(int1 / int2)
```

If the user enters a zero for the second integer they'll be presented with an error message like the one below: 
```
Enter the first integer: 2
Enter the second integer: 0

Traceback (most recent call last):
   File "/Users/Darivanh/Documents/_PythonClass/Assignment07/test.py", line 4, in <module>
     print(int1 / int2)
 ZeroDivisionError: division by zero
```
What if we could provide the user with a more descriptive message that explains the error, maybe even add a message to take further action? This can be accomplished by using the _try_ statement with the _except_ clause.

For example:
```
try:
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    
    print(int1 / int2)
    
except ZeroDivisionError:
    print("It's not possible to divide a number by 0. Try another number.")
    
```
You'll error message would then read:
```
Enter the first integer: 1
Enter the second integer: 0
It's not possible to divide a number by 0. Try another number.
```
Isn't that a bit more pleasant and informative?

Did you notice that the _execpt_ clause I added had the **ZeroDivisionError** type? That tells the code that if the user decides to divde by 0 display this message. But, what if the user decides to enter a letter? Can we check for that and display a message for each error? The answer is yet. In Michael Dawson's "Python Programming for the Absolute Beginner, Third Edition," the author provides a table on page 207, below.

## Selected Exception Types                                                                                                                   
| Exception Type     | Description                                                                                                           |
| -------------------|-----------------------------------------------------------------------------------------------------------------------|
| IOError            | Raised when an I/O operation fails, such as when an attempt is made to open a nonexistent file in read mode.          |
| IndexError         | Raised when a sequence is indexed with a number of a nonexistent element.                                             |
| KeyError           | Raised when a dictionary key is not found.                                                                            |
| Name Error         | Raised when a name (of a variable or function, for example) is not found.                                             |
| SyntaxError        | Raised when a syntax error is encountered.                                                                            |
| TypeError          | Raised when a built-in operation or function is applied to an object of inappropriate type.                           |
| ValueError         | Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value. |
| ZeroDivisionError  | Raised when the second argument of a division or modulo operation is zero.                                            |


I hope that I was able to help you better understand the concepts of pickling, unpickling, and error exceptions through writing a script for the Rick and Morty show. Please feel visit the sites in the Reference section below for more indept information.

___
### References
"Serialization - A Crash Course." _YouTube.com_, uploaded by NERDfirst, 20 May 2014.https://www.youtube.com/watch?v=uS37TujnLRw&ab_channel=0612TVw%2FNERDfirst. 27 February 2021

Kinsley, Harrison. "Python Pickle Module for saving objects (serialization)." _YouTube.com_, uploaded by Sendex, 22 May 2015. https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex. 27 February 2021

Root, Randall. _Zoom_. 23 February 2021. https://www.youtube.com/watch?v=jiXmXhwgHp8&feature=youtu.be&ab_channel=IntelliJIDEAbyJetBrains. 23-28 Feb 2021.

Dawson, Michael. Python Programming for the Absolute Beginner, Third Edition. Boston, MA, Course Technology, a part of Cengage Learning, 2010.

Sharma, Aditya. “Exception and Error Handling in Python”. _Datacamp.com_. 22 November 2019. https://www.datacamp.com/community/tutorials/exception-handling-python. 28 February 2021

Rangoli Thakur. "How to use append with pickle in python?" _stackoverflow.com_, https://stackoverflow.com/questions/12761991/how-to-use-append-with-pickle-in-python. 28 February 2021

Pickle – Python object serialization. 2001 – 2021. Python Software Foundation. 02 March 2021. https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy. 27 February 2021

“Pickle Rick.” Rick and Morty, created by Justin Roiland and Dan Harmon, written by Jessica Gao, Season 3, Episode 3, _Adult Swim_, Cartoon Network, 6 August 2017.

