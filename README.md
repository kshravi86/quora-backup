quora-backup
============

A syncing approach to backing up Quora answers, questions, votes, and follows. Rather than fetching your entire history of Quora activity all at once, quora-backup checks your recent Quora activity and saves only the new entries. Run it regularly to maintain a full backup. This not only allows backups to be performed faster and more frequently, but also makes less requests to Quora's servers and doesn't face request rate-limiting issues like some older backup techniques do.

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
    * [Backup Formats](#backup-formats)

## Installation

    $ git clone https://github.com/csu/quora-backup.git
    $ cd quora-backup
    $ pip install -r requirements.txt

## Usage

    $ python backup.py Christopher-J-Su  # defaults to flat-file json backups

To access the help for the options and arguments:

    $ python backup.py --help
    Usage: backup.py [OPTIONS] USER

    Options:
      -p, --path TEXT          specify a path to store the backup files at
      -f, --format [json|csv]
      --help                   Show this message and exit.

### Backup Formats
To specify a format for your backup:

    $ python backup.py --format csv Christopher-J-Su

For a list of available backup formats, read the help (see [Usage](#usage) section).

#### JSON Backup Details
Your content will be stored in the following files, in whatever directory you run the above command in:

    answers.json
    questions.json
    upvotes.json
    question_follows.json