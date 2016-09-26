# parchment

parchment is a simple static site generator written in Python

Note: `parchment` now is only tested on Python3.x and Linux

## install

#### clone from repository

```
git clone https://github.com/gaotongfei/parchment.git
cd parchment/
virtualenv -p python3 venv
source venv/bin/activate
python setup.py install
```

## quick start

```
parchment/
    src/
    content/
    public/
    templates/
    venv/
    config.yaml
    ...
```

`parchment init`: create two empty folders: `content` and `public`

edit a markdown file named `YYYY-MM-DD-title.md`, for example `2015-10-19-parchment is a simple static site generator.md` under `content` folder

`parchment generate`: (you may need to use `sudo parchment generate` if you are using Mac OSX) you will see your markdown files have been generated to html files under the folder `public`

**Note: make sure run `parchment generate` command in `parchment` directory**

## FAQ

Q: How to solve `error: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1`?
A: run `sudo apt-get install python3-dev` on Debian/Ubuntu, if still get that error see <a href="http://stackoverflow.com/a/30279877/4144064">stackoverflow</a>.
