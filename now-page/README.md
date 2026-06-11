# Now Page Generator

This is a Python script that generators the 'now' page for [ianwilder.dev](https://ian.wilder.dev).

## What it does

It reads 'now.json' -- simple data file containing my current goals, reading, certifications, and study progress. Then it generates a static HTML page at 'static/now/index.html', which Hugo serves at 'ianwilder.dev/now'

## How to update

1. Open 'now-page/now.json'
2. edit the relevant fields
3. Run the generator script:

'''bash
python3 now-page/generate_now.py
'''

4. Commit and push the changes

## Files

- 'now.json' - the data source you eidt to update the page
- 'generate_now.py' - the script that reads the data and builds the HTML