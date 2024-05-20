def extract(ancestor, selector=None, attribute=None, return_list=False):
    if selector:
        if return_list:
            if attribute:
                return [tag[attribute].strip() for tag in ancestor.select(selector)]
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if attribute:
            try:
                return ancestor.select_one(selector)[attribute].strip()
            except TypeError:
                return None
        try:
            return ancestor.select_one(selector).text.strip()
        except AttributeError:
            return None
    
    if attribute:
        return ancestor[attribute].strip()
    return ancestor.text.strip()


selectors = { 
    'opinion_id' : (None, 'data-entry-id'),
    'author' : ('.user-post__author-name',),
    'recommendation' : ('.user-post__author-recomendation',),
    'stars' : ('.user-post__score-count',),
    'content' : ('.user-post__text',),
    'pros' : ('.review-feature__title--positives ~ .review-feature__item', None, True),
    'cons' : ('.review-feature__title--negatives ~ .review-feature__item', None, True),
    'helpful' : ('button.vote-yes > span',),
    'unhelpful' : ('button.vote-no > span',),
    'publish_date' : ('span.user-post__published > time:nth-child(1)',"datetime"),
    'purchase_date' : ('span.user-post__published > time:nth-child(2)',"datetime")
    }