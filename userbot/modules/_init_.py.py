# Copyright (C) 2020 z2sofwares - BristolMyers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# BristolMyers tarafından hazırlanmıştır

from random import choice
from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DOGRULUK_STRINGS = [
    "**✨En büyük ve pişman olduğun kötülüğün neyle alakalı idi?\n®️CeteUserBot✔**",
    "**✨Hiç kimsenin bilmediği bir şeyini bana söyler misin?\n®️CeteUserBot✔**",
    "**✨En çok utandığın an ne zamandı?\n®️CeteUserBot✔**",
    "**✨En son neden ağladın?\n®️CeteUserBot✔**",
    "**✨Hayatta olmazsa olmaz dediğin aşırılık durumuna bir tane örnek verir misin?\n®️CeteUserBot✔**",
    "**✨En çaresiz anında kimi aradın?\n®️CeteUserBot✔**",
    "**✨Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)\n®️CeteUserBot✔**",
    "**✨Diyelim bilgi yarışmasında ödül kazandın, karşılığında üç gezi biletin var bunlar; Brezilya/ San Francisco ve Tokyo. Tercihin hangisi olurdu?\n®️CeteUserBot✔**",
    "**✨Deseler ki sana “geçmişte bir anı seç ve seni oraya döndüreceğiz” Tekrar yaşamak istediğin an nedir?\n®️CeteUserBot✔**",
    "**✨İç çamaşarı giyiyor musun?\n®️CeteUserBot✔**",
    "**✨Bu gruptakiler arasında sır tutma  konusunda en çok zorlanan kişi kimdir?\n®️CeteUserBot✔**",
    "**✨Yapıpta tamamen utanç duyduğun birşeyden bahset.\n®️CeteUserBot✔**",
    "**✨Vücudunun en çok hangi tarafıyla gurur duyuyorsun?\n®️CeteUserBot✔**",
    "**✨En kötü alışkanlığın nedir?\n®️CeteUserBot✔**",
    "**✨Bu gruptaki birini kölen olarak alabilme şansın olsaydı, kim olurdu ve ne yapmasını isterdin?\n®️CeteUserBot✔**",
    "**✨Sana kendini ne güvensiz hissettirir?\n®️CeteUserBot✔**",
    "**✨En büyük kusurun nedir?\n®️CeteUserBot✔**",
    "**✨Hayatında yaptığın en büyük hata nedir?\n®️CeteUserBot✔**",
    "**✨Daha önce karşı cinsten birine iç çamaşırı aldığın oldu mu?\n®️CeteUserBot✔**",
    "**✨Gruba senden önce mesaj atan kişiyi öpme düşüncesi seni heyecanlandırıyor mu?\n®️CeteUserBot✔**",
    "**✨İlk ne zaman öpüştün?\n®️CeteUserBot✔**",
    "**✨Daha önce annenle babanı sevişirken yakaladın mı?\n®️CeteUserBot✔**",
    "**✨Söylediğin en son yalan neydi?\n®️CeteUserBot✔**",
    "**✨Seni en çok tahrik eden şey nedir?\n®️CeteUserBot✔**",
    "**✨Alır mısın yoksa daha çok verir misin?\n®️CeteUserBot✔**",
    "**✨Bize bir sarhoşluk hikayeni anlat!\n®️CeteUserBot✔**",
    "**✨Daha önce gördüğün en açık seçik rüya neydi? Detayıyla açıkla!\n®️CeteUserBot✔**",
    "**✨Hiç fetişin var mı? Varsa açıkla!\n®️CeteUserBot✔**",
    "**✨Bakir/bakire misin?\n®️CeteUserBot✔**",
    "**✨Daha önce hiç komşudan birşey çaldın mı?\n®️CeteUserBot✔**",
    "**✨Ön sevişme sırasında nelerden hoşlanırsın?\n®️CeteUserBot✔**",
    "**✨Şimdiye kadar yaşadığınız en iyi orgazm hangisi?\n®️CeteUserBot✔**",
    "**✨En son ne zaman mastürbasyon yaptın?\n®️CeteUserBot✔**",
    "**✨En sevdiğiniz pozisyon nedir?\n®️CeteUserBot✔**",
    "**✨Seks yaparken müzik dinlemeyi sever misin?\n®️CeteUserBot✔**",
    "**✨Hiç başka bir çiftin seks yapmasını izledin mi?\n®️CeteUserBot✔**",
    "**✨İlk seks deneyiminiz nasıldı?\n®️CeteUserBot✔**",
    "**✨Zevk vermek ister misin?\n®️CeteUserBot✔**",
    "**✨Yataktayken en utanç verici durumun neydi?\n®️CeteUserBot✔**",
    "**✨Sana ilk orgazmını kim verdi?\n®️CeteUserBot✔**",
    "**✨Telefonunda en son arama yaptığın şey neydi?\n®️CeteUserBot✔**",
    "**✨Çıplak olmak mı yoksa düşündüğün her şeyin tişörtünde yazması mı? Hangisini seçerdin?\n®️CeteUserBot✔**",
    "**✨Yere düşürdüğün, uzun süre bekledikten sonra yediğin en son şey neydi?\n®️CeteUserBot✔**",
    "**✨Hiç bilindik hayvan etlerinden farklı bir et yedin mi?\n®️CeteUserBot✔**",
    "**✨Bir gün karşı cins olarak uyansan yapacağın ilk şey ne olurdu?\n®️CeteUserBot✔**",
    "**✨Hiç havuza işeyip hiçbir şey olmamış gibi davrandın mı?\n®️CeteUserBot✔**",
    "**✨Hiç asansörde osurdun mu?\n®️CeteUserBot✔**",
    "**✨Bu gruptaki insanlardan kiminle hayatını değiştirmek isterdin?\n®️CeteUserBot✔",
    "**✨Tuvalete oturduğun zaman ne düşünürsün?\n®️CeteUserBot✔**",
    "**✨Hiç aynada öpüşmeyi denedin mi?\n®️CeteUserBot✔**",
    "**✨Yaptığında utanmana neden olan mahcup zevkin nedir?\n®️CeteUserBot✔**",
    "**✨Hiç sen banyodayken birisi içeri pat diye girdi mi?\n®️CeteUserBot✔**",
    "**✨Burnunu karıştırır mısın?\n®️CeteUserBot✔**",
    "**✨Hiç sınıfta yüksek sesle osurdun mu?\n®️CeteUserBot✔**",
    "**✨Web geçmişini birisi görece utanacağın şey ne olurdu?\n®️CeteUserBot✔**",
    "**✨Hiç seksi bir fotoğrafını çekmeyi denedin mi?\n®️CeteUserBot✔**",
    "**✨Gizli aşkın kim?\n®️CeteUserBot✔**",
    "**✨Bu grupta en az kimden hoşlanıyorsun ve neden?\n®️CeteUserBot✔**",
    "**✨Bu grupta en seksi kişi sence kim?\n®️CeteUserBot✔**",
    "**✨Şu an hangi renk iç çamaşırı giyiyorsun?\n®️CeteUserBot✔**",
    "**✨Son attığın mesaj neydi?\n®️CeteUserBot✔**",
    "**✨Mevcut sevgilinle evleneceğini düşünüyor musun?\n®️CeteUserBot✔**",
    "**✨İç çamaşırlarını ne sıklıkla yıkıyorsun?\n®️CeteUserBot✔**",
    "**✨Hiç osurup başka birini suçladın mı?\n®️CeteUserBot✔**",
    "**✨En son izlediğin 18+ film hangisiydi?\n®️CeteUserBot✔**",
    "**✨Kimsenin senin hakkında bilmediği şey nedir?\n®️CeteUserBot✔**",
    "**✨Sevgilinin ölümcül hastalığa yakalansa ondan ayrılır mısın?\n®️CeteUserBot✔**",
    "**✨Ayakların kokuyor mu?\n®️CeteUserBot✔**",
    "**✨Saçma takma adlara sahip misin?\n®️CeteUserBot✔**",
    "**✨En son ne zaman yatağını ıslattın?\n®️CeteUserBot✔**",
    "**✨Herhangi bir Marvel karakteriyle çıkmak zorunda olsan kimi seçerdin?\n®️CeteUserBot✔**",
    "**✨Hiç izlememen gereken bir film izledin mi?\n®️CeteUserBot✔**",
    "**✨Telefonunda hangi uygulamayı daha sık kullanıyorsun?\n®️CeteUserBot✔**",
    "**✨Hiç bir şeyden kaçmak için hasta numarası yaptın mı?\n®️CeteUserBot✔**",
    "**✨Bir oturuşta en fazla yediğin yemek hangisi?\n®️CeteUserBot✔**",
    "**✨Karanlıktan korkar mısın?\n®️CeteUserBot✔**",
    "**✨Bütün günü evde geçirsen ne yaparsın?\n®️CeteUserBot✔**",
    "**✨En son ne zaman dişlerini fırçaladın?\n®️CeteUserBot✔**",
    "**✨Reglmısın?\n®️CeteUserBot✔**",
    "**✨Yaptığın en yasa dışı şey neydi?\n®️CeteUserBot✔**",
    "**✨Kardeşini 1 milyon TL karşılığında başka bir kardeşle değişir misin?\n®️CeteUserBot✔**",
    "**✨Birden fazla kişiyle evlenme şansın olsa kimleri seçerdin?\n®️CeteUserBot✔**",
    "**✨Seks organlarını kaybetmeyi mi yoksa 150 kilo almayı mı tercih edersin?\n®️CeteUserBot✔**",
    "**✨Sence bu gruptaki en kötü insan kim olabilir?\n®️CeteUserBot✔**",
    "**✨İnternetsiz yaşamak mı? Isınma sistemi olmadan yaşamak mı? Hangisi?\n®️CeteUserBot✔**",
    "**✨Sevgilinden ayrılman için birisi sana 1 milyon TL verse ayrılır mıydın?\n®️CeteUserBot✔**",
    "**✨Yeniden doğma şansın olsaydı hangi dönemde yaşamak isterdin?\n®️CeteUserBot✔**",
    "**✨Sevgilin seni hiç utandırdı mı?\n®️CeteUserBot✔**",
    "**✨Hiç sevgilini aldatmayı düşündün mü?\n®️CeteUserBot✔**",
    "**✨Birdenbire görünmez olsaydın ne yapardın?\n®️CeteUserBot✔**",
    "**✨Hiç birini gözetlerken yakalandın mı?\n®️CeteUserBot✔**",
    "**✨Hiç sosyal medyada pişman olduğun bir şey paylaştın mı?\n®️CeteUserBot✔**",
    "**✨Duşta işiyor musun?\n®️CeteUserBot✔**",
    "**✨Hiç birini terk ettin mi?\n®️CeteUserBot✔**",
    "**✨Gelecek hafta dünyanın sonu olacak ve her şeyi yapma imkanına sahipsin. Ne yapardın?\n®️CeteUserBot✔**",
    "**✨Birisi gün boyu tişörtünü ters giymen için sana 100 TL verse yapar mısın?\n®️CeteUserBot✔**",
    "**✨Bir saat boyunca karşı cinsten biri olsaydın ne yapardın?\n®️CeteUserBot✔**",
    "**✨Bir alışveriş merkezinde başına gelen en çılgınca şey neydi?\n®️CeteUserBot✔**",
    "**✨Oldukça samimi bir andan (öpüşmek gibi) kaçınmak için hiç sevgiline yalan söyledin mi?\n®️CeteUserBot✔**",
    "**✨Sevgilinle yapmak istediğin en çılgınca şey nedir?\n®️CeteUserBot✔**",
    "**✨Hiç 16 yaşından önce içki içtin mi?\n®️CeteUserBot✔**",
    "**✨Bir başkasından etkilenerek yaptığın en çılgınca şey neydi?\n®️CeteUserBot✔**",
    "**✨Daha önce hiç sümüğünün tadına baktın mı?\n®️CeteUserBot✔**",
    "**✨Kendinden en az 15-20 yaş büyük birine aşık oldun mu?\n®️CeteUserBot✔**",
    "**✨Görünümünü 1-10 arasında nasıl değerlendirirsin?\n®️CeteUserBot✔**",
    "**✨Hiç kulak kirinin tadına baktın mı?\n®️CeteUserBot✔**",
    "**✨Çamaşırlarını ne sıklıkla değiştiriyorsun?\n®️CeteUserBot✔**",
    "**✨Hiç terinin tadına baktın mı?\n®️CeteUserBot✔**",
    "**✨En sevdiğin alkollü içecek hangisi?\n®️CeteUserBot✔**",
    "**✨Banyoda ne kadar uzun süre kaldın ve neden bu kadar uzun sürdü?\n®️CeteUserBot✔**",
    "**✨Eğer seçmek zorunda olsaydın kırık bir bacağı mı yoksa kırık bir kolu mu tercih ederdin?\n®️CeteUserBot✔**",
    "**✨İlk kiminle öpüştün?\n®️CeteUserBot✔**",
    "**✨Senden daha kısa biriyle çıkar mısın?\n®️CeteUserBot✔**",
    "**✨Bir gün boyunca sutyenini tişörtünün dışında giymen için sana 5.000 TL verilse bunu kabul eder miydin?\n®️CeteUserBot✔**",
    "**✨Çirkin ama yatakta iyi olan biriyle mi yoksa güzel ama yatakta kötü olan biriyle mi çıkmak isterdin?\n®️CeteUserBot✔**",
    "**✨Kardeşinin kız arkadaşıyla çıkabilecek olsaydın bu kim olurdu?\n®️CeteUserBot✔**",
    "**✨Ailen kız arkadaşından nefret ederse onu terk eder misin?\n®️CeteUserBot✔**",
    "**✨Hiç bir arkadaşının kız arkadaşına aşık oldun mu?\n®️CeteUserBot✔**",
    "**✨Bizim grupta yer alan en ateşli kişi sence kim?\n®️CeteUserBot✔**",
    "**✨Hiç biri tarafından reddedildin mi?\n®️CeteUserBot✔**",
    "**✨Fakir ve akıllı olmak ile zengin ama dilsiz olmak arasında seçim yapmak zorunda olsaydın hangisini seçerdin?\n®️CeteUserBot✔**",
    "**✨Senden daha yaşlı bir kadınla çıkar mısın?\n®️CeteUserBot✔**",
    "**✨Boxer mı külot mu?\n®️CeteUserBot✔**",
    "**✨Hiç yaşın hakkında yalan söyledin mi?\n®️CeteUserBot✔**",
    "**✨Hiç aynı cinsiyetten seks yaptın mı?\n®️CeteUserBot✔**",
    "**✨Benimle seks yaptın. Daha sonra bana ne söylerdin?\n®️CeteUserBot✔**",
    "**✨Hiç seks için para ödedin mi?\n®️CeteUserBot✔**",
    "**✨Hiç seks sırasında şaşırdınız mı - ve kim tarafından?\n®️CeteUserBot✔**",
    "**✨Erojen bölgen nerede?\n®️CeteUserBot✔**",
    "**✨En son ne zaman seks yaptın?\n®️CeteUserBot✔**",
    "**✨Nerede samimi piercingler var?\n®️CeteUserBot✔**",
    "**✨Kaç tane kadın / erkek öpüştün?\n®️CeteUserBot✔**",
    "**✨Tuvalette: Tuvalet kağıdının katlanması veya yuvarlanması?\n®️CeteUserBot✔**",
    "**✨Kıçına dövme yapmayı mı yoksa dilini delmeyi mi tercih edersin?\n®️CeteUserBot✔**",
    "**✨Şimdi nereye ışınlanmak istersiniz?\n®️CeteUserBot✔**",
    "**✨Gecenizi hangi ünlü kişiyle geçirmek istersiniz?\n®️CeteUserBot✔**",
    "**✨İlk öpücüğün nasıl / nerede / kiminle oldu?\n®️CeteUserBot✔**",
    "**✨Genital bölgede hangi saç stiline sahipsin?\n®️CeteUserBot✔**",
    "**✨Kendini tatmin ettiğinde ne düşünüyorsun?\n®️CeteUserBot✔**",
    "**✨Bu gruptan birisiyle 30 dakika boyunca öpüşmen gerekseydi kimi seçerdin?\n®️CeteUserBot✔**",
    "**✨+18 doğruluk cesaretlik soruları seni tahrik ediyor mu?\n®️CeteUserBot✔**",
    "**✨Bugüne kadar mastürbasyon yaparken kullandığın en ilginç obje neydi?\n®️CeteUserBot✔**",
    "**✨Bugüne Kadar Kaç Kişiyle Yattın?\n®️CeteUserBot✔**",
    "**✨Şu an giydiğin iç çamaşırının rengi ne?\n®️CeteUserBot✔**",
    "**✨Erken Boşalma Sorunun Var mı?\n®️CeteUserBot✔**",
    "**✨Fetiş Sahibi Misin? Gizli fetişini açıkla!\n®️CeteUserBot✔**",
    "**✨Bu grupta birinin koltuk altını yalaman gerekse, kiminkini yalardın? Neden?\n®️CeteUserBot✔**",
    "**✨Telefonunda hiç çıplak fotoğrafın var mı? Başkasınınki de olur. Bize göster?\n®️CeteUserBot✔**",
    "**✨İlk seks deneyimini yaşadığında yaşın kaçtı ve neredeydin?\n®️CeteUserBot✔**",
    "**✨Hiç tanımadığın birisiyle seks yaptın mı? Nasıl bir deneyimdi?\n®️CeteUserBot✔**",
    "**✨Çoraplarını çıkardıktan sonra koklamak gibi bir alışkanlığın var mı?\n®️CeteUserBot✔**",
    "**✨Ailenden herkes ölecek ve sadece birini kurtarma şansın var! Kimi seçerdin? Neden?\n®️CeteUserBot✔**",
    "**✨Gerçek yaşın kaç?\n®️CeteUserBot✔**",
    "**✨Çok fazla paran olacak ama bir daha hiç tuvalete gitmeyeceksin! Kabul eder miydin?\n®️CeteUserBot✔**",
    "**✨En son ne zaman ağda yaptın? ve Nerene Yaptın?\n®️CeteUserBot✔**",
    "**✨Mahrem bölgendeki kılları kaç güne bir alırsın?\n®️CeteUserBot✔**",
    "**✨En komik kızlar tuvaleti anını anlat!\n®️CeteUserBot✔**",
    "**✨Ped kullanıyormusun kullanıyorsan markası ne.\n®️CeteUserBot✔**",
    "**✨Göğüslerinin boyutlarından memnun musun?\n®️CeteUserBot✔**",
    "**✨Ne tarz külotları giymeyi tercih ediyorsun?\n®️CeteUserBot✔**",
    "**✨Zengin koca bulsan kaçar mısın?\n®️CeteUserBot✔**",

]

@register(outgoing=True, pattern="^.dsor$")
async def dsor(e):
    """ Cete'nin sözlüğü """
    await e.edit(choice(DOGRULUK_STRINGS))


CMD_HELP.update({
    "dsor":
    ".dsor veya .dsor ile birinin metnine cevap verin.\
    \nKullanım: Doğruluk soruları sorar"
})