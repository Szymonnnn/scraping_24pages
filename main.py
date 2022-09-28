def wyprintuj(output, i):
    print("Lines writen: " + str(int(len(output)/i)))

from scripts_for_pages.komunikaty_giff import KomunikatyGiff
output = KomunikatyGiff.scrap()
wyprintuj(output, 2)

from scripts_for_pages.uknf_sektor_bankowy import UknfSektorBaknowy
output2 = UknfSektorBaknowy.scrap()
wyprintuj(output2, 2)

from scripts_for_pages.komunikacja_komunikaty import KomunikacjaKomunikaty
output3 = KomunikacjaKomunikaty.scrap()
wyprintuj(output3, 2)

from scripts_for_pages.knf_aktualnosci import KnfAktualnosci
output4 = KnfAktualnosci.scrap()
wyprintuj(output4, 2)

from scripts_for_pages.nbp_komunikaty import NbpKomunikaty
output5 = NbpKomunikaty.scrap()
wyprintuj(output5, 2)

from scripts_for_pages.zbp_wydarzenia import ZbpWydarzenia
output6 = ZbpWydarzenia.scrap()
wyprintuj(output6, 2)

from scripts_for_pages.rf_gov import RfGov
output7 = RfGov.scrap()
wyprintuj(output7, 2)

from scripts_for_pages.aktualnosci_rzecznika_finansowego import AktualnosciRzecznikaFinansowego
output8 = AktualnosciRzecznikaFinansowego.scrap()
wyprintuj(output8, 2)

from scripts_for_pages.nbp_nadzor import NbpNadzor
output9 = NbpNadzor.scrap()
wyprintuj(output9, 2)

from scripts_for_pages.bankowy_fundusz_gwarancyjny import BankowyFunduszGwarancyjny
output10 = BankowyFunduszGwarancyjny.scrap()
wyprintuj(output10, 2)

from scripts_for_pages.gpw_aktualnosci import GpwAktualnosci
output11 = GpwAktualnosci.scrap()
wyprintuj(output11, 2)

from scripts_for_pages.piu import Piu
output12 = Piu.scrap()
wyprintuj(output12, 2)

from scripts_for_pages.piu_rekomendacje import PiuRekomendacje
output13 = PiuRekomendacje.scrap()
wyprintuj(output13, 2)

from scripts_for_pages.piu_aktualnosci import PiuAktualnosci
output14 = PiuAktualnosci.scrap()
wyprintuj(output14, 2)

from scripts_for_pages.idm import Idm
output15 = Idm.scrap()
wyprintuj(output15, 2)

from scripts_for_pages.idm_aktualnosci_otc import IdmAktualnosciOtc
output16 = IdmAktualnosciOtc.scrap()
wyprintuj(output16, 2)

from scripts_for_pages.stanowiska_idm import StanowiskaIdm
output17 = StanowiskaIdm.scrap()
wyprintuj(output17, 2)

from scripts_for_pages.rf_sadu_najwyzszego import RfSaduNajwyzszego
output18 = RfSaduNajwyzszego.scrap()
wyprintuj(output18, 3)

from scripts_for_pages.nbp_publikacje import NbpPublikacje
output19 = NbpPublikacje.scrap()
wyprintuj(output19, 2)

from scripts_for_pages.kdpw_aktualnosci import KdpwAktualnosci
output20 = KdpwAktualnosci.scrap()
wyprintuj(output20, 2)

from scripts_for_pages.izfa_aktualnosci import IzfaAktualnosci
output21 = IzfaAktualnosci.scrap()
wyprintuj(output21, 2)

from scripts_for_pages.dziennik_urzedowy import DziennikUrzedowy
output22 = DziennikUrzedowy.scrap()
wyprintuj(output22, 2)

from scripts_for_pages.nbp_actbymonths import NbpActbymonths
output23 = NbpActbymonths.scrap()
wyprintuj(output23, 2)

from scripts_for_pages.gpw_komunikaty_uchwaly import GpwKomunikatyUchwaly
output24 = GpwKomunikatyUchwaly.scrap()
wyprintuj(output24, 2)

#wpisywanie do pliku xlsx
from xlsxwriter import Workbook

def write_to_xls(output, kol, wiersz, worksheet):
    for out in output:
        if kol%2+1 == 1:
            kolumna = 'A'
        if kol%2+1 ==2:
            kolumna = 'B'
        msc = kolumna +str(wiersz)

        worksheet.write(msc, out)

        kol += 1
        if kolumna == 'B':
            wiersz += 1
    #wiersz +=1
    kol=0
    return wiersz, kol

def write_to_xls_3(output, kol, wiersz, worksheet):
    for out in output:
        if kol%3+1 == 1:
            kolumna = 'A'
        if kol%3+1 == 2:
            kolumna = 'B'
        if kol%3+1 == 3:
            kolumna = 'C'
        msc = kolumna +str(wiersz)
        #print(msc)

        worksheet.write(msc, out)

        kol += 1
        if kolumna == 'C':
            wiersz += 1
    #wiersz +=1
    kol=0
    return wiersz, kol

import datetime
date_time = datetime.datetime.now()
date_time = date_time.strftime("%d%m%Y%H%M%S")
workbook_name = 'Output_' + str(date_time) + '.xlsx'
workbook_path = 'output/' + workbook_name
workbook = Workbook(workbook_path)
worksheet = workbook.add_worksheet()
kol = 0
wiersz = 1

wiersz, kol = write_to_xls(output, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output2, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output3, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output4, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output5, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output6, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output7, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output8, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output9, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output10, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output11, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output12, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output13, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output14, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output15, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output16, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output17, kol, wiersz, worksheet)
wiersz, kol = write_to_xls_3(output18, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output19, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output20, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output21, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output22, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output23, kol, wiersz, worksheet)
wiersz, kol = write_to_xls(output24, kol, wiersz, worksheet)

workbook.close()

print("Script in beta testing phase, please report any bugs")