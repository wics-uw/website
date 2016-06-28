# The code that runs the WiCS site #

The site is generates static content from Markdown articles, using software
called [Pelican](http://docs.getpelican.com/en/3.5.0/).

These docs are aimed at a Debian-based Linux user.

## Installation ##

### `git` ###

`git` is the source control that we use to manage changes to the website. It
comes preinstalled on most Linux systems. If you don't already have it, just
run

```
sudo apt-get install git-core
```

For more information about what a typical `git` workflow for contributing to
the site might look like, check out [this OpenHatch
document](http://openhatch.readthedocs.org/en/latest/advanced/working_with_git.html)
and look into completing the [OpenHatch `git` training
mission](http://openhatch.org/missions/git).

### `pelican` ###

The easiest way to install Pelican is to create a `virtualenv`. To do so,
first ensure that `virtualenv` is installed:

```
sudo apt-get install python-virtualenv
```

Now you can create a `virtualenv`:

```
mkdir -p ~/virtualenvs/pelican
cd ~/virtualenvs/pelican
virtualenv .
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
source ~/virtualenvs/pelican/bin/activate
```

## Setup ##

Before you get started with development, we're going to walk through some setup
steps.

### Cloning your repository ###

Only complete this step once!

You'll need to fork a copy of this repo in order to contribute. To do so, click
the "Fork" button in the upper right hand corner.

One the project is forked, you'll be taken to your very own local copy of the
WiCS website, perhaps at `https://github.com/<your-username>/website`. This is
your personal remote repository on GitHub, or what we'll call `origin`.

Next, you'll need a folder to store the code in. On Linux, use the command line
to create a new directory and navigate there (`mkdir /path/to/code` and `cd
/path/to/code`). On Windows, you can make a folder in Windows Explorer, and
since you have git installed, right click and select "Open Git Bash Here" to
launch a terminal.

Now you can clone your code:

```
git clone https://github.com/<your-username>/website.git
```

which will create a folder called `website`. This is your git repository! In
both git bash or your Linux terminal, `cd website`.

Now we need to add a reference to our upstream remote repository:

```
git remote add upstream https://github.com/wics-uw/website.git
```

### Feature development ###

In git, when we are working on a feature, we usually split it off from the
master branch and refer to this branch as a "feature" or "topic branch."

If you're ready to work on a topic branch, follow these easy steps. First,
ensure your master branch is up to date:

```
git checkout master         # Check out your master branch
git fetch upstream          # Fetch any new upstream code
git rebase upstream/master  # Rebase your master branch to match upstream
git push origin master      # Update your remote `origin` repository
```

Now you can make a new topic branch off master:

```
git checkout -b topic-name  # Equivalent to git branch topic-name then checkout
```

### Commit structure ###

Here are some tips for structuring your commits. These are generally considered
best practices.

+ Use present-tense, imperative commit messages.
  + **DON'T** write "This fixes issue #234 by optimizing the algorithm"
  + **DO** write "Optimizes algorithm; fixes #234"
+ Write descriptive commit messages that give the reviewer the big picture
  + **DON'T** write "Updates in css files"; this is redundant and can be
    determined by viewing the files the patch modifies
  + **DO** feel free to write multi-line commit messages; keep in mind that
    while only the first line is visible in summary view, additional comments
    below go into the git log and can be very useful
+ Separate commits in the smallest logical, reversible steps possible.
  + **DON'T** submit multiple small commits fixing typos; rebase these into a
    single commit
  + **DO** include whitespace updates in a separate commit from code changes,
    template changes separate from adding content, etc.
+ Ask for help if you're not sure how to do some of these things!

Remember: code reviews will help catch these things and give you a better idea
of what's considered standard. Don't fear constructive feedback!

### Submitting pull requests ###

After you've made your modifications on your topic branch, perhaps following
the guide in the **Development** section, you can now ask for your code to be
merged by submitting a pull request.

To do so, first push your code to your personal remote, `origin`:

```
git push origin topic-name
```

Then log onto GitHub. You'll find a big green button asking if you want to
submit a pull request. Click it and follow the steps to submit your pull
request.

Once it's merged, you can click the "Delete branch" button on GitHub. In your
local repository, the branch can be deleted with the

```
git branch -d topic-name
```

command.

### Reviewing a pull request ###

There are three views for reviewing a pull request on GitHub: **Conversation**,
**Commits**, and **Files changed**.

#### Conversation ####

Comments on the pull request show up here, including any inline comments that
are added when viewing the file diffs. A summary of submitted commits is also
listed.

Use this section to submit general feedback about the pull request.

#### Commits ####

A more detailed list of commits included in the pull request, that will allow a
reviewer to view each individually.

#### Files changed ####

The `diff` view of the pull request. Lets the reviewer see the full patch in
its entirety, and add inline comments on changes.

Use this section to submit line-specific feedback.

#### Merging ####

A back-and-forth revision process will occur during the course of the review.
For the developer to update the pull request, they simply need to push new
changes to the topic branch being considered (sometimes using a force-push if
they need to rewrite commits).

When all parties are happy with the patch, the reviewer can then sign off and
merge the code by clicking the big green "Merge" button. This code is then
merged into the upstream master branch. For the changes to appear on the
website, someone needs to deploy the new code (see the **Deployment** section
for more details).

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

### Testing Locally ###

To test a local copy of the site, you'll need to start the development server.
There's no additional software you need to install to launch a local version of
the site! Simply run

```
./develop_server.sh start
```

in the top directory, which will launch the development server on port 8000.
Then you can navigate to the local site by visiting http://localhost:8000 in
your browser. This script will conveniently regenerate the site every time you
make a change to a file, so you won't need to rerun this command.

To shut down the development server, use

```
./develop_server stop
```

## Heroku Review Apps ##

When prompted, Heroku will provision temporary public web hosting and a domain
name for any open pull request, and post a pingback on GitHub. This allows
anyone to access the temporary site and review what our website would look
like upon merging the changes from that pull request.

### Permissions to access Heroku

Access to Heroku is granted to all committers in the wics-uw GitHub
organization. Membership to the "committers" group is granted to all full
Systems Committee members, as well as individuals that the Systems Committee
have chosen in recognition of their contributions and demonstrated
responsibility and good judgment.

To become a committer, you'll need to learn git, contribute regularly to the
WiCS website (both opening pull requests and reviewing them), and then ask the
Systems Committee for access, by emailing <wics-sys@lists.uwaterloo.ca>.

### To deploy a pull request

1. Go to [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps)
2. Click on *wics-site*
3. In the left column, named *Review Apps*, find the PR you want to deploy and
   click the button that says *Create Review App*

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
source ~/virtualenvs/pelican/bin/activate
make rsync_upload
```

Which conveniently deploys the site into the `wics` user's `www/` directory.
