# Instagram-Direct-Message-Posts

Created this app because my friends send me lots of reels on Instagram and when you want to watch it on pc it can become the most frustrating thing because you are not able to open new tabs from the posts of direct messages meaning you would have to click on post, go back to direct message of the person, and scroll to where you were before (if they send you lots of reels you can imagine how frustrating this can be).

So I found out this work around to speed up and make things easier.

## Instagram

When you are on the direct messages of the person open console (F12) and go to network and filter by keyword ***cursor***

Click on the latest protocol and go to response, copy the whole thing and when you run the program it will instantly wait for input. 

Just paste the whole response unchanged to the program and it will filter everything needed from the json and parse it to the post URLs.

![image](https://user-images.githubusercontent.com/43582852/222040528-60a27bef-e89d-4cae-a02f-ee9ee085811b.png)

Example output: 

![image](https://user-images.githubusercontent.com/43582852/222039569-47cdd927-4193-41ca-9588-cd1dc6d04be0.png)

The program orders the posts from the newest sent from your friends to latest, after watching all if you want to see more of your friend posts just scroll up and a new cursor request will be sent from instagram just copy the new response of the request and paste it back on the program it will parse the new urls. 
