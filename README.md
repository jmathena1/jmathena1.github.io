# Welcome to my site!

I built this personal site, blog, and digital garden using vanilla HTML, CSS, and JS with some help from Python, uv, and PageFind.

## Prequisites
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [pandoc](https://pandoc.org/installing.html)
    - I needed to install the Pandoc cli to allow my project to use pandoc inside uv. Not sure why! Let me know if you're able to do without this

## Running Locally
The steps to running this site locally are:
1. Install the prereqs above
2. Clone this repo
3. Navigate to the root of the cloned repo and run `uv sync` on the command line
    - I recommend creating and activating a virtual environment as well. You
      can do this using `uv venv <your-name-here>` and then activating it with
      `source .venv/bin/activate` (macOS and linux)
4. Run `make build` to apply the templates to my markdown files and setup my searchable wiki
5. Run `make serve` to serve the website locally through localhost. Click on the URL generated to open the site homepage on your default browser.


Happy blogging!
