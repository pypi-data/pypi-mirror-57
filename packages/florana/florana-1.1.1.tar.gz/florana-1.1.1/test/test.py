import re

loc_text_pattern = re.compile(r'0[\)\]]?\s+?m;.*?\..*?\n', re.DOTALL)
#pattern = re.compile(r'(0[\)\]]?\s+?m;)', re.DOTALL)
s = """6. Merremia quinquefolia (Linnaeus) Hallier f., Bot.
Jahrb. Syst. 16: 552. 1893 * Rock rosemary
Ipomoea quinquefolia Linnaeus, Sp. Pl. 1: 162. 1753

Page 3 of 3
22 Nov 2019

Merremia05e_map (Austin) - Convolvulaceae
Volume 14

TaxEd: Strother
TechEd: MASchmidt

Stems glabrous.
Leaf blades +/- orbiculate to
polygonal, palmately compound, 15--50 x 25--70 mm,
(3--)5(--7)-foliolate; leaflets elliptic or lanceolate to
oblanceolate, margins remotely serrate to subentire,
surfaces glabrous. Inflorescences 3--9-flowered cymes
or compound cymes or flowers solitary. Flowers:
sepals oblong, outer 3--5 mm, inner 4--7 mm, apex
obtuse, abaxial surface glabrous; corolla white, 15--25
mm, glabrous.
Flowering Dec--Jun. Pinelands, disturbed sites; 0-10[--1500] m; Fla.; West Indies; Central America;
South America; introduced in Old World subtropics
and tropics.

Page 4 of 4
22 Nov 2019

Merremia05e_map (Austin) - Convolvulaceae
Volume 14

TaxEd: Strother
TechEd: MASchmidt

Page 5 of 5
22 Nov 2019

Other Reference
Samões, A. R. and G. W. Staples. 2017. Dissolution of Convolulaceae tribe Merremieae and a
new classification of the constituent genera. Bot. J. Linn. Soc. 183: 561--586.

Merremia05e_map (Austin) - Convolvulaceae
Volume 14

Aguinaldo amarillo, 2
Alamo vine, 2
Austin, D. F., 1
Camonea
umbellata, 1
Convolvulus
cissoides, 3
dissectus, 2
umbellatus, 2
Distimake
aegyptia, 1
cissoides, 1
dissectus, 1
quinquefolius, 1
tuberosus, 1
Hairy wood-rose, 3
Ipomoea
aegyptia, 3
polyanthes, 2
quinquefolia, 4
sinuata, 2

TaxEd: Strother
TechEd: MASchmidt

tuberosa, 3
Merremia, 1
aegyptia, 1, 3
cissoides, 1, 3
dissecta, 1, 2
hastata, 1
quinquefolia, 1, 2, 4
tridentata, 1
tuberosa, 1, 3
umbellata, 1, 2
Noyau vine, 2
Operculina
dissecta, 2
tuberosa, 3
Roadside wood-rose, 3
Rock rosemary, 4
Samões, A. R., 1
Staples, G. W., 1
Strother, J. L., 1

Page 6 of 6
22 Nov 2019

Merremia05e_map (Austin) - Convolvulaceae
Volume 14

TaxEd: Strother
TechEd: MASchmidt

Page 7 of 7
22 Nov 2019

Tracking Sheet:
02/09/12
03/22/12
11/03/15
08/19/16
08/25/16
03/06/17
03/07/17
12/14/17
03/14/17
03/15/17
03/21/17
09/26/17
03/26/18
05/04/18
06/15/18
08/21/18
10/23/18
10/26/18
01/14/19
04/10/19
05/07/19
05/07/19
05/07/19
05/15/19
11/22/19

Received 2-6-12; initially formatted; saved as 02a.
Incorporated Zarucchi changes/comments; saved as 02b.
Created 02rev.
Incorporated HSchmidt changes/comments; saved as 02c.
Incorporated SC review comments; saved as 03a.
Strother revision began.
Strother revision continued (through 9/22/17).
Strother revisions made in response to reviews.
Received revised version from Strother.
Incorporated Strother changes; saved as 03b.
Incorporated Biblio 1 changes; saved as 03c.
Incorporated Strother changes; saved as 03d.
Incorporated Strother additions; saved as 03e.
Tech edited, compared to key to genera, checked CFW; saved as 03f.
Incorporated TaxEd changes; saved as 03g.
Incorporated Kanchi’s changes; saved as 04a.
Incorporated Biblio 2 changes; saved as 04b.
Tech edit 2; saved as 04c.
Incorporated Zarucchi changes; saved as 04d.
Read through; saved as 05a.
Cleaned up spacing; saved as 05b.CH.
Indexed; saved as 05c.CH.
Applied galley formatting; saved as 05d.CH.
Changed font to Sabon, accepted changes; saved as 05e.
Saved as PDF (05e_map); sent to Geoff Levin to make maps.




"""

print(loc_text_pattern.findall(s))
