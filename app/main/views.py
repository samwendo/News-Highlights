from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news, search_news, sources_news

@main.route("/")
def index():
    '''
    view root page function that reterns index
    '''

    top_headlin = get_news("top-headlin")

    title = "News headlines"

    search_news = request.args.get("news_query")
    search_sources = request.args.get("news_sources")
    if search_news:
        return redirect(url_for(".search", news_name = search_news))
    
    if search_sources:
        return redirect(url_for(".sources",sources_name= search_sources ) )

    return render_template("index.html", title = title, top= top_headline )

@main.route("/search/<news_name>")
def search(news_name):
    '''
    desplay search function
    '''
    
    news_name_list  = news_name.split("")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f" search resalt for {news_name}"
    
    return render_template("search.html", news = searched_news)
  
@main.route("/sources")
def sources():
    '''
    desplay source of news
    '''

    sources = sources_news()
    title = f"{sources} news"

    return render_template("sources.html", source = sources)
