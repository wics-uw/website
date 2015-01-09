# The code that runs the WiCS site #

The site is generates static content from Markdown articles, using software
called [Pelican](http://docs.getpelican.com/en/3.5.0/).

## Installation ##

The easiest way to install Pelican is to create a `virtualenv`. To do so,
first ensure that `virtualenv` is installed:

```
sudo apt-get install python-virtualenv
```

Now you can create a `virtualenv`:

```
mkdir -p ~/virtualenvs/pelican
cd ~/virtualenvs/pelican
source bin/activate
```

Your shell prompt will change slightly, like this:

```
user@honk ~/virtualenvs/pelican $ source bin/activate
(pelican)user@honk ~/virtualenvs/pelican $
```

Now you can install Pelican by typing

```
pip install pelican markdown
```

If you ever need to re-enable the `virtualenv`, simply run

```
source ~/virtualenvs/pelican
```

## Development ##

You can either add content to the site or modify its theme.

### Adding site content ###

All site content is contained in the `content/` directory. Posts are sorted by
term directories, e.g. "F2014". There is also a `pages/` directory that
contains non-post type pages, such as contact info, about us, etc.

#### Posts ####

We currently use three posting categories: **Blog**, **Events**, and **Media**.

+ Use the **Media** category for video recordings of talks and events.
+ Use the **Events** category to advertise event details.
+ Use the **Blog** category for everything else: news, essays, etc.

You can also tag posts! Try to use tags that have already been used on the
other posts, but feel free to add new tags as necessary.

Please try to use a consistent naming scheme. Articles are named by term,
category, and slug; for instance, posting a video of a talk about automata in 
S13 might be named `S13-media-automata.md`.

#### Pages ####

We only need a limited number of pages. You probably won't need to add many 
more. These include things like our Code of Conduct, contact info, etc.

It might be useful to add a page that doesn't show up in the site navigation. 
To do so, make sure you set `Status: hidden` in the Markdown preamble. This 
will cause the page to be generated without showing up in the site's main 
navigation.

### Markup beautification ###

The theme we are currently using is called `notmyidea`. Pelican uses the 
[jinja2](http://jinja.pocoo.org/docs/dev/) templating system; if you've used 
Django, you'll find the templates very similar. 

To modify the theme css or html, simply take a look at the theme data under
`theme/notmyidea/` and modify it at will.

## Deployment ##

We are currently using the [Computer Science 
Club](https://csclub.uwaterloo.ca)'s ["club 
hosting"](http://wiki.csclub.uwaterloo.ca/Club_Hosting) as our webhost. You 
must have a CSC login in the `wics` group to complete the next steps.

To deploy the site, first log into the CSC's webserver:

```
ssh userid@csclub.uwaterloo.ca
```

Then use `become_club` to switch to the WiCS user account:

```
become_club wics
```

Pull the latest version of the site from GitHub:

```
cd ~/pelican
git pull
```

Then build and deploy the site:

```
make rsync_upload
```

Which conveniently deploys the site into the `wics` user's `www/` directory.
