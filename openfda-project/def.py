def companies_list():
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    data = self.path.strip('/search?')
    limit = data[0].split('=')[1]
    print("client has succesfully made a request")
    url = "/drug/label.json?limit=" + limit
    print(url)
    conn.request("GET", url, None, headers)
    r1 = conn.getresponse()
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)

    drug = []
    a = 0
    nlimit = int(limit)
    intro = "<head>" + '<h1>' + "Here is your drug default list" + '<body style="background-color:snow;">' + '</h1>' + '</head>'
    sd = "<ol>"

    while a < nlimit:
        try:
            drug.append(repos['results'][a]['openfda']['brand_name'][0])
            a += 1

        except:
            a += 1
            print("There is no drug with this active ingredient")

    with open("trial4.html", "w") as f:
        f.write(intro)
        f.write(sd)
        for el in drug:
            el_1 = "<t>" + "<li>" + el
            f.write(el_1)