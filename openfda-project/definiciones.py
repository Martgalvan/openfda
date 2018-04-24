

def active_ingredient(drug,limit):
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    print("client has succesfully made a request")
    conn.request("GET", "/drug/label.json?search=active_ingredient::%s&limit=%s" % (drug, limit), None, headers)
    r1 = conn.getresponse()
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    with open('send_info','w'):
        self.wfile.write(bytes('<html><head><h1>OpenFDA Application</h1><h2>you have searched for %.YOu have %' % (drug, limit)), "utf8")

        for i in range(len(repos['results'])):
            try:
                for n in range(len(repos['results'][i]["openfda"]["brand_name"])):
                    try:
                        self.wfile.write(bytes('<li>'+ 'the active ingredient is'+repos['results'][i]["openfda"]["brand_name"][0] + "</li>", "utf8"))
                    except KeyError:
                        break
