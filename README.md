# Bitcoin Proof-of-Life
Take a photo with the QR image which is generated to prove that you were alive at the current Bitcoin block height.

This repository contains
1. Front-end as PWA to generate and display the QR image
2. Python script to automate posting to Twitter

Run the python script periodically with the following command
```
python3 ./bin/twitterProofOfLife.py consumer_key consumer_secret access_token access_token_secret
```
The keys and tokens must be generated with a Twitter developer account. This script works with Tweepy v4.12.0 and Twitter API v2.
