# world_time

This simple software calculates the times for most major timezones of the world. Whatever time you want to convert, this software will output the time you'd like to know.
For example, if you'd like to know what time 5:00pm PST is in Germany, you type it in, and out comes the Germany time.

I made this softare because, surprisingly, I couldn't find a single website that would let me know this. Due to our global nature nowadays, it's amazing how frequent somebody might need something that can instantly output the other country's time. For instance, when somebody in Korea asked if it would be ok to call me at 8:30am KST, I had to spend a few seconds to mentally calculate my time, which was kind of annoying. So, I tried searching on Google for something that would let me know what 8:30am KST means in US time, and I couldn't find a single website that would do this! All of the existing websites would tell me the different times of the my curren time, not my desired time.

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
