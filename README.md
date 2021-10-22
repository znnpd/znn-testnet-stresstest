# znn-testnet-stresstest
Scripts for stresstesting the ZNN testnet

# Prerequisits
* Download the testnet bundle for your operating system: https://testnet.znn.space/#!downloads.md
  * Make sure to run the znnd daemon for some time to update the momentums. Current momentum be checked with `znn-cli frontierMomentum`
  * Make sure that all addresses have enough tZNNs (2000 per address is fine, depends on AMOUNT (see below))
  * Make sure that all addresses have enough plasma fused (10'000 tQSR per address is fine)
* Python 3.7.x

# Script Configuration
## Adjust the following variables
| Variable | Description |
| --- | --- |
| USE_SCHEDULED_MODE | Toggles scheduled mode on/off. Scheduled mode runs the script at a specific time (max. +30s) for a defined number of seconds.  |
| START_TIME | Start time for scheduled mode. Format: YYYY-MM-DD_HH-MM (must be set in local time of your operating system) |
| DURATION_IN_SECS | Duration of script execution in seconds for scheduled mode |
| KEYSTORE | Name of the keystore. Use `znn-cli wallet.list` to see all available keystores. Note: Keystores are either named as addresses (z1qz.....) or like `Instance of 'Future<Address?>'_1234567890123`. In 2nd case make sure to escape the quotes with backslash (as example in the scripts). |
| PASSPHRASE | Your Syrius passphrase |
| AMOUNT | Amount of <COIN> that will be used for the transactions |
| COIN | Coin that will be used for the transactions, e.g. 'znn' |
| ZNN_CLI | Path to the znn-cli executable |
| SYRIUS_ADDRESS_X | Some of your addresses in Syrius wallet, recommended number is 10 |
# Run the script
1. `python3 bin/stresstest_linux_1-0-0.py`