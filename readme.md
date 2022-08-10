Remember
========

A simple utility that stores strings and fetches them
sorted by the frequency and recency of their use.

Insipired by [zoxide](https://github.com/ajeetdsouza/zoxide).

Usage
-----

`remember use <collection> <value>`

`remember recall <collection>`

Algorithm
---------

Each value starts with a score of 1. Each use of the value
will increase its score by 1. During recall, the frecency
is calculated based on the last time the value was used:

| last use time    | frecency  |
|------------------|-----------|
| within last hour | score * 4 |
| within last day  | score * 2 |
| within last week | score / 2 |
| otherwise        | score / 4 |

Tasks
-----

  - Respect the XDG Base Directory specification.

  - Add support for Windows and other platforms.

  - Handle file system exceptions (e.g. permission denied).

  - In case of errors write to stderr and exit with error code.

  - Make `history_size` configurable.

  - Write shell autocompletion functions for collections.
