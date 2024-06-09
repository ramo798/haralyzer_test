from haralyzer import HarParser
import json

with open('202406090358-12.har', 'r', encoding='utf-8-sig') as f:
    har_parser = HarParser(json.loads(f.read()))

all_tweet = []
for page in har_parser.pages:
  entries = page.entries
  for entry in entries:
      if 'Bookmarks?' in entry.request.url:
          json_data = json.loads(entry.response.text)
          for instruction in json_data['data']['bookmark_timeline_v2']['timeline']['instructions']:
            cursor_count = sum(1 for entry in instruction['entries'] if entry['content']['entryType'] == 'TimelineTimelineCursor')
            tweet_count = 0
            for i, entry in enumerate(instruction['entries']):
              if entry['content']['entryType'] == 'TimelineTimelineCursor':
                continue
              text = ''
              try:
                text = entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
              except:
                pass

              try:
                text = entry['content']['itemContent']['tweet_results']['result']['tweet']['legacy']['full_text']
              except:
                pass

              print(text)
              print('-------------------')
              tweet_count += 1
              all_tweet.append(text)

          if len(instruction['entries']) - cursor_count != tweet_count:
            print('sdiouhvslodihvsoidhvsiodhvosihdvosihdvoishdvioh')

print(len(all_tweet))