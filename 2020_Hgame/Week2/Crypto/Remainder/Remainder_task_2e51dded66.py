#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Util import number
from secret import msg

assert 256 < len(msg) < 384

p, q, r = [number.getPrime(1024) for _ in range(3)]
# p = 94598296305713376652540411631949434301396235111673372738276754654188267010805522542068004453137678598891335408170277601381944584279339362056579262308427544671688614923839794522671378559276784734758727213070403838632286280473450086762286706863922968723202830398266220533885129175502142533600559292388005914561
# q = 150088216417404963893679242888992998793257903343994792697939121738029477790454833496600101388493792476973514786401036309378542808470513073408894727406158296404360452232777491992630316999043165374635001806841520490997788796152678742544032835808854339130676283497122770901196468323977265095016407164510827505883
# r = 145897736096689096151704740327665176308625097484116713780050311198775607465862066406830851710261868913835866335107146242979359964945125214420821146670919741118254402096944139483988745450480989706524191669371208210272907563936516990473246615375022630708213486725809819360033470468293100926616729742277729705727

m = number.bytes_to_long(msg)
e = 65537
for prime in [p, q, r]:
    print( pow(m, e, prime) )

# 78430786011650521224561924814843614294806974988599591058915520397518526296422791089692107488534157589856611229978068659970976374971658909987299759719533519358232180721480719635602515525942678988896727128884803638257227848176298172896155463813264206982505797613067215182849559356336015634543181806296355552543 
# 49576356423474222188205187306884167620746479677590121213791093908977295803476203510001060180959190917276817541142411523867555147201992480220531431019627681572335103200586388519695931348304970651875582413052411224818844160945410884130575771617919149619341762325633301313732947264125576866033934018462843559419 
# 48131077962649497833189292637861442767562147447040134411078884485513840553188185954383330236190253388937785530658279768620213062244053151614962893628946343595642513870766877810534480536737200302699539396810545420021054225204683428522820350356470883574463849146422150244304147618195613796399010492125383322922
