# Command Line: Data Manipulation

## wget

Download several files simultaneously. This command will download Q1-Q4 for each year out of 2014-2016

```
cd ~/Development/house-expenditure/
wget https://projects.propublica.org/congress/assets/staffers/201{4,5,6}Q{1,2,3,4}-house-disburse-detail.csv
```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the wget command above to download expenditures from each quarter of 2017.

## CSVKit, Sed, Awk

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

#### Why would you ever do this?

* Reproducibility
* Portability
* Transparency
* To be obnoxious
* Simplicity and ease of use. Once you're comfortable with this, its easier sometimes to use the command line for simple cleaning operations before piping to file and starting the real analysis.
