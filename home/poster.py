import facebook


def main():
    cfg = {
        "page_id": "270451476898417",
        "access_token": "EAALxi7OrNjsBAJCaF4eJfkZBakRYoIqXLGU1iArjzKRAUMq5mbUUdqM8MZADGoZCuyHgE482DgUWYRuDiaciuVLZCfmES6ZBetstZAUWJisyfHlpFmcNpgoPFZB19tyPeM2WvIDm1oh54YNp5lgjGZBaEJJhr3EOdwLJXJ9KtUEUk4dEtkNmSyLDexIwsL0RXRlKUQ2DEp1RRAZDZD"
        # "access_token": "EAAIbbZC6n2pwBAGS85ztzYYzZBnOQ35ZCO78ZAjEd4siEcDFkWZCGmXJzcQtgBARGvR1AxtDJquXgK5eu65R4HArnTgxthkTZBVZBFbU6TOtpmtZCNoZAfyWbANWjBDINfs6rI1JcpA2ffWxgJX5N9DSgc6qanLM7fWr8upkrKloDfowSwORXbDtCZBARNmxxcFbDp4AZAnDTrQnAZDZD",
        # "page_access_token": "EAAFdBI1Q0aIBAKSldHeQIVgdGOhmeLb5YkuocWEZCMabynzxK7vQes9KfGXTnGwFEWfpzUd0OQZBJb8PnOylex9NMDw8AaEFdL5sk5WqfpY4SZAkRIpPhKuYZC9eUev7n8zbjpCHXWW56uw2o6KX9qTBARoZAdleHnzk3c8eQciq0FfGn1eybSGMzU2UakQ4ZD"
        # "page_access_token": "EAAIbbZC6n2pwBAGS85ztzYYzZBnOQ35ZCO78ZAjEd4siEcDFkWZCGmXJzcQtgBARGvR1AxtDJquXgK5eu65R4HArnTgxthkTZBVZBFbU6TOtpmtZCNoZAfyWbANWjBDINfs6rI1JcpA2ffWxgJX5N9DSgc6qanLM7fWr8upkrKloDfowSwORXbDtCZBARNmxxcFbDp4AZAnDTrQnAZDZD"
    }

    api = get_api(cfg)
    msg = "Welcome to YS Tours and Travels..."
    status = api.put_object(
        parent_object = "me",
        connection_name = "feed",
        message=msg)


    post = api.get_object(id=status['id'], fields='message')
    print(post['message'])

    # feed = api.get_connections(id="me", connection_name="feed")
    # # post = feed["data"]
    # print(feed, 'post..')
    #

def get_api(cfg):
    graph = facebook.GraphAPI(cfg["access_token"])
    resp = graph.get_object('me/accounts')
    page_access_token = None

    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']

    graph = facebook.GraphAPI(page_access_token)
    # graph = facebook.GraphAPI(cfg['page_access_token'])

    return graph

if __name__=="__main__":
    main()
