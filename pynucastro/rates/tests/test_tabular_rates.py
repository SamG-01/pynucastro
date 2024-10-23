# unit tests for rates

import warnings

import pytest
from pytest import approx, raises

import pynucastro as pyna


class TestTabularRates:

    @pytest.fixture(scope="class")
    def rc_su(self, suzuki_library):
        return pyna.RateCollection(libraries=[suzuki_library])

    @pytest.fixture(scope="class")
    def rc_la(self, langanke_library):
        return pyna.RateCollection(libraries=[langanke_library])

    def test_rate_values_suzuki(self, rc_su):

        rho = 1.2e8
        T = 1.5e9

        comp_su = pyna.Composition(rc_su.get_nuclei())
        comp_su.set_all(1)
        comp_su.normalize()

        # this is generated by doing
        # rvals = rc_su.evaluate_rates(rho, T, comp_su)
        # for r in sorted(rvals, key=lambda r: r.fname):
        #     print(f"'{r.fname}': {rvals[r]},")

        stored_rates_su = {
            'Al23__Mg23': 0.0018356969491904495,
            'Al24__Mg24': 0.0010224143375329186,
            'Al25__Mg25': 0.0004742839102314945,
            'Al26__Mg26': 8.208195176601902e-06,
            'Al27__Mg27': 1.3548922253387587e-12,
            'Al28__Mg28': 2.82771853373719e-14,
            'Al28__Si28': 6.552181957939603e-07,
            'F17__O17': 0.0004964162849900655,
            'F18__O18': 0.00014752795061742893,
            'F19__O19': 1.4589243454067581e-18,
            'F20__Ne20': 4.575609904051387e-05,
            'F20__O20': 1.413854271576516e-15,
            'F21__Ne21': 0.0001131073690508162,
            'F21__O21': 3.123684503103512e-30,
            'F22__Ne22': 0.0001215897114169894,
            'F23__Ne23': 0.00023974141956359604,
            'Mg20__Na20': 0.005114821722250049,
            'Mg21__Na21': 0.0027551736679093503,
            'Mg22__Na22': 0.0013109707173084527,
            'Mg23__Na23': 0.0004219912985023772,
            'Mg24__Na24': 1.6598635700843666e-22,
            'Mg25__Na25': 8.591632561336034e-16,
            'Mg26__Na26': 8.68429638614793e-33,
            'Mg27__Al27': 1.361348911272524e-08,
            'Mg27__Na27': 8.723314871252093e-32,
            'Mg28__Al28': 3.336720258691769e-11,
            'Mg28__Na28': 2.8134798652347447e-48,
            'Na19__Ne19': 0.002449472490421163,
            'Na20__Ne20': 0.002428040325297442,
            'Na21__Ne21': 0.00037796168976840364,
            'Na22__Ne22': 8.135557391945126e-07,
            'Na23__Ne23': 1.1720011968249513e-17,
            'Na24__Mg24': 4.406876111298294e-07,
            'Na24__Ne24': 3.756853129605931e-12,
            'Na25__Mg25': 4.479044974800567e-06,
            'Na25__Ne25': 3.72540094885677e-27,
            'Na26__Mg26': 0.001022078977999804,
            'Na27__Mg27': 0.0017911484289089184,
            'Na28__Mg28': 0.009005626791070679,
            'Ne18__F18': 0.0022422277113142404,
            'Ne19__F19': 0.0006992986372563014,
            'Ne20__F20': 9.47646722208835e-26,
            'Ne21__F21': 2.715931312189591e-21,
            'Ne22__F22': 9.580760966938022e-40,
            'Ne23__F23': 1.6479178669188904e-31,
            'Ne23__Na23': 9.3540132273414e-06,
            'Ne24__Na24': 1.0429568596930843e-07,
            'Ne25__Na25': 0.0007774750136737904,
            'O17__F17': 2.992303848236561e-23,
            'O18__F18': 6.178789007042831e-23,
            'O19__F19': 1.4762829483676722e-05,
            'O20__F20': 1.1564141869489023e-05,
            'O21__F21': 0.0001140275780950444,
            'P27__Si27': 0.0017552224872207786,
            'P28__Si28': 0.0011558955780814398,
            'S28__P28': 0.0025226735211831297,
            'Si24__Al24': 0.002836345548021039,
            'Si25__Al25': 0.0018713317001937818,
            'Si26__Al26': 0.0012411477482899727,
            'Si27__Al27': 0.0004907519533774708,
            'Si28__Al28': 3.1330669347239767e-18,
        }

        ys_su = comp_su.get_molar()

        # the individual rate is
        # r = Y(reactant) * table_value

        for r in rc_su.get_rates():
            rr = ys_su[r.reactants[0]] * r.eval(T, rho=rho, comp=comp_su)
            if r.fname in stored_rates_su:
                assert rr == approx(stored_rates_su[r.fname], rel=1.e-6, abs=1.e-100), f"rate: {r} does not agree"
            else:
                warnings.warn(UserWarning(f"missing Suzuki tests for tabular rate {r}"))

    def test_rate_values_langanke(self, rc_la):

        rho = 1.2e8
        T = 1.5e9

        comp_la = pyna.Composition(rc_la.get_nuclei())
        comp_la.set_all(1)
        comp_la.normalize()

        # this is generated by doing
        # rvals = rc_la.evaluate_rates(rho, T, comp_la)
        # for r in sorted(rvals, key=lambda r: r.fname):
        #     print(f"'{r.fname}': {rvals[r]},")

        stored_rates_la = {
            'Ca45__Sc45': 4.855704922199137e-16,
            'Ca46__Sc46': 1.5522740355394187e-20,
            'Ca47__Sc47': 1.5747941882298966e-12,
            'Ca48__Sc48': 1.6946455891576352e-19,
            'Ca49__Sc49': 1.1521390705403127e-08,
            'Ca50__Sc50': 2.4502356056441734e-06,
            'Ca51__Sc51': 8.85909262069812e-06,
            'Co54__Fe54': 0.0002705235253373661,
            'Co55__Fe55': 9.5652557631686e-07,
            'Co55__Ni55': 4.613845979541839e-42,
            'Co56__Fe56': 2.6071179447027625e-07,
            'Co56__Ni56': 1.011055955423377e-21,
            'Co57__Fe57': 2.9043236806438992e-08,
            'Co57__Ni57': 7.432314436280484e-25,
            'Co58__Fe58': 3.3573965600085414e-08,
            'Co58__Ni58': 5.576648379700194e-15,
            'Co59__Fe59': 8.343639289664051e-12,
            'Co59__Ni59': 1.2622970145148682e-18,
            'Co60__Fe60': 1.5237728690386513e-10,
            'Co60__Ni60': 1.3868527094318867e-09,
            'Co61__Fe61': 1.8548010283318373e-17,
            'Co61__Ni61': 1.8011446043723412e-11,
            'Co62__Fe62': 4.506358431873026e-13,
            'Co62__Ni62': 6.466492473123774e-07,
            'Co63__Fe63': 1.048906247594336e-24,
            'Co63__Ni63': 1.376607699983757e-06,
            'Co64__Fe64': 4.044474852574769e-19,
            'Co64__Ni64': 0.00013627811552984132,
            'Co65__Ni65': 4.957151531534562e-05,
            'Cr45__V45': 0.0046698196947193025,
            'Cr46__V46': 0.001499489363639145,
            'Cr47__V47': 0.0006899831256383501,
            'Cr48__V48': 7.571352114071061e-06,
            'Cr49__Mn49': 7.433738901148172e-39,
            'Cr49__V49': 7.386078531165092e-06,
            'Cr50__Mn50': 2.1428080220384474e-38,
            'Cr50__V50': 5.067980095340174e-09,
            'Cr51__Mn51': 5.066529843884422e-25,
            'Cr51__V51': 2.8117767495413197e-07,
            'Cr52__Mn52': 3.103513880893331e-29,
            'Cr52__V52': 3.670221541615632e-16,
            'Cr53__Mn53': 3.8263316970390884e-17,
            'Cr53__V53': 1.3387987573919933e-14,
            'Cr54__Mn54': 1.013667316700379e-18,
            'Cr54__V54': 6.665222632236972e-26,
            'Cr55__Mn55': 7.256665061517085e-08,
            'Cr55__V55': 1.2831282118471635e-22,
            'Cr56__Mn56': 9.794964605213119e-10,
            'Cr56__V56': 6.121316564807127e-32,
            'Cr57__Mn57': 3.03357436763274e-06,
            'Cr57__V57': 3.959576224384351e-29,
            'Cr58__Mn58': 5.01523744527494e-06,
            'Cr58__V58': 8.675910303654274e-40,
            'Cr59__Mn59': 0.00010275108129222282,
            'Cr60__Mn60': 0.00017137413392307195,
            'Cu58__Ni58': 0.00017784848747368512,
            'Cu59__Ni59': 1.683477878625942e-05,
            'Cu60__Ni60': 6.785687080176845e-06,
            'Cu60__Zn60': 2.120862865885726e-28,
            'Cu61__Ni61': 3.8144240685512e-06,
            'Cu61__Zn61': 2.8392166452009976e-32,
            'Cu62__Ni62': 2.295908681423182e-06,
            'Cu62__Zn62': 6.878369678534576e-21,
            'Cu63__Ni63': 4.4889388627755914e-08,
            'Cu63__Zn63': 1.3376725011997922e-25,
            'Cu64__Ni64': 8.248814184399841e-07,
            'Cu64__Zn64': 6.947648680351284e-14,
            'Cu65__Ni65': 2.4753401580387368e-11,
            'Cu65__Zn65': 2.0405971409944253e-19,
            'Fe52__Mn52': 4.787219355322723e-06,
            'Fe53__Mn53': 8.389340266943337e-06,
            'Fe54__Co54': 2.898133536915984e-40,
            'Fe54__Mn54': 1.8410238166940182e-10,
            'Fe55__Co55': 4.566820525297116e-25,
            'Fe55__Mn55': 3.2502661955127306e-08,
            'Fe56__Co56': 1.2332566030348113e-28,
            'Fe56__Mn56': 1.46122831525815e-15,
            'Fe57__Co57': 3.611408875082576e-18,
            'Fe57__Mn57': 1.2218402907704675e-12,
            'Fe58__Co58': 1.053053591138989e-21,
            'Fe58__Mn58': 3.46194799861307e-23,
            'Fe59__Co59': 3.125054149873378e-11,
            'Fe59__Mn59': 2.479534123059382e-20,
            'Fe60__Co60': 3.9680395271644945e-15,
            'Fe60__Mn60': 4.947356914548806e-30,
            'Fe61__Co61': 2.0156123610846696e-07,
            'Fe61__Mn61': 2.5197439739383014e-26,
            'Fe62__Co62': 4.5286789636822494e-08,
            'Fe63__Co63': 8.502332999827177e-06,
            'Fe64__Co64': 3.427116675529298e-05,
            'Ga62__Zn62': 0.0011622096439144766,
            'Ga63__Zn63': 3.878609018769381e-05,
            'Ga64__Ge64': 1.0811747982562144e-29,
            'Ga64__Zn64': 1.9023595580300654e-05,
            'Ga65__Ge65': 1.114548307480868e-34,
            'Ga65__Zn65': 6.37651584721512e-06,
            'Ge64__Ga64': 2.8541864580127472e-05,
            'Ge65__Ga65': 4.5634622740133776e-05,
            'Mn49__Cr49': 0.0007366727091328324,
            'Mn50__Cr50': 0.0003320708504027954,
            'Mn51__Cr51': 2.990364258374366e-06,
            'Mn52__Cr52': 6.294704049658e-07,
            'Mn52__Fe52': 4.9550651949748136e-23,
            'Mn53__Cr53': 2.593741082296412e-08,
            'Mn53__Fe53': 1.6197172776864845e-26,
            'Mn54__Cr54': 2.6804293397015252e-08,
            'Mn54__Fe54': 5.915912286093991e-14,
            'Mn55__Cr55': 4.690827616959843e-13,
            'Mn55__Fe55': 3.1786876316835767e-16,
            'Mn56__Cr56': 2.006277538772467e-10,
            'Mn56__Fe56': 1.6654682313995537e-07,
            'Mn57__Cr57': 1.4902073258602157e-20,
            'Mn57__Fe57': 1.3529256470820917e-07,
            'Mn58__Cr58': 1.386874163298365e-17,
            'Mn58__Fe58': 7.212896806066104e-06,
            'Mn59__Cr59': 1.055975482576685e-28,
            'Mn59__Fe59': 9.193634624183979e-06,
            'Mn60__Cr60': 1.1543026476741542e-23,
            'Mn60__Fe60': 0.0002523175757511599,
            'Mn61__Fe61': 0.0002405893758526718,
            'Ni55__Co55': 0.001092971896532629,
            'Ni56__Co56': 2.7460336176477442e-06,
            'Ni57__Co57': 1.4297847059934802e-06,
            'Ni58__Co58': 1.5073472828636503e-09,
            'Ni58__Cu58': 1.9261419599572421e-41,
            'Ni59__Co59': 9.204452012861679e-08,
            'Ni59__Cu59': 6.0375091231382575e-30,
            'Ni60__Co60': 3.0447610267041136e-14,
            'Ni60__Cu60': 1.330246078621377e-33,
            'Ni61__Co61': 2.0629665785991204e-09,
            'Ni61__Cu61': 1.3980690264558952e-22,
            'Ni62__Co62': 1.8156900147676334e-20,
            'Ni62__Cu62': 2.5197407113074367e-27,
            'Ni63__Co63': 1.0423029600868452e-15,
            'Ni63__Cu63': 2.1613603971935713e-15,
            'Ni64__Co64': 2.0080238344541994e-26,
            'Ni64__Cu64': 3.4861182695749173e-20,
            'Ni65__Co65': 9.94953222887641e-23,
            'Ni65__Cu65': 5.151947984134186e-09,
            'Sc45__Ca45': 1.4249560465402422e-08,
            'Sc45__Ti45': 1.971444692845618e-21,
            'Sc46__Ca46': 2.0409046852200486e-09,
            'Sc46__Ti46': 1.641566581899633e-11,
            'Sc47__Ca47': 2.2040872232122854e-13,
            'Sc47__Ti47': 7.88273474642574e-14,
            'Sc48__Ca48': 1.118446910435972e-13,
            'Sc48__Ti48': 3.7929936224990936e-10,
            'Sc49__Ca49': 5.019112055724216e-22,
            'Sc49__Ti49': 1.0253057189009096e-09,
            'Sc50__Ca50': 9.815024110622622e-21,
            'Sc50__Ti50': 7.650556725134291e-07,
            'Sc51__Ca51': 1.0649754816967587e-27,
            'Sc51__Ti51': 4.887208059988256e-06,
            'Sc52__Ti52': 8.78873905865045e-06,
            'Ti45__Sc45': 4.616855683611821e-06,
            'Ti45__V45': 5.872939309482288e-37,
            'Ti46__Sc46': 5.867366817718865e-13,
            'Ti46__V46': 1.4496653582828003e-36,
            'Ti47__Sc47': 1.6548140491798895e-08,
            'Ti47__V47': 3.916164753248513e-24,
            'Ti48__Sc48': 5.830569043231174e-18,
            'Ti48__V48': 3.677401427897203e-27,
            'Ti49__Sc49': 1.5249852627304697e-11,
            'Ti49__V49': 5.810177720745907e-17,
            'Ti50__Sc50': 7.2002659684862e-26,
            'Ti50__V50': 6.578550245877096e-22,
            'Ti51__Sc51': 1.1499236782532747e-24,
            'Ti51__V51': 1.5507969328138803e-08,
            'Ti52__Sc52': 4.073435696668371e-32,
            'Ti52__V52': 1.6071233767121864e-08,
            'Ti53__V53': 8.254182130785463e-07,
            'Ti54__V54': 1.5829704749976513e-06,
            'Ti55__V55': 4.910700748333321e-05,
            'Ti56__V56': 0.0003639081657878419,
            'V45__Cr45': 2.484681743228909e-54,
            'V45__Ti45': 0.0005849436783209476,
            'V46__Cr46': 3.9647014283670007e-38,
            'V46__Ti46': 0.0007232474633662782,
            'V47__Cr47': 5.457509736374555e-38,
            'V47__Ti47': 5.8837546770481e-06,
            'V48__Cr48': 8.677545859282911e-21,
            'V48__Ti48': 1.7181574998064635e-06,
            'V49__Cr49': 3.106152897610862e-23,
            'V49__Ti49': 5.103636011700232e-08,
            'V50__Cr50': 1.9511245942000273e-12,
            'V50__Ti50': 1.2347598384252832e-08,
            'V51__Cr51': 1.3496462612884804e-17,
            'V51__Ti51': 1.6564156694656686e-12,
            'V52__Cr52': 2.056124898394512e-07,
            'V52__Ti52': 2.9024820713256162e-11,
            'V53__Cr53': 3.876055239475765e-07,
            'V53__Ti53': 1.434760225852427e-20,
            'V54__Cr54': 3.457264637295427e-06,
            'V54__Ti54': 4.8619355857031675e-18,
            'V55__Cr55': 1.0180364624002767e-05,
            'V55__Ti55': 7.643454394259597e-28,
            'V56__Cr56': 0.0002038854997373826,
            'V56__Ti56': 7.026842584712173e-27,
            'V57__Cr57': 0.0002704636301270961,
            'V58__Cr58': 0.0005832894503875095,
            'Zn60__Cu60': 1.575204010868408e-05,
            'Zn61__Cu61': 1.6022144582326007e-05,
            'Zn62__Cu62': 4.910009858372687e-06,
            'Zn62__Ga62': 1.4835721381223987e-43,
            'Zn63__Cu63': 2.7450034291161515e-06,
            'Zn63__Ga63': 1.3112323974839515e-32,
            'Zn64__Cu64': 8.303524662605314e-08,
            'Zn64__Ga64': 3.5548473689954254e-37,
            'Zn65__Cu65': 1.875612071034173e-07,
            'Zn65__Ga65': 1.061812599757104e-25,
            'n__p': 8.687195028683885e-10,
            'p__n': 7.558870243248579e-05,
        }

        ys_la = comp_la.get_molar()

        # the individual rate is
        # r = Y(reactant) * table_value

        for r in rc_la.get_rates():
            rr = ys_la[r.reactants[0]] * r.eval(T, rho=rho, comp=comp_la)
            if r.fname in stored_rates_la:
                assert rr == approx(stored_rates_la[r.fname], rel=1.e-6, abs=1.e-100), f"rate: {r} does not agree"
            else:
                warnings.warn(UserWarning(f"missing Langanke tests for tabular rate {r}"))

    def test_nu_loss_values_suzuki(self, rc_su):

        rho = 1.2e9
        T = 1.5e9

        comp_su = pyna.Composition(rc_su.get_nuclei())
        comp_su.set_all(1)
        comp_su.normalize()

        # this is generated by doing
        #
        # for r in sorted(rc_su.rates, key=lambda r: r.fname):
        #     nu_loss_rate = r.get_nu_loss(T, rho*comp_su.ye)
        #     print(f"'{r.fname}': {nu_loss_rate},")

        stored_nu_loss_su = {
            'Al23__Mg23': 0.0004372874399337381,
            'Al24__Mg24': 0.0002444261479368015,
            'Al25__Mg25': 0.00011500170073365321,
            'Al26__Mg26': 2.0956240501428204e-06,
            'Al27__Mg27': 3.255106279693442e-11,
            'Al28__Mg28': 1.49477663243628e-11,
            'Al28__Si28': 3.831060797866789e-14,
            'F17__O17': 7.899054617378834e-05,
            'F18__O18': 2.5282475946235158e-05,
            'F19__O19': 1.093403227437941e-14,
            'F20__Ne20': 2.1240115337229592e-08,
            'F20__O20': 2.057038605088727e-12,
            'F21__Ne21': 4.983256254206788e-08,
            'F21__O21': 3.478821084686598e-26,
            'F22__Ne22': 1.0792505314678724e-07,
            'F23__Ne23': 3.5106676050488424e-07,
            'Mg20__Na20': 0.0011319135934955277,
            'Mg21__Na21': 0.0006340336907068992,
            'Mg22__Na22': 0.0002767982218577626,
            'Mg23__Na23': 9.610438271090285e-05,
            'Mg24__Na24': 1.8757107528850667e-18,
            'Mg25__Na25': 5.385813495789488e-12,
            'Mg26__Na26': 1.042881660253991e-28,
            'Mg27__Al27': 2.6083434105025398e-15,
            'Mg27__Na27': 1.0899697988607703e-27,
            'Mg28__Al28': 5.426292791567733e-18,
            'Mg28__Na28': 6.450491997157852e-44,
            'Na19__Ne19': 0.000493293000357844,
            'Na20__Ne20': 0.0005899195182275463,
            'Na21__Ne21': 7.599282323751405e-05,
            'Na22__Ne22': 2.2006497168948355e-07,
            'Na23__Ne23': 1.2578502390300712e-13,
            'Na24__Mg24': 3.93370337581875e-10,
            'Na24__Ne24': 1.9814147087010928e-10,
            'Na25__Mg25': 2.6657308423828652e-11,
            'Na25__Ne25': 4.5166273695294323e-23,
            'Na26__Mg26': 5.681065910388462e-06,
            'Na27__Mg27': 7.802299251728987e-06,
            'Na28__Mg28': 9.465293245065728e-05,
            'Ne18__F18': 0.0003974021604949035,
            'Ne19__F19': 0.0001252832096143487,
            'Ne20__F20': 9.695265306659568e-22,
            'Ne21__F21': 2.923719748936441e-17,
            'Ne22__F22': 1.0542944818300268e-35,
            'Ne23__F23': 1.9118167540106322e-27,
            'Ne23__Na23': 4.3009430056097873e-10,
            'Ne24__Na24': 4.472165318443309e-17,
            'Ne25__Na25': 1.7531245231618863e-06,
            'O17__F17': 1.5965647193812905e-32,
            'O18__F18': 1.6695331795511284e-33,
            'O19__F19': 1.3591873287418124e-09,
            'O20__F20': 1.8668550656057127e-13,
            'O21__F21': 1.0304477129326074e-07,
            'P27__Si27': 0.0004940585002600768,
            'P28__Si28': 0.0003484280237167292,
            'S28__P28': 0.0007818005881530282,
            'Si24__Al24': 0.0007522480887757669,
            'Si25__Al25': 0.0005089386787967424,
            'Si26__Al26': 0.00031462787988451046,
            'Si27__Al27': 0.00013141083163038222,
            'Si28__Al28': 9.226341626912568e-15,
        }

        for r in rc_su.get_rates():
            nu_loss = r.get_nu_loss(T, rho=rho, comp=comp_su)
            if r.fname in stored_nu_loss_su:
                assert nu_loss == approx(stored_nu_loss_su[r.fname], rel=1.e-6, abs=1.e-100), f"rate: {r} does not agree"
            else:
                warnings.warn(UserWarning(f"missing Suzuki tests for tabular nu loss rate {r}"))

    def test_bounds(self, rc_su):

        comp = pyna.Composition(rc_su.get_nuclei())
        comp.set_all(1)
        comp.normalize()

        r = rc_su.get_rates()[0]

        T = 1.e11
        rho = 1.e7

        with raises(ValueError):
            r.eval(T, rho=rho, comp=comp)

        rho = 1.e2

        with raises(ValueError):
            r.eval(T, rho=rho, comp=comp)
