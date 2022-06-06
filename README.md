**ABSTRACT**

In today\'s times, so many things have been automated such as
recommendations, vision related tasks, but there has not been much
diversity in the field of NLP and chatbots.

Our chatbot, Honeycomb, is a one-of-a-kind chatbot which can perform
tasks related to cryptocurrencies, data visualization, and much more
with the use of Natural Language Understanding.

A lot of people either deny or turn away from tasks when they need to
perform extra irrelevant steps to get the result they want, for example,
surveys, forms, etc.

Our chatbot works entirely using NLU to bridge this information
retrieval problem that many modern systems face. Users can chat with our
chatbot regarding various crypto related tasks like graph plotting,
market caps, historical market data using normal human language, and the
bot will reply with a proper response regarding the query.

The bot is called Honeycomb as a honeycomb is the most efficient
structure, and leaves no space for errors!

**TABLE OF CONTENTS**

**Chapter 1: Introduction 1**

1.1 Problem Statement 1

1.2 Motivation 1

1.3 Objective 2

1.4 Scope 2

**Chapter 2: System Requirement 3**

2.1 Hardware Requirement 3

2.2 Software Requirement 3

**Chapter 3: System Analysis 4**

3.1 Study of Current system 4

3.2 Proposed System 4

3.3 Feasibility Study 5

3.3.1 Technical Feasibility 5

3.3.2 Economical Feasibility 6

3.3.3 Operational Feasibility 6

**Chapter 4: System Design 8**

4.1 Data Dictionary 8

4.2 Data Flow Diagram 10

4.3 ER Diagram 11

4.4 Use Case Diagram 12

**Chapter 5: Project Implementation 13**

**Chapter 6: Testing 33**

**Chapter 7: Conclusion and Future Work 39**

**LIST OF TABLES**

  ----- ---------------------- ---
  4.1   coin_list              8
  4.2   guilds                 8
  4.3   supported_currencies   9
  ----- ---------------------- ---

**LIST OF FIGURES**

  ------ -------------------------------------- ----
  4.1    Data Flow Diagram                      10
  4.2    ER Diagram                             11
  4.3    Use Case Diagram                       12
  5.1    Bot joins server                       13
  5.2    Bot setup command                      13
  5.3    Bot setup command output               14
  5.4    Bot info command                       14
  5.5    Bot supported currencies list          15
  5.6    Bot price command                      15
  5.7    Bot coin search command                16
  5.8    Bot coin data command Page 1           16
  5.9    Bot coin data command Page 2           17
  5.10   Bot coin data command Page 3           17
  5.11   Bot global holdings command            18
  5.12   Bot change default currencies          19
  5.13   Bot dictionary command                 19
  5.14   Bot normal chart command               20
  5.15   Bot normal chart command output plot   20
  5.16   Bot ranged chart command               21
  5.17   Bot ranged chart command output plot   21
  5.18   Bot OHLC chart command                 22
  5.19   Bot OHLC chart command output plot     22
  5.20   Bot NLU Basic Conversation             23
  5.21   Bot NLU Coin search                    23
  5.22   Bot NLU Coin price                     24
  5.23   Bot NLU Coin Price debug               25
  5.24   Bot NLU Coin Data                      25
  5.25   Bot NLU Feel good, Feel bad intents    26
  5.26   Bot NLU Global Holdings                26
  5.27   Bot NLU Future Work                    27
  5.28   Bot NLU Price Chart                    27
  5.29   Bot NLU Price Chart output             28
  5.30   Bot NLU Chart defaults                 28
  5.31   Bot NLU Chart default output           29
  5.32   Bot NLU Volume Chart                   30
  5.33   Bot NLU Volume Chart Output            30
  5.34   Bot NLU Market Cap Chart               31
  5.35   Bot NLU Market Cap Chart output        31
  5.36   Bot NLU OHLC Chart                     32
  5.37   Bot NLU OHLC Chart output              32
  6.1    Bot supported currencies Error         33
  6.2    Bot unknown coin error                 33
  6.3    Bot command cooldown                   34
  6.4    Bot Chart unknown days                 34
  6.5    Bot ranged, OHLC, Dictionary errors    35
  6.6    Bot Dictionary error                   36
  6.7    Bot unhandled exceptions               36
  6.8    Bot NLU unspecified fields             37
  6.9    Bot NLU fallback intents               38
  6.10   Bot NLU Date discrepancy               38
  ------ -------------------------------------- ----

**CHAPTER 1:**

**INTRODUCTION**

**CHAPTER 1: INTRODUCTION**

**1.1 Problem Statement:**

These days, there are multiple services and applications which fulfill
crypto related user requests. But most of these services have various
drawbacks, such as being too complicated to navigate and fulfill even
the simplest tasks, requiring too much information, having to input the
information in a primitive way using forms, and being a static service.
These are just some problems that are faced by modern crypto related
services.

Due to these issues, a lot of the users who are looking for a source of
quick, precise, and accurate information either deny or turn away from
these services. Honeycomb, our chatbot, aims to bridge these problems,
and make crypto related information easier to access using NLP!

Honeycomb is capable of understanding and responding to user queries in
English, making it easier for users to obtain accurate and precise
information. It also does not require any extra information, and
fulfills mostly every task related to cryptocurrencies, ranging from
market caps and historical market data to company holdings.

**1.2 Motivation:**

Having used cryptocurrency services before, we have faced many
complications regarding the information overload, complications in
navigating this information, visualizing the information in an
understandable way, and even requiring extensive amounts of data to
obtain even the most basic information.

Being regular bot users on various platforms such as Telegram and
Discord, we were inclined to create an NLP-powered crypto chatbot which
solves these issues and also makes the information much easier and
efficient to access, and simpler to understand, thus saving time and
sanity!

**1.3 Objective:**

**Objective of this project is to: **

1.  Remove the complications regarding information retrieval.

2.  Make information related to cryptocurrency easily accessible.

3.  Implement NLP modules to understand human language and therefore
    process requests seamlessly.

4.  Make it easier for users to understand complex crypto related data
    using graphing and charts.

5.  Fetch latest up-to-date data by using reliable APIs.

6.  Create a cryptocurrency related service in the form of a chatbot.

**1.4 Scope:**

Honeycomb is designed for people looking for a reliable source of
cryptocurrency related information which is very easily available in an
understandable format. Users can access real-time data regarding current
prices, conversion rates, market caps, company holdings, etc. Our bot is
capable of understanding human language, making it overly convenient for
each and every user capable of communicating in English.

**CHAPTER 2:**

**SYSTEM REQUIREMENTS**

**CHAPTER 2: SYSTEM REQUIREMENTS**

**2.1 Hardware Requirements:**

**Developer side:**

1.  Processor: Intel i5

2.  RAM: 8GB

3.  SSD/HDD: 5GB

4.  Virtual Private Server to host Chatbot & NLP Module.

**User side:**

1.  Personal computer, Laptop or Smartphone.

2.  Internet connection.

**2.2 Software Requirements:**

**Developer side:**

1.  Python 3.8

2.  MySQL

3.  py-cord (Discord's Application API)

4.  Rasa (NLU Engine)

5.  Matplotlib (Chart plotting library)

**User side:**

1.  Web Browser or Discord client running on any device.

**CHAPTER 3:**

**SYSTEM ANALYSIS**

**CHAPTER 3: SYSTEM ANALYSIS**

**3.1 Study of Current System:**

Although there are some similar yet not so similar systems available in
the market, our chatbot stands out of the crowd with groundbreaking
features that help any individual looking for information about crypto
currency. There are many reasons to call the systems as
"[Unpolished]{.ul}" because of these following reasons.

-   The current systems are totally command based i.e. there is no NLU
    module/segment which could help a user to navigate through their
    information quickly and reliably.

-   Commands are "Hard Coded" which make the whole system stiff for new
    users.

-   Many commands do not function even though they are provided by the
    respective developers. \[Fig. 3.1\]

> ![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image1.png){width="1.8127526246719161in"
> height="1.9377701224846895in"}
>
> **Fig. 3.1** Unusable features

**3.1 Proposed System:**

Honeycomb, our crypto chatbot, is a one-stop solution for real-time
crypto related information accessible at ease and presented in an
understandable format. It also overcomes several drawbacks mentioned
above in the following way:

-   Honeycomb has an independent NLP/NLU component which enables it to
    efficiently and easily understand user queries in English without
    having to browse through the documentation of the bot.

```{=html}
<!-- -->
```
-   Users do not have to remember the proper notation or syntactical
    details regarding the commands as our chatbot offers help
    functionality, and is also capable of addressing subtle user
    queries.

```{=html}
<!-- -->
```
-   Our chatbot operates on free APIs which provide us with an immensely
    reasonable amount of requests per minute. Even then, users are met
    with a custom timeout message to prevent spamming, thus keeping it
    clean, informative and hassle-free.

```{=html}
<!-- -->
```
-   Honeycomb is capable of handling both - command based and natural
    language based user queries, which makes it much more flexible.

-   It provides a chart-making functionality which has been built from
    scratch to be able to parse extremely complex information into a
    user-friendly format which is easy to understand and does not
    require any extra information.

```{=html}
<!-- -->
```
-   In our chatbot, all processes are executed asynchronously and
    independent of each other, due to which our bot responds within mere
    seconds.

```{=html}
<!-- -->
```
-   Honeycomb automatically caches cryptocurrency related information,
    guild/channel related information, and currency related information
    automatically on boot.

```{=html}
<!-- -->
```
-   Our chatbot presents complex crypto-related information to the user
    in an easily understandable format.

**3.3 Feasibility Study:**

**3.3.1 Technical Feasibility:**

Current operational chatbot applications require the Discord
application, a working mobile phone, laptop or a PC, stable internet
connection on the user side. It also requires the users to be in contact
with the bot through a connected channel.

Similarly, our chatbot application works upon the common underlying
hardware and software, and requires no additional technology. As there
are no changes to be made here, it is technically feasible for the user.

For the developers of the chatbot, the following is required:

1.  A virtual private server to host the chatbot

2.  Python 3.8+ release

3.  Pycord library to interface with Discord

4.  Rasa library for NLP/NLU tasks

5.  Matplotlib library for charting purposes

6.  Data-serving APIs

7.  SQLite (DBMS)

The VPS, and all the APIs are free to use and hence, no financial
investments are necessary, and hence, our system is technically
feasible.

**3.3.2 Economical Feasibility:**

For the users of our chatbot, no extra investment is required as most
people have a working device with active internet connection.

On the developer side too, no financial investment is necessary unless
the user base increases exponentially, requiring more API calls per
minute. This financial investment can be compensated for through revenue
earned by the chatbot by ads, donations, or a premium subscription.

As the chatbot provides real-time data, NLP support, and
easy-to-understand information, it is highly likely that the additional
revenue earned by the bot will outweigh the financial investment that
may be required in the future. This makes the chatbot highly
economically feasible.

**3.3.3 Operational Feasibility:**

Our chatbot aims at eradicating and solving many of the underlying
problems that users face while using similar chatbots and crypto-related
bots. Honeycomb is one of the first crypto chatbots on any platform
which provides NLP/NLU functionality. As it works on the underlying
software and hardware, users won't have to change anything.

On the developer side, we aim to scale and expand our chatbot in a
modular and sequential way. To incur for all the possible investments,
we will incorporate ads, donations, or a premium subscription scheme.

Our chatbot makes realtime up-to-date information readily available to
the user in an easily understandable way using Discord embeds without
any hassle, which is not possible in many of the other chatbots in place
on other platforms such as Telegram and Whatsapp.

To make sure that the information is presented in an easily
understandable format, a small-scale survey was conducted to find out
what information users look for. This ensures that the users will
actively endorse and use our chatbot, making it operationally feasible.

**CHAPTER 4:**

**SYSTEM DESIGN**

**CHAPTER 4: SYSTEM DESIGN**

**4.1 Data Dictionary**

**Table name:-** coin_list

**Description:-** It contains all the cryptocurrency coins with its
**id**, **symbol** and **name**. It gets updated automatically when the
bot restarts.

**Table 4.1: coin_list**

  ----------- ---------- ---------- ---------- ---------------- -------------------------------------------------
  **Sr.No**   **Name**   **Type**   **Size**   **Constraint**   **Description**
  1           Id         Text       Variable   Primary Key      It is a unique string that identifies the coin.
  2           Symbol     Text       Variable   Not Null         It is a string that acts as a symbol for coins.
  3           Name       Text       Variable   Not Null         It is a string denoting the name of coins.
  ----------- ---------- ---------- ---------- ---------------- -------------------------------------------------

**Table name**:- guilds

**Description**:- It contains all the information about all the guilds
and channels that our bot is connected to. The updation for this table
is also fully automated.

**Table 4.2: guilds**

  ----------- --------------------- ---------- ---------- ---------------- -------------------------------------------------------------------------------------------------------------------
  **Sr.No**   **Name**              **Type**   **Size**   **Constraint**   **Description**
  1           guild_id              BIGINT     8          Primary Key      It is a unique integer that identifies a guild/channel.
  2           nlu_channel_id        BIGINT     8                           It is an integer that identifies the channel reserved for NLU mode in the respective guild.
  3           default_vs_currency   Text       Variable                    It is a singular value or a group of values that denote the default conversion currency for the respective guild.
  ----------- --------------------- ---------- ---------- ---------------- -------------------------------------------------------------------------------------------------------------------

**Table name**:- supported_currencies

**Description**:- It contains the currencies which are currently
supported by our chatbot. The updation of this table is automated.

**Table 4.3: supported_currencies**

  ----------- ---------- ---------- ---------- ---------------- ----------------------------------------------------------------------------
  **Sr.No**   **Name**   **Type**   **Size**   **Constraint**   **Description**
  1           id         Text       Variable                    It is a unique string that identifies a currency supported by the chatbot.
  ----------- ---------- ---------- ---------- ---------------- ----------------------------------------------------------------------------

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image2.png){width="8.385416666666666in"
height="8.526735564304461in"}**4.2 Data Flow Diagram**

**Fig 4.1 Data Flow Diagram**

**4.3 Entity Relationship Diagram**

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image3.png){width="8.301736657917761in"
height="6.354166666666667in"}

**Fig 4.2 ER Diagram**

**4.4 Use Case Diagram**

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image4.png){width="8.228819991251093in"
height="6.21875in"}

**Fig 4.3 Use Case Diagram**

**CHAPTER 5:**

**PROJECT IMPLEMENTATION**

**CHAPTER 5: PROJECT IMPLEMENTATION**

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image5.png){width="6.295776465441819in"
height="4.119097769028872in"}

**Fig 5.1 Bot joins server**

**Description:** Our bot displays this message whenever it joins a new
server. It gives details about the bot, how to use it, and other useful
information.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image6.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.2 Bot setup command**

**Description:** The admin of the server can use the setup command to
set up the NLU channel and the default exchange currencies.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image7.png){width="6.097577646544182in"
height="4.111111111111111in"}

**Fig 5.3 Bot setup command output**

**Description:** Our bot sends this output message in the NLU channel as
soon as it has been set, so that other users are also informed about it.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image8.png){width="6.562847769028871in"
height="3.2705938320209973in"}

**Fig 5.4 Bot info command**

**Description:** Users can use the info command to obtain information
about the NLU channel and the default exchange currencies in the current
server.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image9.png){width="6.097577646544182in"
height="3.7083333333333335in"}

**Fig 5.5 Bot supported currencies list**

**Description:** Our bot keeps an updated list of supported exchange
currencies, which can be fetched through the supported_currencies
command.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image10.png){width="6.097577646544182in"
height="3.7222222222222223in"}

**Fig 5.6 Bot price command**

**Description:** Users can use the price command to fetch the price of
multiple specified coins in multiple specified currencies.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image11.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.7 Bot coin search command**

**Description:** Users can use this command to find respective entries
of coins by searching for either their id, symbol, or name.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image12.png){width="6.097577646544182in"
height="3.7222222222222223in"}

**Fig 5.8 Bot coin data command Page 1**

**Description:** Users can use the coin_data command to fetch relevant
information about a specified coin. Page 1 represents the description of
the coin.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image13.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.9 Bot coin data command Page 2**

**Description:** Page 2 represents price-related information like
Current Price, All Time High/Low, and Price Change %.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image14.png){width="6.097577646544182in"
height="3.7777777777777777in"}

**Fig 5.10 Bot coin data command Page 3**

**Description:** Page 3 represents volume and market cap related
information like Total supply, Total volume, Market Cap Change,
Circulating supply.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image15.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.11 Bot global holdings command**

**Description:** Users can use the global_holdings command to fetch the
current company holdings of Ethereum or Bitcoin, along with Entry value,
current value, and Total supply %.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image16.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.12 Bot change default currencies**

**Description:** The server admin can use this command to change the
default currencies of the respective server.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image17.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.13 Bot dictionary command**

**Description:** Users can use this command to find the different
meanings of any word.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image18.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.14 Bot Normal Chart command**

**Description:** Users can use the simple chart command to obtain a
historical chart of the price, market cap, or volume of any specified
coin for any number of days.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image19.png){width="6.479514435695538in"
height="3.2395833333333335in"}

**Fig 5.15 Bot Normal Chart command output plot**

**Description:** This is the output of the simple chart command. The
last value of the data is also annotated with the occurring time and
date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image20.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.16 Bot Ranged Chart command**

**Description:** Users can use the ranged chart command to obtain a
historical chart of the price, market cap, or volume of any specified
coin for a range of dates.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image21.png){width="6.269340551181102in"
height="3.1711811023622047in"}

**Fig 5.17 Bot Ranged Chart command output plot**

**Description:** This is the output of the ranged chart command. The
last value of the data is also annotated with the occurring time and
date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image22.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.18 Bot OHLC Chart command**

**Description:** Users can use the OHLC chart command to obtain the OHLC
chart of any specified coin for a fixed number of days in any specified
currency.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image23.png){width="6.30415135608049in"
height="3.6100688976377953in"}

**Fig 5.19 Bot OHLC Chart command output plot**

**Description:** This is the output of the OHLC chart command. If the
Open price of a coin is lower than the Close price on a given day, the
bar is colored green. Otherwise, it is colored red.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image24.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.20 Bot NLU Basic Conversation**

**Description:** This is a basic conversation between the bot and a
user.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image25.png){width="6.097577646544182in"
height="3.763888888888889in"}

**Fig 5.21 Bot NLU Coin Search**

**Description:** The user can search information about a coin. If the
specified coin does not exactly match any of the coins in the database,
our bot will automatically choose the lexicographically closest coin
using fuzzy logic.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image26.png){width="6.097577646544182in"
height="3.763888888888889in"}

**Fig 5.22 Bot NLU Coin Price**

**Description:** The user can search for the price of multiple specified
coins in multiple specified currencies. If the specified coin does not
exactly match any of the coins in the database, our bot will
automatically choose the lexicographically closest coin using fuzzy
logic.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image27.png){width="5.864583333333333in"
height="2.84375in"}

**Fig 5.23 Bot NLU Coin Price Debug**

**Description:** This is the processing of NLU that goes on under the
hood. Relevant entities are extracted and passed to the processing
script to execute the command specified by the user intent.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image28.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.24 Bot NLU Coin Data**

**Description:** On receiving the intent of coin_data, our bot will send
a message to the user indicating that this feature is not yet possible
without commands, and it specifies which commands the user can use to
get the data.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image29.png){width="6.097577646544182in"
height="3.7222222222222223in"}

**Fig 5.25 Bot NLU Feel good, Feel bad intents**

**Description:** If the user says anything affirmative or positive or
negative, our bot will reply with a message from a fixed set of
responses.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image30.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.26 Bot NLU Global Holdings**

**Description:** If our bot detects that the user wants the global
holdings, it will fetch the relevant coins and successfully respond with
the global holdings.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image31.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.27 Bot NLU Future Work**

**Description:** Using the future work intent, our bot displays all the
future works that have been planned for our bot.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image32.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.28 Bot NLU Price Chart**

**Description:** Using the chart intent, users can render ranged charts
of any specified coin in any specified currency.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image33.png){width="6.344097769028871in"
height="3.296761811023622in"}

**Fig 5.29 Bot NLU Price Chart output**

**Description:** This is the output of the ranged chart command. The
last value of the data is also annotated with the occurring time and
date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image34.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.30 Bot NLU Chart defaults**

**Description:** Whenever the time is not specified, our bot will
default it to one day. Whenever the chart type is not specified, our bot
will default it to price, and whenever the currency is not specified,
our bot will use the default currencies.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image35.png){width="6.369323053368329in"
height="3.2663188976377953in"}

**Fig 5.31 Bot NLU Chart default output**

**Description:** This is the ranged price chart generated using the
default values and the coin provided by the user.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image36.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 5.32 Bot NLU Volume Chart**

**Description:** This is the ranged volume chart for a specified coin in
a specified currency between a specified date. Here, only the start date
is mentioned, so our bot will automatically default the end date to be
the current date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image37.png){width="6.375347769028871in"
height="3.2367147856517935in"}

**Fig 5.33 Bot NLU Volume Chart Output**

**Description:** This is the ranged volume chart generated using the
time and the coin provided by the user.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image38.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.34 Bot NLU Market Cap Chart**

**Description:** This is the ranged market cap chart for a specified
coin in a specified currency between a specified date. Here, only the
start date is mentioned, so our bot will automatically default the end
date to be the current date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image39.png){width="6.323264435695538in"
height="3.231890857392826in"}

**Fig 5.35 Bot NLU Market Cap Chart Output**

**Description:** This is the ranged market cap chart generated using the
time and the coin provided by the user.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image40.png){width="6.097577646544182in"
height="3.75in"}

**Fig 5.36 Bot NLU OHLC Chart**

**Description:** This is the OHLC chart for a specified coin in a
specified currency for a specified number of days.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image41.png){width="6.417014435695538in"
height="3.6747003499562556in"}

**Fig 5.37 Bot NLU OHLC Chart Output**

**Description:** This is the OHLC chart generated using the number of
days and the coin provided by the user.

**CHAPTER 6:**

**TESTING**

**CHAPTER 6: TESTING**

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image42.png){width="6.097577646544182in"
height="3.75in"}

**Fig 6.1 Bot Supported Currencies Error**

**Description:** If the user specified an unknown currency which is not
supported by us, our bot will display an error message saying that the
currency is unsupported.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image43.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 6.2 Bot Unknown Coin error**

**Description:** If the user specified an unknown coin which is not
supported by us, our bot will display an error message.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image44.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 6.3 Bot Command Cooldown**

**Description:** After the user uses a command once, they go into
command cooldown for that particular command. This is done to reduce
spam and limit user requests per minute.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image45.png){width="6.097577646544182in"
height="3.763888888888889in"}

**Fig 6.4 Bot Chart Unknown days**

**Description:** If the date specified in the Chart command is not a
number, the bot will output an error message telling the user to input a
valid and sensible date.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image46.png){width="6.097577646544182in"
height="3.7222222222222223in"}

**Fig 6.5 Bot Ranged, OHLC Chart, Dictionary Errors**

**Description:** If the coin id or currency found in the ranged or OHLC
chart command is unknown, it displays an error message telling the user
to input a valid crypto/exchange id. For the dictionary command, if the
meaning for a word is not found, it will display respective error.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image47.png){width="6.097577646544182in"
height="3.75in"}

**Fig 6.6 Bot Dictionary Error**

**Description:** If a user tries to fetch the meaning of multiple words,
or a sentence, our bot will automatically output an error message saying
that there are multiple words in the message.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image48.png){width="6.097577646544182in"
height="3.763888888888889in"}

**Fig 6.7 Bot Unhandled Exceptions**

**Description:** If our bot encounters any unhandled exceptions in any
of the active guilds, the traceback messages will be posted to this
channel automatically, so as to get the developer's attention.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image49.png){width="6.097577646544182in"
height="3.75in"}

**Fig 6.8 Bot NLU Unspecified Fields**

**Description:** If the user specifies any intent without any of the
mandatory fields like coin id, our bot will send a fallback message back
to the user.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image50.png){width="6.097577646544182in"
height="3.763888888888889in"}

**Fig 6.9 Bot NLU Fallback intents**

**Description:** If the user specifies any unknown intent, which is not
registered by our bot, it will detect that and send a message back
accordingly.

![](https://raw.githubusercontent.com/nyu19/HoneyComb/master/media/image51.png){width="6.097577646544182in"
height="3.736111111111111in"}

**Fig 6.10 Bot NLU Date Discrepancy**

**Description:** If the user specifies the from date which is greater
than the to date, our bot will not respond to save power and time.

**CHAPTER 7:**

**CONCLUSION & FUTURE WORKS**

**\
**

**CHAPTER 7: CONCLUSION AND FUTURE WORKS**

**CONCLUSION**

Thus, through this project we aim to become the one stop solution for
all things crypto! This is just a stepping stone in the wide world of
AI. We have incorporated two types of query processing methods - normal
command based and natural language based.

Using our NLP-powered state-of-the-art crypto chatbot, users can easily
obtain real-time data presented in a clear and formatted (tabulated)
way. Users also bypass the extra hassle that comes with other platforms
for obtaining simple information, as only basic crypto and English
knowledge is required.

**FUTURE WORKS**

Following are the future plans for the development of HoneyComb:

-   Adding Logo caching in-order to display symbol of crypto coin in
    each response.

-   Add support for multi-intent classification.

-   Make NLU Asynchronous to reduce bot's latency when multiple users
    make requests at once.

-   Render charts Asynchronously to reduce waiting for chart. (Current
    time taken 2 seconds).

-   Integrate Rasa X for CI/CD (Self-Learning/ Learning from mistakes).

**BIBLIOGRAPHY**

1.  [Py-Cord](https://docs.pycord.dev/en/master/index.html) -
    https://docs.pycord.dev/en/master/api.html

2.  [Rasa](https://rasa.com/docs/rasa/) - https://rasa.com/docs/rasa/

3.  [Rasa Actions server](https://rasa.com/docs/action-server/) -
    https://rasa.com/docs/action-server/

4.  [TheFuzz](https://github.com/seatgeek/thefuzz) -
    https://github.com/seatgeek/thefuzz

5.  [MatPlotLib](https://matplotlib.org/) - https://matplotlib.org/

6.  [MPLfinance](https://github.com/matplotlib/mplfinance) -
    https://github.com/matplotlib/mplfinance

7.  [CoinGecko](https://www.coingecko.com/en/api/documentation) -
    https://www.coingecko.com/en/api/documentation

8.  [Dictionary](https://owlbot.info/api-reference) -
    https://owlbot.info/api-reference
