# znn-testnet-stresstest
Scripts for stresstesting the ZNN testnet

# Prerequisits
* Download the testnet bundle for your operating system: https://testnet.znn.space/#!downloads.md
  * Make sure to run the znnd daemon for some time to update the momentums. Current momentum be checked with `znn-cli frontierMomentum`
* Python 3.7.x

# Script Configuration
## Adjust the following variables
| Variable | Description |
| --- | --- |
| USE_SCHEDULED_MODE | Toggles scheduled mode on/off. Scheduled mode runs the script at a specific time for a defined number of seconds.  |
| START_TIME | Start time for scheduled mode. Format: YYYY-MM-DD_HH-MM (must be set in local time of your operating system) |
| DURATION_IN_SECS | Duration of script execution in seconds for scheduled mode |
| PASSPHRASE | Your Syrius passphrase |
| AMOUNT | Amount of <COIN> that will be used for the transactions |
| COIN | Coin that will be used for the transactions, e.g. 'znn' |
| ZNN_CLI | Path to the znn-cli executable |
| SYRIUS_ADDRESS_X | Some of your addresses in Syrius wallet, recommended number is 10 |
