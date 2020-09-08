# Using-Python-to-Interact-with-the-Operating-System-Final-project-
Final project for course "Using Python to Interact with the Operating System "  as the part of Google IT Automation with Python Specialisation through Coursera

# Introduction
Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it.

# Technology used
* Regex to parse a log file
* Append and modify values in a dictionary
* Write to a file in CSV format

# Input data (System Log)

`
Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)

Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)

Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)

Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)

Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)

Jan 31 01:29:16 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)

Jan 31 01:33:12 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)

Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)

Jan 31 01:49:29 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)

Jan 31 02:30:04 ubuntu.local ticky: ERROR Timeout while retrieving information (oren)

Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)

Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)

Jan 31 03:08:55 ubuntu.local ticky: ERROR Ticket doesn't exist (blossom)
`
