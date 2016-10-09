Title: Using Internet Relay Chat (IRC)
Category: pages
Status: hidden
Slug: irc

The Women in Computer Science Undergraduate Committee uses a public [Internet
Relay Chat](http://en.wikipedia.org/wiki/Internet_Relay_Chat) (IRC) channel
to chat, plan events, and hold discussions. If you've never used IRC before,
this document is designed to help you get set up.

Our public IRC channel, #wics, is located on the Open and Free Technology
Community (OFTC) network. We also have a separate channel for our systems
commitee, #wics-sys. You can visit us by connecting to
[irc.oftc.net](http://www.oftc.net/) or using our webchat, as detailed below.

**Note:** All conversations in the channel are logged for future reference, but
we do not publish our logs. Communication in the channel is governed by our
[Code of Conduct]({filename}/pages/code-of-conduct.md). If you haven't given it
a read yet, please take a few minutes to familiarize yourself with it!

## Setting Up IRC (you can pick any of these options)

#### Web

If you just want to drop by our channel to see what all the fuss is about, it's
as easy as clicking a link  to join us via a web chat client. You can join our
general channel, [#wics](http://webchat.oftc.net/?channels=wics), or our
systems committee channel,
[#wics-sys](http://webchat.oftc.net/?channels=wics-sys), in this way. Simply
choose a username and click "Connect"!

#### WeeChat
Weechat has become a favourite among committee, so if you like to have a gui
and point-and-clickness, we recommend you try this first. It also has
notifications on phone and desktop, and you are always connected if you keep it
on a screen.

Steps:

1. ssh into taurine or mother gooose, by running one of these commands in PuTTY
   (Windows) or in a Terminal (Mac/Linux):
   - `ssh userid@taurine.csclub.uwaterloo.ca` (for CSC) - If you don’t have an
      account, visit the CSC office and pay $2 to sign up
   - `ssh userid@mother-goose.wics.uwaterloo.ca` (for WiCS) - If you don’t have
     a userid, ask Fatema to create one.
2. type into the terminal `screen weechat`
3. in WeeChat buffer type: `/set relay.network.password [pick a password that
   you don’t use for anything important]`
4. `/relay add weechat #####` where ##### is a port number. Pick a number
   between 28000 and 28500
5. To set up on a web browser, go to glowing-bear.org, and enter the
   information, (eg. host: taurine.uwaterloo.ca; port: 00009; password:
   butts123)
6. To set up on your phone, download WeeChat Android, or the Glowing Bear app,
   and go to settings>connection settings, fill out the same information again
7. Either in the app or the web interface, you need to join all the channels
   and servers. In the buffer type:
    - `/server add oftc irc.oftc.net`
    - `/connect oftc`
8. Go to the oftc screen, in glowing-bear click on the bear’s face, and click
   on oftc, in weechat android click on the W in the top-left corner
    - `/join #wics` (public conversation)
    - `/join #wics-sys`
    - `/join #wics-general` (committee -only channel! wics-sys people don't
      join this)
8. All these channels will appear on the list on the left.
9. You should be connected forevs, unless sucrose goes down for some reason.

# Important things for using IRC

### Notifications
- It's important that you check IRC frequently - for some people notifications
  help this be a thing
- WeeChat has notifications!
- If you're not using weechat and have an Android phone, see documentation on
  irssinotifier

#### Beginner's Guide to IRC Commands
- IRC is command based. Here are the basic commands you should know:
- `/connect $ircNetwork` (e.g. `/connect irc.oftc.org`): this connects you to
  an irc network
- `/nick new_name` (e.g. `/nick evy`): If you want to change your nickname use
  this command  where `new_name` is the name you want. If that nick is
  registered, you have 30 seconds to "identify" yourself
- `/msg nickserv identify $password`: this is the command used to identify
  yourself. Your password is whatever you set it to be when you register your
  nick
- `/join $channel` (e.g. `/join #wics`): This is the command used to join a
  channel
- `/q $nick` (e.g. `/q evy`): This opens a "query" window with another user.
  This is used to PM someone. You can then switch to that window and chat with
  another user
- `/wc` or `/close` closes the window you’re in

#### Hilight

Highlight will give you notifications for certain words. You are automatically
hilighted on your nick when it is at the beginning of a line. You can add
additional hilight by typing `/hilight $word`).

We recommend you add at least these hilight:
- your nick (so it will hilight anywhere)
- your actual name (if it differs from your nick)
- the word "all" and the word "channel" (we use these to get everyone's
  attention)

If you have a Quest account and want to read more about IRC, you can view
the full IRC documentation
[here](https://git.uwaterloo.ca/wics/documentation/wikis/irc)
