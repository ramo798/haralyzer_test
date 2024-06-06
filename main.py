from haralyzer import HarParser
import json

har_parser = HarParser.from_file("twitter.com.har")

for page in har_parser.pages:
    entries = page.entries
    for entry in entries:
        if 'Bookmarks?' in entry.request.url:
            # print(entry.response.text)
            json_data = json.loads(entry.response.text)
            # print(json.dumps(json_data, ensure_ascii=False, indent=2))
            for instruction in json_data['data']['bookmark_timeline_v2']['timeline']['instructions']:
              for entry in instruction['entries']:
                print(json.dumps(entry['content']['itemContent']['tweet_results']['result'], ensure_ascii=False, indent=2))
                # a = entry['content']['itemContent']['tweet_results']['result']['quoted_status_result']['result']['legacy']['full_text']
                # print(json.dumps(a, ensure_ascii=False, indent=2))
            break