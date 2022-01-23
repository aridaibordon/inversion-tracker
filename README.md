# Inversion tracker for DEGIRO.

*At the time of written (01/2022) the platform DEGIRO does not support any official API nor allows any in-platform tracking to keep track of your balance.*

This repository tracks the balance of any DEGIRO account and send reports using a telegram bot. To work properly, the repository needs the following environment variables:

* Your DEGIRO account and password (USERDEGIRO and PASSWORD).
* Telegram token and a your chat id (TOKEN and CHAT_ID).
* Server, database, user and password of a postgreSQL database. For example, you can get one for free [here](https://www.elephantsql.com/).

## Features

### In progress
* Create monthly documents.
* Add BTC and ETH wallet tracker for some given public address.

### Raw ideas
* Create web server and application.
* Add more brokers (eToro, Interactive Brokers).
* Unify bot service and database.

### Completed
* Compare daily earnings with a selection of indexes and stocks (01/22).
* Add weekly reports with custom plots (01/22).
* Migrate from sqlite to postgreSQL (12/21). 
