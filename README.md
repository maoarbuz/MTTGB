# MTTGB (Mao Technology Telegram Bot)

![image](https://github.com/maoarbuz/MTTGB/assets/137228787/86bbde7e-98cc-4e8f-b628-8554b09291df)


This repository contains a simple Telegram chatbot that responds to user queries with predefined answers. The bot uses the `python-telegram-bot` library for interaction with the Telegram API and `pandas` for managing dialogues.

## Features

- Responds to user queries based on a predefined list of dialogues.
- Cleans input text to handle case insensitivity and punctuation.
- Randomly selects a response from possible answers for each query.
- Asynchronous handling of commands and messages for better performance.

## Getting Started

### Prerequisites

- Python 3.x
- Telegram Bot API token

### Libraries

Install the required Python libraries using pip:

```pip install python-telegram-bot pandas```

###Answers and queries

Edit file ```dialogues.txt``` for this!
Format: 

```query1:query2:query3;response1;response2```

You can add multiple answers and queries
