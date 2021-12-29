# Flippy - Your personalized voicebot

This bot can help you find your order,start a return, subscribe to our e-mails, find the best promotions and discounts,even see if we carry your desired shoes and cancel your ongoing order. Built using Rasa 2.3.1

## Install dependencies

Run:
```bash
pip install -r requirements.txt
```

## Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions
```
Then, to run the server in another terminal window:
```bash
rasa run
```

In another window, run the duckling server (for entity extraction):
```bash
docker run -p 8000:8000 rasa/duckling
```
Then to connect the rasa model through Aimybox to run the voicebot(in another terminal window):
```bash
ngrok http 5005
```
To talk to your rasa model as a chatbot run:
```bash
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.


## Overview of the files

`data/stories.yml` - contains stories

`data/nlu.yml` - contains NLU training data


`data/rules.yml` - contains the rules upon which the bot responds to queries

`actions/actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`tests/test_stories.yml` - end-to-end test stories


## Things you can ask the bot

1. Check the status of an order
2. Return an item
3. Cancel an item
4. Search a product inventory for shoes
5. Subscribe to product updates
6. Register for the Flipkart Axis credit card
7. how to pay the credit card bills


The main flows have the bot retrieving or changing information in a SQLite database (the file `example.db`). You can use `initialize.db` to change the data that exists in this file.

For the purposes of illustration, the bot has orders for the following contact numbers:

- `8171 427 101`
- `9999 888 777`
- `9898 989 898`
- `9123 456 789`
- `9191 919 191`
- `9999 999 999`
- `888 888 8888`
- `8989 898 989`
- `878 7878 787`

And these are the shoes that should show as in stock (size, color):

```
inventory = [(7, 'blue'),
             (8, 'blue'),
             (9, 'blue'),
             (10, 'blue'),
             (11, 'blue'),
             (12, 'blue'),
             (7, 'black'),
             (8, 'black'),
             (9, 'black'),
             (10, 'black'),
             (8, 'green'),
             (7, 'purple'),
             (10, 'white'),
             (9, 'red'),
            ]
```

## Testing the bot

You can test the bot on test conversations by running  `rasa test`.
This will run [end-to-end testing](https://rasa.com/docs/rasa/user-guide/testing-your-assistant/#end-to-end-testing) on the conversations in `tests/test_stories.yml`.

Note that if duckling isn't running when you do this, you'll see some failures.

## Rasa X Deployment

To [deploy this bot](https://rasa.com/docs/rasa/user-guide/how-to-deploy/), it is highly recommended to make use of the
[one line deploy script](https://rasa.com/docs/rasa-x/installation-and-setup/one-line-deploy-script/) for Rasa X. As part of the deployment, you'll need to set up [git integration](https://rasa.com/docs/rasa-x/installation-and-setup/integrated-version-control/#connect-your-rasa-x-server-to-a-git-repository) to pull in your data and
configurations, and build or pull an action server image.


## Action Server Image

You will need to have docker installed in order to build the action server image. If you haven't made any changes to the action code, you can also use
the [public image on Dockerhub](https://hub.docker.com/repository/docker/cdesmar/retail-demo) instead of building it yourself.

It is recommended to use an [automated CI/CD process](https://rasa.com/docs/rasa/user-guide/setting-up-ci-cd) to keep your action server up to date in a production environment.


