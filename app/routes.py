from flask import Flask, request, abort, json
import instagram

app = Flask(__name__)

@app.route('/search/<string:target>/<string:keyword>')
def search(target, keyword):
    if(target == 'instagram'):
        return search_instagram(keyword)
    return ''

def search_instagram(keyword):
    return instagram.crawler.get_posts_by_hashtag(keyword, 100)

if __name__ == '__main__':
  app.run(port=8080, debug=False)
