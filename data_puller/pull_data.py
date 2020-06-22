from bs4 import BeautifulSoup
import urllib.request
from  selenium import webdriver
import time
import json





def get_org_links():
    url = 'https://westernu.campuslabs.ca/engage/organizations'
    driver = webdriver.PhantomJS('/mnt/c/Users/Vaskar/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)

    load_more = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/button")
    while True:
        try:
            load_more.click()
        except:
            break

    data = driver.page_source

    parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    soup = BeautifulSoup(data, parser)

    all_links = []

    for link in soup.find_all('a', href=True):
        if "/engage/organization" in link['href']:
            all_links.append(link['href'])

    return all_links

def get_org_data(links):
    i = 1
    result = {}
    for link in links:
        print("On Site ", i)
        url = "https://westernu.campuslabs.ca" + link
        driver = webdriver.PhantomJS('/mnt/c/Users/Vaskar/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.get(url)
        data = driver.page_source
        driver.close()
        parser = 'html.parser'
        soup = BeautifulSoup(data, parser)
        desc = ""

        for para in soup.find_all('p'):
            text = para.get_text()
            if "Home" in text or "Campus Labs 2020" in text:
                pass
            else:
                desc += text
        
        org_name = url[url.rfind('/') + 1 : ]
        result[org_name] = desc
        i += 1
    with open('../data/org_data.json', 'w') as fp:
        json.dump(result, fp)
        

if __name__ == "__main__":
    # result = get_org_links()
    result = ['/engage/organization/acapellaproject', '/engage/organization/activeminds', '/engage/organization/asua', '/engage/organization/aims', '/engage/organization/africanstudentsassociation', '/engage/organization/alsuwo', '/engage/organization/alzheimerswesternclub', '/engage/organization/amnestyinternationalatwestern', '/engage/organization/anthropologysociety', '/engage/organization/arabstudentsassociation', '/engage/organization/asianchristianfellowship', '/engage/organization/associationofinternationalrelations', '/engage/organization/associationofroleplayers', '/engage/organization/autismwestern', '/engage/organization/automotivesociety', '/engage/organization/bangladesh', '/engage/organization/bestbuddies', '/engage/organization/beyondthebooks', '/engage/organization/bicyclesafety', '/engage/organization/bsa', '/engage/organization/boardgames', '/engage/organization/breakdancingclub', '/engage/organization/crown', '/engage/organization/caisa', '/engage/organization/carrm', '/engage/organization/canadianfeedthechildren', '/engage/organization/canadian-italianawarenessorganization', '/engage/organization/cjpme', '/engage/organization/cancerawarenesssociety', '/engage/organization/canfar', '/engage/organization/capitalmarkets', '/engage/organization/cso', '/engage/organization/chambermusic', '/engage/organization/charitychords', '/engage/organization/chess', '/engage/organization/chinesechristianclub', '/engage/organization/chineseculturalgames', '/engage/organization/csauwo', '/engage/organization/clashroyalewestern', '/engage/organization/cas', '/engage/organization/croatianclub', '/engage/organization/mossa', '/engage/organization/danceforce-uwo', '/engage/organization/decauwestern', '/engage/organization/dignitasyouth', '/engage/organization/dukeofed', '/engage/organization/darmy', '/engage/organization/electronicgamingassociation', '/engage/organization/empower', '/engage/organization/envelopeforjoy', '/engage/organization/enviro', '/engage/organization/eim', '/engage/organization/HBAA', '/engage/organization/ahsc', '/engage/organization/DentalStudents', '/engage/organization/education', '/engage/organization/fhssc', '/engage/organization/Hippo', '/engage/organization/FIMS', '/engage/organization/facultyoflaw', '/engage/organization/Music', '/engage/organization/facultysocialsciencestudentscouncil', '/engage/organization/Engineering', '/engage/organization/ScienceSC', '/engage/organization/fashionandlifestylesociety', '/engage/organization/fjc', '/engage/organization/frenchclub', '/engage/organization/friendsofmedecinssansfrontieres', '/engage/organization/germanclub', '/engage/organization/gccuwo', '/engage/organization/gujarati', '/engage/organization/habitatforhumanity', '/engage/organization/hanvoice', '/engage/organization/hosa', '/engage/organization/HealthStudies', '/engage/organization/heartandstrokeclub', '/engage/organization/hellenicsociety', '/engage/organization/hillel', '/engage/organization/hindustudentsassociation', '/engage/organization/hiphopwestern', '/engage/organization/historysociety', '/engage/organization/firstnationsstudentassociation', '/engage/organization/ismailistudentsassociation', '/engage/organization/israeloncampus', '/engage/organization/japanesecultureclub', '/engage/organization/jugglersclub', '/engage/organization/kidneyclubofwestern', '/engage/organization/google', '/engage/organization/knittingsociety', '/engage/organization/westernkcf', '/engage/organization/koreanstudentsassociation', '/engage/organization/londonbrigdes', '/engage/organization/londonchinesecatholiccommunity', '/engage/organization/magic', '/engage/organization/miss', '/engage/organization/modelunitednationssociety', '/engage/organization/moviesandvideos', '/engage/organization/mswestern', '/engage/organization/musicbox', '/engage/organization/muslimstudentsassociation', '/engage/organization/newmancatholicstudents', '/engage/organization/novascientia-newscience', '/engage/organization/Nursing', '/engage/organization/ohm', '/engage/organization/operationsmilestudentsassociation', '/engage/organization/OrganAdvocacyInitiative', '/engage/organization/oxfamwestern', '/engage/organization/pakistanistudentsassociation', '/engage/organization/palestinian', '/engage/organization/paperartclub', '/engage/organization/polishstudentsunion', '/engage/organization/psa', '/engage/organization/campusforchrist', '/engage/organization/pbsn', '/engage/organization/pre-dentalsociety', '/engage/organization/pre-lawsociety', '/engage/organization/premed', '/engage/organization/pre-optometryclub', '/engage/organization/pre-pharmacy', '/engage/organization/pre-vet', '/engage/organization/purplespursociety', '/engage/organization/purpleyogis', '/engage/organization/righttoplay', '/engage/organization/romanian', '/engage/organization/rotaract', '/engage/organization/runwithus', '/engage/organization/makingwaveslondon', '/engage/organization/salsa', '/engage/organization/savethechildren', '/engage/organization/seniorsinit', '/engage/organization/smartsolutions', '/engage/organization/ssauwo', '/engage/organization/ssa', '/engage/organization/sonicart', '/engage/organization/southeastasianassociation', '/engage/organization/spacesocietyoflondon', '/engage/organization/spectrum', '/engage/organization/spokenword', '/engage/organization/srilanka', '/engage/organization/studentsfightparkinsons', '/engage/organization/swingkids', '/engage/organization/uwotaw', '/engage/organization/tamilstudentsassociation', '/engage/organization/teaclub', '/engage/organization/tbc', '/engage/organization/thebutterflyeffect', '/engage/organization/comedyclub', '/engage/organization/ccw', '/engage/organization/skisnowboard', '/engage/organization/thewell', '/engage/organization/transitionaljusticeclub', '/engage/organization/trekforteens', '/engage/organization/ukrainianstudentsclub', '/engage/organization/unicefwestern', '/engage/organization/alliedmedicine', '/engage/organization/uwohksa', '/engage/organization/westernusc', '/engage/organization/uwochoir', '/engage/organization/conservatives', '/engage/organization/redcrosssociety', '/engage/organization/mbs', '/engage/organization/uwowv', '/engage/organization/vegansociety', '/engage/organization/vietnamesestudentsassociation', '/engage/organization/wawestern', '/engage/organization/freethechildren', '/engage/organization/weball', '/engage/organization/accounting', '/engage/organization/waid', '/engage/organization/animevideoexplosion', '/engage/organization/artclub', '/engage/organization/aviationsociety', '/engage/organization/billiards', '/engage/organization/wbc', '/engage/organization/climbingclub', '/engage/organization/coffeeclub', '/engage/organization/craftingforacure', '/engage/organization/westerncrypto', '/engage/organization/wdc', '/engage/organization/westerndiabetesassociation', '/engage/organization/wfa', '/engage/organization/fitnessassociation', '/engage/organization/kitchenanddiningroom', '/engage/organization/westernforooch', '/engage/organization/westernforelderly', '/engage/organization/forexassociation', '/engage/organization/foundersnetwork', '/engage/organization/wgc', '/engage/organization/hockey', '/engage/organization/wicsa', '/engage/organization/investmentclub', '/engage/organization/westernliberals', '/engage/organization/lifelinewestern', '/engage/organization/mealexchange', '/engage/organization/woof', '/engage/organization/photographyclub', '/engage/organization/wps', '/engage/organization/WPA', '/engage/organization/punjabi', '/engage/organization/wrec', '/engage/organization/signlanguage', '/engage/organization/wssa', '/engage/organization/soccerassociation', '/engage/organization/wsbc', '/engage/organization/wsac', '/engage/organization/stemcell', '/engage/organization/strength', '/engage/organization/wtaa', '/engage/organization/westerntrivia', '/engage/organization/lsa', '/engage/organization/ppe', '/engage/organization/wutr', '/engage/organization/wva', '/engage/organization/wwil', '/engage/organization/marketingassoc', '/engage/organization/wildlifeconservationsociety', '/engage/organization/wif', '/engage/organization/womenstem', '/engage/organization/worlduniversityserviceofcanada', '/engage/organization/youngtutors', '/engage/organization/zua']
    get_org_data(result)
    print(len(result))
    print(result)

