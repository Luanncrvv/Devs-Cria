from playwright.sync_api import sync_playwright
from PIL import Image

with sync_playwright() as p:
    browser = p.chromium.launch()
    # browser = p.chromium.launch(headless=False) #para aparecer o navegador
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto("https://br.op.gg/summoners/br/salamandralw/ingame")

    page.wait_for_timeout(4000)

    # time azul

    AzulUm = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(1) > td.summoner-name > a")
    AzulUmElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(1) > td.current-rank > div")

    AzulDois = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(2) > td.summoner-name > a")
    AzulDoisElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(2) > td.current-rank > div")

    AzulTres = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(3) > td.summoner-name > a")
    AzulTresElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(3) > td.current-rank > div")

    AzulQuatro = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(4) > td.summoner-name > a")
    AzulQuatroElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(4) > td.current-rank > div")

    AzulCinco = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(5) > td.summoner-name > a")
    AzulCincoElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-v0lkwc.e1snzzz71 > tbody > tr:nth-child(5) > td.current-rank > div")

    # time vermelho

    VermelhoUm = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(1) > td.summoner-name > a")
    VermelhoUmElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(1) > td.current-rank > div")

    VermelhoDois = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(2) > td.summoner-name > a")
    VermelhoDoisElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(2) > td.current-rank > div")

    VermelhoTres = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(3) > td.summoner-name > a")
    VermelhoTresElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(3) > td.current-rank > div")

    VermelhoQuatro = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(4) > td.summoner-name > a")
    VermelhoQuatroElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(4) > td.current-rank > div")

    VermelhoCinco = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(5) > td.summoner-name > a")
    VermelhoCincoElo = page.query_selector("#__next > div.css-1n276kj.eafu1dm0 > div.css-yspf3p.e1k2e1zv5 > table.css-18rus4b.e1snzzz71 > tbody > tr:nth-child(5) > td.current-rank > div")

    AzulUm_ = (AzulUm.inner_html()); AzulUmElo_ = (AzulUmElo.inner_html())

    AzulDois_ = (AzulDois.inner_html()); AzulDoisElo_ = (AzulDoisElo.inner_html())

    AzulTres_ = (AzulTres.inner_html()); AzulTresElo_ = (AzulTresElo.inner_html())

    AzulQuatro_ = (AzulQuatro.inner_html()); AzulQuatroElo_ = (AzulQuatroElo.inner_html())

    AzulCinco_ = (AzulCinco.inner_html()); AzulCincoElo_ = (AzulCincoElo.inner_html())

    VermelhoUm_ = (VermelhoUm.inner_html()); VermelhoUmElo_ = (VermelhoUmElo.inner_html())

    VermelhoDois_ = (VermelhoDois.inner_html()); VermelhoDoisElo_ = (VermelhoDoisElo.inner_html())

    VermelhoTres_ = (VermelhoTres.inner_html()); VermelhoTresElo_ = (VermelhoTresElo.inner_html())

    VermelhoQuatro_ = (VermelhoQuatro.inner_html()); VermelhoQuatroElo_ = (VermelhoQuatroElo.inner_html())

    VermelhoCinco_ = (VermelhoCinco.inner_html()); VermelhoCincoElo_ = (VermelhoCincoElo.inner_html())

    times = (f'Time Azul: \n \n {AzulUm_} - {AzulUmElo_} \n {AzulDois_} - {AzulDoisElo_}\n {AzulTres_} - {AzulTresElo_}\n {AzulQuatro_} - {AzulQuatroElo_}\n {AzulCinco_} - {AzulCincoElo_}\n\n Time Vermelho: \n \n {VermelhoUm_} - {VermelhoUmElo_} \n {VermelhoDois_} - {VermelhoDoisElo_} \n {VermelhoTres_} - {VermelhoTresElo_} \n {VermelhoQuatro_} - {VermelhoQuatroElo_} \n {VermelhoCinco_} - {VermelhoCincoElo_}')


    page.locator("div.css-yspf3p.e1k2e1zv5").screenshot(path="Game\WebScrapingPartida\AOVIVOPartida.png")

    print(times)