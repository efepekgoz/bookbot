# BookBot

BookBot is a simple command line utility written in Python that takes a plain‑text novel and prints a compact analytics report, including:

* Total word count
* Frequency of each alphabetic character, sorted from most to least common

The project is a hands‑on exercise from the **Build a BookBot in Python** course on Boot.dev, adapted here as a public GitHub repository.

---

## Features

| Feature | Description |
|---------|-------------|
| Word counter | Splits the input text on whitespace and returns the number of words. |
| Character histogram | Counts how many times every letter `a‑z` appears, case‑insensitive. |
| Sorted report | Displays the character counts in descending order so the most frequent letters are shown first. |
| Easy to extend | The source is under 100 lines, well commented, and divided into small functions that are straightforward to modify or reuse. |

---

## Requirements

* Python 3.9 or later (tested with 3.12)
* No third‑party packages

---

## Installation

```bash
git clone https://github.com/efepekgoz/bookbot.git
cd bookbot
```

---

## Usage

The default script analyses Mary Shelley’s *Frankenstein* which lives in the `books/` folder.  
To run that demo:

```bash
python main.py
```

To analyse a different text file, pass a relative or absolute path:

```bash
python main.py path/to/your/novel.txt
```

The output will look similar to:

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
--- End report ---
```

---

## Project structure

```
bookbot/
├── books/                  # Sample texts for experimentation
│   └── frankenstein.txt
├── main.py                 # Entry point, orchestrates the workflow
├── stats.py                # Helper utilities used by main.py
├── README.md               # You are here
└── .gitignore
```

---

## Extending BookBot

* **Analyse multiple files:** wrap the logic in a loop or accept a directory path.
* **Visualise data:** export the histogram to JSON or CSV then plot with matplotlib.
* **Ignore stop words:** add a filter list to refine the word count.

Pull requests are welcome. For major changes, please open an issue first so we can discuss what you would like to change.

---

## Acknowledgements

* Built while following the [Boot.dev](https://www.boot.dev) Python track.
* Original repository by [efepekgoz](https://github.com/efepekgoz).

---

## License

The repository currently does not include an explicit license file.  
If you plan to use this code in your own project, please contact the author or open an issue to clarify licensing.
