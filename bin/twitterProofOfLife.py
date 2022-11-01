#!/usr/bin/env python3
import requests, json, tweepy, sys

def main():
    # Get latest block
    latestblock = requests.get("https://blockchain.info/latestblock")

    # Create dictionary from block
    latestblockdict = latestblock.json()

    # Convert block json to text
    latestblocktxt = json.dumps(latestblockdict)

    # Get latest block stored
    latestblockfile = "./latestblock.txt"
    f = open(latestblockfile, "r")
    blockstored = f.read()
    f.close()

    if latestblocktxt == blockstored:
        print("Block stored is already the latest.")
        return

    # Write the latest block to storage
    f = open(latestblockfile, "w")
    f.write(latestblocktxt)
    f.close()

    # Get latest block hash and height
    blockhash = latestblockdict["hash"]
    blockheight = latestblockdict["height"]

    # Replace with
    client = tweepy.Client(
        consumer_key=sys.argv[1],
        consumer_secret=sys.argv[2],
        access_token=sys.argv[3],
        access_token_secret=sys.argv[4]
    )

    # Standard tweet
    tweet = "Latest #Bitcoin block at height " + str(blockheight) + ": " + blockhash + "\n\n" + "Get QR code here" + "\n" + "https://blockslide.org/bitcoin-proof-of-life/"  

    # About thread parts
    about_thread_part1 = "Approximately every 10 minutes a new block is generated and added to the #Bitcoin timechain. The latest is at block height " + str(blockheight) + "."
    about_thread_part2 = "The hash of this block " + str(blockheight) + " is impossible to predict and very easy to verify after the fact."
    about_thread_part3 = "Take a photo with our QR to prove that you were alive at block height " + str(blockheight) + "." + "\n" + "https://blockslide.org/bitcoin-proof-of-life/"

    try:
        if blockheight % 5 == 0:
            # Tweet about as a thread
            response1 = client.create_tweet(text=about_thread_part1)
            id_part1 = response1.data["id"]
            response2 = client.create_tweet(text=about_thread_part2, in_reply_to_tweet_id=id_part1)
            id_part2 = response2.data["id"]
            response3 = client.create_tweet(text=about_thread_part3, in_reply_to_tweet_id=id_part2)
            response = (response1, response2, response3)
            tweetposted = about_thread_part1 + about_thread_part2 + about_thread_part3
        else:
            # Standard tweet
            response = client.create_tweet(text=tweet)
            tweetposted = tweet
        
        print(response)
        
    except Exception as err:
        print("Error: " + str(err))
        print("------------------")
        pass

if __name__ == "__main__":
    main()