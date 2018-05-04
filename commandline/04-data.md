# Command Line: Data Manipulation

Below, we're going to show a bunch of command line tools to manipulate "data". But it's important to first know a couple different common formats that you'll find data.

## Formats

### CSV (Comma Separated Values)

A simple format that can be viewed in excel. Really easy to see in text editor, contains only one table.

### TSV (Tab Separated Values)

Same as CSV, but separates values with tabs rather than commas, can also be opened in excel.

### JSON (JavaScript Object Notation)

Another great Mozilla [tutorial](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

![](https://www.evernote.com/shard/s150/sh/90cf283d-4adc-4f6f-aeaf-c8f2660d13c7/793cabb9f194996b/res/62dd9784-077a-45ee-8b47-c23054e2cc59/skitch.png?resizeSmall&width=832)
source: http://stackoverflow.com/questions/4310315/what-exactly-is-json

Example JSON:
https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json

---------------------------------------------------------------------------------

## Commands

⚠️ The Instructor will demo this part - Don't try it yourself...yet...

### `grep`

`grep` can be used to filter any text document. It is most useful for data formats where each line of text is a single record (like a csv).

```bash
curl -s 'https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv' | grep 'water'
```

### wget

We've already gone over `curl`. `wget` is similar but it makes it easier to download files to disk.

This example download several files simultaneously. This command will download Q1-Q4 for each year out of 2014-2016:

```
cd ~/Development/house-expenditure/
wget https://projects.propublica.org/congress/assets/staffers/201{4,5,6}Q{1,2,3,4}-house-disburse-detail.csv
```

You can see that we are using the curly braces `{}` for string expansion. 201{4,5,6} means 2014, 2015, 2016. Similarly Q{1,2,3,4} is Q1, Q2, Q3, Q4.

4 * 3 = 12 so 12 files will be downloaded.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the wget command above to download expenditures from each quarter of 2017.

For the future, there is CSVKit: [https://csvkit.readthedocs.io/en/1.0.1/](https://csvkit.readthedocs.io/en/1.0.1/). This program is its both a command line interface (CLI) and a python package. It helps parse CSVs cleanly.

```
pip3 install csvkit
```

### csvkit: csvcut

csvcut is used to grab a specific column. `csvcut -n` can be used to get the headers of a csv as shown below:

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | csvcut -n
```

list all the unique OFFICEs

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | tail -n +2 | csvcut -c 2 | sort | uniq
```

### csvkit: csvgrep

We've used grep previously- what if we wanted to just grep through a specific column in a CSV?

This command looks for each row that has the "HON. JOHN CONYERS, JR." as the OFFICE.

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2015Q4-house-disburse-detail.csv" | csvgrep -c "OFFICE" -m "HON. JOHN CONYERS, JR."
```

### csvkit: csvcut

csvcut allows one to get a specific column(s) from a csv

This command gets the AMOUNT column from all of Conyers expenditures.

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2015Q4-house-disburse-detail.csv" | csvgrep -c "OFFICE" -m "HON. JOHN CONYERS, JR." | csvcut -c "AMOUNT"
```

### csvkit: csvstat

We can use csvstat to perform differnt statistical operations on columns.

This example just sums up all the amounts to show the total expenditure from the Conyers office in 2015 Q4.

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2015Q4-house-disburse-detail.csv" | csvgrep -c "OFFICE" -m "HON. JOHN CONYERS, JR." | csvcut -c "AMOUNT" | csvstat --sum
```

When you're first starting with a dataset, it can be useful to just pass it through `csvstat` without any options. `csvstat` will do its best to give you something useful for each column (mean, median, mode, etc.)

```
curl -s "https://projects.propublica.org/congress/assets/staffers/2015Q4-house-disburse-detail.csv" | csvgrep -c "OFFICE" -m "HON. JOHN CONYERS, JR." | csvstat -c "CATEGORY,PAYEE,AMOUNT,RECIP (orig.)"
```

### csvkit: in2csv

`in2csv` allows converting various formats like xlsx into csv

```
in2csv roster.xlsx | csvstat
```

### csvkit: csvlook

`csvlook` is part of `csvkit` that we installed earlier. It allows to "pretty print" a csv file in the command line.

Here is an example from an old FiveThirtyEight [article on Alcohol Consumption](https://fivethirtyeight.com/features/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/).

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvlook
```

For very long or very wide CSV files, you can pipe the output of `csvlook` into `less`.

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvlook | less
```

### sed and awk

`sed` and `awk` are really old string manipulation tools. they are very powerful but can be hard to work with. this example below shows the power of sed and awk to parse really anything.

```
in2csv roster.xlsx | csvcut -c 9 | tail -n +2 | awk '{gsub("\"", "")}1' | cut -d'|' -f 1 | sed 's/^[ \t]*//;s/[ \t]*$//' | sort | uniq -c
```

### egrep

```
curl "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | egrep -i "water|bioguide" | csvstat
```

```
cd ~/Development/house-expenditure
cat 2017Q1-house-disburse-detail.csv | grep "BIOGUIDE\|WATER" | csvstat
cat 2017Q1-house-disburse-detail.csv | grep "BIOGUIDE\|,HON" | grep "40333.33"
```

### `jq`

`jq` is a Command-line JSON processor. Here are a few examples using the [superheroes.json](https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json) dataset.

If you don't have jq installed, run `brew install jq` on macOS and `sudo apt-get install jq` on Ubuntu.

#### Pretty Print JSON

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq
```

#### Extract just 'members' from JSON

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq '.members'
```

#### Get Member Names

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[].name'
```

#### Get List of Powers

```
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[].powers[]'
```

#### Create CSV of Members

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[] | [.name, .secretIdentity, .age] | @csv'
```

## Why would you ever do this?

* Reproducibility
* Portability
* Transparency
* To be obnoxious
* Simplicity and ease of use. Once you're comfortable with this, its easier sometimes to use the command line for simple cleaning operations before piping to file and starting the real analysis.
