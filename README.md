quora-backup
============

A syncing approach to backing up Quora answers, questions, votes, and follows. Rather than fetching your entire history of Quora activity all at once, quora-backup regularly checks your Quora activity and saves only the new entries. This not only allows backups to be performed faster and more frequently, but also makes less requests to Quora's servers and doesn't face request rate-limiting issues like some older backup techniques do.

## Installation

    git clone https://github.com/csu/quora-backup.git
    cd quora-backup
    pip install -r requirements.txt

## Usage

    python json-backup.py Christopher-J-Su

Your content will be stored in the following files, in whatever directory you run the above command in:

    answers.json
    questions.json
    upvotes.json
    question_follows.json