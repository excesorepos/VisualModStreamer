#!/usr/bin/env python3
import asyncpraw
import asyncio

async def run():

    username = 'REDDIT_USERNAME'
    passwd = 'REDDIT_PASSWORD'

    reddit = asyncpraw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    password=f'{passwd}',
    username=f'{username}',
    user_agent=f'Visualmod Streamer (by u/{username})'
    )
    reddit.read_only = True

    sub = await reddit.subreddit('wallstreetbets')
    async for comment in sub.stream.comments(skip_existing=True):

        if comment.author == 'visualmod':
            if 'User Report' in str(comment.body):
                visualmod = ''
                visualmod += f'{comment.submission.id}\n'
                sub = await reddit.submission(comment.submission.id)
                visualmod += f'{sub.author}\n'
                visualmod += f'{sub.title}\n'
                visualmod += f'https://www.reddit.com{sub.permalink}\n'
                visualmod += f'{comment.body}\n'
                with open('visualmod.md', 'a') as fd:
                    fd.write(visualmod)
                print(visualmod)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())