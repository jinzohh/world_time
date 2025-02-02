# world_time

This simple software calculates the times for most major timezones of the world. Whatever time you want to convert, this software will output the time you'd like to know.
For example, if you'd like to know what time 5:00pm PST is in Germany, you type it in, and out comes the Germany time.

I made this softare because, surprisingly, I couldn't find a single website that would let me know this. Due to our global nature nowadays, it's amazing how frequent somebody might need something that can instantly output the other country's time. For instance, when somebody in Korea asked if it would be ok to call me at 8:30am KST, I had to spend a few seconds to mentally calculate my time, which was kind of annoying. So, I tried searching on Google for something that would let me know what 8:30am KST means in US time, and I couldn't find a single website that would let me do this! All of the existing websites would tell me the different times of the my current time, not my desired time.

Thanks to modular arithmetic, building this software wasn't so complicated.
FYI, modular arithmetic is basically a "wrap around" arithmetic. I don't think most people learn about this unless one is a software engineer, but basically it is a mathematical principle that deals with sequence of things that comes back to the beginning. For example, a clock. Once the time hits the 60-minute mark, it starts counting from 1, again. Once the time hits the 12-hour mark, it starts counting from 1, again. Another example is our alphabet. After Z, we typically come back to A and begin counting from A, again. Like, ..., X, Y, Z, A, B, C, ... So anytime you are dealing with something that wraps around, you can leave the calculation to modular math.

Basically, modular math deals with the remainders rather than the quotient. For example, 1 % 24 (read as 1 mod 24) is dividng 1 by 24 where the remainder equals to 1. So, in other words, 1 % 24 = 1.
We begin to notice the "wrap around" or "starting back at the beginning" when we do 24 % 24, which equals 0 (24 divided by 24 has a remainder of 0). And then 25 % 24 = 1, 26 % 24 = 2, 27 % 24 = 3, and so on. Now, with our clock, which is usually 12-hour format or 24-hour format, we mod 12 or mod 24 based on the format we'd like to use to easily calculate the time. For example, if it is 8:00pm EST and we know that France is 6 hours ahead, then we do (8 + 6) % 12 to get the time in 12-hour format. The answer comes out to be 2:00am in France.

So, here it is. That is what this software does: making the world a better place through accessing world times at the tip of one's fingertips.

### How to conveniently run this program in Terminal.

Clone the repository.
```
git clone https://github.com/jinzohh/world_time.git
```

Open ~/.bashrc (linux) or ~/.bash_profile (macos)
```
nano ~/.bashrc
```

Add at the end of file:
```
world_time () { python3 path/to/world_time.py }
```

Apply the changes.
```
source ~/.bashrc
```

Execute the program.
```
world_time
```

If you do not want to do all of the above, you can always just call from the Terminal:
```
python3 path/to/world_time.py
```
