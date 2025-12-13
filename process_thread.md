For the Attched json file itself contains the informaiton for the whole reddit thread itself

You are an expert Lead finder

We are the company doing the following:

We have build a renderfarm named Renderperk and we use GPU in it to do rendering for people themselves 
which makes their work quicker and cheaper

we currently only support to work with blender but open for opportunities for other sotwares too and hence it would be 
great if specify blender and seek as potential helpers for people not directly using blender snd all



Your task is as follows:

1. Extract all usernames mentioned in the Reddit thread, along with the Reddit profile URL for each user. For every user, identify their role in the conversation (e.g., original poster, commenter, expert, etc.). Present this information as a list, where each entry contains the Reddit URL and the user's role in the thread.

Example format:
```json
[
    {
        "reddit_url": "https://www.reddit.com/user/Tricky-Chocolate-304",
        "role": "Commenter - recommended XRender as an alternative render farm option"
    },
    {
        "reddit_url": "https://www.reddit.com/user/cstoof",
        "role": "Commenter (FX Lead flair) - Experienced professional explaining that big studios have local render farms but use cloud when overburdened"
    }
]
```
This list should be stored under the field name `context`.

If a username appears multiple times with different roles or contexts, append the new information to their entry in the list.

If a new user is found, add their details to the `user-names.json` file.

A sample record:
```json
{
    "username": "Tricky-Chocolate-304",
    "context": [
        {
            "reddit_url": "https://www.reddit.com/user/Tricky-Chocolate-304",
            "role": "Commenter - recommended XRender as an alternative render farm option"
        }
    ]
}
```




2. Find out the relevant context for the initial conversation and find out the relevant comments at the relevant places that I can make to intitial meaning full conversation and even to provide value so that my activity on reddit increases and all

Need to add the comments I need to make all of that in the actions.json file itself.
Make sure to mention at under which user should I make the commment too
Make sure to put the reddit url itself 
Also write down the reason for that comments and all under the json record itself
Make sure that it is humane and it is something that looks humane to read for that maybe try including some humane language and spelling erros and all
Dont promote on every comment give something meaningful to add to teh conversation some tip some question and offer help if it seems like a good place to provide some

https://www.renderperk.studio
this is the link of the website itself so we need to include the website link in the comment itself if we are trying the user to check us out

3. find out relevant pieces of ideas that I can make out of which can be useful and even insightful for more reach itself.

Need to add the ideas in the ideas.json file itself
Make sure to link to the correct reddit url for the idea 
Add proper context in respective json record for the same.


4. Do competion analysis figure out the render famrs which people are talking about 

In the json file make a record for all the unique render farms names found in it
for competetor record stores the positives the users are saying the negative users are saying
Store all the relevant context found regarding them (How they Market, Scale, potential bottlenecks, business execution etc...)
also make sure to having a counter so that we can have data about how many people are syaing the same thing

eg. it has a great UI and a lot of people have the same intent then make sure to have some metadata stored of how many people are saying that and all
(Add we need to do this for all the pros and cons for the platform or the renderfarm found)


After processing the whole file from the unprocess remove it from the unprocess folder and add the json file into the processed folder itself