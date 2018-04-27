# slack-py-type
Script for Slack to show yourself as typing whenever someone starts typing to you, and stop when they stop typing.

This is an adapation of [this](https://github.com/will/slacktyping) brilliant/evil project from Ruby to Python. As soon as someone starts typing to you in Slack, it will show you as typing in the same channel.


Note that the Python Slack dev kit doesn't seem to have any built-in functionality for updating typing status using the real time messaging interface, so you'll need to use my [fork](https://github.com/joetimmerman/python-slackclient) with the functionality added. By default, this script assumes the slackclient package will be in the same directory as the script.
